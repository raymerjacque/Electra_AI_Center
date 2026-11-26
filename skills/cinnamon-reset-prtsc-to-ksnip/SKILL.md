---
name: cinnamon-reset-prtsc-to-ksnip
description: Resets the Print Screen (PrtSc) key to launch ksnip instead of the default Cinnamon screenshot tool. Useful after system resets, new installs, or when ksnip takes over the shortcut but gsettings need reconfiguration.
triggers: ["print screen launches default tool instead of ksnip", "ksnip shortcut not working after system update", "resetting cinnamon media-keys to ksnip"]
---

# Reset Print Screen (PrtSc) to ksnip in Cinnamon

## Overview
In Cinnamon desktops, the Print Screen (PrtSc) key is typically bound to the default screenshot utility. When ksnip is installed and configured as the preferred screenshot tool, the global shortcut may need to be reset via gsettings to ensure PrtSc launches ksnip instead of the built-in Cinnamon capturer.

## Proven Procedure
Run the following command to set the Print Screen key to launch ksnip:

```bash
gsettings set org.cinnamon.desktop.keybindings.media-keys screenshot "['ksnip']"
```

Verify the change took effect:

```bash
gsettings get org.cinnamon.desktop.keybindings.media-keys screenshot
```

Expected output: `['ksnip']`

If the shortcut does not respond, ensure ksnip is running and its own internal shortcut settings are not conflicting (ksnip may have its own global shortcut override).

## Pitfalls & Troubleshooting
- **ksnip not launching**: Check that ksnip is installed and currently running. ksnip may require a restart or re-registration of its global shortcut after system boot.
- **Conflicting shortcuts**: If ksnip has its own shortcut configured in its UI, it may override the gsettings binding. Use ksnip's preferences to disable its internal shortcut if you want gsettings to take full control.
- **Multiple DE environments**: This skill is specific to Cinnamon. For KDE Plasma, use `kde-` prefix; for XFCE, use `xfce-`. This task assumes the active desktop is Cinnamon (prefix: `cinnamon`).
