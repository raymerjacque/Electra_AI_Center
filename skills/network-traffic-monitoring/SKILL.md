---
name: network-traffic-monitoring
description: Monitor real-time network bandwidth consumption per process using nethogs to identify heavy network usage.
triggers: ["пожиратель трафика", "network traffic monitor", "bandwidth usage by process", "кто жрет интернет", "nethogs"]
---

# Network Traffic Monitoring per Process

## Overview
Use `nethogs` to inspect which specific applications and processes are consuming network bandwidth in real-time, rather than just viewing abstract IP connections.

## Proven Procedure
1. Install `nethogs` if not already present:
   ```bash
   sudo apt update && sudo apt install nethogs
   ```
2. Run `nethogs` with root privileges to monitor network interfaces:
   ```bash
   sudo nethogs
   ```
3. Use interactive keys inside `nethogs` if needed:
   - `m`: Switch between kb/s, kb, mb, and gb display modes.
   - `r`: Sort by REV/TRAFFIC or RPM.
   - `q`: Quit.

## Pitfalls & Troubleshooting
- **Permission Denied**: `nethogs` requires root privileges (`sudo`) to inspect network sockets of other processes.
- **Interface selection**: If you have multiple network interfaces, specify the interface directly (e.g., `sudo nethogs eth0` or `sudo nethogs wlan0`).
