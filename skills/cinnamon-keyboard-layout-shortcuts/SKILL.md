---
name: cinnamon-keyboard-layout-shortcuts
description: Change keyboard layout switching hotkeys (input sources) in Cinnamon using gsettings.
triggers: ["change language hotkey", "keyboard layout shortcut", "switch input source", "cinnamon language switch key"]
---

# Cinnamon Keyboard Layout Shortcuts

## Overview
This skill outlines how to configure keyboard layout switching shortcuts (input sources) programmatically in the Cinnamon desktop environment using `gsettings`.

## Proven Procedure
To change the hotkey for switching between input sources/languages to `Ctrl+Shift`, run the following commands:

```bash
gsettings set org.cinnamon.desktop.keybindings.wm switch-input-source "['<Ctrl><Shift>']"
gsettings set org.cinnamon.desktop.keybindings.wm switch-input-source-backward "['<Shift><Ctrl>']"
```

To verify the current settings:
```bash
gsettings get org.cinnamon.desktop.keybindings.wm switch-input-source
```

## Pitfalls & Troubleshooting
- Ensure proper key notation is used (e.g., `['<Ctrl><Shift>']` wrapped in a JSON array format).
- If the shortcut conflicts with other window manager shortcuts, use Cinnamon's Keyboard Settings GUI or adjust conflicting keybindings.
