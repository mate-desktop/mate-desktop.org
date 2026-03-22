---
title: Building from Source
weight: 3
---

Most MATE packages must be installed (not just compiled) to work correctly, because the installation step copies desktop files, schemas, icons, and libraries to the expected system locations.

## Install build dependencies

{{< tabs >}}
  {{< tab name="Debian/Ubuntu/Linux Mint" icon="server" >}}
```bash
sudo apt build-dep <package-name>
```
  {{< /tab >}}
  {{< tab name="Fedora" icon="server" >}}
```bash
sudo dnf builddep <package-name>
```
  {{< /tab >}}
{{< /tabs >}}

## Build

```bash
git submodule update --init --recursive   # initialise Git submodules
./autogen.sh --prefix=/usr                # configure the build
make                                      # compile
```

## Install

{{< callout type="warning" >}}
This installs directly into your system prefix (`/usr`) and will overwrite the packaged version of the component. Doing this inside a [virtual machine](../getting-started#development-environment) is strongly recommended.
{{< /callout >}}

```bash
sudo make install
```

## Uninstall

```bash
sudo make uninstall
```
