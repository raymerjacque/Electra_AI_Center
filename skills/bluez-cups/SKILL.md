---
name: bluez-cups
description: Skill for bluez-cups
---

# bluez-cups Skill

This skill provides functionality for `bluez-cups`, which provides Bluetooth printing support for CUPS.

**Overview:**
- `bluez-cups` adds Bluetooth printing support to the CUPS printing system
- Allows printing to Bluetooth-enabled printers without requiring a wired connection
- Part of the `bluez-cups` package on Debian/Ubuntu systems
- Integrates Bluetooth printers as CUPS backend devices

**Usage:**
- Ensure `bluez-cups` package is installed
- The CUPS service will automatically detect Bluetooth printers when `bluez-cups` is loaded
- Printers can be added via the CUPS web interface or `lpadmin` command
- Works alongside the main `bluez` Bluetooth stack

**Package purpose:**
- Enables Bluetooth printing capabilities on Linux systems
- Extends CUPS to support wireless Bluetooth printers
- Commonly used with portable and mobile Bluetooth printers
