---
title: Building from Source
weight: 3
---

Most MATE packages must be **installed**, not just compiled. The installation step copies desktop files, GSettings schemas, icons, and shared libraries to the locations the rest of the system expects to find them.

{{< callout type="warning" >}}
Installing into `/usr` overwrites your distribution's packaged version of that component. Always work inside a [virtual machine](../dev-environment#virtual-machine-workflow) so your main system stays intact.
{{< /callout >}}

## Clone the repository

All MATE repositories are hosted under [github.com/mate-desktop](https://github.com/mate-desktop). Clone the one you want to work on:

```bash
git clone https://github.com/mate-desktop/<package-name>
cd <package-name>
git submodule update --init --recursive
```

The submodule step is only needed for packages that have them (most do not).

## Install build dependencies

The easiest way to get all required headers and libraries is to ask the package manager for the build-dependencies of the already-packaged version:

{{< tabs >}}
  {{< tab name="Debian/Ubuntu/Linux Mint" >}}
First make sure source repositories are enabled — `apt build-dep` reads from them:

```bash
sudo apt-get build-dep <package-name>
```

If the package is not in your repositories, install the dependencies manually by looking at the `configure.ac` or `meson.build` file for `PKG_CHECK_MODULES` calls.
  {{< /tab >}}
  {{< tab name="Fedora" >}}
```bash
sudo dnf builddep <package-name>
```
  {{< /tab >}}
  {{< tab name="Arch Linux" >}}
```bash
# Install the base-devel group if you have not already
sudo pacman -S --needed base-devel

# Use asp to get the PKGBUILD and read its makedepends list
asp checkout <package-name>
```
  {{< /tab >}}
{{< /tabs >}}

## Build systems

Most MATE packages support both **Autotools** (`autogen.sh` + `make`) and **Meson** (`meson` + `ninja`). Both are fine. Meson is faster for incremental builds.

### Autotools

```bash
./autogen.sh --prefix=/usr
make -j$(nproc)
```

`--prefix=/usr` is important — without it, files land in `/usr/local` and many components will not find each other at runtime (D-Bus services, GSettings schemas, icon themes).

`-j$(nproc)` compiles on all available CPU cores.

To see every available configure option:

```bash
./autogen.sh --help
```

Common flags:

| Flag | Effect |
|------|--------|
| `--enable-debug` | Enable extra runtime checks (if supported) |
| `--disable-silent-rules` | Show the full compiler command for each file |
| `--with-gtk=3.0` | Select GTK version (where configurable) |

### Meson

```bash
meson setup build --prefix=/usr
ninja -C build -j$(nproc)
```

To see all build options:

```bash
meson configure build
```

Change an option after the initial setup:

```bash
meson configure build -Doption=value
ninja -C build
```

## Install

### Autotools

```bash
sudo make install
```

### Meson

```bash
sudo ninja -C build install
```

## Verify the installation

Check that the new binary is picked up:

```bash
which <binary-name>
<binary-name> --version
```

For GSettings schemas to take effect immediately without logging out:

```bash
sudo glib-compile-schemas /usr/share/glib-2.0/schemas/
```

## Rebuild after changes

Only the files that changed are recompiled. After editing source files:

### Autotools

```bash
make -j$(nproc)
sudo make install
```

### Meson

```bash
ninja -C build -j$(nproc)
sudo ninja -C build install
```

For some components you can run the binary directly from the build tree without installing — useful for quick tests. Whether this works depends on the component: standalone applications often work, while panel applets and background daemons generally require installation.

## Debug builds

To produce debug symbols and disable optimisation (required before using GDB or Valgrind — see [Debugging](../debugging)):

### Autotools

```bash
./autogen.sh --prefix=/usr CFLAGS="-g -O0"
```

### Meson

```bash
meson setup build --prefix=/usr --buildtype=debug
```

## Uninstall

### Autotools

```bash
sudo make uninstall
```

### Meson

Meson does not have a built-in uninstall target, but it records every installed file:

```bash
sudo ninja -C build uninstall
```

## Common errors

**`configure: error: Package requirements ... were not met`**
A required library or its development headers are missing. The error message names the `pkg-config` package. Install the corresponding `-dev` / `-devel` package.

**`GLib-GIO-ERROR: No GSettings schemas are installed`**
The schemas were not compiled after installation. Run:
```bash
sudo glib-compile-schemas /usr/share/glib-2.0/schemas/
```

**`error while loading shared libraries`**
A newly installed library is not visible to the dynamic linker. Run:
```bash
sudo ldconfig
```

**Icons or theme not updating**
Regenerate the icon cache for the affected theme:
```bash
sudo gtk-update-icon-cache /usr/share/icons/<theme-name>/
```
