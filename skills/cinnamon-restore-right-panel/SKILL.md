---
name: cinnamon-restore-right-panel
description: Restores or recreates a missing right panel on the Cinnamon desktop environment.
triggers: ["restore right panel", "missing right panel", "reset cinnamon panels", "add panel right edge"]
---

# Cinnamon Restore Right Panel

## Overview
This skill guides users on how to restore, add, or reset a missing right-side panel in the Cinnamon desktop environment.

## Proven Procedure
1. Open **System Settings** from the application menu or by right-clicking an existing panel.
2. Navigate to the **Panel** module.
3. Click **Add a new panel** and position/configure it on the right edge of the screen, or reset panel layouts to factory defaults if corrupted.

## Pitfalls & Troubleshooting
- If panels are completely broken or unresponsive, they can be reset via terminal using Cinnamon's settings schema reset commands (e.g., `dconf reset -f /org/cinnamon/`).
