---
name: cinnamon-desktop-shortcut-heimdall
description: Create a desktop application shortcut (.desktop file) for Heimdall frontend on the Cinnamon desktop environment.
triggers: ["heimdall desktop shortcut", "cinnamon launcher erstellen", "app auf dem desktop heimdall"]
---

# Heimdall Desktop Shortcut on Cinnamon

## Overview
This skill covers installing the Heimdall flash frontend on Debian/Ubuntu-based Linux distributions using Cinnamon and creating a custom `.desktop` application launcher file so it appears on the desktop and in the application menu.

## Proven Procedure
1. Install Heimdall and its graphical frontend via APT:
   ```bash
   sudo apt update && sudo apt install heimdall-flash-frontend
   ```

2. Create a custom `.desktop` file for the application launcher (either in `~/.local/share/applications/` for the current user or `/usr/share/applications/` system-wide):
   ```bash
   nano ~/.local/share/applications/heimdall-frontend.desktop
   ```

3. Insert the following configuration:
   ```ini
   [Desktop Entry]
   Name=Heimdall Flash Frontend
   Comment=Flashing tool for Samsung Galaxy devices
   Exec=heimdall-frontend
   Icon=heimdall
   Terminal=false
   Type=Application
   Categories=System;Device;
   ```

4. Make the desktop file executable (required by Cinnamon):
   ```bash
   chmod +x ~/.local/share/applications/heimdall-frontend.desktop
   ```

5. Copy the launcher to the desktop if a direct desktop icon is desired:
   ```bash
   cp ~/.local/share/applications/heimdall-frontend.desktop ~/Desktop/
   chmod +x ~/Desktop/heimdall-frontend.desktop
   ```

## Pitfalls & Troubleshooting
- **Untrusted Launcher Warning:** Cinnamon may show an untrusted launcher warning upon double-clicking the desktop icon. Right-click the icon on the desktop and select "Allow Launching" (or ensure `chmod +x` was executed).
- **Missing Icon:** If the icon doesn't appear, check if `heimdall` provides an icon in `/usr/share/icons/` or specify an absolute path to a custom PNG/SVG icon in the `Icon=` field.
