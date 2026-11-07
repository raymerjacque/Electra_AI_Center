---
name: kde-xrandr-custom-resolution
description: Add a custom display resolution using xrandr and cvt for unlisted or older VGA monitors lacking proper EDID data in KDE Plasma.
triggers: ["add custom resolution", "xrandr custom mode", "vga monitor resolution fix", "cvt modeline xrandr"]
---

# Add Custom Display Resolution via Xrandr

## Overview
Use this skill when an external monitor (especially older VGA displays lacking EDID data) fails to display its native or maximum supported resolution automatically. This provides a repeatable procedure to generate and apply a custom modeline using `cvt` and `xrandr`.

## Proven Procedure
1. Identify the exact connected display output name:
   ```bash
   xrandr
   ```
   *(Look for connected outputs like `VGA-1`, `HDMI-1`, etc.)*

2. Generate the modeline for the desired resolution and refresh rate (e.g., 1336x768 at 60Hz):
   ```bash
   cvt 1336 768 60
   ```

3. Copy the generated `Modeline` parameters (everything after `Modeline`) and add the new mode to Xrandr:
   ```bash
   xrandr --newmode "1336x768_60.00" <generated_parameters>
   ```

4. Add the new mode to the specific display output:
   ```bash
   xrandr --addmode <OUTPUT_NAME> "1336x768_60.00"
   ```

5. Apply the resolution:
   ```bash
   xrandr --output <OUTPUT_NAME> --mode "1336x768_60.00"
   ```

## Pitfalls & Troubleshooting
- **VGA Limitations:** VGA analog cables frequently fail to transmit EDID data, requiring manual mode generation via `cvt`.
- **Persistence:** Changes made via `xrandr` are temporary and reset upon reboot. To make them permanent, add the commands to an autostart script or Xorg configuration file (`/etc/X11/xorg.conf.d/`).
