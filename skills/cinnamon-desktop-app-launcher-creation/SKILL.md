---
name: cinnamon-desktop-app-launcher-creation
description: Create custom .desktop application launchers for the user's desktop and applications menu on Cinnamon.
triggers: ["wo ist die app", "app launcher erstellen", "desktop datei erstellen", "heimdall desktop shortcut"]
---

# Cinnamon Custom Desktop App Launcher Creation

## Overview
When an application lacks a graphical menu entry or desktop launcher on MakuluLinux Cinnamon, you can manually create a freedesktop-compliant `.desktop` file in `~/.local/share/applications/` and copy it to the desktop (`~/Desktop/`) with executable permissions.

## Proven Procedure
1. Create the `.desktop` file in the user applications directory:
   ```bash
   cat << 'EOF' > ~/.local/share/applications/appname.desktop
   [Desktop Entry]
   Name=Application Name
   Comment=Description of application
   Exec=executable-command
   Icon=system-run
   Terminal=false
   Type=Application
   Categories=System;
   EOF
   ```
2. Copy to desktop and make executable:
   ```bash
   cp ~/.local/share/applications/appname.desktop ~/Desktop/ && chmod +x ~/Desktop/appname.desktop
   ```
3. Under Cinnamon, right-click the desktop launcher and select *"Trust Launch"* ("Als vertrauenswürdig starten") if prompted.

## Pitfalls & Troubleshooting
- **Untrusted Launcher:** Cinnamon requires desktop launchers to be marked as trusted before executing. Right-click and trust the file.
- **Incorrect Exec Path:** Ensure the `Exec=` path points to a valid binary accessible via PATH or provide the absolute path.
