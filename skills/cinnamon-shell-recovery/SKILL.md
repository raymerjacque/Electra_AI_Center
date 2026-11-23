---
name: cinnamon-shell-recovery
description: Troubleshooting and command-line recovery for Cinnamon desktop crashes, including panel restoration and session reset.
triggers: ["cinnamon desktop crash", "panel disappeared", "cinnamon shell failed", "wallpaper change crash"]
---

# Cinnamon Shell Recovery

## Overview
This skill provides the immediate steps to recover a Cinnamon desktop environment when a UI change (like a wallpaper update) or a system event causes the desktop shell (panel, desktop icons, etc.) to crash or fail to render.

## Proven Procedure

### 1. Attempt Soft Restart of Cinnamon
If you are still in a terminal (Ctrl+Alt+F2 if the GUI is unresponsive) or have a terminal window open:
```bash
# Restart the Cinnamon shell without logging out
cinnamon --replace &
```
*Wait a few seconds for the panel to redraw.*

### 2. Verify Session Health
If the shell continues to fail, check the system logs to identify the specific error (e.g., memory exhaustion or library incompatibility):
```bash
# Check the last 50 lines of the Cinnamon journal for session errors
journalctl /usr/bin/cinnamon -n 50
```

### 3. Clear Desktop Config (Last Resort)
If the crash is persistent because of a corrupted settings file (e.g., due to a wallpaper path issue):
```bash
# Reset Cinnamon settings to default (Warning: This will reset your theme/applet configurations)
dconf reset -f /org/cinnamon/
cinnamon --replace &
```

## Pitfalls & Troubleshooting
*   **Wallpaper Format:** If the crash happened specifically while changing the wallpaper, verify the file isn't a massive BMP or a corrupted file format. Use standard .jpg or .png files.
*   **Permissions:** Ensure your user has write access to `~/.config/cinnamon-settings-daemon/` if changes aren't saving.
*   **Scope Errors:** If you see `app-cinnamon-env-*.scope` errors in `journalctl`, this often indicates a resource constraint or a hardware acceleration issue with the window manager (`muffin`). Check if your GPU drivers are running correctly.
