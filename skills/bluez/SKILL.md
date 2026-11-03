---
name: bluez
description: Skill for bluez
---

# bluez Skill

This skill provides functionality for `bluez`, the official Linux Bluetooth protocol stack.

**Overview:**
- `bluez` is the official Linux Bluetooth protocol stack maintained by the Linux Bluetooth group
- Provides comprehensive Bluetooth support including drivers, daemons, tools, and libraries
- Manages Bluetooth hardware, devices, connections, and profiles
- Part of the core `bluez` package on Debian/Ubuntu/MakuluLinux systems

**Commands:**
- `systemctl start bluetooth` - Start the Bluetooth daemon
- `systemctl status bluetooth` - Check Bluetooth service status
- `bluetoothctl` - Interactive Bluetooth command line tool
- `hciconfig` - Configure Bluetooth hardware
- `hcitool` - Bluetooth tool for scanning and inquiry
- `btmgmt` - Bluetooth management tool (newer generation)

**Usage examples:**
- Start Bluetooth: `systemctl start bluetooth`
- Pair device: `bluetoothctl pair <device_address>`
- Connect device: `bluetoothctl connect <device_address>`
- Scan devices: `bluetoothctl devices`
- Information: `bluetoothctl info <device_address>`

**Package purpose:**
- Official Bluetooth protocol stack for Linux kernel
- Essential for Bluetooth hardware support
- Provides both system services and user-space tools
- Works with hardware vendors for driver support
