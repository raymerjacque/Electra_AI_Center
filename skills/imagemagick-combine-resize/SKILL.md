---
name: imagemagick-combine-resize
description: Resize multiple images to a uniform height or width and combine them side-by-side or vertically using ImageMagick.
triggers: ["redimensionner et assembler des images", "combiner des images côte à côte imagemagick", "resize and append images convert"]
---

# ImageMagick: Resize and Combine Images

## Overview
Use this skill when you need to take two or more images of different dimensions, normalize their size (e.g., matching heights), and concatenate/append them into a single composite image using the ImageMagick CLI (`convert`).

## Proven Procedure
To resize images to a specific height (e.g., 300 pixels) while maintaining aspect ratio and append them horizontally side-by-side:

```bash
convert "(" "path/to/image1" -resize x300 ")" "(" "path/to/image2" -resize x300 ")" +append "path/to/output.png"
```

- `-resize x300`: Resizes the image to a height of 300 pixels, automatically adjusting the width to preserve the aspect ratio.
- `+append`: Concatenates the images horizontally. Use `-append` instead if you want to stack them vertically.
- Parentheses `(` and `)` isolate the resize operations to each individual input image before they are merged.

## Pitfalls & Troubleshooting
- **Shell Escaping**: In Bash, parentheses `()` must be escaped or quoted (`"("` and `")"`) so the shell doesn't interpret them as subshell syntax.
- **ImageMagick Version**: On newer systems (ImageMagick v7+), the command `magick` is used instead of `convert`. If `convert` fails, try replacing it with `magick`.
