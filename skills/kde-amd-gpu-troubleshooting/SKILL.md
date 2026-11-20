---
name: kde-amd-gpu-troubleshooting
description: Procedures for resolving visual artifacts and display glitches specifically on AMD GPU configurations within KDE Plasma/Wayland environments.
triggers: ["amd gpu artifacts", "green lines on screen", "amd wayland flickering", "fix amd display glitches", "disable freesync kde"]
---

# KDE AMD GPU Troubleshooting

## Overview
This skill encapsulates the workflow for diagnosing and resolving common visual artifact issues (such as "green stripes" or frame tearing) that occur on AMD GPU setups running KDE Plasma, particularly under the Wayland compositor. It focuses on isolating driver/compositor handshakes before moving to kernel-level fixes.

## Proven Procedure

### 1. Disable Adaptive Sync (Variable Refresh Rate)
The most common cause of GPU artifacts on AMD/Wayland is a synchronization mismatch between the GPU and the display.
1. Open **System Settings**.
2. Navigate to **Display & Monitor** > **Adaptive Sync**.
3. Set the value to **Never**.
4. Apply changes and restart the KWin compositor (or reboot if persistent).

### 2. Kernel Parameter Adjustments
If artifacts persist, you may need to modify the kernel boot parameters to change how the AMD driver manages power states (often helpful for newer GPUs on older kernels).
1. Edit the GRUB configuration:
   `sudo nano /etc/default/grub`
2. Locate the line `GRUB_CMDLINE_LINUX_DEFAULT`.
3. Add `amdgpu.ppfeaturemask=0xffffffff` to the existing parameters (this enables advanced power management features which can stabilize voltage control).
   *Example:* `GRUB_CMDLINE_LINUX_DEFAULT="quiet splash amdgpu.ppfeaturemask=0xffffffff"`
4. Update GRUB and reboot:
   `sudo update-grub`
   `sudo reboot`

## Pitfalls & Troubleshooting
*   **Wayland vs. X11:** If the issue persists, log out and switch the session from Plasma (Wayland) to Plasma (X11) at the login screen. If the artifacts vanish on X11, the issue is strictly a compositor/Wayland compatibility bug.
*   **Firmware:** Ensure you have the latest non-free firmware packages installed: `sudo apt update && sudo apt install firmware-amd-graphics`.
*   **Hardware:** Green stripes can sometimes indicate physical video cable failure (DisplayPort/HDMI). Always swap the physical cable before assuming a software driver issue.
