---
title: Translator Documentation
weight: 150
---

Translating MATE into your language is one of the most impactful ways to contribute — it makes the desktop accessible to people who would otherwise not be able to use it. No programming knowledge is required.

## How translation works in MATE

MATE source strings are marked up with `gettext` in C code:

```c
_("Open Terminal")
```

These strings are extracted into `.pot` template files during the build. Translators work on per-language `.po` files derived from those templates. Compiled `.mo` files are installed with the package and loaded at runtime based on the user's locale.

MATE uses [Transifex](https://www.transifex.com) to manage this workflow — you do not need to handle `.po` files or Git directly.

## Getting started on Transifex

{{% steps %}}

### Create an account

Sign up for free at [transifex.com/signup](https://www.transifex.com/signup/).

### Open the MATE project

Go to the [MATE project on Transifex](https://www.transifex.com/projects/p/MATE/).

### Join your language team

Find your language in the list and click **Join team**. If your language does not exist yet, you can request it to be added.

### Start translating

Pick a resource — start with a smaller one like `mate-calc` or `mate-utils` to get familiar with the workflow. Click a string, type the translation, and save.

{{% /steps %}}

## Translation guidelines

- **Be consistent** — use the same term for the same concept throughout a component. Check existing translations in the same file first.
- **Preserve formatting** — keep `%s`, `%d`, `\n`, and similar placeholders exactly as they appear in the source string.
- **Preserve accelerators** — strings like `_File` define keyboard accelerators. Keep the underscore in front of a letter that makes sense in your language.
- **Do not translate** — code, command names, URLs, and proper nouns (e.g. "MATE", "GLib", "GitHub").
- **Use formal or informal address** consistently within a component, following the convention of your language community.

## Working with .po files directly

If you prefer working locally:

```bash
# Install gettext tools
sudo apt install gettext          # Debian/Ubuntu
sudo dnf install gettext          # Fedora

# Edit the translation file for your language
$EDITOR po/de.po

# Check for syntax errors
msgfmt --check po/de.po

# Compile (optional — the build system does this automatically)
msgfmt -o po/de.mo po/de.po
```

Open a pull request with the updated `.po` file against the relevant package repository if you want to contribute outside of Transifex.

## Testing your translation

Build and install the package with your updated `.po` file, then set your locale and launch the application:

```bash
LANG=de_DE.UTF-8 mate-calc
```

Check that:
- All translated strings appear correctly
- No strings are cut off by the UI layout
- Accelerators do not conflict within the same menu

## Becoming a language team coordinator

If your language has no active coordinator, you can volunteer to maintain it. Coordinators review suggestions from other contributors and approve translations before they are merged. Contact the MATE team via the [Community](/community) page if you are interested.
