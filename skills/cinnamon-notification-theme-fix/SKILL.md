---
name: cinnamon-notification-theme-fix
description: Fixes unreadable text in Cinnamon notifications by adjusting GTK color schemes and notification positioning via gsettings.
triggers: ["cinnamon notification white text", "fix unreadable notifications cinnamon", "cinnamon notification theme contrast"]
---

# Cinnamon Notification Theme Fix

## Overview
This skill resolves readability issues in Cinnamon notification pop-ups (such as white text on an off-white background) by configuring GTK color schemes and adjusting notification placement via `gsettings`.

## Proven Procedure
Run the following commands in the terminal to adjust the Cinnamon notification colors and layout:

1. Set a high-contrast GTK color scheme for Cinnamon notifications to ensure dark text on light backgrounds:
   ```bash
   gsettings set org.cinnamon.theme name "YourThemeName"
   gsettings set org.cinnamon.desktop.interface gtk-color-scheme 'selected_bg_color:#f0f0f0;selected_fg_color:#000000;text_color:#000000;base_color:#ffffff'
   ```
   *(Adjust color hex codes to match your specific theme's contrast requirements).*

2. Move notifications to the bottom or adjust their screen behavior if overlapping causes readability issues:
   ```bash
   gsettings set org.cinnamon bottom-notifications true
   gsettings set org.cinnamon notification-fixed-screen 0
   ```

## Pitfalls & Troubleshooting
- **Theme Overrides:** Some heavy Cinnamon themes override `gsettings` colors directly in their `gnome-shell.css` or `cinnamon.css` stylesheets. If `gsettings` does not apply, edit the theme's CSS file directly under `~/.themes/` or `/usr/share/themes/`.
- **Resetting Defaults:** To revert notification color changes back to default:
  ```bash
  gsettings reset org.cinnamon.desktop.interface gtk-color-scheme
  ```
