---
title: GTK Themes
weight: 2
---

GTK themes are in [mate-themes](https://github.com/mate-desktop/mate-themes) under `desktop-themes/`. Each theme directory contains:

```
MyTheme/
├── index.theme.in        # theme metadata
├── gtk-2.0/              # GTK 2 CSS/assets (keep for compatibility)
├── gtk-3.0/              # GTK 3 CSS and assets  ← main work
│   ├── gtk.css
│   ├── gtk-main.css
│   ├── gtk-widgets-*.css
│   └── assets/           # PNG or SVG widget graphics
├── metacity-1/           # window border decorations
└── xfwm4/                # XFWM4 compatibility (optional)
```

## index.theme

```ini
[Desktop Entry]
Type=X-GNOME-Metatheme
Name=MyTheme
Comment=A MATE GTK theme

[X-GNOME-Metatheme]
GtkTheme=MyTheme
MetacityTheme=MyTheme
IconTheme=menta
CursorTheme=mate
ButtonLayout=menu:minimize,maximize,close
```

## GTK 3 CSS

GTK 3 themes are plain CSS with GTK-specific properties and selectors. Key files:

| File | Purpose |
|------|---------|
| `gtk.css` | Entry point — imports the others |
| `gtk-main.css` | Colours, fonts, base widget styles |
| `gtk-widgets-*.css` | Per-widget rules (buttons, entries, etc.) |
| `assets/` | PNG/SVG graphics referenced by `url()` in CSS |

Look at **Menta** or **GreenLaguna** as well-maintained starting points. **BlackMATE** is a good reference for dark themes.

## Testing a theme

Install the theme directory to your local themes folder and switch to it:

```bash
mkdir -p ~/.themes
cp -r MyTheme ~/.themes/

# Apply with gsettings
gsettings set org.mate.interface gtk-theme 'MyTheme'

# Or change it in the Control Center → Appearance → Theme
```

Use the [GTK Inspector](../../developer/debugging#gtk-inspector) to live-edit CSS while the app is running — no restart needed:

```bash
GTK_DEBUG=interactive mate-terminal
```

## References

- [GTK 3 CSS properties](https://docs.gtk.org/gtk3/css-properties.html)
- [GNOME HIG 2.2.1](https://mbkma.github.io/gnome-2-hig-book/) — MATE's visual design reference
