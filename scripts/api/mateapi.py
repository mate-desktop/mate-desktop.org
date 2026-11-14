#!/usr/bin/env python3
"""Generate the MATE ecosystem graph and API reference for mate-desktop.org.

Subcommands (run in this order; see .github/workflows/deploy.yml):

  clone      shallow-clone / update every package listed in packages.toml
  graph      extract dependencies and write data/ecosystem.json
  doxygen    generate Doxygen source reference for every C package
  gir        build the introspectable libraries from git and run gi-docgen
  finalize   record which docs exist in data/ecosystem.json

Generated output (both git-ignored):
  data/ecosystem.json        consumed by layouts/_shortcodes/ecosystem-graph.html
  static/docs/api/src/<pkg>/ Doxygen source reference
  static/docs/api/lib/<ns>/  gi-docgen library reference
"""

import argparse
import concurrent.futures
import datetime
import json
import os
import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parent.parent
ORG = "mate-desktop"
DEFAULT_SRC = SITE / ".cache" / "mate-src"
DEFAULT_OUT = SITE / "static" / "docs" / "api"
GRAPH_JSON = SITE / "data" / "ecosystem.json"
API_URL = "/docs/api"

SKIP_DIRS = {".git", "build", "builddir", "_build", "subprojects", "mate-submodules",
             "po", "help", "man", "autom4te.cache", ".cache"}

# External pkg-config modules that belong to one well-known project are
# collapsed into a single node so the graph stays readable.
EXTERNAL_FAMILIES = [
    (re.compile(r"^(glib|gio|gio-unix|gobject|gmodule|gmodule-export|gmodule-no-export|gthread)-2\.0$"), "GLib"),
    (re.compile(r"^(gtk\+|gdk|gail|gtk\+-x11|gtk\+-unix-print|gdk-x11|gtk\+-wayland)-3\.0$"), "GTK 3"),
    (re.compile(r"^gdk-pixbuf-2\.0$"), "gdk-pixbuf"),
    (re.compile(r"^(pango|pangocairo|pangoft2|pangox)$"), "Pango"),
    (re.compile(r"^(cairo|cairo-gobject|cairo-xlib|cairo-pdf|cairo-ps|cairo-svg)$"), "cairo"),
    (re.compile(r"^(x11|xext|xrandr|xi|xinerama|xcomposite|xdamage|xfixes|xrender|xcursor|xtst|xxf86vm|xkbfile|xscrnsaver|xres|ice|sm|xmu|xt|xpresent|x11-xcb|xcb.*)$"), "X11 / Xorg"),
    (re.compile(r"^(libwnck-3\.0)$"), "libwnck"),
    (re.compile(r"^(dconf)$"), "dconf"),
    (re.compile(r"^(gobject-introspection-1\.0)$"), "gobject-introspection"),
    (re.compile(r"^(libnotify)$"), "libnotify"),
    (re.compile(r"^(polkit-gobject-1|polkit-agent-1)$"), "polkit"),
    (re.compile(r"^(libpulse|libpulse-mainloop-glib)$"), "PulseAudio"),
    (re.compile(r"^(alsa)$"), "ALSA"),
    (re.compile(r"^(gstreamer.*)$"), "GStreamer"),
    (re.compile(r"^(poppler.*)$"), "Poppler"),
    (re.compile(r"^(libxml-2\.0)$"), "libxml2"),
    (re.compile(r"^(dbus-1|dbus-glib-1)$"), "D-Bus"),
    (re.compile(r"^(libsoup-.*)$"), "libsoup"),
    (re.compile(r"^(gtk-layer-shell-0|wayland-.*)$"), "Wayland"),
    (re.compile(r"^(vte-2\.91)$"), "VTE"),
    (re.compile(r"^(libpeas.*)$"), "libpeas"),
    (re.compile(r"^(gtksourceview-.*)$"), "GtkSourceView"),
    (re.compile(r"^(libcanberra.*)$"), "libcanberra"),
    (re.compile(r"^(gtkmm-3\.0|glibmm-2\.4|giomm-2\.4)$"), "gtkmm"),
    (re.compile(r"^(libgtop-2\.0)$"), "libgtop"),
    (re.compile(r"^(upower-glib)$"), "UPower"),
    (re.compile(r"^(libsecret-1)$"), "libsecret"),
    (re.compile(r"^(libsystemd|libelogind|systemd)$"), "systemd / elogind"),
    (re.compile(r"^(ayatana-.*|indicator.*|appindicator.*)$"), "Ayatana indicators"),
]

# Where external GObject-Introspection namespaces are documented.
GIR_EXTERNAL_DOCS = {
    "GLib-2.0": ("GLib", "https://docs.gtk.org/glib/", "General-purpose utility library"),
    "GObject-2.0": ("GObject", "https://docs.gtk.org/gobject/", "The base type system library"),
    "Gio-2.0": ("GIO", "https://docs.gtk.org/gio/", "GObject interfaces and objects"),
    "Gtk-3.0": ("GTK 3", "https://docs.gtk.org/gtk3/", "The GTK toolkit"),
    "Gdk-3.0": ("GDK 3", "https://docs.gtk.org/gdk3/", "The GTK windowing system abstraction"),
    "GdkPixbuf-2.0": ("GdkPixbuf", "https://docs.gtk.org/gdk-pixbuf/", "Image loading and scaling"),
    "Pango-1.0": ("Pango", "https://docs.gtk.org/Pango/", "Text shaping and rendering"),
}

