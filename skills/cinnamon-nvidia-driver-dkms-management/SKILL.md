---
name: cinnamon-nvidia-driver-dkms-management
description: Handles the installation, updating, and troubleshooting of NVIDIA proprietary drivers using DKMS, including Nouveau blacklisting and initramfs regeneration.
triggers: ["update nvidia drivers", "check nvidia driver status", "install nvidia-driver-dkms", "nvidia-smi not found", "blacklist nouveau", "nvidia kernel mismatch"]
---

# NVIDIA DKMS Driver Management

## Overview
This skill provides a structured, automated approach to installing or upgrading NVIDIA drivers on Debian-based systems. It addresses common failure points: kernel module mismatches, conflicting open-source drivers (Nouveau), and DKMS compilation issues. Use this when `nvidia-smi` is missing or reporting version mismatches.

## Proven Procedure
1.  **Identify Hardware & Drivers:**
    Verify the hardware and current driver status.
    ```bash
    lspci -nnk | grep -i nvidia -A 3
    ```

2.  **Clean & Prepare:**
    Purge existing problematic installations and ensure the system is ready for the new driver.
    ```bash
    sudo apt update
    sudo apt purge nvidia*
    sudo apt autoremove
    ```

3.  **Blacklist Nouveau:**
    Prevent conflicts with the open-source driver.
    ```bash
    echo "blacklist nouveau" | sudo tee /etc/modprobe.d/blacklist-nvidia-nouveau.conf
    echo "options nouveau modeset=0" | sudo tee -a /etc/modprobe.d/blacklist-nvidia-nouveau.conf
    sudo update-initramfs -u
    ```

4.  **Install Driver via DKMS:**
    Install the driver and ensure DKMS builds the module against the current kernel.
    ```bash
    sudo apt install nvidia-driver nvidia-dkms nvidia-smi
    ```

5.  **Finalize & Verify:**
    Update initramfs again to include the new modules and reboot.
    ```bash
    sudo update-initramfs -u
    sudo reboot
    # After reboot, verify with:
    nvidia-smi
    ```

## Pitfalls & Troubleshooting
*   **Kernel Mismatch:** If `nvidia-smi` fails with a version mismatch, it usually means the DKMS module failed to compile against the *current* kernel. Check logs in `/var/lib/dkms/nvidia/`.
*   **Secure Boot:** If the driver fails to load after reboot, check if UEFI Secure Boot is enabled. You must sign the kernel modules or disable Secure Boot in the BIOS for third-party proprietary drivers to function.
*   **Missing Headers:** Ensure `linux-headers-$(uname -r)` is installed before attempting to install `nvidia-dkms`.
