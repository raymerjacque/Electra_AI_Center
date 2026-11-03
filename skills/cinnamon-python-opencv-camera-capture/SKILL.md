---
name: cinnamon-python-opencv-camera-capture
description: Capture raw or uncompressed images from a connected USB/web camera using Python and OpenCV without external CLI tools like gphoto2.
triggers: ["python capture image from camera", "opencv webcam capture python", "save raw frame python opencv"]
---

# Python OpenCV Camera Capture

## Overview
Provides a reliable Python script template using OpenCV (`cv2.VideoCapture`) to connect to a camera device, grab a frame, and save the raw pixel data directly to disk without JPEG loss or external CLI dependencies like `gphoto2`.

## Proven Procedure
1. Install OpenCV and NumPy if not already present:
   ```bash
   pip install opencv-python numpy
   ```
2. Create a Python script (`capture.py`) in the target directory:
   ```python
   import cv2
   import os

   # Determine script directory
   script_dir = os.path.dirname(os.path.abspath(__file__))
   output_path = os.path.join(script_dir, "captured_image.raw")

   # Initialize camera (0 is usually the default webcam/connected camera)
   cap = cv2.VideoCapture(0)

   if not cap.isOpened():
       print("Error: Could not open camera.")
       exit(1)

   # Capture a single frame
   ret, frame = cap.isOpened() and cap.read()

   if ret:
       # Save raw numpy array bytes directly to file
       frame.tofile(output_path)
       print(f"Raw image saved successfully to {output_path}")
   else:
       print("Error: Failed to capture image.")

   # Release the camera
   cap.release()
   ```

## Pitfalls & Troubleshooting
- **Camera Index**: If multiple cameras are connected, `cv2.VideoCapture(0)` might pick the wrong device; try indices `1`, `2`, etc.
- **Permissions**: Ensure the user has read/write permissions to `/dev/video*`.