# Introspectable libraries, built from git in dependency order for gi-docgen.
# "gir" lists (relative build-dir path or glob, namespace) pairs.
GIR_BUILD = ["mate-desktop", "mate-menus", "libmatekbd", "libmateweather",
             "mate-panel", "caja", "eom", "pluma", "atril"]

# Meson options set when building for gi-docgen: True = enable, False = disable.
# Values are translated to the option's declared type (boolean or feature).
MESON_WANTED = {"introspection": True, "gir": True, "gtk-doc": False, "docs": False,
                "tests": False, "caja": False}


def log(*a):
    print("[mateapi]", *a, file=sys.stderr, flush=True)


def load_config():
    with open(HERE / "packages.toml", "rb") as f:
        return tomllib.load(f)


def run(cmd, **kw):
    log("$", " ".join(map(str, cmd)))
    return subprocess.run(cmd, check=True, **kw)


# --------------------------------------------------------------------- clone

def cmd_clone(args):
    cfg = load_config()
    src = Path(args.src)
    src.mkdir(parents=True, exist_ok=True)

    def one(name):
        d = src / name
        url = f"https://github.com/{ORG}/{name}.git"
        try:
            if (d / ".git").exists():
                subprocess.run(["git", "-C", d, "fetch", "-q", "--depth=1", "origin", "HEAD"], check=True)
                subprocess.run(["git", "-C", d, "reset", "-q", "--hard", "FETCH_HEAD"], check=True)
            else:
                subprocess.run(["git", "clone", "-q", "--depth=1", url, d], check=True)
            # caja, pluma, mate-panel, … embed mate-submodules
            subprocess.run(["git", "-C", d, "submodule", "update", "-q", "--init", "--depth=1"], check=True)
            return name, None
        except subprocess.CalledProcessError as e:
            return name, str(e)

    with concurrent.futures.ThreadPoolExecutor(8) as ex:
        for name, err in ex.map(one, cfg["packages"]):
            log(f"{name}: {'ok' if not err else 'FAILED ' + err}")


# --------------------------------------------------------------------- graph

def read(p):
    try:
        return Path(p).read_text(errors="replace")
    except OSError:
        return ""


def strip_m4_comments(text):
    return "\n".join(l for l in text.splitlines() if not re.match(r"\s*(dnl\b|#)", l))


def m4_defines(text):
    d = {}
    for _, _, a in macro_calls(text, "m4_define"):
        if len(a) >= 2:
            d[unquote(a[0])] = unquote(",".join(a[1:]))
    return d


def expand_m4(s, defs, depth=0):
    new = re.sub(r"\b(\w+)\b", lambda m: defs.get(m.group(1), m.group(1)), s)
    if new != s and depth < 8:
        return expand_m4(new, defs, depth + 1)
    return re.sub(r"\[\]|\(\)|[\[\]]", "", new).strip()


def shell_vars(text):
    v = {}
    for m in re.finditer(r"^\s*([A-Z][A-Z0-9_]*)=([\"']?)([^\"'\n]*)\2\s*$", text, re.M):
        v.setdefault(m.group(1), m.group(3))
    return v


def macro_calls(text, name):
    """Yield (start, end, [args]) for every NAME(...) call, honouring m4 quotes."""
    for m in re.finditer(r"\b" + name + r"\s*\(", text):
        i, depth, quote, args, cur = m.end(), 1, 0, [], []
        while i < len(text) and depth:
            c = text[i]
            if c == "[":
                quote += 1
            elif c == "]":
                quote -= 1
            elif not quote and c == "(":
                depth += 1
            elif not quote and c == ")":
                depth -= 1
                if not depth:
                    break
            if not quote and depth == 1 and c == ",":
                args.append("".join(cur))
                cur = []
            else:
                cur.append(c)
            i += 1
        args.append("".join(cur))
        yield m.start(), i, [a.strip() for a in args]


def unquote(s):
    s = s.strip()
    while s.startswith("[") and s.endswith("]"):
        s = s[1:-1].strip()
    return s


def conditional_spans(text):
    spans = []
    for name in ("AS_IF", "AM_COND_IF", "AS_CASE", "AC_ARG_ENABLE", "AC_ARG_WITH"):
        spans += [(s, e) for s, e, _ in macro_calls(text, name)]
    # shell if/case blocks
    stack = []
    for m in re.finditer(r"^\s*(if|case)\b|^\s*(fi|esac)\b|;\s*(fi|esac)\b", text, re.M):
        if m.group(1):
            stack.append(m.start())
        elif stack:
            spans.append((stack.pop(), m.end()))
    return spans


def parse_modules(spec, svars, defs):
    spec = expand_m4(unquote(spec), defs)
    spec = re.sub(r"\$\{?(\w+)\}?", lambda m: svars.get(m.group(1), m.group(0)), spec)
    toks = re.split(r"[\s\[\]]+", spec)
    mods, skip = [], False
    for t in toks:
        if not t:
            continue
        if skip:
            skip = False
            continue
        if t in (">=", "<=", "=", ">", "<", "!="):
            skip = True
            continue
        if t.startswith("$") or not re.match(r"^[A-Za-z][\w.+-]*$", t):
            continue
        mods.append(t)
    return mods


