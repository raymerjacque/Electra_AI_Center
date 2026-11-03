---
name: bolt
description: Skill for bolt
---

# bolt Skill

This skill provides functionality for `bolt`, a power and battery management tool for Linux systems.

**Overview:**
- `bolt` is a power and battery management tool for Linux systems
- Provides battery status, power profile management, and power-saving features
- Part of the `bolt` package on some Linux distributions (particularly Fedora/Flatpak)
- Works with upower and system power management

**Commands:**
- `bolt --status` - Show battery and power status
- `bolt --show-profile` - Show current power profile
- `bolt --set-profile <profile>` - Set power profile (performance, power-saver, etc.)
- `bolt --list-profiles` - List available power profiles

**Usage examples:**
- Check battery status: `bolt --status`
- Switch to power-saver mode: `bolt --set-profile power-saver`
- List available profiles: `bolt --list-profiles`
- Check power percentage: `bolt --status | grep percentage`

**Package purpose:**
- Power management and battery status for Linux laptops
- Provides quick access to power settings from the command line
- Works with system power management frameworks (UPower, systemd)
