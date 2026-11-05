---
name: cinnamon-keyboard-applet-fix
description: Automatically repairs, restores, or configures the Cinnamon keyboard applet, input sources, and necessary systemd DBus integration.
triggers: ["cinnamon keyboard applet missing", "configure cinnamon keyboard layout", "fix cinnamon input sources", "cinnamon-keyboard-applet-fix"]
---

# Cinnamon Keyboard Applet & Layout Configuration

## Overview
This skill resolves issues where the Cinnamon keyboard applet is missing from the panel, fails to load, or requires specific keyboard layout configurations (e.g., US + Romanian). It automates the verification of `gsettings` keys, ensures the applet is registered in `enabled-applets`, and manages the underlying DBus service dependency often required for stable operation.

## Proven Procedure

1.  **Ensure the Applet is Enabled:**
    Use `gsettings` to verify and inject the keyboard applet into the Cinnamon panel layout:
    ```bash
    # Check current enabled applets
    gsettings get org.cinnamon enabled-applets

    # Add the keyboard applet to panel1, right side, at position 10 (adjust index as needed)
    # Ensure 'keyboard@cinnamon.org' exists in the list
    gsettings set org.cinnamon enabled-applets "['menu@cinnamon.org', 'keyboard@cinnamon.org:8']"
    ```

2.  **Configure Input Sources:**
    Set the keyboard layouts specifically for the session:
    ```bash
    # Enable visibility of sources
    gsettings set org.cinnamon.desktop.input-sources show-all-sources true

    # Set layout list (example: US and Romanian)
    gsettings set org.cinnamon.desktop.input-sources sources "[('xkb', 'us'), ('xkb', 'ro')]"
    ```

3.  **Restart Cinnamon:**
    Apply changes without logging out:
    ```bash
    cinnamon --replace & disown
    ```

4.  **Verify DBus Integration (If custom service is used):**
    If utilizing a custom user service (e.g., `electra-dbus.service`), ensure the `ExecStart` path in `~/.config/systemd/user/` points correctly to the current user home directory:
    ```bash
    # Edit the path if necessary
    sed -i "s|/home/makulu/|/home/$USER/|g" ~/.config/systemd/user/electra-dbus.service
    systemctl --user daemon-reload
    systemctl --user restart electra-dbus.service
    ```

## Pitfalls & Troubleshooting
*   **Path Mismatches:** Always ensure that scripts calling Python helpers (like `electra_dbus.py`) use the correct absolute path for the current user's home directory. Hardcoded paths like `/home/makulu` will fail on other user accounts.
*   **Applet Conflicts:** If the applet doesn't appear, check `looking-glass` (Alt+F2, type `lg`) to see if `keyboard@cinnamon.org` reports errors in the logs.
*   **Panel Index:** Adding `keyboard@cinnamon.org` to `enabled-applets` requires a correct index (e.g., `:8`). If the index is taken, the applet may not render. Check existing indices in `gsettings` output first.
