---
name: kde-electra-dbus-service-fix
description: Fixes D-Bus Python service method signature TypeError issues in MakuluLinux/Electra tools by updating method arguments and restarting the systemd user service.
triggers: ["electra_dbus.py", "TypeError: ping() takes", "dbus service typeerror", "makulusetup tools dbus"]
---

# Electra D-Bus Service TypeError Fix

## Overview
This skill resolves Python D-Bus service failures caused by mismatched method signatures (such as unexpected positional arguments like `self` or missing `*args`/`**kwargs`) in `electra_dbus.py` under MakuluLinux user tools.

## Proven Procedure
1. Inspect the service script:
   ```bash
   cat /home/elcis/.local/share/makulusetup/tools/electra_dbus.py
   ```
2. Update the offending method (e.g., `ping`) to accept flexible arguments (`*args`, `**kwargs`) to prevent parameter count mismatches:
   ```python
   @dbus.service.method(dbus_interface='com.makulu.electra', in_signature='', out_signature='s')
   def ping(self, *args, **kwargs):
       return "pong"
   ```
3. Restart the D-Bus user service via systemctl:
   ```bash
   systemctl --user restart electra-dbus.service
   ```
4. Verify service status and test the method call:
   ```bash
   systemctl --user status electra-dbus.service
   dbus-send --session --dest=com.makulu.electra --type=method_call /com/makulu/electra com.makulu.electra.ping
   ```

## Pitfalls & Troubleshooting
- Ensure `dbus-python` decorators (`@dbus.service.method`) align with the expected DBus signature.
- Always restart the correct user-level systemd service (`--user`) rather than root daemon services.
