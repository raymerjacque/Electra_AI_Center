---
name: systemd-user-service-fix
description: Fix incorrect home directory paths in systemd user service files and reload the systemd daemon.
triggers: ["systemctl --user", "systemd user service", "home/makulu", "daemon-reload"]
---

# Systemd User Service Path Fix

## Overview
When migrating or setting up user-specific systemd services (`~/.config/systemd/user/`), hardcoded paths pointing to a default or old home directory (e.g., `/home/makulu`) will cause services to fail. This skill provides the procedure to update these paths and restart the user service.

## Proven Procedure
1. Locate and update the path in the service file using `sed`:
   ```bash
   sed -i 's|/home/makulu|/home/NEW_USER|g' ~/.config/systemd/user/<service-name>.service
   ```
2. Reload the systemd user daemon:
   ```bash
   systemctl --user daemon-reload
   ```
3. Restart the service and check its status:
   ```bash
   systemctl --user restart <service-name>.service
   systemctl --user status <service-name>.service --no-pager
   ```

## Pitfalls & Troubleshooting
- Ensure `--user` flag is passed to `systemctl` since these are user-level services, not system-wide.
- If the service fails immediately after restart, check logs via `journalctl --user -u <service-name>.service -n 50 --no-pager`.
