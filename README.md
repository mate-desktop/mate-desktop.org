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

Translations are managed via filename suffixes (e.g., `_index.de.md` for German).

## License

Content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
