# MATE Desktop Website

Official website for the MATE Desktop Environment: https://mate-desktop.org

## Built With

- [Hugo](https://gohugo.io/) - Static site generator
- [Hextra](https://github.com/imfing/hextra) - Hugo theme

## Development

### Prerequisites

- Hugo extended version >= 0.146.0
- Go >= 1.21 (required for Hugo Modules)

### Local Development

Install dependencies:

```bash
hugo mod get
```

Start the development server:

```bash
hugo serve
```

The site will be available at http://localhost:1313

### Build

```bash
hugo
```

Output will be in the `public/` directory.

### Updating the Theme

To update the Hextra theme to the latest version:

```bash
hugo mod get -u github.com/imfing/hextra
```

To update all Hugo modules:

```bash
hugo mod get -u
```

After updating, commit the changes to `go.mod` and `go.sum`:

```bash
git add go.mod go.sum
git commit -m "Update Hugo modules"
```

### API Reference and Ecosystem Graph

`/docs/api/` shows an interactive dependency graph of all MATE packages and
links to their API reference. Everything is generated from the MATE
repositories by `scripts/api/mateapi.py` and is never committed: CI rebuilds it
on every push and nightly (see `.github/workflows/deploy.yml`).

The package list, categories and descriptions live in `scripts/api/packages.toml`;
dependencies, versions, pkg-config modules and GIR namespaces are detected
automatically.

To generate it locally (requires `doxygen` and `graphviz`; `gi-docgen` plus the MATE build
dependencies for the library reference):

```bash
python3 scripts/api/mateapi.py clone      # shallow clones into .cache/mate-src
python3 scripts/api/mateapi.py graph      # data/ecosystem.json
python3 scripts/api/mateapi.py doxygen    # static/docs/api/src/<package>/
python3 scripts/api/mateapi.py gir        # optional: static/docs/api/lib/<Namespace>/
python3 scripts/api/mateapi.py finalize   # link the generated docs into the graph
hugo server
```

For the themed Doxygen output, clone
[doxygen-awesome-css](https://github.com/jothepro/doxygen-awesome-css) into
`.cache/doxygen-awesome-css`. Without any generated data the page still builds
and shows a notice instead of the graph.

## Multilingual Support

The site supports multiple languages:
- English (default)
- Deutsch
- Español
- Italiano
- 日本語
- Български
- Català
- 简体中文
- 繁體中文
- עברית
- Polski
- Português
- Português (Brasil)
- Русский
- Srpski
- Українська
- Svenska

The language configuration and localized pages are in `hugo.yaml` and `content/<language-code>/`.
Theme and interface strings live in `i18n/*.yaml`; `.weblate.yml` defines the Weblate component.

## License

Content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
