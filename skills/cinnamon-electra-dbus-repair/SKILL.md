---
name: cinnamon-electra-dbus-repair
description: Fixes the electra-dbus.service which handles desktop integration, AT-SPI communication, and multi-agent system state.
triggers: ["electra-dbus.service failed", "fix electra dbus", "repair ai-center connection", "restart electra service"]
---

# Electra D-Bus Repair

## Overview
This skill resolves issues when the `electra-dbus.service` fails to start, which typically results in broken AT-SPI (Assistive Technology Service Provider Interface) connectivity. When this service is down, Electra cannot effectively interact with desktop elements, agents, or provide system-aware automation.

## Proven Procedure
To restore the D-Bus interface and re-establish connection between the AI agent and the system:

1.  **Check current status:**
    ```bash
    systemctl status electra-dbus.service
    ```

2.  **Reset and Restart:**
    If the status shows failed or inactive, perform a forced reset:
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl stop electra-dbus.service
    sudo systemctl reset-failed electra-dbus.service
    sudo systemctl start electra-dbus.service
    ```

3.  **Verify connection:**
    ```bash
    systemctl status electra-dbus.service
    # The status should return 'active (running)'
    ```

## Pitfalls & Troubleshooting
- **Missing Binary:** If `systemctl start` returns "Unit not found," ensure the `electra-core` package is fully installed via `apt`.
- **Permissions:** If the service starts but fails to interact with the desktop, ensure the user running the service has access to the current D-Bus session. You may need to run `export DISPLAY=:0` or `export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$(id -u)/bus` before starting the service if running manually.
