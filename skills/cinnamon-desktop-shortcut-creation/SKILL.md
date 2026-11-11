---
name: cinnamon-desktop-shortcut-creation
description: Create and install custom .desktop application shortcuts for Cinnamon environment so apps appear correctly in the system menu.
triggers: ["adauga in meniu", "creaza scurtatura", "desktop shortcut", "app not in menu", "cinnamon menu entry"]
---

# Cinnamon Desktop Shortcut Creation

## Overview
This skill covers creating custom `.desktop` application launcher files for the Cinnamon desktop environment so that unlisted binaries or scripts appear properly in the application menu.

## Proven Procedure
1. Create a `.desktop` file in the user's application directory (`~/.local/share/applications/`):
   ```ini
   [Desktop Entry]
   Name=App Name
   Comment=Description of the application
   Exec=/path/to/executable_or_script
   Icon=application-default-icon
   Terminal=false
   Type=Application
   Categories=Network;Utility;
   ```
2. Ensure the `.desktop` file has execution permissions if it launches a script:
   ```bash
   chmod +x ~/.local/share/applications/app-name.desktop
   ```
3. Update the desktop database if necessary (handled automatically by Cinnamon, but can be forced via menu refresh or logout/login).

## Pitfalls & Troubleshooting
- **Missing Icon / Category:** Make sure `Categories=` contains valid FreeDesktop categories (like `Network`, `Development`, `Utility`) so the Cinnamon menu parser assigns it to a visible folder.
- **Path Issues:** Always use absolute paths for both `Exec` and `Icon` fields.
