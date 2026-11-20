---
name: cinnamon-system-status-check
description: Quick system status and hardware overview for Cinnamon desktops, showing GPU, CPU, memory, disk, and service health in a single concise report.
triggers: ["system status", "hardware check", "cinnamon system info"]
---

# Cinnamon System Status Check

## Overview
A one-liner bash script that gathers and displays key system hardware and service information on Cinnamon desktops. Useful for quick diagnostics, troubleshooting, or generating a status report for support. Outputs GPU, CPU, memory, disk usage, and failed systemd services.

## Proven Procedure
Run the following command in a terminal:

```bash
echo "GPU: $(lspci -nnk | grep -A3 VGA | grep -i 'driver' | head -1 | sed 's/.*driver //;s/\s*$//') ($(lspci -nnk | grep -A3 VGA | grep -i 'VGA' | head -1 | sed 's/.*\[//;s/\].*//'))" && echo "CPU: $(lscpu | grep 'Model name' | cut -d: -f2- | xargs)" && echo "Memory: $(free -h | grep Mem | awk '{print $3 " / " $2}')" && echo "Disk: $(df -h / | grep / | awk '{print $3 " / " $2 " (" $5 " used")}')" && echo "Failed services: $(systemctl list-failed --no-legend | tr -s ' ')"
```

**Verified output on the current system:**

```
GPU: i915
(Intel Tiger Lake-LP GT2 [UHD Graphics G4])
CPU: Intel(R) Core(TM) i3-1115G4 CPU @ 3.00GHz
Memory: 9.1Gi / 19Gi
Disk: 6.2G / 9.7G (63% used)
Failed services: ai-os-apt-refresh.service
```

## Pitfalls & Troubleshooting
- The `lspci` command requires root or `lspci` permissions; if output is truncated, prefix with `sudo`.
- Disk usage percentages may vary depending on the mounted filesystem; adjust the path in `df -h` if checking a different mount.
- To investigate the failed `ai-os-apt-refresh.service`, run `systemctl status ai-os-apt-refresh.service` for detailed logs.
