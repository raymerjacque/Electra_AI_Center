---
name: cinnamon-window-decoration-fix
description: Restores missing window decorations (title bars) and resets the Cinnamon window manager without logging out.
triggers: ["cinnamon missing title bars", "cinnamon window border gone", "reset cinnamon window manager", "fix cinnamon window decoration", "alt+f2 r cinnamon"]
---

# Cinnamon Window Decoration Fix

## Overview
This skill provides immediate recovery steps when the Cinnamon window manager (Muffin) fails to draw window decorations (title bars, borders) or becomes unresponsive. This is a common transient issue in Cinnamon desktop environments that does not require a full system reboot or user logout.

## Proven Procedure

### 1. The Quick Restart (No Logout)
If the window decorations disappear, perform a "Soft Reset" of the Cinnamon shell:
1. Press **`Alt + F2`** to open the "Enter a Command" dialog.
2. Type exactly the letter: **`r`**
3. Press **`Enter`**.
*The screen will briefly flicker, and the Cinnamon interface will reload, typically restoring the missing title bars.*

### 2. If the Quick Restart Fails (Terminal Recovery)
If the GUI method is inaccessible, use the terminal to force-restart the window manager:

```bash
# Force the window manager to replace itself
DISPLAY=:0 muffin --replace &
```

### 3. Clearing Cache (Persistent Fix)
If the issue occurs frequently, the Cinnamon cache might be corrupted. Clear it to prevent recurrence:

```bash
# Remove temporary Cinnamon settings and restart
rm -rf ~/.cache/cinnamon/*
cinnamon --replace &
```

## Pitfalls & Troubleshooting
- **`Alt+F2` not working?** If the keyboard shortcut is disabled, you must switch to a TTY (`Ctrl + Alt + F2`), log in, and execute the `DISPLAY=:0 muffin --replace &` command from there.
- **NVIDIA Users:** If this happens constantly, it is often related to the GPU driver failing to handle compositing. Ensure the NVIDIA drivers are up to date and that the "V-Sync" setting in *General Settings* is enabled in Cinnamon's "Effects" menu.
- **The "r" command:** This only works if Cinnamon is running as a desktop shell. It will not work inside other desktop environments like GNOME or XFCE.