def iter_files(root, suffixes):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS and not d.startswith(".")]
        for f in filenames:
            if f.endswith(suffixes):
                yield Path(dirpath) / f


def analyze(name, d):
    ac_raw = read(d / "configure.ac")
    ac = strip_m4_comments(ac_raw)
    meson = read(d / "meson.build")
    defs = m4_defines(ac_raw)
    svars = shell_vars(ac)
    info = {"name": name, "pkgconfig": [], "gir": [], "requires": [], "gir_requires": [],
            "submodules": [], "mate_common": False, "version": None, "c_files": 0,
            "languages": []}

    for _, _, a in macro_calls(ac, "AC_INIT"):
        if len(a) > 1:
            info["version"] = expand_m4(unquote(a[1]), defs) or None
        break
    if not info["version"]:
        m = re.search(r"project\s*\([^)]*?version\s*:\s*'([^']+)'", meson, re.S)
        info["version"] = m.group(1) if m else None

    # Provided pkg-config files
    for macro in ("AC_CONFIG_FILES", "AC_OUTPUT"):
        for _, _, a in macro_calls(ac, macro):
            for tok in re.split(r"\s+", unquote(a[0]) if a else ""):
                out = tok.split(":")[0]
                out = expand_m4(out, defs)
                if out.endswith(".pc") and "uninstalled" not in out:
                    info["pkgconfig"].append(Path(out).name[:-3])
    if not info["pkgconfig"]:
        for p in iter_files(d, (".pc.in",)):
            if "uninstalled" not in p.name:
                info["pkgconfig"].append(p.name[:-6])

    # Provided GIR namespaces
    girs = set()
    for p in iter_files(d, ("Makefile.am", "meson.build")):
        girs |= set(re.findall(r"\b([A-Z][A-Za-z]+-\d+\.\d+)\.gir\b", read(p)))
    for p in iter_files(d, ("meson.build",)):
        for m in re.finditer(r"namespace\s*:\s*'([A-Z]\w+)'", read(p)):
            if m.group(1) in ("AtrilDocument", "AtrilView"):
                girs.add(m.group(1) + "-1.5.0")
    info["gir"] = sorted(girs)

    # Required pkg-config modules
    spans = conditional_spans(ac)
    seen = {}
    for macro in ("PKG_CHECK_MODULES", "PKG_CHECK_EXISTS"):
        for s, e, a in macro_calls(ac, macro):
            spec = a[1] if macro == "PKG_CHECK_MODULES" and len(a) > 1 else a[0]
            optional = any(cs < s < ce for cs, ce in spans)
            not_found = a[3] if macro == "PKG_CHECK_MODULES" and len(a) > 3 else (a[2] if macro == "PKG_CHECK_EXISTS" and len(a) > 2 else "")
            if unquote(not_found) and "AC_MSG_ERROR" not in not_found:
                optional = True
            for mod in parse_modules(spec, svars, defs):
                seen[mod] = seen.get(mod, True) and optional
    if not ac:  # meson-only fallback
        for m in re.finditer(r"dependency\s*\(\s*'([^']+)'([^)]*)\)", meson):
            seen.setdefault(m.group(1), "required : false" in m.group(2) or "required: false" in m.group(2))
    info["requires"] = [{"module": k, "optional": v} for k, v in sorted(seen.items())]

    # Python GObject-Introspection users
    gi = set()
    for p in iter_files(d, (".py", ".py.in")):
        gi |= set(re.findall(r"require_version\(\s*['\"](\w+)['\"]\s*,\s*['\"]([\d.]+)['\"]", read(p)))
    info["gir_requires"] = sorted(f"{n}-{v}" for n, v in gi)

    for m in re.finditer(r"url\s*=\s*\S*github\.com[/:]" + ORG + r"/([\w.-]+?)(?:\.git)?\s*$", read(d / ".gitmodules"), re.M):
        info["submodules"].append(m.group(1))

    autogen = read(d / "autogen.sh")
    info["mate_common"] = bool(re.search(r"mate-autogen|MATE_COMPILE_WARNINGS|MATE_DEBUG_CHECK|MATE_MAINTAINER_MODE|MATE_COMMON_INIT|MATE_CXX_WARNINGS", ac + autogen))

    counts = {"C": 0, "C++": 0, "Python": 0, "Vala": 0}
    for p in iter_files(d, (".c", ".h", ".cpp", ".cc", ".hh", ".py", ".vala")):
        counts[{".c": "C", ".h": "C", ".cpp": "C++", ".cc": "C++", ".hh": "C++", ".py": "Python", ".vala": "Vala"}[p.suffix]] += 1
    info["c_files"] = counts["C"] + counts["C++"]
    info["languages"] = [k for k, v in sorted(counts.items(), key=lambda kv: -kv[1]) if v]

    try:
        r = subprocess.run(["git", "-C", d, "log", "-1", "--format=%H%x00%cI"], capture_output=True, text=True, check=True)
        info["commit"], info["commit_date"] = r.stdout.strip().split("\0")
    except (subprocess.CalledProcessError, ValueError):
        info["commit"] = info["commit_date"] = None
    return info


def external_name(mod):
    for rx, label in EXTERNAL_FAMILIES:
        if rx.match(mod):
            return label
    return mod


