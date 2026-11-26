---
name: cinnamon-snap-app-handler-fix
description: Fixes broken or missing mime-type associations for Snap-installed applications on Cinnamon/Nemo by pointing XDG handlers to the correct Snap desktop entry files.
triggers: ["fix snap application not opening links", "snap app association repair", "xdg-mime snap handler", "slack snap integration fix"]
---

# Cinnamon Snap Application Handler Fix

## Overview
Snap-installed applications often fail to register as default handlers for URL schemes (e.g., `slack://`) because the system's XDG configuration looks in standard directories (`/usr/share/applications`), but Snap packages keep their desktop files in `/var/lib/snapd/desktop/applications/`. This skill automates the process of locating the correct Snap desktop file and correctly registering it as the handler.

## Proven Procedure
To fix a broken or missing URL handler for a Snap application, perform the following steps:

1.  **Locate the Snap desktop file:**
    Snap desktop files are typically located in `/var/lib/snapd/desktop/applications/`. Verify the exact filename for the target app:
    ```bash
    ls /var/lib/snapd/desktop/applications/ | grep <app_name>
    ```

2.  **Register the handler:**
    Use `xdg-mime` to associate the specific scheme (e.g., `x-scheme-handler/slack`) with the full path of the Snap desktop file.

    ```bash
    # Example for Slack
    xdg-mime default /var/lib/snapd/desktop/applications/slack_slack.desktop x-scheme-handler/slack
    ```

3.  **Update the mime database:**
    Refresh the database to ensure the changes take effect immediately:
    ```bash
    update-desktop-database ~/.local/share/applications
    ```

## Pitfalls & Troubleshooting
*   **Permissions:** You do not typically need `sudo` for `xdg-mime` unless modifying system-wide defaults, but if the association persists in failing, verify that the `.desktop` file actually exists at the targeted path.
*   **Path Variations:** Snap desktop filenames often include the vendor or specific build identifier (e.g., `slack_slack.desktop`). Always use `ls` to confirm the exact filename before running the `xdg-mime` command.
*   **Multiple Desktop Files:** If multiple similar files exist (e.g., a snap and a deb version), ensure you are referencing the file in `/var/lib/snapd/desktop/applications/` to avoid pointing to a broken or non-existent standard install path.
