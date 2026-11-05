---
name: zram-optimize-swap
description: Configures and enables Zram swap with Zstd compression for improved system responsiveness and memory management.
triggers: ["optimize swap memory", "enable zram", "improve system responsiveness", "configure zram swap"]
---

# Zram Swap Optimization

## Overview
This skill configures Zram (compressed RAM-based swap) to optimize memory usage, particularly useful on systems with limited physical RAM. It ensures the `zram-tools` package is configured with high-performance `zstd` compression.

## Proven Procedure
1.  **Install/Verify Zram Tools:**
    Ensure the necessary package is installed:
    ```bash
    sudo apt update
    sudo apt install zram-tools
    ```

2.  **Configure Zram:**
    Edit the configuration file `/etc/default/zramswap`:
    ```bash
    sudo nano /etc/default/zramswap
    ```
    Set the following parameters for optimal performance:
    *   `ALGO=zstd` (Best balance between compression ratio and speed)
    *   `PERCENT=50` (Allocates 50% of available RAM to Zram)
    *   `PRIORITY=100` (Ensures Zram is used before physical disk swap)

3.  **Apply Configuration:**
    Restart the Zram service to apply changes:
    ```bash
    sudo systemctl restart zramswap
    ```

4.  **Verify Status:**
    Check that the swap device is active and using the correct settings:
    ```bash
    swapon --show
    # Look for /dev/zram0
    cat /sys/block/zram0/comp_algorithm
    ```

## Pitfalls & Troubleshooting
*   **Compression Choice:** If the CPU is extremely constrained, `lz4` can be used as an alternative to `zstd` for faster compression/decompression at the cost of a slightly lower compression ratio.
*   **Service Failure:** If the service fails to restart, check the logs with `journalctl -u zramswap` to ensure the Zram kernel module is loaded properly.
