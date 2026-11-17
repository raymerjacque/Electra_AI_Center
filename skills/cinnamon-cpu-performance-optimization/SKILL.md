---
name: cinnamon-cpu-performance-optimization
description: Optimizes CPU frequency scaling by setting governors and disabling power-save features to ensure consistent desktop-grade performance on laptop hardware.
triggers: ["prevent cpu throttling", "set cpu to performance mode", "disable power saving", "make laptop act like desktop", "improve cpu performance"]
---

# CPU Performance Optimization

## Overview
This skill forces the system to ignore power-saving states and prioritizes raw processing power. This is useful when a laptop is used as a "desktop replacement" where power efficiency is secondary to maintaining high performance without clock-speed throttling.

## Proven Procedure
1.  **Install necessary tools** (if not present):
    ```bash
    sudo apt update
    sudo apt install linux-cpupower
    ```

2.  **Verify current CPU state**:
    ```bash
    cpupower frequency-info
    ```

3.  **Set the CPU governor to performance mode**:
    This command instructs the kernel to set all CPU cores to their maximum supported frequency.
    ```bash
    sudo cpupower frequency-set -g performance
    ```

4.  **Make the setting persistent** (optional but recommended):
    By default, these settings reset on reboot. You can create a systemd service or add the command to `/etc/rc.local` (if enabled) or a custom startup script. For a robust approach, use a `udev` rule or `systemd` unit:

    Create `/etc/systemd/system/cpu-performance.service`:
    ```ini
    [Unit]
    Description=Set CPU governor to performance
    After=multi-user.target

    [Service]
    Type=oneshot
    ExecStart=/usr/bin/cpupower frequency-set -g performance

    [Install]
    WantedBy=multi-user.target
    ```

    Enable it:
    ```bash
    sudo systemctl enable --now cpu-performance.service
    ```

## Pitfalls & Troubleshooting
*   **Hardware Limitations**: If the BIOS/UEFI firmware has "Battery Limit" protection (common in some laptops without a battery connected), no OS-level setting can override it. The hardware will throttle regardless of the OS governor.
*   **Heat**: Setting the CPU to `performance` mode will significantly increase power draw and heat generation. Ensure adequate cooling is present.
*   **Permissions**: `cpupower` requires root privileges to apply changes to the governor.