def build_graph(src):
    cfg = load_config()
    infos = {}
    for name in cfg["packages"]:
        d = Path(src) / name
        if d.is_dir():
            infos[name] = analyze(name, d)
        else:
            log(f"warning: {name} not cloned, skipping")

    pc_owner = {pc: n for n, i in infos.items() for pc in i["pkgconfig"]}
    gir_owner = {g: n for n, i in infos.items() for g in i["gir"]}

    packages, externals = [], {}
    for name, meta in cfg["packages"].items():
        if name not in infos:
            continue
        i = infos[name]
        deps = {}

        def add(target, kind, via, optional):
            if target == name:
                return
            e = deps.setdefault(target, {"target": target, "kinds": [], "via": [], "optional": True})
            if kind not in e["kinds"]:
                e["kinds"].append(kind)
            if via and via not in e["via"]:
                e["via"].append(via)
            e["optional"] = e["optional"] and optional

        ext = {}
        for r in i["requires"]:
            owner = pc_owner.get(r["module"])
            if owner:
                add(owner, "pkg-config", r["module"], r["optional"])
            else:
                label = external_name(r["module"])
                e = ext.setdefault(label, {"name": label, "modules": [], "optional": True})
                e["modules"].append(r["module"])
                e["optional"] = e["optional"] and r["optional"]
        for g in i["gir_requires"]:
            if g in gir_owner:
                add(gir_owner[g], "introspection", g, False)
        for s in i["submodules"]:
            if s in infos:
                add(s, "submodule", None, False)
        if i["mate_common"] and name != "mate-common":
            add("mate-common", "build", None, False)

        for e in ext.values():
            x = externals.setdefault(e["name"], {"name": e["name"], "modules": set(), "used_by": []})
            x["modules"] |= set(e["modules"])
            x["used_by"].append(name)

        packages.append({
            "name": name,
            "category": meta["category"],
            "description": meta.get("description", ""),
            "version": i["version"],
            "commit": i["commit"],
            "commit_date": i["commit_date"],
            "repo": f"https://github.com/{ORG}/{name}",
            "languages": i["languages"],
            "provides": {"pkgconfig": i["pkgconfig"], "gir": i["gir"]},
            "deps": sorted(deps.values(), key=lambda e: e["target"]),
            "external": sorted(ext.values(), key=lambda e: e["name"].lower()),
            "has_c": i["c_files"] > 0,
            "docs": {"source": None, "library": []},
        })

    cats = [{"id": k, "label": v["label"], "order": v["order"]} for k, v in cfg["categories"].items()]
    return {
        "generated": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
        "categories": sorted(cats, key=lambda c: c["order"]),
        "packages": packages,
        "external": sorted(({"name": x["name"], "modules": sorted(x["modules"]), "used_by": sorted(x["used_by"])}
                            for x in externals.values()), key=lambda x: x["name"].lower()),
    }


def save_graph(g):
    GRAPH_JSON.parent.mkdir(parents=True, exist_ok=True)
    GRAPH_JSON.write_text(json.dumps(g, indent=1, ensure_ascii=False) + "\n")
    log(f"wrote {GRAPH_JSON} ({len(g['packages'])} packages, {sum(len(p['deps']) for p in g['packages'])} internal edges)")


def load_graph():
    return json.loads(GRAPH_JSON.read_text())


def topo_order(g):
    deps = {p["name"]: [d["target"] for d in p["deps"]] for p in g["packages"]}
    order, state = [], {}

    def visit(n):
        if state.get(n) == 2:
            return
        if state.get(n) == 1:  # cycle: ignore back edge
            return
        state[n] = 1
        for d in deps.get(n, []):
            visit(d)
        state[n] = 2
        order.append(n)

    for n in deps:
        visit(n)
    return order


def cmd_graph(args):
    save_graph(build_graph(args.src))


# ------------------------------------------------------------------- doxygen

