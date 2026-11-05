---
name: systemd-user-service-path-fix
description: Automates the process of identifying and correcting hardcoded, incorrect user paths within systemd user service unit files.
triggers: ["systemd user service path error", "fix systemd user service path", "update systemd service directory", "correcting absolute paths in systemd"]
---

# Systemd User Service Path Fix

## Overview
This skill addresses errors where systemd user services fail due to hardcoded, incorrect home directory paths (e.g., `/home/makulu/` vs `/home/dacic/`). It provides a methodology to audit and patch these configuration files to ensure services run correctly in the user's specific environment.

## Proven Procedure
To resolve path-related failures in user services:

1.  **Identify the unit file:** Locate the service file causing the error.
    ```bash
    systemctl --user status <service-name>
    # Check the path shown in the output
    cat ~/.config/systemd/user/<service-name>.service
    ```

2.  **Verify the current user path:**
    ```bash
    echo $HOME
    ```

3.  **Update the unit file:** Use `sed` to replace the incorrect path with the actual user path.
    ```bash
    # Example: Replacing /home/makulu/ with /home/dacic/
    sed -i 's|/home/makulu/|/home/dacic/|g' ~/.config/systemd/user/<service-name>.service
    ```

4.  **Reload and Restart:** Apply the changes and restart the service.
    ```bash
    systemctl --user daemon-reload
    systemctl --user restart <service-name>
    systemctl --user status <service-name>
    ```

## Pitfalls & Troubleshooting
*   **Variable Expansion:** Systemd service files do not natively support `$HOME` expansion in all directives (like `ExecStart`). Always prefer full, verified absolute paths.
*   **Permissions:** Ensure the service file remains owned by the user (`chown $USER:$USER ~/.config/systemd/user/<service-name>.service`).
*   **Symlinks:** If you use a symlink for the service, ensure the path resolution is correct; often it is safer to edit the source file directly rather than the symlink.
