---
name: kde-kwin-window-rules
description: Configure custom window rules in KDE Plasma KWin to force specific window placement, virtual desktops, and borderless states.
triggers: ["configure window rules in kde", "kwin window rules", "open app on virtual desktop automaticallykde", "borderless window rule kwin"]
---

# KDE KWin Window Rules Configuration

## Overview
Use this skill when configuring custom window management rules in KDE Plasma via KWin, such as forcing specific applications to open on particular virtual desktops or without window borders/titlebars.

## Proven Procedure
1. Via GUI: Open **System Settings** -> **Window Management** -> **Window Rules**, then click **Add New...**.
2. Configure window matching (e.g., *Window class* -> *exact match* -> `org.kde.konsole`).
3. Add desired properties:
   - **Desktop**: Set to *Apply initially* -> Select target desktop (e.g., Desktop 2).
   - **No titlebar and frame**: Set to *Force* -> *Yes*.
4. Via Config File (`~/.config/kwinrulesrc`): Manually define rule blocks.
5. Apply changes dynamically without restarting KWin session using D-Bus:
   ```bash
   qdbus org.kde.KWin /KWin reconfigure
   ```

## Pitfalls & Troubleshooting
- Ensure the window class is exact (use `xprop` or `kwin_wayland --help` or Window Info utility to verify window classes).
- If rules do not apply immediately after editing configuration files directly, ensure `qdbus org.kde.KWin /KWin reconfigure` is executed to reload KWin rules.