DOXYFILE = """\
PROJECT_NAME           = "{name}"
PROJECT_NUMBER         = "{version}"
PROJECT_BRIEF          = "{brief}"
OUTPUT_DIRECTORY       = "{out}"
HTML_OUTPUT            = .
INPUT                  = "{src}"
RECURSIVE              = YES
FILE_PATTERNS          = *.c *.h *.cpp *.cc *.hh
EXCLUDE_PATTERNS       = */build/* */builddir/* */_build/* */subprojects/* */mate-submodules/* */.git/* */po/* */test/* */tests/*
EXCLUDE_SYMLINKS       = YES
FULL_PATH_NAMES        = YES
STRIP_FROM_PATH        = "{src}"
STRIP_FROM_INC_PATH    = "{src}"
OPTIMIZE_OUTPUT_FOR_C  = YES
EXTENSION_MAPPING      = h=C
EXTRACT_ALL            = YES
EXTRACT_STATIC         = YES
JAVADOC_AUTOBRIEF      = YES
MARKDOWN_SUPPORT       = YES
ENABLE_PREPROCESSING   = YES
MACRO_EXPANSION        = YES
EXPAND_ONLY_PREDEF     = YES
PREDEFINED             = G_BEGIN_DECLS= G_END_DECLS= G_GNUC_CONST= G_GNUC_PURE= \\
                         "G_GNUC_PRINTF(a,b)=" G_GNUC_NULL_TERMINATED= G_GNUC_WARN_UNUSED_RESULT= \\
                         G_GNUC_UNUSED= G_GNUC_MALLOC= G_GNUC_INTERNAL= G_GNUC_DEPRECATED= \\
                         "G_GNUC_DEPRECATED_FOR(f)=" "G_DEFINE_AUTOPTR_CLEANUP_FUNC(a,b)=" \\
                         "G_DECLARE_FINAL_TYPE(a,b,c,d,e)=typedef struct _##a a;" \\
                         "G_DECLARE_DERIVABLE_TYPE(a,b,c,d,e)=typedef struct _##a a;" \\
                         "G_DECLARE_INTERFACE(a,b,c,d,e)=typedef struct _##a a;"
SOURCE_BROWSER         = NO
INLINE_SOURCES         = NO
STRIP_CODE_COMMENTS    = NO
REFERENCED_BY_RELATION = YES
REFERENCES_RELATION    = YES
VERBATIM_HEADERS       = NO
ALPHABETICAL_INDEX     = YES
GENERATE_HTML          = YES
GENERATE_LATEX         = NO
GENERATE_TREEVIEW      = YES
DISABLE_INDEX          = NO
FULL_SIDEBAR           = NO
SEARCHENGINE           = YES
HTML_COLORSTYLE        = LIGHT
HTML_DYNAMIC_SECTIONS  = NO
HTML_EXTRA_STYLESHEET  = {stylesheets}
HTML_EXTRA_FILES       = {extra_files}
HTML_HEADER            = {header}
HAVE_DOT               = {have_dot}
DOT_IMAGE_FORMAT       = svg
INTERACTIVE_SVG        = YES
DOT_NUM_THREADS        = 2
DOT_COMMON_ATTR        = "fontname=Helvetica,fontsize=10"
DOT_EDGE_ATTR          = "labelfontname=Helvetica,labelfontsize=10"
CLASS_GRAPH            = YES
COLLABORATION_GRAPH    = YES
GROUP_GRAPHS           = YES
INCLUDE_GRAPH          = YES
INCLUDED_BY_GRAPH      = YES
CALL_GRAPH             = YES
CALLER_GRAPH           = NO
GRAPHICAL_HIERARCHY    = YES
DIRECTORY_GRAPH        = YES
DIR_GRAPH_MAX_DEPTH    = 2
DOT_GRAPH_MAX_NODES    = 40
MAX_DOT_GRAPH_DEPTH    = 3
DOT_MULTI_TARGETS      = YES
DOT_CLEANUP            = YES
QUIET                  = YES
WARNINGS               = NO
WARN_IF_UNDOCUMENTED   = NO
WARN_NO_PARAMDOC       = NO
GENERATE_TAGFILE       = "{tagfile}"
TAGFILES               = {tagfiles}
"""


def doxygen_theme(work):
    """Use doxygen-awesome-css when present ($DOXYGEN_AWESOME or .cache/doxygen-awesome-css)."""
    d = Path(os.environ.get("DOXYGEN_AWESOME", SITE / ".cache" / "doxygen-awesome-css"))
    if not (d / "doxygen-awesome.css").exists():
        log("doxygen-awesome-css not found, using the default Doxygen theme")
        return None
    sheets = [d / "doxygen-awesome.css", d / "doxygen-awesome-sidebar-only.css",
              d / "doxygen-awesome-sidebar-only-darkmode-toggle.css", HERE / "doxygen-mate.css"]
    extras = [d / "doxygen-awesome-darkmode-toggle.js", d / "doxygen-awesome-fragment-copy-button.js"]
    work.mkdir(parents=True, exist_ok=True)
    subprocess.run(["doxygen", "-w", "html", work / "header.html", work / "footer.html", work / "style.css"],
                   check=True, capture_output=True)
    return {"sheets": " ".join(f'"{p}"' for p in sheets), "extras": " ".join(f'"{p}"' for p in extras),
            "header": (work / "header.html").read_text()}


GITHUB_ICON = ('<svg class="mate-gh-icon" viewBox="0 0 16 16" width="16" height="16" aria-hidden="true">'
               '<path fill="currentColor" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 '
               '0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 '
               '1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15'
               '-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82'
               '.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93'
               '-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>')


def package_header(theme, p, work):
    """Doxygen header with the doxygen-awesome scripts and MATE links in the sidebar title area."""
    commit = p["commit"] or ""
    gh = f'{p["repo"]}/tree/{commit}' if commit else p["repo"]
    links = (f'<div class="mate-api-links">'
             f'<a class="mate-api-back" href="{API_URL}/#{p["name"]}">&larr; All MATE packages</a>'
             f'<a class="mate-api-gh" href="{gh}" title="{p["name"]} on GitHub'
             + (f' (documented at {commit[:10]})' if commit else "") + '">'
             + GITHUB_ICON + (f'<span>{commit[:7]}</span>' if commit else "") + "</a></div>")
    js = ('<script type="text/javascript" src="$relpath^doxygen-awesome-darkmode-toggle.js"></script>\n'
          '<script type="text/javascript" src="$relpath^doxygen-awesome-fragment-copy-button.js"></script>\n'
          '<script type="text/javascript">DoxygenAwesomeDarkModeToggle.init();'
          'DoxygenAwesomeFragmentCopyButton.init();</script>\n')
    h = theme["header"].replace("</head>", js + "</head>", 1)
    brief = '<!--BEGIN PROJECT_BRIEF--><div id="projectbrief">$projectbrief</div><!--END PROJECT_BRIEF-->'
    assert brief in h, "unexpected Doxygen header template"
    h = h.replace(brief, brief + "\n   " + links, 1)
    f = work / f".{p['name']}-header.html"
    f.write_text(h)
    return f


