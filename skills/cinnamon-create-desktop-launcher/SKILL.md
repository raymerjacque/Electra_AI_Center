---
name: cinnamon-create-desktop-launcher
description: Generates a .desktop file to create custom application launchers on the Cinnamon desktop environment.
triggers: ["crear acceso directo", "add desktop shortcut", "create launcher", "desktop entry file", "add .desktop file"]
---

# Cinnamon: Create Custom Desktop Launcher

## Overview
This skill provides the standard procedure for creating a custom application launcher (`.desktop` file) on the Cinnamon desktop environment. This is useful for running scripts, custom Python apps, or binary executables directly from the desktop or the Cinnamon application menu.

## Proven Procedure
To create a functioning desktop launcher, follow this template structure. Create a file named `your-app.desktop` in `~/Desktop` (for a desktop icon) or `~/.local/share/applications` (for the Cinnamon menu).

1. **Create the file:**
   ```bash
   nano ~/Desktop/my-app.desktop
   ```

2. **Populate with standard structure:**
   ```ini
   [Desktop Entry]
   Type=Application
   Name=My Custom App
   Exec=/usr/bin/python3 /path/to/script.py
   Icon=utilities-terminal
   Terminal=false
   Categories=Office;Utility;
   Comment=Description of my application
   ```

3. **Make it executable:**
   In Cinnamon, the file must be marked as executable to function:
   ```bash
   chmod +x ~/Desktop/my-app.desktop
   ```

4. **Verify/Trust:**
   Upon moving/creating the file on the desktop, Cinnamon may display a "Untrusted Application Launcher" warning. Right-click the icon on the desktop and select **"Allow Launching"** to trust the file.

## Pitfalls & Troubleshooting
*   **Permission Denied:** If the launcher doesn't open, ensure `chmod +x` was executed on the file.
*   **Untrusted Launcher:** Cinnamon security defaults will block untrusted `.desktop` files. You must manually right-click and "Allow Launching" the first time, or the icon will look like a generic text file.
*   **Pathing:** Always use absolute paths (e.g., `/home/user/...`) in the `Exec` line, as desktop files do not inherit the user's shell environment or `~` home expansion in some contexts.
