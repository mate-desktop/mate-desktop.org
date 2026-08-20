---
title: Wallpapers
weight: 1
---

Wallpapers are collected in [mate-backgrounds](https://github.com/mate-desktop/mate-backgrounds), organised into three categories:

| Directory | Content |
|-----------|---------|
| `nature/` | Photographs — landscapes, plants, wildlife |
| `abstract/` | Abstract or artistic imagery |
| `desktop/` | Minimal or MATE-branded backgrounds |

## File format and resolution

- **JPEG** for photographs, **PNG** for images with transparency or flat colours.
- Minimum resolution: **1920×1200**. Providing **2560×1600** gives good coverage for HiDPI displays.
- Keep file sizes reasonable — under 3 MB per image is a good target.

## Licensing

All wallpapers must be released under a free licence. MATE backgrounds use [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Include licence and attribution information in your pull request.

## Adding a wallpaper

Place the image file in the appropriate category directory. Then register it in `Makefile.am`:

```makefile
nature_backgrounds_DATA = \
    nature/YourImage.jpg \
    ...
```

And in `meson.build`:

```python
install_data(
    'nature/YourImage.jpg',
    install_dir: backgrounds_dir / 'nature',
)
```

## Testing

Apply the wallpaper before submitting: right-click the desktop → **Change Desktop Background**, then navigate to your image file.

## Tools

- [GIMP](https://www.gimp.org/) — raster editing, photo retouching, compositing
- [Inkscape](https://inkscape.org/) — vector graphics (export to PNG at the target resolution)
- [ImageMagick](https://imagemagick.org/) — batch conversion and resizing from the terminal
