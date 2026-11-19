---
name: boot-repair-lightdm
description: Fix GRUB command-line boot prompt and configure LightDM display manager for automatic graphical startup.
triggers: ["grub prompt", "fix grub", "update-grub", "lightdm enable", "graphical.target", "startx manual"]
---

# Boot and Display Manager Recovery

## Overview
This skill covers recovering from a GRUB bootloader prompt (`grub>`) and fixing issues where the system boots into a terminal requiring a manual `startx` command instead of starting the graphical display manager automatically.

## Proven Procedure

### 1. Fix GRUB Bootloader Prompt
If the system boots into the `grub>` rescue/command-line prompt, boot into a live USB or recovery environment, chroot into the installation if necessary, and update the GRUB configuration:
```bash
sudo update-grub
```
If the GRUB bootloader itself needs reinstalling to the EFI partition or MBR:
```bash
sudo grub-install /dev/sdX
sudo update-grub
```

### 2. Configure LightDM for Automatic Graphical Startup
If the system boots to a text login or requires manual `startx`, ensure LightDM is enabled and the default system target is set to graphical:
```bash
sudo systemctl enable lightdm
sudo systemctl set-default graphical.target
sudo systemctl start lightdm
```

## Pitfalls & Troubleshooting
- Ensure you have root privileges or use `sudo` for `systemctl` and `update-grub`.
- If `lightdm` is not installed, install it via your package manager (e.g. `sudo apt install lightdm`) and select it via `sudo dpkg-reconfigure lightdm`.
