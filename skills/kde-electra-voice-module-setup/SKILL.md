---
name: kde-electra-voice-module-setup
description: Handles the installation of system audio dependencies and Python libraries required to enable the Electra voice/transcription module.
triggers: ["setup electra voice module", "enable microphone in electra", "install faster-whisper dependencies", "electra offline voice configuration"]
---

# Electra Voice Module Setup

## Overview
This skill automates the configuration of the audio subsystem and necessary Python environment dependencies for the "Electra" assistant voice functionality. Use this when setting up a new voice-enabled instance of Electra or when troubleshooting voice recognition failures.

## Proven Procedure

1. **Install System Audio Dependencies**
   Ensure the necessary system libraries for audio recording and processing are installed:
   ```bash
   sudo apt update && sudo apt install -y portaudio19-dev ffmpeg
   ```

2. **Setup Python Environment**
   Navigate to the application workspace and ensure the required Python packages are installed within the virtual environment.
   ```bash
   cd /home/elcis/workspace
   # Activate your virtual environment if not already active
   source venv/bin/activate
   # Install dependencies
   pip install sounddevice faster-whisper keyboard requests pynput
   ```

3. **Verify Execution**
   Launch the application using the designated launcher or directly via terminal to verify the microphone listener is active:
   ```bash
   python3 app.py
   ```

## Pitfalls & Troubleshooting
*   **Permission Denied:** If the script fails to access the microphone, ensure the user account is part of the `audio` group (check with `groups` command).
*   **Missing ffmpeg:** `faster-whisper` relies heavily on `ffmpeg`. If transcription fails, ensure `ffmpeg` is properly installed via apt.
*   **Virtual Environment:** Always ensure the virtual environment (`venv`) is activated before running the script; otherwise, global package conflicts may occur.
