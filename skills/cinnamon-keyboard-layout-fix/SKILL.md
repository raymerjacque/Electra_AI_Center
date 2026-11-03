---
name: cinnamon-keyboard-layout-fix
description: Fixes incorrect or swapped keyboard layouts (like Y and Z swapped to English QWERTY) on Cinnamon / MakuluLinux using setxkbmap or localectl.
triggers: ["tastatur layout fehlerhaft", "tasten vertauscht", "y und z vertauscht", "keyboard layout german", "setxkbmap de"]
---

# Cinnamon Keyboard Layout Fix

## Overview
This skill solves the issue of an incorrect or swapped keyboard layout (typically switching from German QWERTZ to English QWERTY, where `Y` and `Z` are swapped) in a Cinnamon environment on MakuluLinux.

## Proven Procedure
Run the following commands in the terminal to switch back to the German layout:

1. Temporary fix (immediate effect):
```bash
setxkbmap de
```

2. Permanent system-wide fix:
```bash
localectl set-x11-keymap de
```

## Pitfalls & Troubleshooting
- If `setxkbmap` reverts after a reboot, ensure `localectl` is used to persist the setting.
- Check current layout settings using `setxkbmap -query` if unexpected layouts persist.
