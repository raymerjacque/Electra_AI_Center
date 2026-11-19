---
name: cinnamon-boot-repair-grub-display-manager
description: Troubleshoot and fix GRUB prompt startup issues and missing graphical login manager (lightdm) requiring manual startx in Cinnamon.
triggers: ["grub prompt fix", "lightdm enable graphical target", "fix startx manual boot"]
---

# Fix GRUB Prompt and Display Manager Boot Issues

## Overview
This skill resolves two common boot failures on Linux systems running Cinnamon:
1. GRUB dropping into the rescue/interactive `grub>` prompt instead of loading the menu.
2. System booting into a text-only TTY, requiring a manual `startx` command to launch the graphical environment due to a disabled or misconfigured display manager (LightDM).

## Proven Procedure

### 1. Fix GRUB Boot Configuration
If the system drops to the `grub>` prompt at boot:
```bash
sudo update-grub
```
If the GRUB bootloader itself needs to be reinstalled to the primary disk (e.g., `/dev/sda` or `/dev/nvme0n1`):
```bash
sudo grub-install /dev/sda
sudo update-grub
```

### 2. Fix Graphical Environment / Display Manager Startup
If the system boots to a text TTY and requires manual `startx`:
1. Check the status of the display manager (LightDM is standard for many Cinnamon setups):
   ```bash
   sudo systemctl status lightdm
   ```
2. Enable and start the display manager service:
   ```bash
   sudo systemctl enable lightdm
   sudo systemctl start lightdm
   ```
3. Ensure the system default target is set to graphical:
   ```bash
   sudo systemctl set-default graphical.target
   ```

## Pitfalls & Troubleshooting
- Ensure you identify the correct disk when reinstalling GRUB (`lsblk` can help verify partitions).
- If `lightdm` is not installed or corrupted, reinstall it via package manager: `sudo apt install --reinstall lightdm lightdm-gtk-greeter`.
