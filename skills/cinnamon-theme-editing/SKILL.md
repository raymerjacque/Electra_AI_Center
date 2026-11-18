---
name: cinnamon-theme-editing
description: Switches the Cinnamon desktop theme and GTK interface between light and dark modes using gsettings.
triggers: ["change to light theme", "switch to dark theme", "change cinnamon theme", "set light mode"]
---

# Cinnamon Theme Editing

## Overview
This skill handles switching system themes (light/dark) on the Cinnamon desktop environment using `gsettings` to configure both the GTK theme and the Cinnamon shell theme.

## Proven Procedure
To change the desktop to a light theme:
1. Update the GTK theme interface:
   ```bash
   gsettings set org.cinnamon.desktop.interface gtk-theme 'Mint-Y' # or relevant light theme
   ```
2. Update the Cinnamon shell theme:
   ```bash
   gsettings set org.cinnamon.theme name 'Mint-Y'
   ```
3. If window borders/decorations need separate adjustment:
   ```bash
   gsettings set org.cinnamon.desktop.interface wm-theme 'Mint-Y'
   ```

## Pitfalls & Troubleshooting
- Ensure the theme name specified in `gsettings` actually exists in `/usr/share/themes/` or `~/.themes/`.
- Cinnamon might require a shell restart (`Alt+F2`, then type `r`, then press Enter) for theme changes to fully propagate across all applets and panels if `gsettings` alone doesn't trigger an immediate redraw.
