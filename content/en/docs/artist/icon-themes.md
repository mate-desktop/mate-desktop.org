---
title: Icon Themes
weight: 3
---

Icon themes live in [mate-icon-theme](https://github.com/mate-desktop/mate-icon-theme) and follow the [Freedesktop Icon Naming Specification](https://specifications.freedesktop.org/icon-naming-spec/latest/).

## Directory layout

```
MyIconTheme/
├── index.theme
├── 16x16/
│   ├── actions/
│   ├── apps/
│   ├── devices/
│   ├── mimetypes/
│   ├── places/
│   └── status/
├── 22x22/
├── 24x24/
├── 32x32/
├── 48x48/
└── scalable/      # SVG icons (preferred)
```

## index.theme

```ini
[Icon Theme]
Name=MyIconTheme
Comment=My MATE icon theme
Inherits=menta,hicolor
Directories=scalable/actions,48x48/apps,...

[scalable/actions]
Size=48
MinSize=8
MaxSize=512
Type=Scalable
Context=Actions
```

`Inherits` sets the fallback chain — always include `hicolor` at the end.

## File format

- **SVG** is preferred for `scalable/` — it renders crisply at any size.
- **PNG** at the exact pixel size for each fixed-size directory.
- Name icons according to the [Freedesktop naming spec](https://specifications.freedesktop.org/icon-naming-spec/latest/) so applications can find them automatically.

## Testing

```bash
mkdir -p ~/.icons
cp -r MyIconTheme ~/.icons/

gsettings set org.mate.interface icon-theme 'MyIconTheme'
```

Refresh the icon cache after installing:

```bash
gtk-update-icon-cache ~/.icons/MyIconTheme/
```

## Tools

- [Inkscape](https://inkscape.org/) — SVG icon design
- [GNOME Icon Library](https://flathub.org/apps/org.gnome.design.IconLibrary) — browse existing Freedesktop icons for reference
