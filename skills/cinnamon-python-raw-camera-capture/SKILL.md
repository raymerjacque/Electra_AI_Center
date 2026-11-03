---
name: cinnamon-python-raw-camera-capture
description: Captures raw image data from a connected camera using Python (OpenCV) and saves it to a specified directory without relying on gphoto2.
triggers: ["python capture raw image", "opencv camera capture raw file", "save raw image python without gphoto2"]
---

# Python Raw Camera Capture without gphoto2

## Overview
This skill provides a Python script utilizing OpenCV (`cv2`) to grab a raw frame from a connected camera device and store the raw byte stream directly into a designated local directory.

## Proven Procedure
1. Create the target directory:
   ```bash
   mkdir -p /home/allen/Desktop/Photos/Testing_Gphoto2
   ```
2. Create and run the Python script (`capture_image.py`):
   ```python
   import cv2
   import os

   # Determine script's directory
   script_dir = os.path.dirname(os.path.abspath(__file__))
   output_path = os.path.join(script_dir, "captured_image.raw")

   # Initialize video capture (device index 0)
   cap = cv2.VideoCapture(0)

   if not cap.isOpened():
       print("Error: Could not open camera.")
       exit(1)

   ret, frame = cap.read()
   if ret:
       # Save raw frame bytes
       with open(output_path, "wb") as f:
           f.write(frame.tobytes())
       print(f"Raw image saved successfully to {output_path}")
   else:
       print("Error: Failed to capture image.")

   cap.release()
   ```

## Pitfalls & Troubleshooting
- Ensure user permissions allow access to video devices (`/dev/video*`). If permission is denied, add the user to the `video` group: `sudo usermod -aG video $USER`.
- Verify the correct camera index if multiple video devices are connected (change `cv2.VideoCapture(0)` to `1`, etc.).
