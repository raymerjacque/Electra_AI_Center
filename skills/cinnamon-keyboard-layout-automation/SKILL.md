---
name: cinnamon-keyboard-layout-automation
description: Automates the enforcement of keyboard layouts (e.g., forcing QWERTY) using systemd user services and Cinnamon gsettings.
triggers: ["force keyboard layout to qwerty", "fix keyboard layout on startup", "automate keyboard settings in cinnamon", "cinnamon keyboard config script"]
---

# Cinnamon Keyboard Layout Automation

## Overview
This skill provides a mechanism to persistently force a specific keyboard layout (like QWERTY) within the Cinnamon desktop environment. It uses a Python helper script combined with a systemd user service to ensure the setting is applied reliably upon session start, bypassing potential GUI resets or conflicting input source settings.

## Proven Procedure

### 1. Create the Keyboard Enforcement Script
Create a Python script (e.g., `~/.config/fix_keyboard_applet.py`) to handle the `gsettings` command.

```python
import subprocess
import os

def set_keyboard_layout():
    # Force the layout to US/QWERTY using gsettings
    subprocess.run(["gsettings", "set", "org.cinnamon.desktop.input-sources", "sources", "[('xkb', 'us')]"])

if __name__ == "__main__":
    set_keyboard_layout()
```

### 2. Create the Systemd User Service
Create a service file at `~/.config/systemd/user/electra-keyboard-fix.service` to run the script upon login:

```ini
[Unit]
Description=Fix Keyboard Layout to QWERTY
After=graphical-session.target

[Service]
Type=oneshot
ExecStart=/usr/bin/python3 /home/%u/.config/fix_keyboard_applet.py

[Install]
WantedBy=graphical-session.target
```

### 3. Enable the Service
Execute the following commands to activate the automation:

```bash
systemctl --user daemon-reload
systemctl --user enable electra-keyboard-fix.service
systemctl --user start electra-keyboard-fix.service
```

## Pitfalls & Troubleshooting
*   **Dependency on Graphical Session:** Always ensure the service is configured with `After=graphical-session.target` and `WantedBy=graphical-session.target`. If it starts too early, the `gsettings` command will fail because the D-Bus session is not yet active.
*   **Permissions:** Ensure the Python script is not required to be executable if called directly via `/usr/bin/python3`, but verify the path is absolute in the systemd service file.
*   **Overwrites:** This method overrides the GUI "Keyboard" settings in Cinnamon. If the user changes the layout in the GUI, this script may reset it back to QWERTY on the next login. Adjust the Python script if toggle-functionality is required.
