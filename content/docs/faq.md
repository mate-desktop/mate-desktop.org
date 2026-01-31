---
title: FAQ
weight: 6
---

Frequently asked questions about MATE Desktop Environment.

## General

### What does MATE stand for?

MATE is named after *yerba mate*, a species of holly native to South America, and the caffeinated drink made from it. The name was chosen because it's a continuation of GNOME (which contains letters from "mate"), and because the MATE project was started by an Argentinian developer.

### Is MATE related to GNOME?

Yes. MATE is a fork of GNOME 2, which was discontinued in 2011. MATE continues development of the GNOME 2 codebase, providing the traditional desktop experience that many users prefer.

### Is MATE still actively developed?

Yes! MATE is actively maintained with regular releases. The project has a dedicated team of developers and a vibrant community of contributors.

### Is MATE only for older computers?

No. While MATE runs excellently on older hardware due to its efficiency, it's a full-featured desktop suitable for any computer. Many users choose MATE on modern hardware because they prefer the traditional desktop paradigm.

## Technical

### Does MATE support Wayland?

MATE is primarily designed for X11. Wayland support is being worked on, but X11 remains the recommended and fully supported option. Some MATE applications can run on Wayland through XWayland.

### Which GTK version does MATE use?

MATE uses GTK3. The project migrated from GTK2 to GTK3 several years ago while maintaining its classic look and feel.

### Can I use MATE applications on other desktops?

Yes! MATE applications like Caja, Pluma, and Atril work well on any GTK-based desktop environment. They'll integrate with your system theme and work alongside other applications.

### Does MATE support HiDPI displays?

Yes, MATE supports HiDPI (high resolution) displays. You can adjust the scaling in **System → Preferences → Look and Feel → Appearance → Fonts** and set the DPI manually if auto-detection doesn't work correctly.

## Customization

### Can I make MATE look like [another desktop]?

MATE is highly customizable. With the right themes, icons, and panel configuration, you can make it resemble many other desktop environments. The GTK3 base means most GTK themes work with MATE.

### How do I change the icon theme?

1. Install icon themes via your package manager
2. Go to **System → Preferences → Look and Feel → Appearance**
3. Click the **Theme** tab and customize, or use **Customize** to pick an icon theme

### Can I have multiple panels?

Yes! Right-click on an existing panel and select **New Panel**. You can have panels on any edge of the screen, with different sizes and content.

### How do I change the login screen?

The login screen (display manager) is separate from MATE. Common display managers include LightDM and GDM. Configuration depends on which one your distribution uses:

- **LightDM**: `/etc/lightdm/lightdm.conf`
- **GDM**: GNOME Settings app

## Comparison

### MATE vs Cinnamon?

Both are forks aimed at preserving traditional desktop experience:
- **MATE** forked GNOME 2 directly, maintaining its codebase
- **Cinnamon** was built on GNOME 3 technologies but with a traditional interface

MATE is generally lighter on resources, while Cinnamon offers more modern effects.

### MATE vs Xfce?

Both are lightweight, traditional desktops:
- **MATE** came from GNOME 2 and maintains that workflow
- **Xfce** was independently developed with similar goals

They're similar in resource usage. Choose based on which applications and workflow you prefer.

### MATE vs GNOME 3/4?

GNOME 3+ adopted a very different interface paradigm (GNOME Shell). MATE preserves the GNOME 2 experience with:
- Traditional application menu
- Panel-based workflow
- Window list and minimization
- No activities overlay

## Contributing

### How can I contribute to MATE?

Many ways:
- **Code**: Submit patches on [GitHub](https://github.com/mate-desktop)
- **Translations**: Help translate via [Transifex](https://www.transifex.com/mate/MATE/)
- **Testing**: Try pre-release versions and report bugs
- **Documentation**: Improve wiki and help files
- **Support**: Help users in forums and chat

### Where do I report bugs?

Report bugs on the relevant GitHub repository under the [mate-desktop organization](https://github.com/mate-desktop). Include:
- Distribution and version
- MATE version
- Steps to reproduce
- Expected vs actual behavior

### How can I test development versions?

- **Debian/Ubuntu**: Use the MATE testing PPA
- **Arch**: AUR has development packages
- **Fedora**: COPR repositories available
- **Build from source**: Clone from GitHub and compile
