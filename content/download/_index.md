---
title: Download
---

MATE Desktop is available for most Linux and BSD distributions. Choose your preferred distribution below.

## Distributions with MATE Pre-installed

These distributions ship MATE as the default desktop environment:

{{< cards >}}
  {{< card link="https://ubuntu-mate.org" title="Ubuntu MATE" icon="external-link" subtitle="Official Ubuntu flavor with MATE" >}}
  {{< card link="https://linuxmint.com" title="Linux Mint MATE" icon="external-link" subtitle="User-friendly, based on Ubuntu" >}}
  {{< card link="https://fedoraproject.org/spins/mate-compiz/" title="Fedora MATE-Compiz" icon="external-link" subtitle="Cutting-edge Fedora with MATE" >}}
  {{< card link="https://www.debian.org" title="Debian" icon="external-link" subtitle="MATE available as a desktop option" >}}
{{< /cards >}}

## Installing on Your Distribution

### Debian / Ubuntu

```bash
sudo apt update
sudo apt install mate-desktop-environment
```

For the complete experience:

```bash
sudo apt install mate-desktop-environment-extras
```

### Fedora

```bash
sudo dnf groupinstall "MATE Desktop"
```

### Arch Linux

```bash
sudo pacman -S mate mate-extra
```

### openSUSE

```bash
sudo zypper install -t pattern mate
```

### Gentoo

```bash
emerge --ask mate-base/mate
```

### FreeBSD

```bash
pkg install mate-desktop
```

Or via ports:

```bash
cd /usr/ports/x11/mate-desktop && make install clean
```

### Void Linux

```bash
sudo xbps-install -S mate
```

### Solus

```bash
sudo eopkg install -c desktop.mate
```

## Source Code

Build MATE from source for development or if packages aren't available:

- **GitHub Organization**: [github.com/mate-desktop](https://github.com/mate-desktop)
- **Build Instructions**: See README in each repository

### Core Components

| Component | Description | Repository |
|-----------|-------------|------------|
| mate-desktop | Core desktop libraries | [GitHub](https://github.com/mate-desktop/mate-desktop) |
| mate-panel | Desktop panel | [GitHub](https://github.com/mate-desktop/mate-panel) |
| caja | File manager | [GitHub](https://github.com/mate-desktop/caja) |
| marco | Window manager | [GitHub](https://github.com/mate-desktop/marco) |
| mate-session-manager | Session manager | [GitHub](https://github.com/mate-desktop/mate-session-manager) |
| mate-settings-daemon | Settings daemon | [GitHub](https://github.com/mate-desktop/mate-settings-daemon) |
| mate-control-center | Control center | [GitHub](https://github.com/mate-desktop/mate-control-center) |

## Release Archives

Official release tarballs are available on our [releases page](/releases/) or directly from each repository's GitHub releases.

## Verification

For security, verify downloads using:

```bash
# Check GPG signature
gpg --verify mate-desktop-x.xx.x.tar.xz.sig mate-desktop-x.xx.x.tar.xz
```

## Next Steps

After installing MATE:

1. Log out of your current session
2. Select "MATE" from your display manager's session menu
3. Log in and enjoy your new desktop!

Check out the [Getting Started](/docs/getting-started) guide for tips on using MATE.
