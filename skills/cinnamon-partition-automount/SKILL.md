---
name: cinnamon-partition-automount
description: Automatically mount a disk partition at boot using its UUID in fstab for Cinnamon and Ubuntu-based systems.
triggers: ["auto mount partition", "mount drive at boot", "fstab uuid mount", "cinnamon auto mount drive"]
---

# Cinnamon Partition Automount

## Overview
This skill provides a reliable, safe procedure to configure a partition to automatically mount at system boot using its unique UUID in `/etc/fstab` on MakuluLinux Cinnamon or other Ubuntu/Debian-based distributions.

## Proven Procedure
1. Identify the exact filesystem type of the target partition using its UUID:
   ```bash
   sudo blkid /dev/disk/by-uuid/<YOUR-UUID>
   ```
2. Create a backup of the current `/etc/fstab` file to prevent unbootable system states in case of syntax errors:
   ```bash
   sudo cp /etc/fstab /etc/fstab.bak
   ```
3. Create the mount point directory if it does not already exist:
   ```bash
   sudo mkdir -p /media/username/4a179792-f2d6-434b-b81c-5b95360152141
   ```
4. Open `/etc/fstab` with a text editor:
   ```bash
   sudo nano /etc/fstab
   ```
5. Append the entry using the UUID format (adjust filesystem type like `ext4`, `ntfs`, or `exfat` and options as appropriate):
   ```text
   UUID=4a179792-f2d6-434b-b81c-5b95360152141 /media/jacque/4a179792-f2d6-434b-b81c-5b95360152141 ext4 defaults 0 2
   ```
6. Test the fstab configuration without rebooting:
   ```bash
   sudo mount -a
   ```

## Pitfalls & Troubleshooting
- **Typos in fstab:** A syntax error in `/etc/fstab` can cause the system to drop into emergency mode or fail to boot. Always run `sudo mount -a` to test entries before rebooting.
- **Wrong Filesystem Type:** Ensure the filesystem type in `fstab` matches the output of `blkid` (e.g., `ntfs-3g` for NTFS drives instead of just `ntfs`).
