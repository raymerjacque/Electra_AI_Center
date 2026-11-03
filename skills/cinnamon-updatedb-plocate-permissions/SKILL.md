---
name: cinnamon-updatedb-plocate-permissions
description: Fix permission denied errors for updatedb when running under plocate by managing group membership and database file permissions.
triggers: ["updatedb", "plocate permission denied", "plocate.db permission", "update database file search perm"]
---

# Updatedb Plocate Permissions Fix

## Overview
This skill resolves permission denied issues encountered when running `updatedb` (using `plocate`) as a non-root user or when group permissions on `/var/lib/plocate/plocate.db` are misconfigured.

## Proven Procedure
1. Add the current user to the `plocate` group:
   ```bash
   sudo usermod -aG plocate $USER
   ```
2. Ensure the `/var/lib/plocate` directory and database file allow group write/read access for the `plocate` group:
   ```bash
   sudo chown root:plocate /var/lib/plocate/plocate.db
   sudo chmod g+rw /var/lib/plocate/plocate.db
   sudo chmod g+rwx /var/lib/plocate/
   ```
3. Run `updatedb` within the `plocate` group context if necessary:
   ```bash
   sg plocate -c "updatedb"
   ```

## Pitfalls & Troubleshooting
- If `updatedb` still fails with permission errors, check if `plocate` package daemon or systemd timers are overriding file permissions.
- Always verify group membership took effect by running `groups` or logging out and back in.
