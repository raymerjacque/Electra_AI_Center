---
name: cinnamon-ai-os-voice-notifications
description: Adds audible feedback to system notifications by integrating text-to-speech engines like espeak-ng into background processes or notification hooks.
triggers: ["voice notifications", "audible alerts", "espeak-ng integration", "text-to-speech notifications", "system audio alerts"]
---

# AI Voice Notifications Integration

## Overview
This skill provides the workflow for adding audible voice output to existing background Python scripts or system event handlers. It utilizes `espeak-ng` to vocalize notification strings, enhancing system accessibility and feedback loops.

## Proven Procedure
1.  **Install dependencies:** Ensure the speech engine is available on the system.
    ```bash
    sudo apt update
    sudo apt install espeak-ng -y
    ```

2.  **Implementation Pattern:** Integrate the following pattern into your existing notification function:
    ```python
    import subprocess

    def send_desktop_notification(title, message):
        # 1. Standard visual notification code here...
        
        # 2. Add Voice Notification
        # Ensure the text is sanitized for shell execution if necessary
        clean_msg = message.replace('"', '\\"')
        subprocess.run(["espeak-ng", f"{title}: {clean_msg}"], check=True)
    ```

3.  **Verification:** Test the execution manually from the terminal to ensure audio output is configured correctly in the OS:
    ```bash
    espeak-ng "System notification test, voice operational."
    ```

## Pitfalls & Troubleshooting
*   **Audio Muted:** If no sound is heard, check the system volume levels (e.g., `alsamixer`) to ensure the output channel is not muted or set to zero.
*   **Missing Dependencies:** If `espeak-ng` is not found, verify the package installation in the environment path.
*   **Blocking Calls:** `subprocess.run` is synchronous. If the notification happens in the main thread of a UI application, it may cause a stutter; consider using `subprocess.Popen` or `threading` if asynchronous speech is required.
