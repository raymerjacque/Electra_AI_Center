---
name: cinnamon-systemd-user-service-path-repair
description: Troubleshoot and fix systemd user services failing due to incorrect hardcoded user home directory paths or missing backend scripts.
triggers: ["fix systemd user service", "systemd user service failed", "systemctl user path error", "repair systemd user daemon"]
---

# Systemd User Service Path and Script Repair

## Overview
This skill solves issues where systemd user services (`systemctl --user`) fail to start because they reference incorrect hardcoded home directory paths (e.g., from a different username or template setup) or point to missing script files.

## Proven Procedure

1. **Check Service Status and Logs:**
   ```bash
   systemctl --user status <service-name>.service
   journalctl --user -u <service-name>.service -n 50 --no-pager
   ```

2. **Locate the Systemd Unit File:**
   User service files are typically located in:
   ```bash
   ~/.config/systemd/user/<service-name>.service
   ```
   (Or system-wide in `/etc/systemd/system/` or `/lib/systemd/system/`).

3. **Inspect and Fix Paths:**
   Open the service file and check `ExecStart`, `WorkingDirectory`, and other path definitions for incorrect usernames or missing directories:
   ```ini
   [Service]
   ExecStart=/home/correct-user/.local/share/path/to/script.py
   ```
   Replace any stale or incorrect paths with the actual current user home directory (`$HOME`).

4. **Verify and Restore Missing Scripts:**
   Ensure the script targeted by `ExecStart` actually exists at the specified path. If missing, restore or recreate the script with proper permissions (`chmod +x`).

5. **Reload and Restart:**
   After making modifications, reload the systemd user daemon and restart the service:
   ```bash
   systemctl --user daemon-reload
   systemctl --user restart <service-name>.service
   systemctl --user enable --now <service-name>.service
   ```

## Pitfalls & Troubleshooting
- **Environment variables:** Systemd user services do not always inherit the full shell environment. Always use absolute paths for executables and interpreters (e.g., `/usr/bin/python3` instead of `python3`).
- **X11/Wayland context:** If a user service requires a graphical display, ensure `DISPLAY` and `XAUTHORITY` or appropriate graphical targets are configured, or use desktop autostart mechanisms instead.
