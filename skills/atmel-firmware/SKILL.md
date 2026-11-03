---
name: atmel-firmware
description: Skill for atmel-firmware
---

# atmel-firmware Skill

This skill provides information about `atmel-firmware`, which contains firmware files for Atmel (now Microchip) microcontrollers and devices.

**Overview:**
- `atmel-firmware` contains firmware files for various Atmel microcontrollers and embedded devices
- Used by Linux kernel drivers to initialize and control Atmel hardware
- Part of the standard firmware packages on Debian/Ubuntu systems
- Essential for devices based on Atmel AVR, ARM, and other Atmel architectures

**Usage:**
- Firmware is automatically loaded by the kernel when the corresponding device driver is probed
- Can view loaded firmware with: `dmesg | grep firmware`
- Device drivers for Atmel devices will automatically request the necessary firmware files
- No manual firmware loading typically needed on modern kernels

**Package purpose:**
- Provides the binary firmware blobs that Atmel-based devices require at boot time
- Works alongside the Linux kernel's firmware loading mechanism
- Part of the `firmware-linux` or `firmware-linux-nonfree` packages on Debian/Ubuntu
