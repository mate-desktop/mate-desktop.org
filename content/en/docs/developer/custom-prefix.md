---
title: Custom Prefix Installation
weight: 8
---

When you compile MATE from source you will typically install it into a directory other than `/usr` so that it does not interfere with the version your package manager installed. The most common choice is `/usr/local`, which is where compiled software traditionally lives on UNIX systems. This page explains every piece you need to wire together so that a custom-prefix MATE build is fully functional — from the shell environment all the way to the login screen.

## Why a separate prefix?

| | System prefix (`/usr`) | Custom prefix (`/usr/local`) |
|---|---|---|
| Managed by | Package manager | You |
| Upgraded with distro | Yes (may overwrite your changes) | No |
| Affects all users immediately | Yes | Only after env setup |
| Easy to remove | No | Yes — just delete the tree |

Installing into `/usr/local` keeps every MATE binary, library, schema, icon, and data file under a clean, parallel directory tree. You can wipe it and start fresh without touching the rest of the system.

## Directory layout under `PREFIX=/usr/local`

After a full build the prefix tree looks like:

```
/usr/local/
├── bin/          ← mate-session, caja, pluma, marco, ...
├── lib/          ← libmate-desktop.so, libcaja-extension.so, ...
│   ├── pkgconfig/        ← .pc files used by pkg-config
│   └── mate-panel/       ← panel applet factory executables
├── libexec/      ← internal helper binaries (mate-settings-daemon helpers, ...)
├── share/
│   ├── applications/     ← .desktop files
│   ├── dbus-1/services/  ← D-Bus service activation files
│   ├── glib-2.0/schemas/ ← compiled GSettings schema database
│   ├── icons/            ← icon themes
│   ├── mate/             ← core MATE data
│   ├── mate-panel/       ← applet definitions
│   └── xsessions/        ← session .desktop files (handled separately, see below)
└── etc/
    └── xdg/autostart/    ← autostart entries specific to this build
```

## Environment variables

The shell needs five variables set **before** you run any binary from the custom prefix — both for interactive terminal use and for building further packages against it.

### `PATH`

```bash
export PATH="/usr/local/bin:$PATH"
```

This puts the custom binaries first. `which mate-session` should now return `/usr/local/bin/mate-session`.

### `PKG_CONFIG_PATH`

`pkg-config` searches this colon-separated list for `.pc` files. On a multiarch system (e.g. x86_64 Debian) there is a three-way triplet directory as well:

```bash
TRIPLET="$(gcc -print-multiarch 2>/dev/null)"   # e.g. x86_64-linux-gnu
export PKG_CONFIG_PATH="\
/usr/local/lib/$TRIPLET/pkgconfig:\
/usr/local/lib/pkgconfig:\
/usr/local/lib64/pkgconfig:\
${PKG_CONFIG_PATH:-}"
```

To verify a package is found:

```bash
pkg-config --modversion mate-desktop-2.0
# → 1.28.2
```

### `LD_LIBRARY_PATH`

The dynamic linker searches this list at **run time**. Without it, programs will fail to start because `libmate-desktop.so` cannot be found:

```bash
export LD_LIBRARY_PATH="\
/usr/local/lib/$TRIPLET:\
/usr/local/lib:\
/usr/local/lib64:\
${LD_LIBRARY_PATH:-}"
```

