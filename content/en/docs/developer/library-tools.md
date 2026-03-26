---
title: Library & Binary Tools
weight: 9
---

Understanding what libraries a program needs, which package provides a file, and whether the right version is actually loaded are everyday tasks in MATE development. This page covers the tools that answer those questions.

## pkg-config

`pkg-config` is the standard way to query metadata about installed development libraries. It reads `.pc` files (found in `lib/pkgconfig/`) and outputs the compiler and linker flags a package needs.

### Check installed version

```bash
pkg-config --modversion gtk+-3.0
# → 3.24.38

pkg-config --modversion mate-desktop-2.0
# → 1.28.2

pkg-config --modversion libmatepanelapplet-4.0
# → 1.28.0
```

If the package is not found you will see:
```
Package gtk+-3.0 was not found in the pkg-config search path.
```

That means either the **development package** (e.g. `libgtk-3-dev`) is not installed, or `PKG_CONFIG_PATH` does not include the directory where the `.pc` file lives. See [Custom Prefix Installation](../custom-prefix#pkg_config_path) for setting `PKG_CONFIG_PATH` when building against a non-system prefix.

### Get compiler and linker flags

```bash
pkg-config --cflags gtk+-3.0
# → -I/usr/include/gtk-3.0 -I/usr/include/pango-1.0 ...

pkg-config --libs gtk+-3.0
# → -lgtk-3 -lgdk-3 -lpangocairo-1.0 ...

pkg-config --cflags --libs gtk+-3.0 glib-2.0
```

These are exactly the flags that go into `Makefile`s and `meson.build` files via `PKG_CHECK_MODULES`.

### Query individual variables

`.pc` files can expose arbitrary named variables:

```bash
pkg-config --variable=prefix mate-desktop-2.0
# → /usr/local

pkg-config --variable=datadir mate-desktop-2.0
# → /usr/local/share

pkg-config --variable=exec_prefix glib-2.0
```

### List all known packages

```bash
pkg-config --list-all | grep mate
```

### Show where the .pc file lives

```bash
PKG_CONFIG_DEBUG_SPEW=1 pkg-config --modversion mate-desktop-2.0 2>&1 | grep "Scanning"
```

Or simply:

```bash
find /usr/local/lib /usr/lib -name "mate-desktop-2.0.pc" 2>/dev/null
```

---

## Finding which package provides a file

When a `./autogen.sh` or `meson setup` fails with a missing header or `.pc` file, you need to find out which distribution package provides it.

### Debian / Ubuntu — `apt-file`

`apt-file` searches the **full package file lists** from all enabled repositories, including packages that are not installed:

```bash
# Install once
sudo apt install apt-file
sudo apt-file update      # syncs the file database (needed after apt-file install)

# Find the package that provides a header
apt-file search atk/atk.h
# → libatk1.0-dev: /usr/include/atk-1.0/atk/atk.h

# Find the package that provides a .pc file
apt-file search mate-desktop-2.0.pc
# → libmate-desktop-dev: /usr/lib/x86_64-linux-gnu/pkgconfig/mate-desktop-2.0.pc

# Find the package that provides a shared library
apt-file search libmate-desktop.so.2
# → libmate-desktop-2-2: /usr/lib/x86_64-linux-gnu/libmate-desktop.so.2.1.0
```

The output format is `package-name: /full/path/to/file`.

{{< callout type="info" >}}
`apt-file search` searches **uninstalled** packages too. For installed packages only, use `dpkg -S /usr/include/atk-1.0/atk/atk.h` — but `apt-file` is more useful when you need to install something new.
{{< /callout >}}

### Fedora / RHEL — `dnf provides`

```bash
# Find the package that provides a header
dnf provides '*/atk/atk.h'
# → atk-devel-2.36.0-4.fc38.x86_64 : Development files for the ATK library

# Find the package that provides a .pc file
dnf provides 'pkgconfig(mate-desktop-2.0)'
# → mate-desktop-devel-1.28.0-1.fc38.x86_64

# Short form for pkgconfig queries
dnf provides 'pkgconfig(gtk+-3.0)'
```

The `pkgconfig(name)` syntax is especially handy — it queries by the logical package name rather than the file path.

```bash
# Also works as a file glob
dnf provides '*/libmate-desktop.so'
```

---

## `nm` — symbol inspection

`nm` lists the **symbol table** of object files (`.o`), static libraries (`.a`), and shared libraries (`.so`). It is the primary tool for diagnosing "undefined symbol" linker errors and for checking whether a function was compiled into a binary.

### Inspect a shared library

```bash
nm -D /usr/local/lib/libmate-desktop.so
```

`-D` prints only the **dynamic** symbol table — the symbols that are exported and visible to other programs at runtime. Output columns:

```
0000000000012a30 T mate_desktop_thumbnail_is_valid
                 U g_object_ref
0000000000019c80 W mate_bg_new
```

| Column | Meaning |
|--------|---------|
| Address | Hex offset in the file (blank for undefined symbols) |
| Type letter | `T` = defined in `.text` (code), `U` = undefined (imported), `W` = weak definition |
| Name | Symbol name |

### Common type letters

| Letter | Meaning |
|--------|---------|
| `T` / `t` | Text (code) section — uppercase = global (exported) |
| `D` / `d` | Initialized data section |
| `B` / `b` | Uninitialized data (BSS) |
| `U` | Undefined — symbol is used but defined elsewhere |
| `W` / `w` | Weak symbol — overridable by a strong symbol |
| `R` / `r` | Read-only data |

### Find where a function is defined

```bash
nm -D /usr/local/lib/libmate-desktop.so | grep mate_bg_
```

### Check if a binary has a symbol

```bash
nm -D /usr/local/bin/mate-session | grep -i "main"
```

### Demangle C++ symbol names

```bash
nm -D --demangle /usr/local/lib/libsomething.so
```

### Show only undefined symbols (the imports)

```bash
nm --undefined-only -D /usr/local/bin/caja
# Shows every shared symbol caja depends on being provided by other libraries
```

---

## Dynamic linking

### How the dynamic linker finds libraries

When you run a dynamically linked binary, the kernel hands control to the **dynamic linker** (`/lib64/ld-linux-x86-64.so.2`). It must resolve every `U` (undefined) symbol the binary imports before `main()` runs. It searches in this order:

1. **RPATH** — paths baked into the binary at link time (see below)
2. **`LD_LIBRARY_PATH`** — colon-separated list from the environment
3. **`/etc/ld.so.cache`** — a binary cache of well-known library directories, built by `ldconfig`
4. **Default paths** — `/lib`, `/usr/lib`, and their 64-bit counterparts

### `ldd` — show runtime dependencies

```bash
ldd /usr/local/bin/mate-session
```

Example output:

```
libmate-desktop-2.so.2 => /usr/local/lib/libmate-desktop-2.so.2
libgl.so.1            => /usr/lib/x86_64-linux-gnu/libgl.so.1
libglib-2.0.so.0      => /usr/lib/x86_64-linux-gnu/libglib-2.0.so.0
...
```

If a library is missing you will see:

```
libmate-desktop-2.so.2 => not found
```

That means neither RPATH, `LD_LIBRARY_PATH`, nor `ldconfig`'s cache knows where the library is.

{{< callout type="warning" >}}
Never run `ldd` on untrusted binaries. `ldd` actually executes the binary's dynamic linker and some ELF initializers run as a side effect. Use `objdump -p binary | grep NEEDED` as a safe alternative to list dependencies without running anything.
{{< /callout >}}

### RPATH vs `LD_LIBRARY_PATH`

| | RPATH | `LD_LIBRARY_PATH` |
|---|---|---|
| Stored in | The ELF binary | Shell environment |
| Set by | Linker flag `-Wl,-rpath,/path` | User / profile script |
| Scope | Affects only that binary | Affects all binaries in the session |
| Overridable | Only by `LD_LIBRARY_PATH` (for regular rpath) | Yes, always |
| Good for | Installed software with private libraries | Development sessions, custom-prefix builds |

When building against a custom prefix, rpath is baked in automatically by passing `-Wl,-rpath,/usr/local/lib` via `LDFLAGS`:

```bash
export LDFLAGS="-Wl,-rpath,/usr/local/lib:/usr/local/lib/x86_64-linux-gnu"
./autogen.sh --prefix=/usr/local
make -j$(nproc)
sudo make install
```

Verify the rpath was embedded:

```bash
objdump -p /usr/local/bin/mate-session | grep RPATH
# or
readelf -d /usr/local/bin/mate-session | grep -E 'RPATH|RUNPATH'
```

### `ldconfig` — update the linker cache

After installing new libraries to a non-default directory, tell `ldconfig` to index them:

```bash
# Add the directory permanently
echo /usr/local/lib | sudo tee /etc/ld.so.conf.d/mate-local.conf
sudo ldconfig

# Or one-shot (not persistent across reboots)
sudo ldconfig /usr/local/lib
```

Verify the cache:

```bash
ldconfig -p | grep libmate
```

### soname and library versioning

Every installed shared library follows a three-part naming convention:

```
libmate-desktop-2.so.2.1.0    ← real filename (full version)
libmate-desktop-2.so.2         ← soname (major version only, symlink)
libmate-desktop-2.so           ← link-name (for the linker, symlink)
```

| Name | Used by | Encoding |
|------|---------|---------|
| Real name | `ls`, `nm`, the file system | `lib<name>.so.<major>.<minor>.<revision>` |
| soname | Dynamic linker at runtime | `lib<name>.so.<major>` |
| Link name | Linker at build time (`-lmate-desktop-2`) | `lib<name>.so` |

`ldconfig` creates the soname symlink automatically. If you install a `.so` file manually and the symlink is missing, programs will fail to start even if the file exists.

```bash
ls -la /usr/local/lib/libmate-desktop*
# libmate-desktop-2.so         -> libmate-desktop-2.so.2
# libmate-desktop-2.so.2       -> libmate-desktop-2.so.2.1.0
# libmate-desktop-2.so.2.1.0
```

### `readelf` — deeper ELF inspection

```bash
# List all shared library dependencies
readelf -d /usr/local/bin/caja | grep NEEDED

# Check architecture
readelf -h /usr/local/lib/libmate-desktop.so | grep "Machine\|Class"

# Show all dynamic section entries
readelf -d /usr/local/lib/libmate-desktop.so
```

---

## Diagnosing common problems

### "cannot open shared object file"

```
error while loading shared libraries: libmate-desktop-2.so.2: cannot open shared object file
```

Run through the checklist:

```bash
# 1. Does the file exist?
find /usr/local/lib -name "libmate-desktop-2.so.2"

# 2. Is it in ldconfig's cache?
ldconfig -p | grep libmate-desktop

# 3. Does LD_LIBRARY_PATH include the directory?
echo $LD_LIBRARY_PATH

# 4. Does the binary have an rpath pointing there?
readelf -d /usr/local/bin/mate-session | grep -E 'RPATH|RUNPATH'
```

### "Package not found" in pkg-config

```
Package 'mate-desktop-2.0', required by 'mate-panel', not found
```

```bash
# Where is the .pc file?
find /usr/local /usr/lib -name "mate-desktop-2.0.pc"

# Is that directory in PKG_CONFIG_PATH?
echo $PKG_CONFIG_PATH

# Which package provides it? (Debian)
apt-file search mate-desktop-2.0.pc

# Which package provides it? (Fedora)
dnf provides 'pkgconfig(mate-desktop-2.0)'
```

### "undefined reference to" at link time

```bash
# Is the symbol present in the library?
nm -D /usr/local/lib/libmate-desktop.so | grep the_missing_symbol

# Is the library listed in the pkg-config output?
pkg-config --libs mate-desktop-2.0

# Build with verbose linker output to see what is/isn't linked
make LDFLAGS="-Wl,--verbose"
```
