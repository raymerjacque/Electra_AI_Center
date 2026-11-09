---
name: cinnamon-desktop-entry-creation
description: Creates custom desktop entry files (.desktop) in /usr/share/applications/ for applications on Cinnamon desktop environments.
triggers: ["create desktop entry", "adauga iconita in meniu", "steam.desktop", "desktop file creation"]
---

# Cinnamon Desktop Entry Creation

## Overview
This skill covers creating and placing `.desktop` files in `/usr/share/applications/` to ensure applications appear correctly with icons in the Cinnamon desktop application menu.

## Proven Procedure
1. Define the desktop entry content with appropriate metadata (`Name`, `Exec`, `Icon`, `Type`, `Categories`).
2. Save the file to `/usr/share/applications/<app-name>.desktop` (requires root privileges if writing to system paths, or `~/.local/share/applications/` for user-specific entries).
3. Ensure the file has correct permissions and update the desktop database if necessary:
   ```bash
   update-desktop-database ~/.local/share/applications/
   ```

## Pitfalls & Troubleshooting
- Ensure the `Exec` path points to a valid executable available in `$PATH` or use the absolute path.
- Verify the `Icon` name matches an icon available in the system theme or provide an absolute path to an image file.
