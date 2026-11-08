---
name: kde-electra-voice-mode-setup
description: Procedures for launching and operating the local offline Electra voice interaction mode, including audio prerequisites and automated conversation logging.
triggers: ["how do I use voice mode", "run electra in voice mode", "how to start speaking to electra"]
---

# Electra Offline Voice Mode Setup

## Overview
This skill outlines the necessary steps to initialize the Electra voice interaction suite (`app.py`). It ensures the user's environment is ready for speech-to-text (`faster-whisper`) and text-to-speech (`pyttsx3`) operations, and manages log archival.

## Proven Procedure
1.  **Hardware Verification**: Ensure that system audio input (microphone) and output (speakers) are active and configured correctly in the OS sound settings.
2.  **Launching the Application**:
    *   **Method A (Terminal)**:
        ```bash
        cd /home/elcis/workspace
        python3 app.py
        ```
    *   **Method B (Desktop Shortcut)**: Launch the pre-configured `.desktop` file located on the desktop: `Electra Offline`.
3.  **Operation**:
    *   Once launched, the application initializes the *Ilgvar* module automatically.
    *   The app enters a listening state immediately.
    *   Ensure silence or ambient noise reduction to improve `faster-whisper` transcription accuracy.

## Pitfalls & Troubleshooting
*   **Dependency Errors**: If the script fails, verify `requirements.txt` has been installed (`pip install -r requirements.txt`).
*   **Audio Access Denied**: If the microphone isn't detected, ensure no other application is holding exclusive lock on the audio device.
*   **Archiving**: If conversation logs are not appearing in `/home/elcis/Desktop/ELEKTRA_SARUNAS`, check that the script has sufficient write permissions to that directory.
