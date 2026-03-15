---
title: Mozo
weight: 10
---

![Mozo icon](https://raw.githubusercontent.com/mate-desktop/mozo/master/data/icons/hicolor_apps_48x48_mozo.png)

{{< badge content="Source Code" link="https://github.com/mate-desktop/mozo" icon="github" >}}
{{< badge content="Bug Tracker" link="https://github.com/mate-desktop/mozo/issues" icon="exclamation-circle" >}}

Mozo is the official menu editor for the MATE desktop. It provides a graphical interface for customizing the application menu, following the [freedesktop.org menu specification](https://specifications.freedesktop.org/menu-spec/latest/). It is a fork of Alacarte.

Open it from **System → Preferences → Main Menu** or by right-clicking the Applications menu and choosing **Edit Menus**.

![Mozo window](/img/applications/mozo-window.png "Mozo menu editor")

## Features

- **Show and hide entries** — toggle the visibility of any application without deleting it
- **Add new items** — create launchers for applications, links, or scripts
- **Edit existing entries** — change name, icon, command, and description
- **Reorder items** — drag entries within a menu to rearrange them
- **Create submenus** — add new categories and nest them within existing ones
- **Undo and redo** — revert accidental changes
- Changes are stored in the user's `~/.local/share/applications` and `~/.config/menus` directories and do not affect system-wide menu files