def add_source_links(p, dest, tagfile):
    """Doxygen's own source browser is disabled (it doubles the size); link to GitHub instead."""
    try:
        import xml.etree.ElementTree as ET
        root = ET.parse(tagfile).getroot()
    except Exception as e:  # noqa: BLE001
        log(f"{p['name']}: cannot read tag file ({e})")
        return
    base = f'{p["repo"]}/blob/{p["commit"] or "HEAD"}/'
    for c in root.iter("compound"):
        if c.get("kind") != "file":
            continue
        html = dest / (c.findtext("filename") or "")
        if not html.suffix:
            html = html.with_suffix(".html")
        rel = (c.findtext("path") or "") + (c.findtext("name") or "")
        if not html.exists() or not rel:
            continue
        text = html.read_text(errors="replace")
        link = (f'<a class="mate-source-link" href="{base}{rel}" title="{rel} on GitHub">'
                f'{GITHUB_ICON}<span>View source</span></a>')
        text, n = re.subn(r'(<div class="title">.*?</div>)', lambda m: m.group(1) + link, text, count=1, flags=re.S)
        if n:
            html.write_text(text)


def public_headers(d):
    """Basenames of headers a package installs (Makefile.am *_HEADERS / header_DATA)."""
    found = set()
    for mk in iter_files(d, ("Makefile.am",)):
        text = re.sub(r"\\\n", " ", read(mk))
        vars_ = dict(re.findall(r"^\s*(\w+)\s*\+?=\s*(.*)$", text, re.M))

        def expand(v, depth=0):
            return re.sub(r"\$\((\w+)\)", lambda m: expand(vars_.get(m.group(1), ""), depth + 1) if depth < 5 else "", v)

        for name, val in vars_.items():
            prefix, _, kind = name.rpartition("_")
            if kind not in ("HEADERS", "DATA") or prefix in ("noinst", "EXTRA", "BUILT", "CLEAN", "DISTCLEAN", "dist", "nodist"):
                continue
            found |= {Path(t).name for t in expand(val).split() if t.endswith(".h")}
    return found


def filter_tagfile(src_tag, dst_tag, pkg_dir):
    """Keep only installed public API in the tag file other packages link against.

    Without this, parameter names in one package get linked to unrelated global
    variables or static helpers that happen to share the name in another.
    """
    import xml.etree.ElementTree as ET
    pub = public_headers(pkg_dir)
    tree = ET.parse(src_tag)
    root = tree.getroot()
    headers_text = "".join(read(f) for f in iter_files(pkg_dir, (".h",)) if f.name in pub)
    for c in list(root):
        kind, name = c.get("kind"), c.findtext("name") or ""
        if kind == "file" and name in pub:
            continue
        if kind in ("struct", "union") and re.search(r"\b" + re.escape(name) + r"\b", headers_text):
            continue
        root.remove(c)
    tree.write(dst_tag)
    return len(root)


def prune_graph_files(dest):
    """Drop files only needed while generating; keeps the site under the Pages size limit.

    INTERACTIVE_SVG writes every graph twice (zoomable *.svg plus *_org.svg, used
    only by the "open in new window" button), which roughly doubles the output.
    Point that button at the zoomable SVG and delete the copies, along with the
    *.md5 / *.map bookkeeping files.
    """
    removed = 0
    for f in dest.iterdir():
        name = f.name
        if name.endswith(".html"):
            # graphs are shown expanded; only load them when scrolled into view
            t = f.read_text(errors="replace")
            if "<iframe " in t:
                f.write_text(t.replace("<iframe ", '<iframe loading="lazy" '))
            continue
        if name.endswith("_org.svg"):
            zoomable = dest / (name[:-len("_org.svg")] + ".svg")
            if zoomable.exists():
                t = zoomable.read_text(errors="replace")
                zoomable.write_text(t.replace(f'xlink:href="{name}"', f'xlink:href="{zoomable.name}"'))
            f.unlink()
            removed += 1
        elif name.endswith((".md5", ".map", ".dot")):
            f.unlink()
            removed += 1
    return removed


