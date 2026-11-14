---
title: API Reference
linkTitle: API Reference
weight: 60
width: full
toc: false
description: "Interactive map of every MATE package, their dependencies, and the API reference for MATE libraries and applications."
---

The whole MATE desktop at a glance: every package, what it depends on, what depends on it, and the documentation for its code. The graph and the reference are rebuilt from the latest code of every MATE repository on each website deployment and nightly.

- **Library API** — reference for MATE's public libraries (`libmate-desktop`, `libmate-panel-applet`, `libcaja-extension`, `libmate-menu`, `libmatekbd`, Atril, Eom and Pluma plugin APIs), generated with [gi-docgen](https://gnome.pages.gitlab.gnome.org/gi-docgen/) from GObject-Introspection data. Start here when writing applets, Caja extensions or plugins.
- **Source reference** — Doxygen-generated reference for the internals of every C package, for contributors finding their way around the code.

{{< ecosystem-graph >}}
