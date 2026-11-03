---
name: bluetooth
description: Skill for bluetooth
---

# bluetooth Skill

This skill provides functionality for `bluetooth`, the Linux Bluetooth protocol stack and utilities.

**Overview:**
- `bluetooth` is the Linux Bluetooth protocol stack (BlueZ) that provides core Bluetooth functionality
- Includes daemons, tools, and libraries for Bluetooth communication
- Part of the core Linux system on systems with Bluetooth hardware
- Manages Bluetooth devices, connections, and profiles

**Commands:**
- `systemctl start bluetooth` - Start the Bluetooth daemon
- `systemctl status bluetooth` - Check Bluetooth service status
- `bluetoothctl` - Interactive Bluetooth command line tool
- `hciconfig` - Configure Bluetooth hardware
- `hcitool` - Bluetooth tool for scanning and inquiry
- `btmgmt` - Bluetooth management tool (newer)

**Usage examples:**
- Start Bluetooth service: `systemctl start bluetooth`
- Pair device: `bluetoothctl pair <device_address>`
- Connect device: `bluetoothctl connect <device_address>`
- Scan for devices: `bluetoothctl devices`
- Check status: `systemctl status bluetooth`

**Package purpose:**
- Core Bluetooth protocol stack for Linux
- Essential for any Bluetooth hardware functionality
- Provides both daemon services and command-line tools