def cmd_doxygen(args):
    if not shutil.which("doxygen"):
        sys.exit("doxygen not found")
    g = load_graph()
    src, out = Path(args.src).resolve(), Path(args.out).resolve() / "src"
    work = SITE / ".cache" / "doxygen-work"
    tags = work / "tags"
    tags.mkdir(parents=True, exist_ok=True)
    out.mkdir(parents=True, exist_ok=True)
    pk = {p["name"]: p for p in g["packages"]}
    theme = doxygen_theme(work)
    only = set(args.packages or [])
    have_dot = "YES" if shutil.which("dot") else "NO"
    if have_dot == "NO":
        log("graphviz (dot) not found: generating without include/call/collaboration graphs")

    # Group packages into levels so each one's dependencies' tag files exist.
    order = [n for n in topo_order(g) if pk[n]["has_c"]]
    level = {}
    for n in order:
        level[n] = 1 + max((level.get(d["target"], -1) for d in pk[n]["deps"] if d["target"] in level), default=-1)
    levels = {}
    for n, l in level.items():
        levels.setdefault(l, []).append(n)

    def one(n):
        if only and n not in only:
            return n, True
        p = pk[n]
        dest = out / n
        shutil.rmtree(dest, ignore_errors=True)
        dest.mkdir(parents=True)
        # Absolute URLs: relative ones break inside Doxygen's sub-directories.
        tagfiles = " ".join(f'"{tags / (d["target"] + ".public.tag")}={API_URL}/src/{d["target"]}"'
                            for d in p["deps"] if (tags / (d["target"] + ".public.tag")).exists())
        conf = DOXYFILE.format(
            name=n, version=p["version"] or "", have_dot=have_dot, brief=p["description"].replace('"', "'"),
            out=dest, src=src / n, tagfile=tags / f"{n}.tag", tagfiles=tagfiles,
            stylesheets=theme["sheets"] if theme else "", extra_files=theme["extras"] if theme else "",
            header=f'"{package_header(theme, p, work)}"' if theme else "")
        r = subprocess.run(["doxygen", "-"], input=conf, text=True, capture_output=True)
        if r.returncode:
            log(f"{n}: doxygen failed\n{r.stderr[-2000:]}")
            return n, False
        add_source_links(p, dest, tags / f"{n}.tag")
        prune_graph_files(dest)
        kept = filter_tagfile(tags / f"{n}.tag", tags / f"{n}.public.tag", src / n)
        log(f"{n}: ok ({kept} public symbols exported)")
        return n, True

    jobs = args.jobs or os.cpu_count() or 2
    failed = []
    with concurrent.futures.ThreadPoolExecutor(jobs) as ex:
        for l in sorted(levels):
            failed += [n for n, ok in ex.map(one, sorted(levels[l])) if not ok]
    if failed:
        log("failed:", " ".join(failed))
        sys.exit(1)


# ----------------------------------------------------------------- gi-docgen

def meson_options(d):
    text = read(d / "meson_options.txt") or read(d / "meson.options")
    opts = []
    for m in re.finditer(r"option\(\s*'([^']+)'(.*?)\)\s*$", text, re.S | re.M):
        name, rest = m.group(1), m.group(2)
        if name not in MESON_WANTED:
            continue
        kind = (re.search(r"type\s*:\s*'(\w+)'", rest) or [None, ""])[1]
        on = MESON_WANTED[name]
        if kind == "feature":
            opts.append(f"-D{name}={'enabled' if on else 'disabled'}")
        elif kind == "boolean":
            opts.append(f"-D{name}={'true' if on else 'false'}")
    return opts


def build_library(name, src, prefix):
    d = Path(src) / name
    env = gir_env(prefix)
    jobs = str(os.cpu_count() or 2)
    if (d / "meson.build").exists():
        b = d / "_build-api"
        run(["meson", "setup", *(["--wipe"] if b.exists() else []), b, d, f"--prefix={prefix}",
             "--libdir=lib", "-Dbuildtype=plain", *meson_options(d)], env=env)
        run(["ninja", "-C", b, "install"], env=env)
    else:
        run(["./autogen.sh", f"--prefix={prefix}", "--libdir=" + str(Path(prefix) / "lib"),
             "--enable-introspection=yes", "--disable-gtk-doc", "--disable-maintainer-mode"], cwd=d, env=env)
        run(["make", "-j" + jobs], cwd=d, env=env)
        run(["make", "install"], cwd=d, env=env)


def gir_env(prefix):
    env = dict(os.environ)
    p = Path(prefix)
    env["PKG_CONFIG_PATH"] = ":".join(filter(None, [str(p / "lib/pkgconfig"), str(p / "share/pkgconfig"), env.get("PKG_CONFIG_PATH")]))
    env["LD_LIBRARY_PATH"] = ":".join(filter(None, [str(p / "lib"), env.get("LD_LIBRARY_PATH")]))
    env["XDG_DATA_DIRS"] = ":".join(filter(None, [str(p / "share"), env.get("XDG_DATA_DIRS", "/usr/local/share:/usr/share")]))
    env["GI_TYPELIB_PATH"] = str(p / "lib/girepository-1.0")
    env["ACLOCAL_PATH"] = ":".join(filter(None, [str(p / "share/aclocal"), env.get("ACLOCAL_PATH")]))
    env["PATH"] = str(p / "bin") + ":" + env["PATH"]
    return env


