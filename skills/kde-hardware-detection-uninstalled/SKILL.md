---
name: kde-hardware-detection-uninstalled
description: Identifies uninstalled or unclaimed hardware devices in KDE Plasma systems, specifically for detecting missing firmware, drivers, or hardware not automatically recognized by the kernel. Useful for troubleshooting hardware visibility in Dolphin/system info and planning firmware/driver installations.
triggers: ["detect uninstalled hardware", "check for unclaimed devices", "hardware not showing in KDE", "missing firmware detection"]
---

# Detect Uninstalled/Unclaimed Hardware in KDE Plasma

## Overview
This skill helps identify hardware devices that are not claimed by the kernel, missing firmware, or not automatically detected in KDE Plasma systems. It is useful when hardware appears missing from system information, Device Manager, or when troubleshooting why a device is not functioning despite physical installation.

## Proven Procedure

### 1. List all PCI devices including unclaimed
```bash
lspci -vvv | grep -E "Unclaimed|Memory at|I/O ports"
```

### 2. Check for devices without kernel driver
```bash
lspci -nnk | grep -A 3 "Kernel driver in use:"
# Look for entries showing "Kernel driver in use: (none)" or nothing
```

### 3. Check USB devices for unclaimed/device issues
```bash
lsusb -v
# Or list all devices with status
lsusb -t
```

### 4. Check dmesg for firmware/boot warnings
```bash
dmesg | grep -i "firmware\|unclaimed\|error\|failed"
```

### 5. List block devices and look for "unknown" or missing sizes
```bash
lsblk -o NAME,SIZE,TYPE,MOUNTPOINT
```

### 6. Install missing firmware (if identified)
```bash
# Example for Intel graphics/firmware
sudo apt install firmware-intel-graphics firmware-intel-misc firmware-intel-sound

# Example for Wi-Fi
sudo apt install firmware-iwlwifi
```

### 7. For NVIDIA/AMD specific unclaimed devices
```bash
# Check NVIDIA driver status
nvidia-smi

# Or install open-source driver
sudo apt install xserver-xorg-video-amdgpu
```

## Pitfalls & Troubleshooting

- **lspci shows device but OS doesn't recognize it**: May require kernel update or specific firmware package. Check `dmesg` for error messages during boot.
- **USB device not appearing**: Try different port, check `lsusb` output, or verify `usermod -a -G plugdev $USER` for group membership.
- **Block device shows 0 size**: May indicate missing partition table or uninitialized disk. Use `sudo fdisk -l` to inspect.
- **KDE System Monitor shows "N/A" for hardware**: Often resolved by restarting system or checking `sudo lshw -short` for complete hardware listing.
- **If `lspci -nnk` shows "Kernel driver in use: " (empty)**: This indicates an unclaimed device. Search for compatible firmware or driver online matching the device ID (e.g., `10de:` for NVIDIA, `8086:` for Intel).

**Note**: Always run system updates before investigating unclaimed hardware:
```bash
sudo apt update && sudo apt full-upgrade
```
Reboot after firmware installations for proper detection.
