---
name: kde-desktop-entry-fix
description: Fix desktop shortcut entries (.desktop files) that incorrectly wrap GUI applications in a terminal emulator.
triggers: ["fix desktop icon terminal", "desktop shortcut opens terminal", "remove terminal wrapper from desktop entry", "edit .desktop file exec line"]
---

# KDE Desktop Entry Terminal Wrapper Fix

## Overview
When a desktop application shortcut (.desktop file) incorrectly launches inside a terminal window (e.g. `gnome-terminal -- /path/to/app`), clicking the icon opens an unwanted terminal first. This skill guides the fixing of the `.desktop` file's `Exec` line to launch the GUI directly.

## Proven Procedure
1. Locate the desktop entry file, usually in `/usr/share/applications/` or `~/.local/share/applications/`.
2. Inspect the file to locate the `Exec=` line:
   ```bash
   grep "Exec=" /usr/share/applications/<app-name>.desktop
   ```
3. Edit the file (with root privileges if in `/usr/share/applications/`) to remove the terminal wrapper:
   * **Before:** `Exec=gnome-terminal -- /usr/bin/python3 /path/to/gui.py`
   * **After:** `Exec=/usr/bin/python3 /path/to/gui.py`
4. Update the desktop database if necessary:
   ```bash
   update-desktop-database ~/.local/share/applications/
   ```

## Pitfalls & Troubleshooting
* Ensure proper permissions (`sudo`) when editing system-wide `.desktop` files in `/usr/share/applications/`.
* If the application requires running in a terminal, use the desktop environment's specific terminal execution flag (e.g., `Terminal=true` inside the `.desktop` file) instead of hardcoding a specific terminal emulator in the `Exec=` string.
