---
name: kde-amdgpu-flicker-fix
description: Stabilizes AMD GPU performance on KDE Plasma by configuring kernel module parameters to resolve display glitches and power state issues.
triggers: ["fix amdgpu glitches", "resolve screen flickering kde", "amdgpu power management config", "gpu firmware crash"]
---

# AMDGPU Kernel Stabilization (KDE Plasma)

## Overview
This skill resolves graphical artifacts (green stripes, tearing, or flickering) on KDE Plasma systems running AMD GPUs. It involves tuning the kernel module parameters for `amdgpu` to force stable power states and Display Core (DC) initialization, often necessary when the kernel aggressive power management conflicts with the Wayland compositor.

## Proven Procedure
1.  **Identify the need:** If encountering graphical artifacts, screen flashing, or hangs while using an AMD GPU on Plasma/Wayland.
2.  **Create the configuration file:** Create or edit the modprobe configuration for the AMD driver.
    ```bash
    sudo nano /etc/modprobe.d/amdgpu.conf
    ```
3.  **Apply parameters:** Add the following line to force the Display Core (DC) initialization, which helps sync the driver with the compositor:
    ```text
    options amdgpu dc=1
    ```
    *Note: If issues persist, try changing `dc=1` to `dc=0`.*
4.  **Regenerate Initramfs:** Apply the changes to the boot image.
    ```bash
    sudo update-initramfs -u
    ```
5.  **Reboot:** Restart the system to apply the new kernel boot parameters.

## Pitfalls & Troubleshooting
*   **The Toggle:** If `dc=1` causes a black screen or worse artifacts, you must boot into a recovery shell or use a Live ISO to change the config to `dc=0` or remove the file entirely.
*   **Compatibility:** This is specific to `amdgpu` drivers. Do not use this for NVIDIA systems.
*   **Kernel Mismatch:** If using a custom kernel (like CachyOS/Xanmod), ensure the kernel headers match your installed kernel version before modifying modules.
