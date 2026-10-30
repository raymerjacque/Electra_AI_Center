---
name: zram-swap-setup
description: Setup and configure zram compressed RAM swap with zstd compression on Debian/Ubuntu systems to prevent system freezes.
triggers: ["zram swap", "setup zram", "zstd compression swap", "prevent system freeze RAM full", "zram-tools"]
---

# Zram Compressed Swap Setup on Debian/Ubuntu

## Overview
Configures compressed RAM swap using `zram` and the high-performance `zstd` algorithm on Debian and Ubuntu systems. This prevents system freezes and severe slowdowns when physical memory (RAM) is exhausted, avoiding slow disk-based swap usage.

## Proven Procedure

1. **Install `zram-tools`:**
   ```bash
   sudo apt update && sudo apt install -y zram-tools
   ```

2. **Configure the zram algorithm and size:**
   Edit or configure `/etc/default/zramswap` to use `zstd` compression and allocate an appropriate percentage of RAM (e.g., 50%):
   ```bash
   sudo tee /etc/default/zramswap << 'EOF'
   ALGO=zstd
   PERCENT=50
   EOF
   ```

3. **Restart the zramswap service:**
   ```bash
   sudo systemctl restart zramswap
   ```

4. **Verify active zram devices and swap status:**
   ```bash
   zramctl
   swapon --show
   ```

## Pitfalls & Troubleshooting
- **Priority Issues:** Ensure that the zram swap device has a higher priority than any disk-based swap files or partitions so the system fills zram first. Check priorities using `swapon --show`.
- **Module Support:** Verify that the running kernel has the `zram` module enabled (`modprobe zram`).
