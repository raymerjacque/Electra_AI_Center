---
name: kde-desktop-launcher-troubleshooting
description: Troubleshooting guide for KDE Plasma .desktop files that fail to launch or immediately close upon double-click.
triggers: ["desktop file not launching", "kde app double click not working", "trust and launch kde", "execute .desktop file kde"]
---

# KDE Desktop Launcher Troubleshooting

## Overview
This skill addresses issues where `.desktop` files on the KDE Plasma desktop fail to execute, close immediately, or require "Trust and Launch" permissions. It helps users diagnose whether the issue is a permission/trust setting in Dolphin/Plasma or an underlying script error.

## Proven Procedure
If a `.desktop` launcher is not opening, follow these steps to verify and fix the configuration:

1.  **Verify Trust Status:**
    KDE Plasma blocks untrusted `.desktop` files for security. Right-click the `.desktop` file and ensure there is an option that says "Trust and Launch" or "Mark as Executable." If prompted, confirm you trust the file.

2.  **Debug via Terminal:**
    Sometimes the GUI silent-fails. Open a terminal to see the actual error output:
    ```bash
    # Navigate to the desktop (or wherever the file is)
    cd ~/Desktop/

    # Run the .desktop file directly to see terminal output
    # (Replace 'filename.desktop' with your actual file name)
    ./filename.desktop
    ```
    *If the output shows a Python or script error, the issue is with the application code, not the launcher.*

3.  **Check Permissions:**
    Ensure the file is marked as executable:
    ```bash
    chmod +x ~/Desktop/filename.desktop
    ```

## Pitfalls & Troubleshooting
*   **Shebang Missing:** If the `.desktop` file points to a script (e.g., `app.py`), ensure the script has a proper shebang line at the very top (e.g., `#!/usr/bin/env python3`).
*   **Pathing Issues:** If the script inside the `.desktop` file uses relative paths, it might fail when launched from a different context. Use absolute paths in the `Exec=` line of the `.desktop` file (e.g., `Exec=/home/user/workspace/app.py`).
*   **Environment Variables:** If the application requires a virtual environment, the `Exec=` line should point to the virtual environment's python binary: `Exec=/home/user/workspace/venv/bin/python /home/user/workspace/app.py`.
