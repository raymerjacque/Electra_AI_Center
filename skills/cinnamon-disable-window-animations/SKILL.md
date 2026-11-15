---
name: cinnamon-disable-window-animations
description: Disable window maximization, minimization, and map animations (gewiebel) in Cinnamon desktop environment.
triggers: ["gewiebel", "venster maximaliseren animatie", "disable window animations cinnamon", "stop window wiggle max"]
---

# Disable Window Animations in Cinnamon

## Overview
This skill disables the desktop animations (such as the scaling/wiggle effect when maximizing, minimizing, or mapping windows) in the Cinnamon desktop environment using `gsettings`.

## Proven Procedure
Run the following terminal commands to turn off the specific window effects:

```bash
gsettings set org.cinnamon.desktop.interface desktop-effects-change-size false
gsettings set org.cinnamon.desktop.interface desktop-effects-map false
gsettings set org.cinnamon.desktop.interface desktop-effects-minimize false
```

## Pitfalls & Troubleshooting
- Ensure you are running a Cinnamon session; these schemas do not apply to other window managers like KWin or XFWM4 without alternative commands.
