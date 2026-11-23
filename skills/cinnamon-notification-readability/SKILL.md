---
name: cinnamon-notification-readability
description: Fixes unreadable white-on-white text in Cinnamon notifications using gsettings color schemes and positioning tweaks.
triggers: ["cinnamon notifications unreadable", "frost white theme notification text fix", "cinnamon notification white font off white background"]
---

# Cinnamon Notification Readability Fix

## Overview
This skill resolves readability issues in Cinnamon desktop notification pop-ups (such as with light/frost white themes where white text appears on an off-white background). It adjusts GTK color schemes and notification positioning via `gsettings`.

## Proven Procedure
Run the following commands in the shell to adjust notification colors and layout:

1. **Set contrast for selected colors in GTK apps/notifications:**
   ```bash
   gsettings set org.cinnamon.desktop.interface gtk-color-scheme 'selected_bg_color:#f0f0f0 selected_fg_color:#000000'
   ```

2. **Reposition notifications to the bottom of the screen (optional layout adjustment):**
   ```bash
   gsettings set org.cinnamon bottom-notifications true
   ```

3. **Disable fixed notification positioning:**
   ```bash
   gsettings set org.cinnamon notification-fixed-screen 0
   ```

## Pitfalls & Troubleshooting
- Some custom GTK themes ignore `gtk-color-scheme` overrides; if notifications remain unreadable, switching the Cinnamon desktop theme to a fully compatible dark or high-contrast variant may be required.
