---
name: cinnamon-desktop-background-icons-gsettings
description: Configure Cinnamon desktop background images and desktop icon visibility using gsettings for background and Nemo file manager.
triggers: ["cinnamon background", "nemo desktop icons", "gsettings cinnamon background", "schimba fundal cinnamon"]
---

# Cinnamon Desktop Background and Icons Management via gsettings

## Overview
This skill covers configuring desktop background images, fade effects, and desktop icon visibility (Home, Computer, Trash, Mounted volumes) under the Cinnamon desktop environment and Nemo file manager using `gsettings`.

## Proven Procedure
To configure background and icons programmatically or via automation:

1. Set the desktop background image:
   ```bash
   gsettings set org.cinnamon.desktop.background picture-uri 'file:///path/to/image.jpg'
   ```

2. Disable/Enable background fade effects:
   ```bash
   gsettings set org.cinnamon.desktop.background fade-background false
   ```

3. Configure Nemo desktop icons visibility:
   - Show/hide Home icon:
     ```bash
     gsettings set org.nemo.desktop show-desktop-icons true
     gsettings set org.nemo.desktop desktop-layout 'true::true'
     ```
   - Control individual standard icons (Computer, Home, Trash, Mounted volumes):
     ```bash
     gsettings set org.nemo.desktop computer-icon-visible false
     gsettings set org.nemo.desktop home-icon-visible false
     gsettings set org.nemo.desktop trash-icon-visible false
     gsettings set org.nemo.desktop volumes-visible true
     ```

## Pitfalls & Troubleshooting
- Ensure `DISPLAY` and `DBUS_SESSION_BUS_ADDRESS` are properly set if running `gsettings` commands via a non-interactive script or remote SSH session.
