---
name: cinnamon-grub-windows-dualboot
description: Add a custom Windows boot entry to the GRUB bootloader menu using EFI partition UUID and /etc/grub.d/40_custom on Cinnamon systems.
triggers: ["add windows to grub", "dual boot grub custom entry", "update grub windows efi"]
---

# Add Windows Dual-Boot Entry to GRUB

## Overview
This skill describes how to manually add a Windows boot entry to the GRUB bootloader menu on Linux systems (specifically tested on Cinnamon/Ubuntu/Debian-based distributions) by editing `/etc/grub.d/40_custom` using the EFI system partition UUID.

## Proven Procedure
1. Identify the EFI system partition and its UUID:
   ```bash
   sudo blkid
   ```
   Locate the EFI partition (e.g., `/dev/sda1`) and note its `UUID`.

2. Create a custom GRUB menu entry in `/etc/grub.d/40_custom`:
   Open the file with root privileges:
   ```bash
   sudo nano /etc/grub.d/40_custom
   ```
   Add the following entry (replace `YOUR-EFI-UUID-HERE` with the actual UUID):
   ```text
   menuentry "Windows 11 / 10" {
       insmod part_gpt
       insmod fat
       search --no-floppy --fs-uuid --set=root YOUR-EFI-UUID-HERE
       chainloader /EFI/Microsoft/Boot/bootmgfw.efi
   }
   ```

3. Update the GRUB configuration:
   ```bash
   sudo update-grub
   ```

## Pitfalls & Troubleshooting
- Ensure `os-prober` is enabled if automatic detection is preferred, but manual configuration via `40_custom` bypasses detection issues.
- Double-check the path to `bootmgfw.efi` inside the EFI partition if Windows fails to boot.
