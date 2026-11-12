---
name: cinnamon-apt-unlock-recovery
description: Fixes APT package manager "could not get lock" errors by safely removing stale lock files that block system updates.
triggers: ["apt lock error", "dpkg lock", "fix apt database lock", "apt-get upgrade failed lock"]
---

# APT Unlock Recovery

## Overview
This skill handles the common "Could not get lock" error in Debian-based systems. It occurs when an APT process (update, upgrade, or install) is interrupted abruptly, leaving stale lock files in `/var/lib/apt/` or `/var/lib/dpkg/` that prevent future package operations.

## Proven Procedure
1. **Identify existing processes** to ensure no legitimate update is running:
   ```bash
   ps aux | grep -i apt
   ```
2. **Remove the stale lock files** with administrative privileges:
   ```bash
   sudo rm /var/lib/apt/lists/lock
   sudo rm /var/lib/dpkg/lock
   sudo rm /var/lib/dpkg/lock-frontend
   ```
3. **Reconfigure the database** to resolve any inconsistencies:
   ```bash
   sudo dpkg --configure -a
   sudo apt-get update
   ```

## Pitfalls & Troubleshooting
* **NEVER remove these files while an update is actually running.** Always run `ps aux | grep -i apt` first. If you delete them while a process is active, you risk corrupting the package database.
* If the error persists, the issue might be a broken package dependency rather than just a lock file. Run `sudo apt-get install -f` to attempt a fix of missing dependencies.
