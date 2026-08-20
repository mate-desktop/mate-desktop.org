---
title: Development Environment
weight: 2
---

This page covers the tools that make MATE development comfortable: API documentation, editors, and utilities.

## API documentation with Devhelp

[Devhelp](https://apps.gnome.org/Devhelp/) gives you searchable, offline API documentation for GTK, GLib, GObject, and all installed development libraries. It is the fastest way to look up function signatures and struct members without leaving the desktop.

{{< tabs >}}
  {{< tab name="Debian/Ubuntu/Linux Mint" >}}
```bash
sudo apt install devhelp libgtk-3-doc libglib2.0-doc
```
  {{< /tab >}}
  {{< tab name="Fedora" >}}
```bash
sudo dnf install devhelp gtk3-devel-docs glib2-devel
```
  {{< /tab >}}
  {{< tab name="Arch Linux" >}}
```bash
sudo pacman -S devhelp
```
  {{< /tab >}}
{{< /tabs >}}

Start Devhelp and use **Ctrl+F** to search, or invoke it from the terminal:

```bash
devhelp --search g_signal_connect
```

## Editors and IDEs

| Tool | Notes |
|------|-------|
| [Pluma](../../user/applications/pluma) | MATE's own text editor — lightweight, ships with MATE |
| [VS Code](https://code.visualstudio.com/) | Great C/C++ extension, clangd support, ctags navigation |
| [GNOME Builder](https://apps.gnome.org/Builder/) | Deep GLib/GTK integration, GObject introspection, Flatpak build support |
| [Geany](https://www.geany.org/) | Lightweight IDE, fast symbol lookup, built-in terminal |

For VS Code, install the **C/C++** and **clangd** extensions. Generate `compile_commands.json` via `bear make` for accurate code navigation.

## Essential CLI tools

| Tool | Purpose |
|------|---------|
| `pkg-config` | Query compiler flags: `pkg-config --cflags --libs gtk+-3.0` |
| `gsettings` | Read/write GSettings keys at runtime |
| `dconf-editor` | Browse all GSettings keys graphically |
| `xdpyinfo` / `xwininfo` | Inspect X display and window properties |
| `gitg` / `gitk` | Graphical git history browser |
| `meld` | Visual diff and merge tool |
| `bear` | Wraps `make` to produce `compile_commands.json` for clangd |

## Virtual machine workflow

Working inside a VM keeps your main system clean and lets you snapshot before risky operations:

1. Install a MATE distribution iinside [VirtManager](https://virt-manager.org/), [GNOME Boxes](https://apps.gnome.org/Boxes/) or [VirtualBox](https://virtualbox.org).
2. Use shared folders or `sshfs` to edit files from your host editor.
3. Do all builds and `sudo make install` inside the VM.
4. Snapshot before installing — reset if anything breaks.
