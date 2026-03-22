---
title: Getting Started
weight: 1
---

MATE is mostly written in C, with some components in Python or C++. If you are new to C, working through the *Introduction*, *Beginning C*, and *Intermediate C* chapters of the [C Wikibook](https://en.wikibooks.org/wiki/C_Programming) is a solid starting point.

You will need a text editor (Pluma, Kate, or VSCodium work well) and a terminal. A full IDE such as [VSCodium](https://vscodium.com/), [Eclipse](https://www.eclipse.org/), or [Code::Blocks](https://www.codeblocks.org/) is also fine.

## Build system: Make

MATE packages contain dozens of source files, language files, desktop files, and more. A Makefile describes how to compile the whole thing correctly and efficiently — only recompiling files that changed.

> Makefile tutorial: https://cs.colby.edu/maxwell/courses/tutorials/maketutor/

## Version control: Git

All MATE source code is managed with [Git](https://git-scm.com/). You will use it to track your changes, create branches, and share your work.

Useful references:

- [gittutorial](https://git-scm.com/docs/gittutorial) — a short introduction
- [giteveryday](https://git-scm.com/docs/giteveryday) — a practical minimum command set
- [GitHub Git cheat sheet](https://training.github.com/downloads/github-git-cheat-sheet/)

## Repository hosting: GitHub

MATE's repositories live at [github.com/mate-desktop](https://github.com/mate-desktop). You will need a free GitHub account to submit pull requests.

Reference: [GitHub Docs — Collaborating with pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests)

## Development environment

If you want a safe sandbox separate from your main system, run MATE development inside a virtual machine. [GNOME Boxes](https://help.gnome.org/users/gnome-boxes/stable/) and [VirtualBox](https://virtualbox.org) are two popular options — install a distribution of your choice inside the VM and do all your MATE builds there.
