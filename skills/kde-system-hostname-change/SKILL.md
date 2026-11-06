---
name: kde-system-hostname-change
description: Safely updates the system hostname across all required configuration files and systemd settings.
triggers: ["change system hostname", "set new computer name", "update machine hostname", "rename system"]
---

# System Hostname Change

## Overview
This skill safely updates the system's hostname. Manually changing the hostname by editing only one file often leads to resolution errors or mismatches between `hostnamectl` and the `/etc/` configuration files. This procedure ensures consistency across the system.

## Proven Procedure
To change the system hostname to a new name, execute the following steps:

1. **Update Systemd Hostname:**
   ```bash
   sudo hostnamectl set-hostname <NEW_HOSTNAME>
   ```

2. **Update the Hostname file:**
   Ensure `/etc/hostname` contains only the new name:
   ```bash
   echo "<NEW_HOSTNAME>" | sudo tee /etc/hostname
   ```

3. **Update the Hosts file:**
   Edit `/etc/hosts` to replace the old hostname with the new one for the loopback address (usually `127.0.1.1`):
   ```bash
   sudo sed -i 's/127.0.1.1.*/127.0.1.1 <NEW_HOSTNAME>/' /etc/hosts
   ```

4. **Verify Change:**
   Apply the changes (often effective immediately, but logging out/in or rebooting ensures all services pick up the change):
   ```bash
   hostnamectl status
   cat /etc/hostname
   cat /etc/hosts
   ```

## Pitfalls & Troubleshooting
*   **Case Sensitivity:** Hostnames are typically lowercase. Avoid using spaces or special characters, as these can break network services (like Avahi or local DNS).
*   **Service Restarts:** Some network-related services may not recognize the name change until the system is rebooted. If local network services fail after a change, a reboot is the safest resolution.
*   **DNS Issues:** If `/etc/hosts` is not updated to match the new hostname, some applications (specifically those using local loopback for IPC) may hang or fail to start. Always ensure the `127.0.1.1` entry matches the new name.
