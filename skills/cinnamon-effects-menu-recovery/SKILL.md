---
name: cinnamon-effects-menu-recovery
description: Recovers missing desktop effects menus in Cinnamon when core effects have been globally disabled via gsettings or GUI toggles.
triggers: ["effects disappeared from menu", "cinnamon effects menu missing", "enable cinnamon effects gsettings", "effects disabled menu gone cinnamon"]
---

# Cinnamon Effects Menu Recovery

## Overview
When desktop effects are globally disabled in Cinnamon, the system often hides or disables the effects settings menu option entirely. This skill provides the `gsettings` command to restore the effect preference toggle and bring the menu back.

## Proven Procedure
To re-enable desktop effects and restore the settings menu options in Cinnamon:

```bash
gsettings set org.cinnamon.desktop.wm.preferences effect-enabled true
```

If you need to verify the current state of effects:
```bash
gsettings get org.cinnamon.desktop.wm.preferences effect-enabled
```

## Pitfalls & Troubleshooting
- **Menu still missing after running the command:** Restart Cinnamon to refresh the desktop environment's UI processes. You can restart Cinnamon by pressing `Alt + F2`, typing `r`, and pressing `Enter`, or by running `nohup cinnamon --replace &` from a terminal.
