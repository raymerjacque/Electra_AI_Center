---
name: kde-desktop-installation-and-session-switch
description: Installs and switches the desktop environment to KDE Plasma using APT and starts the X11 plasma session.
triggers: ["install plasma-desktop", "switch to kde plasma", "startplasma-x11"]
---

# KDE Plasma Desktop Installation and Session Switch

## Overview
This skill covers installing the KDE Plasma desktop package via APT on a Debian-based system and launching the KDE Plasma X11 session (`startplasma-x11`) to transition the active desktop environment.

## Proven Procedure
1. Verify package availability and install via APT:
   ```bash
   sudo apt update
   sudo apt install plasma-desktop -y
   ```
2. Launch the KDE Plasma X11 session:
   ```bash
   startplasma-x11 &
   ```
3. Verify running Plasma processes:
   ```bash
   pgrep -la plasmashell
   ```

## Pitfalls & Troubleshooting
- Ensure display server variables (`DISPLAY`) are properly exported if running inside an existing graphical session.
- Conflicts between window managers can occur if multiple desktop sessions attempt to manage the same X server concurrently.
