---
name: cinnamon-power-menu-brightness-fix
description: Fixes dim power management menu in Cinnamon start menu by adjusting gsettings for minimum-display-brightness and idle-dim-ac
triggers: ["cinnamon power menu dim", "cinnamon start menu brightness too dim", "cinnamon power management menu brightness", "cinnamon screen dimming on AC"]
---

# Cinnamon Power Management Menu Brightness Fix

## Overview
This skill resolves the issue where the power management menu in the Cinnamon start menu appears too dim. It adjusts two gsettings: `minimum-display-brightness` to lower the minimum brightness threshold, and `idle-dim-ac` to prevent screen dimming when on AC power.

## Proven Procedure

### Step 1: Check current gsettings values
```bash
gsettings get org.cinnamon.settings-daemon.plugins.power minimum-display-brightness
gsettings get org.cinnamon.settings-daemon.plugins.power idle-dim-ac
```

### Step 2: Set minimum-display-brightness to 0 (maximum brightness)
```bash
gsettings set org.cinnamon.settings-daemon.plugins.power minimum-display-brightness 0
```

### Step 3: Disable idle dimming on AC power
```bash
gsettings set org.cinnamon.settings-daemon.plugins.power idle-dim-ac false
```

### Step 4: Verify changes
```bash
gsettings get org.cinnamon.settings-daemon.plugins.power minimum-display-brightness
gsettings get org.cinnamon.settings-daemon.plugins.power idle-dim-ac
```

Expected output: `uint32 0` for minimum-display-brightness and `false` for idle-dim-ac.

## Pitfalls & Troubleshooting

- **Changes not taking effect**: Restart Cinnamon (`Alt+F2`, type `r`, press Enter) or log out and back in.
- **gsettings command not found**: Ensure `gsettings` is installed (part of `glib-2.0` package).
- **Permission errors**: These commands run as the user, not root — no sudo needed.
- **Value reverts on reboot**: Some Cinnamon versions may reset settings; add the gsettings commands to startup applications if needed.
