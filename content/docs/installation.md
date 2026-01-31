---
title: Installation
weight: 2
---

MATE Desktop Environment is available in most Linux distributions. Here's how to install it on popular systems.

## Distributions with MATE by Default

These distributions ship with MATE as the default desktop:

- **Ubuntu MATE** - Official Ubuntu flavor
- **Linux Mint MATE Edition** - Popular user-friendly distribution
- **Debian MATE** - Stable and reliable
- **Fedora MATE Spin** - Cutting-edge with MATE

## Installing on Ubuntu/Debian

```bash
sudo apt update
sudo apt install mate-desktop-environment
```

For the full experience with all recommended packages:

```bash
sudo apt install mate-desktop-environment-extras
```

## Installing on Fedora

```bash
sudo dnf groupinstall "MATE Desktop"
```

## Installing on Arch Linux

```bash
sudo pacman -S mate mate-extra
```

## Installing on openSUSE

```bash
sudo zypper install -t pattern mate
```

## Post-Installation

After installation, log out of your current session and select MATE from your display manager's session selector before logging back in.

## Building from Source

For development or if packages aren't available for your distribution, you can build MATE from source. Visit the [MATE GitHub organization](https://github.com/mate-desktop) for source code and build instructions.
