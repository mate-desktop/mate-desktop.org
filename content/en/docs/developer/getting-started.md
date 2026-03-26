---
title: Getting Started
weight: 1
---

MATE is written almost entirely in **C** using **GLib**, **GObject**, and **GTK 3**, with some components in Python or C++. If you are new to C, the [C Wikibook](https://en.wikibooks.org/wiki/C_Programming) (*Introduction* through *Intermediate C*) is a solid starting point before diving into the codebase.

## Workflow overview

Contributing to MATE follows a standard open-source workflow:

{{% steps %}}

### Set up your environment

Install the tools you need — a C compiler, Make, Git, an editor, and the Devhelp API browser. See [Development Environment](../dev-environment).

### Build a MATE package

Clone a repository, install its build dependencies, and do your first build. See [Building from Source](../building).

### Make your change

Edit source files, rebuild, install, and test. Read [C, GLib & GObject](../c-and-gobject) and [GTK Development](../gtk-development) to understand the codebase patterns.

### Submit a pull request

Push your branch to GitHub and open a PR. A maintainer will review it. See [Your First Contribution](../first-contribution).

{{% /steps %}}

## Tools you will need

| Tool | Purpose |
|------|---------|
| C compiler (`gcc` or `clang`) | Compile MATE source code |
| `make` | Build system used by all MATE packages |
| `git` | Version control |
| GitHub account | Submit pull requests |
| `pkg-config` | Query library compiler flags |

All MATE repositories live at [github.com/mate-desktop](https://github.com/mate-desktop).

## Useful references

- [gittutorial](https://git-scm.com/docs/gittutorial) — short Git introduction
- [giteveryday](https://git-scm.com/docs/giteveryday) — practical minimum command set
- [GitHub: Collaborating with pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests)
- [Makefile tutorial](https://cs.colby.edu/maxwell/courses/tutorials/maketutor/)
