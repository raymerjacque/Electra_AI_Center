---
name: cinnamon-ksnip-screenshot-shortcut
description: Reassigns the Print Screen (prtsc) key in Cinnamon to launch ksnip for custom screen capturing.
triggers: ["reset prtsc screen capture to ksnip", "set print screen to ksnip cinnamon", "cinnamon custom screenshot shortcut ksnip"]
---

# Cinnamon Ksnip Screenshot Shortcut Configuration

## Overview
This skill configures the Cinnamon desktop environment to intercept the Print Screen (`prtsc`) key and map it directly to launch the `ksnip` screenshot tool via `gsettings`.

## Proven Procedure
1. Check or set the media-keys screenshot binding in Cinnamon:
   ```bash
   gsettings set org.cinnamon.desktop.keybindings.media-keys screenshot "['ksnip']"
   ```
2. Verify the configuration was applied successfully:
   ```bash
   gsettings get org.cinnamon.desktop.keybindings.media-keys screenshot
   ```
   Expected output: `['ksnip']`

## Pitfalls & Troubleshooting
- Ensure `ksnip` is installed in your `$PATH` before assigning it to media keys (`which ksnip`).
- If Cinnamon ignores the custom command, verify that custom keybindings aren't overridden by another window manager shortcut or standalone screenshot daemon (like `gnome-screenshot` or `xfce4-screenshooter`).
