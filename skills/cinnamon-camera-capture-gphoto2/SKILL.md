---
name: cinnamon-camera-capture-gphoto2
description: Captures a raw image from a connected camera using gphoto2 and saves it to the script's directory. Works on Cinnamon desktops with gphoto2 installed.
triggers: ["capture raw image from camera", "gphoto2 raw capture", "camera photo script"]
---

# Capture Raw Image from Camera using gphoto2

## Overview
This skill provides a simple Python script that uses gphoto2 to capture a raw image from a connected digital camera and saves the file as an uncompressed `.raw` file in the same directory as the script. This is useful for quickly capturing high-resolution raw images without using the camera's native software.

## Proven Procedure

1. **Create the script file:**
   ```bash
   nano /home/allen/Desktop/Photos/Testing_Gphoto2/capture_image.py
   ```

2. **Paste the following script content:**
   ```python
   #!/usr/bin/env python3
   import subprocess
   import os
   import sys

   # Get the directory where the script is located
   script_dir = os.path.dirname(os.path.abspath(__file__))
   os.chdir(script_dir)

   # gphoto2 command to capture a raw image and keep it
   # --capture-image captures a photo
   # --keep keeps the image file on the camera (optional, remove if not needed)
   # The file will be saved in the current working directory
   try:
       result = subprocess.run(
           ["gphoto2", "--capture-image", "--keep"],
           capture_output=True,
           text=True
       )
       
       if result.returncode == 0:
           print("Image captured successfully!")
           # List files in the directory to confirm
           files = [f for f in os.listdir('.') if f.endswith('.raw')]
           if files:
               print(f"Raw file saved: {files[0]}")
           else:
               print("No .raw files found in current directory")
       else:
           print(f"Error capturing image: {result.stderr}")
           sys.exit(1)
   except FileNotFoundError:
       print("Error: gphoto2 not found. Install with: sudo apt install gphoto2")
       sys.exit(1)
   ```

3. **Make the script executable:**
   ```bash
   chmod +x /home/allen/Desktop/Photos/Testing_Gphoto2/capture_image.py
   ```

4. **Run the script:**
   ```bash
   /home/allen/Desktop/Photos/Testing_Gphoto2/capture_image.py
   ```

## Pitfalls & Troubleshooting

- **gphoto2 not installed:** Install with `sudo apt install gphoto2`
- **Camera not detected:** Ensure camera is connected and turned on, and `gphoto2 --list-files` can detect it
- **Permission issues:** May need to be in `plugdev` group or run with appropriate permissions
- **File format:** The `--capture-image` command may capture in the camera's native raw format (typically Bayer pattern .raw files). The exact format depends on the camera model.
- **Image location:** The script changes to its own directory using `os.chdir()`, so ensure the script is in the desired folder before running.
