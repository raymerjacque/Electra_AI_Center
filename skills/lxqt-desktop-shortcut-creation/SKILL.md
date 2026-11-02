---
name: lxqt-desktop-shortcut-creation
description: Creates and installs custom desktop application launchers (.desktop files) into user applications directory for LXQt and other desktop environments.
triggers: ["create desktop icon", "make desktop launcher", "add app to menu", "install .desktop file"]
---

# LXQt Desktop Shortcut Creation

## Overview
This skill covers the creation and manual installation of custom `.desktop` application launcher files for the LXQt desktop environment (and other freedesktop-compliant Linux desktops). It ensures applications appear in the system menu and can be launched easily.

## Proven Procedure
1. Create a freedesktop-compliant `.desktop` file (e.g., `app_name.desktop`) with proper headers:
   ```ini
   [Desktop Entry]
   Type=Application
   Name=My Application
   Exec=python3 /path/to/script/__main__.py
   Icon=/path/to/icon.png
   Terminal=false
   Categories=Game;Utility;
   ```
2. Ensure the user's local application directory exists:
   ```bash
   mkdir -p ~/.local/share/applications
   ```
3. Copy the desktop file to the applications directory:
   ```bash
   cp app_name.desktop ~/.local/share/applications/
   ```
4. Update the desktop database to refresh the application menu:
   ```bash
   update-desktop-database ~/.local/share/applications/
   ```

## Pitfalls & Troubleshooting
- **Executable permissions**: Ensure the target script or binary has execution permissions (`chmod +x`).
- **Absolute paths**: Always use absolute paths for the `Exec=` and `Icon=` fields inside the `.desktop` file.