def gidocgen_config(ns, pkg, all_ns, owner_of=None):
    owner_of = owner_of or {}
    name, version = ns.rsplit("-", 1)
    lines = [
        "[library]",
        f'version = "{pkg["version"] or version}"',
        f'description = "{pkg["description"]}"',
        f'repository_url = "{pkg["repo"]}"',
        'website_url = "https://mate-desktop.org/"',
        'authors = "The MATE Team"',
        'license = "LGPL-2.0-or-later"',
        f'browse_url = "{pkg["repo"]}"',
        f'dependencies = [{", ".join(json.dumps(k) for k in list(GIR_EXTERNAL_DOCS) + [n for n in all_ns if n != ns])}]',
        f'devhelp = false',
        f'search_index = true',
        "",
        "[theme]",
        'name = "basic"',
        'show_index_summary = true',
        'show_class_hierarchy = true',
        "",
        "[source-location]",
        f'base_url = "{pkg["repo"]}/blob/{pkg["commit"] or "master"}/"',
        "",
    ]
    for k, (label, url, desc) in GIR_EXTERNAL_DOCS.items():
        lines += [f'[dependencies."{k}"]', f'name = "{label}"', f'description = "{desc}"', f'docs_url = "{url}"', ""]
    for n in all_ns:
        if n != ns:
            lines += [f'[dependencies."{n}"]', f'name = "{n.rsplit("-", 1)[0]}"',
                      f'description = "MATE library ({owner_of.get(n, "MATE")})"', f'docs_url = "{API_URL}/lib/{n}/"', ""]
    return "\n".join(lines)


def cmd_gir(args):
    g = load_graph()
    pk = {p["name"]: p for p in g["packages"]}
    prefix = Path(args.prefix).resolve()
    out = Path(args.out) / "lib"
    failed = []
    if not args.skip_build:
        for name in GIR_BUILD:
            if name in pk:
                try:
                    build_library(name, args.src, prefix)
                except subprocess.CalledProcessError as e:
                    log(f"{name}: build failed ({e}); continuing")
                    failed.append(name)
    if not shutil.which("gi-docgen"):
        sys.exit("gi-docgen not found")

    girdir = prefix / "share" / "gir-1.0"
    girs = {f.stem: f for f in girdir.glob("*.gir")}
    # A namespace belongs to the package whose build tree generated it
    # (only installed ones count; that skips private helper GIRs).
    owner = {}
    for name in GIR_BUILD:
        for f in Path(args.src, name).rglob("*.gir"):
            if "mate-submodules" not in f.parts and f.stem in girs:
                owner[f.stem] = name
    mine = sorted(owner)
    tmp = SITE / ".cache" / "gidocgen"
    tmp.mkdir(parents=True, exist_ok=True)
    for ns in mine:
        pkg = pk.get(owner.get(ns, ""), None)
        if not pkg:
            continue
        conf = tmp / f"{ns}.toml"
        conf.write_text(gidocgen_config(ns, pkg, mine, owner))
        dest = out / ns
        shutil.rmtree(dest, ignore_errors=True)
        try:
            run(["gi-docgen", "generate", "--quiet", "--no-namespace-dir", f"--config={conf}",
                 f"--output-dir={dest}", f"--add-include-path={girdir}", "--add-include-path=/usr/share/gir-1.0",
                 girs[ns]])
        except subprocess.CalledProcessError:
            log(f"{ns}: gi-docgen failed")
            failed.append(ns)
    manifest = {ns: owner[ns] for ns in mine if (out / ns / "index.html").exists()}
    out.mkdir(parents=True, exist_ok=True)
    (out / "manifest.json").write_text(json.dumps(manifest, indent=1) + "\n")
    log(f"library reference: {len(mine) - len([f for f in failed if f in mine])}/{len(mine)} namespaces generated"
        + (f"; failed: {' '.join(failed)}" if failed else ""))


# ------------------------------------------------------------------ finalize

def cmd_finalize(args):
    g = load_graph()
    out = Path(args.out)
    try:
        manifest = json.loads((out / "lib" / "manifest.json").read_text())
    except (OSError, ValueError):
        manifest = {}
    # namespaces guessed from build files that the real build superseded (e.g. Matekbd-1.0 -> 3.0)
    built = {}
    for ns, owner in manifest.items():
        built.setdefault(owner, set()).add(ns.rsplit("-", 1)[0])
    stale = {p["name"]: [ns for ns in p["provides"]["gir"] if ns.rsplit("-", 1)[0] in built.get(p["name"], set()) and ns not in manifest]
             for p in g["packages"]}
    for p in g["packages"]:
        if (out / "src" / p["name"] / "index.html").exists():
            p["docs"]["source"] = f"{API_URL}/src/{p['name']}/"
        p["docs"]["library"] = [{"namespace": ns, "url": f"{API_URL}/lib/{ns}/"}
                                for ns, owner in sorted(manifest.items()) if owner == p["name"]]
        # what was actually built is authoritative over what the build files suggest
        p["provides"]["gir"] = sorted(set(p["provides"]["gir"]) - set(stale.get(p["name"], [])) | {d["namespace"] for d in p["docs"]["library"]})
    save_graph(g)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", default=str(DEFAULT_SRC), help="directory holding the MATE git checkouts")
    ap.add_argument("--out", default=str(DEFAULT_OUT), help="output directory for generated docs")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("clone").set_defaults(fn=cmd_clone)
    sub.add_parser("graph").set_defaults(fn=cmd_graph)
    p = sub.add_parser("doxygen")
    p.add_argument("-j", "--jobs", type=int)
    p.add_argument("packages", nargs="*", help="limit to these packages")
    p.set_defaults(fn=cmd_doxygen)
    p = sub.add_parser("gir")
    p.add_argument("--prefix", default=str(SITE / ".cache" / "gir-prefix"))
    p.add_argument("--skip-build", action="store_true", help="only run gi-docgen on an existing prefix")
    p.set_defaults(fn=cmd_gir)
    sub.add_parser("finalize").set_defaults(fn=cmd_finalize)
    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
