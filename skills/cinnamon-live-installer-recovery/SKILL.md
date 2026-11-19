---
name: cinnamon-live-installer-recovery
description: Procedures for debugging and restarting the MakuluLinux live installer when it hangs or fails to initialize due to desktop session scope errors.
triggers: ["live installer broken", "fix makulu installer", "installer scope error", "cinnamon installer fail"]
---

# Cinnamon Live Installer Recovery

## Overview
This skill provides a standardized troubleshooting workflow for when the MakuluLinux live installer (often utilized within the Cinnamon desktop environment) fails to launch or becomes unresponsive. It specifically addresses issues where the systemd session scope for the installer gets stuck in a failed state.

## Proven Procedure
If the Live Installer fails to launch, follow these steps in a terminal to identify the blocking process and reset the environment:

1. **Identify the failure cause:**
   Check the systemd logs for the specific installer scope error:
   ```bash
   journalctl -u app-cinnamon-env-*.scope -n 50
   ```
   *Note: Replace the wildcard if you know the exact ID, but the wildcard usually captures the specific session failure.*

2. **Clear systemd failure state:**
   Often, the service manager prevents the installer from restarting because it believes the previous instance is still in a "failed" state. Reset this:
   ```bash
   sudo systemctl reset-failed
   ```

3. **Verify and Relaunch:**
   After resetting the failed state, attempt to launch the installer binary directly from the terminal to bypass GUI shell hang-ups:
   ```bash
   sudo makulu-live-installer
   ```
   *(Or the specific binary path utilized by your version of Makulu).*

## Pitfalls & Troubleshooting
* **Permission Denied:** The live installer requires elevated privileges. Ensure you are using `sudo` when manually invoking the binary.
* **Ghost Processes:** If the command above fails with "already running," use `ps aux | grep installer` to find the rogue PID and terminate it with `sudo kill -9 <PID>`.
* **Cinnamon Environment:** If the installer opens but shows a black window, it may be a compositor issue. Attempt to restart the window manager first using `nemo -q` (if the file manager is causing context locks) or `cinnamon --replace`.
