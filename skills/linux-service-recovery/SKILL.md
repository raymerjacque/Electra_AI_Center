---
name: linux-service-recovery
description: Procedures and diagnostic commands to detect and recover failed Linux systemd services.
triggers: ["systemd service failed", "service recovery", "systemctl status failed", "restart failed service"]
---

# Linux Service Recovery Skill

## Overview
Detects, diagnoses, and safely recovers failed systemd units and background services on Linux systems.

## Proven Procedure
1. Identify failed services:
   ```bash
   systemctl --failed
   ```
2. Inspect the failure logs for the specific unit:
   ```bash
   journalctl -u <unit_name> -n 50 --no-pager
   ```
3. Reset failure state and restart:
   ```bash
   sudo systemctl reset-failed <unit_name>
   sudo systemctl restart <unit_name>
   systemctl status <unit_name> --no-pager
   ```

## Pitfalls & Troubleshooting
- If service is masked: `sudo systemctl unmask <unit_name>` before restarting.
- If PID file remains after crash, check `/run/<service>.pid` and clear stale lock.
