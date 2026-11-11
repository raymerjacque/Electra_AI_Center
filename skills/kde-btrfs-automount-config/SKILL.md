---
name: kde-btrfs-automount-config
description: Automates the process of adding a BTRFS filesystem to /etc/fstab for persistent automounting on KDE systems.
triggers: ["automount btrfs drive", "add disk to fstab", "mount uuid to path"]
---

# KDE/System BTRFS Automount Configuration

## Overview
This skill provides a safe and reproducible method for configuring a BTRFS partition to automount upon system boot. It handles the creation of the mount point and the necessary entry in `/etc/fstab` with optimized BTRFS mount options.

## Proven Procedure
To add a persistent mount for a BTRFS drive, execute the following steps:

1. **Create the mount point:**
   ```bash
   sudo mkdir -p /media/herman/Files
   ```

2. **Verify UUID and filesystem:**
   Ensure you have the correct UUID using `lsblk -f` or `blkid`.

3. **Update /etc/fstab:**
   Append the following line to `/etc/fstab`. Note the use of `nofail` to prevent boot hangs if the drive is disconnected.
   ```bash
   echo "UUID=c898476f-ef49-4d1c-9278-ba0b85bc3875 /media/herman/Files btrfs defaults,nofail,ssd,noatime 0 0" | sudo tee -a /etc/fstab
   ```

4. **Verify the configuration:**
   Reload systemd and test the mount without rebooting:
   ```bash
   sudo systemctl daemon-reload
   sudo mount -a
   ls -la /media/herman/Files
   ```

## Pitfalls & Troubleshooting
* **Check UUID:** Always verify the UUID using `lsblk` before editing `fstab`. An incorrect UUID will cause the system to drop into emergency mode or fail to boot if `nofail` is omitted.
* **nofail option:** Always include `nofail` in the mount options for secondary/external drives. This ensures the system continues to boot even if the specific drive is missing or fails to mount.
* **Mount Point:** Ensure the directory path exists before mounting, or `mount -a` will fail.
