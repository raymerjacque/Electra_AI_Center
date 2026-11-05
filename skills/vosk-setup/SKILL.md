---
name: vosk-setup
description: Installs and sets up the lightweight Vosk speech recognition engine for real-time voice commands and transcription.
triggers: ["install vosk", "setup vosk speech recognition", "offline voice recognition configuration"]
---

# Vosk Offline Speech Recognition Setup

## Overview
This skill provides the procedure to install `vosk` and configure the necessary language model required for offline, low-latency speech recognition. This is ideal for voice-controlled automation (like a "Jarvis"-style assistant) where speed is prioritized over the heavy transcription capabilities of models like Whisper.

## Proven Procedure

1.  **Install the Python package:**
    Execute the following command to install the necessary library:
    ```bash
    pip3 install vosk
    ```

2.  **Prepare the Model Directory:**
    Vosk requires a pre-trained language model to function. Create a dedicated directory to store your models:
    ```bash
    mkdir -p ~/vosk-models
    cd ~/vosk-models
    ```

3.  **Download the Model:**
    Download a standard small English model (optimized for real-time responsiveness):
    ```bash
    wget https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
    unzip vosk-model-small-en-us-0.15.zip
    ```
    *Note: If you need a different language or a larger, more accurate model, check the [Vosk Models page](https://alphacephei.com/vosk/models).*

## Pitfalls & Troubleshooting
- **Missing Dependencies:** Vosk often relies on `ffmpeg` or `soundfile` for audio input. If you encounter errors when running your script, ensure your system audio libraries are updated:
  `sudo apt update && sudo apt install ffmpeg libasound2-dev`
- **Model Pathing:** When writing your Python script, ensure the `Model()` constructor points to the correct directory (e.g., `model = Model("/home/username/vosk-models/vosk-model-small-en-us-0.15")`). Relative paths can fail if the script is launched from a different working directory.
- **Microphone Access:** Ensure your user is in the `audio` group if you experience permission issues accessing the microphone: `sudo usermod -a -G audio $USER`.
