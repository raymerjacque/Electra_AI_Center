---
name: cinnamon-browser-refresh-automation
description: Automates refreshing a browser (Chrome/Chromium) window using xdotool to maintain dashboard activity.
triggers: ["refresh chrome window", "automate browser reload", "keep dashboard alive", "xdotool browser refresh"]
---

# Cinnamon Browser Refresh Automation

## Overview
This skill provides a standardized "protocol" for maintaining active dashboard visibility by periodically refreshing a target browser window (defaulting to Google Chrome). This is useful for monitoring stations where pages might otherwise go idle or sleep.

## Proven Procedure
1.  **Install the automation tool:**
    ```bash
    sudo apt update && sudo apt install xdotool -y
    ```

2.  **Create the automation script (`~/refresh_browser.sh`):**
    ```bash
    #!/bin/bash
    # Set the browser window title to search for
    BROWSER_NAME="Google Chrome"
    
    # Find the Window ID (WID)
    WID=$(xdotool search --name "$BROWSER_NAME" | head -1)
    
    if [ -n "$WID" ]; then
        xdotool windowactivate $WID
        # Send F5 key to trigger a reload
        xdotool key F5
        echo "Protocol executed: $BROWSER_NAME refreshed."
    else
        echo "Error: $BROWSER_NAME window not found."
    fi
    ```

3.  **Set executable permissions:**
    ```bash
    chmod +x ~/refresh_browser.sh
    ```

4.  **Optional: Automate with cron:**
    To run this every 10 minutes, open crontab (`crontab -e`) and add:
    ```bash
    */10 * * * * DISPLAY=:0 ~/refresh_browser.sh
    ```

## Pitfalls & Troubleshooting
*   **Window Title:** `xdotool search --name` is case-sensitive and partial. If the browser title changes (e.g., "Google Chrome" to "Dashboard - Google Chrome"), ensure your script uses a partial match string or correct regex if necessary.
*   **Permissions:** If running via cron, you must include `DISPLAY=:0` (or your current display index) so that `xdotool` knows which X session to manipulate.
*   **Focus:** This command *activates* the window, which means it will force focus to the browser window. If you are actively typing elsewhere, this may interrupt you.
