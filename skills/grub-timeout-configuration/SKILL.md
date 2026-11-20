---
name: grub-timeout-configuration
description: Configures the GRUB boot menu delay timeout duration by modifying system configuration files.
triggers: ["set grub timeout", "change boot menu delay", "grub timeout configuration"]
---

# GRUB Timeout Configuration

## Overview
This skill handles modifying the boot menu timeout duration in the GRUB bootloader. It is necessary when the default timeout is too short for user interaction or too long for fast boot times.

## Proven Procedure
1. **Modify the configuration file:**
   Open `/etc/default/grub` with root privileges.
   ```bash
   sudo nano /etc/default/grub
   ```

2. **Update the timeout variable:**
   Locate the line `GRUB_TIMEOUT=X` (where X is the current time in seconds) and change it to the desired duration (e.g., `60`).
   ```bash
   # Example: Change to 60 seconds
   GRUB_TIMEOUT=60
   ```

3. **Apply the changes:**
   The changes will not take effect until the GRUB configuration is regenerated.
   ```bash
   sudo update-grub
   ```

## Pitfalls & Troubleshooting
* **Permissions:** Always use `sudo` when editing `/etc/default/grub` or running `update-grub`; otherwise, changes will be rejected.
* **Typo/Syntax:** Ensure there are no spaces around the `=` sign in `GRUB_TIMEOUT=60`.
* **Verification:** If unsure the change was applied, run `grep "GRUB_TIMEOUT" /etc/default/grub` to confirm the value was saved correctly before running `update-grub`.
