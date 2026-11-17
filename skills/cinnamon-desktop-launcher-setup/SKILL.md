---
name: cinnamon-desktop-launcher-setup
description: Automatically create and configure a .desktop launcher file on the Cinnamon desktop, ensuring it has execution permissions and correct formatting.
triggers: ["create desktop launcher", "make app executable on desktop", "add shortcut to cinnamon desktop", "install .desktop file"]
---

# Cinnamon Desktop Launcher Setup

## Overview
This skill automates the creation of a functional `.desktop` shortcut on the Cinnamon desktop environment. It handles the writing of the desktop entry file, setting the appropriate `+x` (executable) permissions, and ensuring it renders correctly as a launchable icon in the Cinnamon file manager (Nemo).

## Proven Procedure
1.  **Define the Desktop Entry Content**: Create a file with the `.desktop` extension. The standard format is:
    ```ini
    [Desktop Entry]
    Version=1.0
    Type=Application
    Name=App Name
    Exec=/path/to/executable_or_script
    Icon=/path/to/icon.png
    Terminal=false
    Categories=Utility;
    ```
2.  **Placement**: Place the file in the user's desktop directory: `~/Desktop/`.
3.  **Permissions**: Essential step—the `.desktop` file must be marked as executable by the system, or Cinnamon will refuse to launch it (and it may appear as a simple text file).
    ```bash
    chmod +x ~/Desktop/your_app.desktop
    ```
4.  **Verification**: Cinnamon usually triggers a prompt asking if the user trusts the application the first time it is launched.

## Pitfalls & Troubleshooting
*   **Permission Denied**: If the file does not have `chmod +x` applied, it will simply open in the default text editor (e.g., Xed or Nemo) instead of executing the app.
*   **Invalid Exec Path**: Ensure the `Exec` path in the `.desktop` file is an absolute path. Relative paths often fail depending on the shell environment.
*   **Nemo Handling**: Cinnamon (via Nemo) requires the file to be present in `~/Desktop`. If the file is placed elsewhere, it won't appear as a shortcut on the actual desktop UI.
