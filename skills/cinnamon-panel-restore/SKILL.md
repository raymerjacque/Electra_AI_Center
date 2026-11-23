---
name: cinnamon-panel-restore
description: Fixes a missing or vanished Cinnamon desktop panel by restarting the Cinnamon window manager/shell.
triggers: ["bottom panel disappeared", "cinnamon panel missing", "panel vanished", "restart cinnamon shell", "bring back panel cinnamon"]
---

# Cinnamon Panel Restore

## Overview
Use this skill when the Cinnamon desktop panel disappears, vanishes, or crashes, leaving the desktop without its taskbar, menu, or system tray.

## Proven Procedure
To quickly restore the Cinnamon shell and bring back the panel without rebooting the system:
```bash
cinnamon --replace &
```
The `&` ensures the process runs in the background, keeping the terminal session free.

## Pitfalls & Troubleshooting
- If `cinnamon --replace` fails to start due to display issues, ensure the user session has proper access to the X server (`DISPLAY` environment variable).
- If the panel settings themselves are corrupted and keep disappearing upon restart, reset the panel configuration via `dconf` or through Cinnamon settings.
