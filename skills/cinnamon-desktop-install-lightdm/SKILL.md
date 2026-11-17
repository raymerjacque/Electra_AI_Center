---
name: cinnamon-desktop-install-lightdm
description: Install Cinnamon desktop environment on Debian-based MakuluLinux systems and configure LightDM display manager for session selection.
triggers: ["install cinnamon desktop", "setup cinnamon display manager", "configure lightdm for cinnamon"]
---

# Cinnamon Desktop Installation and LightDM Configuration

## Overview
This skill provides the procedure for installing the Cinnamon desktop environment and configuring LightDM to allow users to select between Cinnamon and other pre-installed desktop environments (such as KDE Plasma).

## Proven Procedure
1. Update package lists and install the Cinnamon desktop environment:
   ```bash
   sudo apt update && sudo apt install cinnamon cinnamon-desktop-environment -y
   ```
2. Verify or configure LightDM as the default display manager and set the default session:
   ```bash
   sudo apt install lightdm lightdm-gtk-greeter -y
   sudo dpkg-reconfigure lightdm
   ```
3. Edit `/etc/lightdm/lightdm.conf` (or drop-in files under `/etc/lightdm/lightdm.conf.d/`) to set the default user session:
   ```ini
   [Seat:*]
   user-session=cinnamon
   ```
4. Verify session availability in `/usr/share/xsessions/cinnamon.desktop`.
5. Reboot the system to apply display manager and session changes.

## Pitfalls & Troubleshooting
- **Display manager conflicts**: If GDM3 or SDDM is running instead of LightDM, LightDM needs to be explicitly enabled via `sudo systemctl enable lightdm --force`.
- **Missing session options**: Ensure `cinnamon-session` and `cinnamon-control-center` are installed if the greeter does not show the Cinnamon session option.
