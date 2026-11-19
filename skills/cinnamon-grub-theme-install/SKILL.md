---
name: cinnamon-grub-theme-install
description: Extract, verify compatibility, and install a GRUB bootloader theme from a tarball archive into /boot/grub/themes and update system configuration.
triggers: ["install grub theme", "apply grub theme", "extract grub theme tarball", "configure grub theme"]
---

# GRUB Theme Installation and Configuration

## Overview
This skill covers the process of analyzing, extracting, verifying, and installing a GRUB bootloader theme archive (such as a `.tar.gz`) into `/boot/grub/themes/` and configuring GRUB to use the theme via `/etc/default/grub` or its configuration snippets.

## Proven Procedure

1. **Locate and Analyze the Archive:**
   - Locate the theme archive (e.g., in `~/Downloads/`).
   - Extract the archive to inspect its contents:
     ```bash
     tar -xzf /path/to/theme.tar.gz -C /tmp/
     ```
   - Verify that essential GRUB theme assets exist in the extracted folder:
     - `theme.txt` (the primary layout and configuration file)
     - Background images (e.g., `background.png`, `.jpg`)
     - Font files (`.pf2` files required by `theme.txt`)
     - UI icons or pixmap graphics (selection boxes, icons, etc.)

2. **Install Theme Files to GRUB Directory:**
   - Create the target theme directory under `/boot/grub/themes/`:
     ```bash
     sudo mkdir -p /boot/grub/themes/<theme-name>
     ```
   - Move or copy the verified theme files into the directory:
     ```bash
     sudo cp -r /tmp/<extracted-theme-folder>/* /boot/grub/themes/<theme-name>/
     ```

3. **Configure GRUB to Use the Theme:**
   - Set the theme path in `/etc/default/grub` or a drop-in configuration file under `/etc/default/grub.d/`:
     ```bash
     GRUB_THEME="/boot/grub/themes/<theme-name>/theme.txt"
     ```
   - Ensure graphical terminal and timeout options are appropriately set if needed (e.g., `GRUB_TERMINAL_OUTPUT="gfxterm"`).

4. **Update GRUB Configuration:**
   - Regenerate the main GRUB configuration file to apply the theme:
     ```bash
     sudo update-grub
     ```
     *(Or on non-Debian systems: `sudo grub-mkconfig -o /boot/grub/grub.cfg`)*

## Pitfalls & Troubleshooting
- **Missing Fonts:** If `.pf2` fonts specified in `theme.txt` are missing, GRUB may fall back to a plain text menu or fail to render the custom layout. Ensure fonts are generated or included in the theme package.
- **Image Formats:** GRUB supports basic PNG and JPEG images, but complex color profiles or interlaced PNGs may fail to render properly during early boot.
- **Root Partition:** Ensure `/boot/grub/` is writable and has sufficient space before copying large theme assets.
