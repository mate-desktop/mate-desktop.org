---
title: Installation
weight: 2
---

MATE Desktop is available for most Linux and BSD distributions. Choose your preferred distribution below.

## Distributions with MATE Pre-installed

These distributions ship MATE as the default desktop environment:

{{< cards >}}
  {{< card link="https://ubuntu-mate.org" title="Ubuntu MATE" icon="external-link" subtitle="Official Ubuntu flavor with MATE" >}}
  {{< card link="https://www.linuxmint.com/edition.php?id=328" title="Linux Mint MATE" icon="external-link" subtitle="User-friendly, based on Ubuntu" >}}
  {{< card link="https://fedoraproject.org/spins/mate/" title="Fedora MATE-Compiz" icon="external-link" subtitle="Cutting-edge Fedora with MATE" >}}
  {{< card link="https://cdimage.debian.org/debian-cd/current-live/amd64/iso-hybrid/" title="Debian" icon="external-link" subtitle="MATE available as a desktop option" >}}
{{< /cards >}}

{{< tabs items="Ubuntu/Debian,Fedora,Arch Linux,openSUSE" >}}

{{< tab >}}
```bash
sudo apt install mate-desktop-environment
```

For the full experience with all recommended packages:

```bash
sudo apt install mate-desktop-environment-extras
```
{{< /tab >}}

{{< tab >}}
```bash
sudo dnf groupinstall "MATE Desktop"
```
{{< /tab >}}

{{< tab >}}
```bash
sudo pacman -S mate mate-extra
```
{{< /tab >}}

{{< tab >}}
```bash
sudo zypper install -t pattern mate
```
{{< /tab >}}

{{< /tabs >}}

## Post-Installation

After installation, log out of your current session and select MATE from your display manager's session selector before logging back in.

## Building from Source

For development or if packages aren't available for your distribution, you can build MATE from source. Visit the [MATE GitHub organization](https://github.com/mate-desktop) for source code and build instructions.
