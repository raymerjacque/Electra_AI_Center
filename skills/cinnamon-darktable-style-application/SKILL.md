---
name: cinnamon-darktable-style-application
description: Applies a specific Kodak-style preset from the darktable database to a captured image using darktable-cli within a Cinnamon desktop environment. Useful for automating photo processing workflows with specific film emulation styles.
triggers: ["apply darkstyle preset", "darktable-cli style application", "Kodak style processing"]
---

# Apply Kodak Styles from darktable Database

## Overview
This skill enables applying specific Kodak-style presets (such as Portra 400) from the darktable database to captured images using the `darktable-cli` command-line tool. It is designed for automation workflows in Cinnamon desktop environments where specific film emulation looks need to be applied programmatically.

## Proven Procedure

### Step 1: List Available Styles
First, identify the exact style names available in the darktable database:
```bash
darktable-cli --list-styles
```

### Step 2: Apply the Desired Style
Use the style name from the list to apply it to an image. The general syntax is:
```bash
darktable-cli --apply-style "<style_name>" input.jpg -o output.jpg
```

### Step 3: Full Workflow Example
Based on the captured script, here is the complete procedure for capturing and applying a Kodak Portra 400 style:

```bash
#!/bin/bash
# Wait 5 seconds for camera/preview setup
sleep 5

# Capture raw image from connected camera using gphoto2
gphoto2 --capture-image-and-download

# Apply the Kodak|Portra 400 nc style from darktable database
# Replace "Kodak|Portra 400 nc" with the exact style name from --list-styles output
darktable-cli --apply-style "Kodak|Portra 400 nc" captured.jpg -o output.jpg

# Clean up or further processing...
```

## Pitfalls & Troubleshooting

1. **Style Name Exact Match**: The style name must match exactly as listed in `darktable-cli --list-styles`. Style names often contain special characters like `|` (pipe) which must be preserved and properly quoted.

2. **Image Format**: Ensure the input image is in a format darktable supports (typically RAW or JPEG). The style application may not work on unsupported formats.

3. **Output Path**: Specify the full output path if not in the current directory to avoid overwriting original files.

4. **Camera Connection**: Verify the camera is properly connected and recognized by gphoto2 before running the capture command.

5. **darktable Database**: If the style doesn't appear in the list, ensure darktable database is up to date and the style preset is properly installed in the darktable configuration.
