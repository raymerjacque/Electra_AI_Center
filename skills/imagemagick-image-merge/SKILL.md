---
name: imagemagick-image-merge
description: Merge or concatenate multiple images horizontally or vertically using ImageMagick CLI.
triggers: ["fusionner images", "merge images", "coller images", "imagemagick append", "concaténer images"]
---

# ImageMagick Image Merge

## Overview
This skill provides the commands to combine two or more images side-by-side (horizontally) or stacked (vertically) using ImageMagick via the command line.

## Proven Procedure
To merge images horizontally (side-by-side):
```bash
convert +append "image1.png" "image2.png" "output.png"
```

To merge images vertically (stacked):
```bash
convert -append "image1.png" "image2.png" "output.png"
```

## Pitfalls & Troubleshooting
- Ensure `imagemagick` is installed (`sudo apt install imagemagick`).
- Note that newer ImageMagick policies might restrict reading/writing certain formats or file sizes (`/etc/ImageMagick-6/policy.xml`).
- If images have different dimensions, the resulting image may have uneven alignment or extra blank space. Resize them beforehand if uniform dimensions are required.
