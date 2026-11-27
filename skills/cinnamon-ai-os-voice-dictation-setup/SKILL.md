---
name: cinnamon-ai-os-voice-dictation-setup
description: Configuration and troubleshooting for AI-based voice dictation systems, including model preloading and microphone diagnostic tools.
triggers: ["voice dictation setup", "configure whisper models", "microphone testing script", "test-mic.sh", "voice recognition troubleshooting"]
---

# AI OS Voice Dictation Setup

## Overview
This skill manages the installation, configuration, and verification of AI-based voice dictation subsystems (e.g., Whisper). It provides standardized scripts for hardware audio probing, model caching, and microphone diagnostic testing to ensure the voice pipeline is functional.

## Proven Procedure

### 1. Microphone Diagnostics
To verify hardware input, use the diagnostic scripts created during setup:

```bash
# Bash implementation (for quick shell testing)
bash /usr/local/bin/test-mic.sh

# Python implementation (for programmatic access)
python3 /usr/local/bin/test_mic.py
```

### 2. Model Management
If voice recognition is failing or latency is high, trigger the pre-loader to ensure model weights are cached correctly:

```bash
# Ensure model weights are present and optimized
sudo /usr/lib/aios/voice/preload-models.sh
```

### 3. Hardware Probing & Configuration
The voice configuration is managed via `/etc/aios/voice/config.py` (or local project copy). When adding new hardware or changing environments, ensure the configuration correctly maps audio inputs:

- **Check Input Source:** Use `arecord -l` to identify hardware device IDs.
- **Update Config:** Modify `voice/config.py` to match the `hw:X,Y` device string identified by `arecord`.

## Pitfalls & Troubleshooting
*   **Permission Issues:** If the microphone script fails to record, ensure the user is part of the `audio` group (`sudo usermod -aG audio $USER`).
*   **Model Latency:** If dictation is slow, verify the model path in `voice/config.py` points to a local, pre-loaded binary rather than a remote URL.
*   **Silence Delay:** If the system cuts off speech too early, increase the `silence_delay` parameter in the `voice/config.py` file.
