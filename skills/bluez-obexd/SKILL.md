---
name: bluez-obexd
description: Skill for bluez-obexd
---

# bluez-obexd Skill

This skill provides functionality for `bluez-obexd`, the OBEX (Object Exchange) daemon for the BlueZ Bluetooth stack.

**Overview:**
- `bluez-obexd` provides Object Exchange (OBEX) protocol support over Bluetooth
- OBEX is used for file transfer, synchronization, and object exchange between devices
- Commonly used for transferring files, contacts, and messages between Bluetooth devices
- Part of the `bluez-obexd` package on Debian/Ubuntu systems

**Commands:**
- `systemctl start bluez-obexd` - Start the OBEX daemon
- `systemctl status bluez-obexd` - Check OBEX daemon status
- `obexftp` - OBEX file transfer tool (user-space)
- `obexctl` - OBEX control tool

**Usage examples:**
- Start OBEX service: `systemctl start bluez-obexd`
- Transfer files via OBEX (details depend on specific implementation)
- OBEX is commonly used for: file transfer, syncing contacts, headset audio

**Package purpose:**
- Provides OBEX protocol implementation over Bluetooth
- Enables file transfer and synchronization capabilities
- Works with the main `bluez` Bluetooth stack
