---
name: cinnamon-ai-os-network-discovery
description: Tools and procedures for discovering AI-OS Rift Desktop instances on a local network via UDP/TCP broadcast scanning.
triggers: ["scan for ai-os peers", "find rift desktop on network", "network discovery for ai-os"]
---

# AI-OS Network Discovery

## Overview
This skill provides the mechanism to identify other AI-OS Rift Desktop nodes on the local subnet. It uses a custom Python-based broadcast scanner that probes port 8765, which is the standard port for AI-OS service discovery and telemetry.

## Proven Procedure
To scan the local network for peers, utilize the verified scanning script located at `/home/guy/scan_aios_peers_v2.py`.

1. **Invoke the scanner**:
   Run the following command to scan your subnet (ensure you have the script in the path):
   ```bash
   python3 /home/guy/scan_aios_peers_v2.py
   ```

2. **Scanner Logic**:
   The script performs the following actions:
   - Initializes a UDP socket.
   - Broadcasts a JSON discovery payload to the `255.255.255.255` address on UDP port `8765`.
   - Listens for a response packet from other active AI-OS nodes.
   - Parses the JSON response to return the hostname, IP, and service status of discovered nodes.

3. **Prerequisites**:
   If the script fails due to missing dependencies, ensure the following are installed:
   ```bash
   sudo apt install python3-gi libgirepository-2.0-dev
   pip install PyGObject
   ```

## Pitfalls & Troubleshooting
- **Firewall Interference**: If the scan returns 0 peers despite knowing one exists, the remote firewall (e.g., UFW) may be blocking UDP port `8765`. On the target machine, run `sudo ufw allow 8765/udp`.
- **Subnet Mismatch**: Ensure your interface is correctly assigned to the `192.168.1.0/24` subnet. If your network configuration differs, the script may require modification to the broadcast address.
- **Service Status**: Ensure the `ai_os_discovery_daemon` is active on the target machine; if the daemon is stopped, the peer will not respond to discovery probes.