{{< callout type="info" >}}
`LD_LIBRARY_PATH` is a session-level override. The preferred production approach is to bake the path into the binaries at link time with `-Wl,-rpath,/usr/local/lib` (see [Library Tools](../library-tools#rpath-vs-ld_library_path)). The build scripts already add this flag so installed binaries find their libraries even in a clean login session without `LD_LIBRARY_PATH`.
{{< /callout >}}

### `XDG_DATA_DIRS`

GTK, GLib, and most freedesktop-aware programs look for icons, schemas, `.desktop` files, and mime types in the directories listed here:

```bash
export XDG_DATA_DIRS="/usr/local/share:${XDG_DATA_DIRS:-/usr/local/share:/usr/share}"
```

Without this, MATE will use system icons and themes rather than any updated ones in the custom prefix.

### `LDFLAGS` (compile time only)

When building packages **against** the custom prefix, add an rpath so the resulting binaries carry the search path into them:

```bash
export LDFLAGS="-Wl,-rpath,/usr/local/lib:/usr/local/lib/$TRIPLET ${LDFLAGS:-}"
```

## Persistent environment profile

Setting these variables by hand in every terminal is impractical. Create a drop-in file under `/etc/profile.d/` so they are exported for every login shell:

```bash
sudo tee /etc/profile.d/mate-prefix.sh > /dev/null << 'EOF'
# Custom MATE prefix environment
_MATE_PREFIX="/usr/local"
_TRIPLET="$(gcc -print-multiarch 2>/dev/null || true)"

export PATH="$_MATE_PREFIX/bin:$PATH"
export XDG_DATA_DIRS="$_MATE_PREFIX/share:${XDG_DATA_DIRS:-/usr/local/share:/usr/share}"

_PKG="$_MATE_PREFIX/lib/pkgconfig:$_MATE_PREFIX/lib64/pkgconfig"
_LD="$_MATE_PREFIX/lib:$_MATE_PREFIX/lib64"
if [ -n "$_TRIPLET" ]; then
    _PKG="$_MATE_PREFIX/lib/$_TRIPLET/pkgconfig:$_PKG"
    _LD="$_MATE_PREFIX/lib/$_TRIPLET:$_LD"
fi
export PKG_CONFIG_PATH="${_PKG}:${PKG_CONFIG_PATH:-}"
export LD_LIBRARY_PATH="${_LD}:${LD_LIBRARY_PATH:-}"
unset _MATE_PREFIX _TRIPLET _PKG _LD
EOF
```

The file is sourced automatically by `bash`, `dash`, and `sh` login shells. Log out and back in, or run `source /etc/profile.d/mate-prefix.sh` in your current session, for it to take effect.

{{< callout type="warning" >}}
Files in `/etc/profile.d/` are sourced for **all** users. If you share the machine with others you may prefer to put the same content in `~/.profile` or `~/.bash_profile` for your user only.
{{< /callout >}}

## Post-install cache updates

After installing, several caches need to be regenerated before the new components are fully visible to the rest of the desktop.

### GSettings schemas

MATE stores its configuration schema in a compiled binary database. Whenever you install (or update) a package that ships `.gschema.xml` files, regenerate it:

```bash
sudo glib-compile-schemas /usr/local/share/glib-2.0/schemas/
```

If the schema is missing or stale, MATE applications will crash at startup with a message like:
```
GLib-GIO-ERROR: Settings schema 'org.mate.panel' is not installed
```

### Icon theme cache

```bash
gtk-update-icon-cache -q /usr/local/share/icons/hicolor/
```

### Desktop file database

```bash
update-desktop-database /usr/local/share/applications/
```

## Xsession file

A **display manager** (the graphical login screen) must know about your custom MATE build to offer it as a choosable session. It scans the directory `/usr/share/xsessions/` for `.desktop` files; each file describes one session.

Create an entry that points to the `mate-session` binary in your custom prefix:

```bash
sudo tee /usr/share/xsessions/mate-custom.desktop > /dev/null << 'EOF'
[Desktop Entry]
Name=MATE (custom build)
Comment=MATE Desktop Environment — built from source
Type=Application
Exec=/usr/local/bin/mate-session
Icon=
EOF
```

{{< callout type="info" >}}
The file must live in `/usr/share/xsessions/`, **not** in `/usr/local/share/xsessions/`. Display managers only scan the systemwide path regardless of your custom prefix.
{{< /callout >}}

### What `Exec=` actually does

When a user selects the session and logs in, the display manager runs the `Exec` command as the user's session process. `mate-session` reads `~/.config/mate-session/` and `/etc/xdg/mate-session/` for autostart lists, then launches the window manager (`marco`), the settings daemon, the panel, and the file manager.

For a custom-prefix build, all of these are found via `PATH` — which is why the environment profile in the previous section must be in place **before** the session starts.

## Display managers

A **display manager** (DM) is the greeter program that shows the login screen, authenticates users via PAM, starts the chosen X or Wayland session, and sets up a minimal base environment. Each common DM handles the session environment slightly differently.

### LightDM

LightDM is the DM most commonly paired with MATE. Its configuration lives in `/etc/lightdm/lightdm.conf`:

```ini
[SeatDefaults]
# Make sure xsession files are read from their standard location:
sessions-directory=/usr/share/xsessions
# Optional: set a default session
user-session=mate-custom
# Source /etc/profile when starting the session wrapper:
session-wrapper=/etc/lightdm/Xsession
```

The `session-wrapper` script is where your `/etc/profile.d/` files are sourced — this is how the custom-prefix environment variables reach the MATE session. Verify it is set:

```bash
grep session-wrapper /etc/lightdm/lightdm.conf
```

If it is commented out, the default Xsession wrapper is used; on Debian/Ubuntu that wrapper already sources `/etc/profile.d/*.sh`.

Restart LightDM to pick up configuration changes:

```bash
sudo systemctl restart lightdm
```

### GDM (GNOME Display Manager)

GDM reads `/usr/share/xsessions/` automatically. It does **not** source `/etc/profile.d/` for X sessions; instead, add environment overrides to `~/.config/environment.d/mate-prefix.conf`:

```ini
PATH=/usr/local/bin:/usr/bin:/bin
PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
LD_LIBRARY_PATH=/usr/local/lib
XDG_DATA_DIRS=/usr/local/share:/usr/share
```

Files in `~/.config/environment.d/` are read by `systemd --user` and exported to all user services and graphical sessions.

### SDDM

SDDM (used by KDE Plasma) also reads `/usr/share/xsessions/`. Environment overrides go in `/etc/sddm.conf` or a drop-in under `/etc/sddm.conf.d/`:

```ini
[X11]
DisplayCommand=/etc/sddm/Xsetup
SessionCommand=/etc/sddm/Xsession
```

Source your profile inside `Xsession` or add a dedicated `Xsetup` script that exports the custom-prefix variables.

## Verifying the session environment

Once you have logged in to the custom MATE session, open a terminal and confirm the environment is correct:

```bash
# Binary comes from the custom prefix
which mate-session                     # → /usr/local/bin/mate-session

# Library version matches what was built
pkg-config --modversion mate-desktop-2.0

# Dynamic linker knows the custom prefix
ldconfig -p | grep libmate-desktop     # should show /usr/local/lib entry

# D-Bus services from the custom prefix are found
ls /usr/local/share/dbus-1/services/  # mate-panel.service, etc.
```

## Quick reference: building a single package against the prefix

If `PKG_CONFIG_PATH`, `LD_LIBRARY_PATH`, `LDFLAGS`, and `PATH` are all exported (as above), building another package against the custom prefix needs no special flags:

```bash
git clone https://github.com/mate-desktop/pluma
cd pluma
./autogen.sh --prefix=/usr/local
make -j$(nproc)
sudo make install
# Re-run post-install steps:
sudo glib-compile-schemas /usr/local/share/glib-2.0/schemas/
update-desktop-database /usr/local/share/applications/
```

`autogen.sh` (via `pkg-config`) automatically finds dependencies in `/usr/local` because `PKG_CONFIG_PATH` is set, and the installed binary will carry the correct rpath from `LDFLAGS`.
