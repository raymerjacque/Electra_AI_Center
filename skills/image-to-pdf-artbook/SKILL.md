---
name: image-to-pdf-artbook
description: Automates the creation of multi-page PDF artbooks from a directory of sorted images using Python and Pillow.
triggers: ["artbook erstellen", "bilder in pdf umwandeln", "image to pdf python", "artbook python script", "create artbook from images"]
---

# Image-to-PDF Artbook Creator

## Overview
This skill provides a quick and reliable workflow for compiling a directory of image files (PNG, JPG, JPEG) into a professionally formatted multi-page PDF artbook using Python and the Pillow library.

## Proven Procedure
1. Ensure Python and Pillow are installed:
   ```bash
   pip install Pillow
   ```
2. Place all artbook images into a dedicated directory and ensure they are named sequentially (e.g., `01_cover.jpg`, `02_page.jpg`, etc.).
3. Run the following Python script inside the image directory:
   ```python
   import os
   from PIL import Image

   # Find and sort image files
   valid_extensions = ('.png', '.jpg', '.jpeg')
   image_files = sorted([f for f in os.listdir('.') if f.lower().endswith(valid_extensions)])

   if image_files:
       print(f"Found {len(image_files)} images. Compiling artbook...")
       images = [Image.open(f).convert('RGB') for f in image_files]
       
       # Save as multi-page PDF
       output_pdf = 'artbook.pdf'
       images[0].save(output_pdf, save_all=True, append_images=images[1:])
       print(f"Artbook successfully created: {output_pdf}")
   else:
       print("No valid images found in the current directory.")
   ```

## Pitfalls & Troubleshooting
- **Color Profile Issues**: CMYK images or images with transparency (RGBA PNGs) can throw errors when saving directly to a standard RGB PDF. Always use `.convert('RGB')` on each opened image.
- **Sorting Order**: Ensure filenames use leading zeros (e.g., `img_01.jpg` instead of `img_1.jpg`) so `sorted()` orders them correctly.
