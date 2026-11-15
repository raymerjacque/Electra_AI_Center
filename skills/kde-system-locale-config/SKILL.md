---
name: kde-system-locale-config
description: Configure system-wide language, regional formats, and localization using localectl and update-locale.
triggers: ["change system locale", "set system language", "update locale", "localectl", "configure regional format"]
---

# System Locale and Regional Configuration

## Overview
Use this skill when you need to change the system-wide language, regional formatting, or default measurement units (such as switching between metric and imperial) via systemd's `localectl` and `update-locale`.

## Proven Procedure
1. Check current locale and keyboard settings:
   ```bash
   localectl status
   ```
2. List available locales on the system:
   ```bash
   localectl list-locales
   ```
3. Update the system locale (e.g., to US English for standard regional formats):
   ```bash
   sudo localectl set-locale LANG=en_US.UTF-8
   ```
   Alternatively, update `/etc/default/locale`:
   ```bash
   sudo update-locale LANG=en_US.UTF-8
   ```
4. Restart your session or reboot for the changes to apply across all desktop environments and applications.

## Pitfalls & Troubleshooting
- Some desktop environments (like KDE Plasma or Cinnamon) have their own GUI region and language settings that may override or require a separate configuration panel adjustment.
- Ensure the target locale is generated in `/etc/locale.gen` and run `sudo locale-gen` if the locale is missing.
