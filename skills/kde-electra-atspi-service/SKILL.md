---
name: kde-electra-atspi-service
description: Create and manage the Electra AT-SPI context daemon user service for KDE Plasma accessibility monitoring.
triggers: ["electra-atspi", "atspi-service", "accessibility daemon", "systemd user service atspi"]
---

# KDE Electra AT-SPI Service Setup

## Overview
This skill covers the setup and deployment of the Electra AT-SPI (Assistive Technology Service Provider Interface) context daemon and its corresponding systemd user service in KDE Plasma.

## Proven Procedure
1. Create the AT-SPI daemon script (e.g., `electra_atspi_daemon_v2.py`) in the appropriate local tools directory (`/home/user/.local/share/MakuluSetup/tools/`).
2. Create a systemd user service configuration file at `/home/user/.config/systemd/user/electra-atspi-v2.service`:
   ```ini
   [Unit]
   Description=Electra AT-SPI Context Daemon v2
   After=graphical-session.target

   [Service]
   ExecStart=/usr/bin/python3 /home/user/.local/share/MakuluSetup/tools/electra_atspi_daemon_v2.py
   Restart=always
   RestartSec=3

   [Install]
   WantedBy=default.target
   ```
3. Reload systemd user daemon and enable/start the service:
   ```bash
   systemctl --user daemon-reload
   systemctl --user enable --now electra-atspi-v2.service
   ```

## Pitfalls & Troubleshooting
- Ensure `graphical-session.target` is set in the `After=` directive so the desktop accessibility bus is fully initialized.
- Always use `systemctl --user` flags since this runs in user space rather than system root space.
