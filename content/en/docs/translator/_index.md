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

MATE uses [Weblate](https://translate.fedoraproject.org/projects/mate-desktop/) to manage this workflow — you do not need to handle `.po` files or Git directly.

## Getting started on Weblate

MATE translations are hosted on the [Fedora Weblate instance](https://translate.fedoraproject.org/), which syncs completed translations back to the MATE repositories on GitHub.

{{% steps %}}

### Create an account

Sign up for a free [Fedora Account](https://accounts.fedoraproject.org/) and use it to log in to [translate.fedoraproject.org](https://translate.fedoraproject.org/).

### Open the MATE project

Go to the [MATE project on Weblate](https://translate.fedoraproject.org/projects/mate-desktop/). Each MATE package (e.g. `caja`, `pluma`, `mate-panel`) is a separate component.

### Pick your language

Open a component and select your language. If your language is not listed yet, use **Start new translation** to add it.

### Start translating

Start with a smaller component like `mate-calc` or `mate-utils` to get familiar with the workflow. Use the **Translate** view to step through untranslated strings, type the translation, and save. Weblate shows suggestions, glossary terms and checks for common mistakes as you go.

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

You can download the `.po` file for any component and language from Weblate (**Files → Download translation**), edit it locally, and upload it back (**Files → Upload translation**). Please submit translations through Weblate rather than opening pull requests with `.po` changes, since Weblate commits to the repositories automatically and direct edits can conflict with it.

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

If your language has no active coordinator, you can volunteer to maintain it. Coordinators review suggestions from other contributors on Weblate and keep terminology consistent across components. Contact the MATE team via the [Community](/community) page if you are interested.
