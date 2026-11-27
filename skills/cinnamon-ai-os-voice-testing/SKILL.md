---
name: cinnamon-ai-os-voice-testing
description: Procedures and scripts for validating microphone hardware, configuring Whisper model selection, and testing voice dictation pipelines.
triggers: ["test microphone", "voice pipeline setup", "whisper model configuration", "check audio input", "troubleshoot microphone"]
---

# AI OS Voice Testing and Configuration

## Overview
This skill provides a standardized way to test microphone hardware and verify the voice dictation pipeline (specifically Whisper models). It includes hardware-aware model configuration and a verified microphone loopback test.

## Proven Procedure

### 1. Microphone Hardware Test
To verify audio input is working correctly before triggering AI voice features, use the provided `test-mic.sh` script.

**Prerequisite:** Ensure the system audio configuration is set to the correct card.
```bash
# Execute the microphone loopback test
./test-mic.sh
```

**What the script does:**
*   Captures 3 seconds of audio via `arecord`.
*   Plays it back immediately via `aplay` on `plughw:1,0` to confirm raw hardware capture and output.

### 2. Voice Configuration and Model Preloading
When deploying or re-configuring the voice pipeline, ensure hardware-accurate model selection is performed.

*   **Config Logic:** Modify `voice/config.py` to adjust how the system probes RAM, CPU, and GPU/NPU availability to select the appropriate Whisper model size (e.g., tiny, base, small, medium).
*   **Preloading:** Use `usr/lib/aios/voice/preload-models.sh` to download and cache the models to `/usr/share/aios/voice/models/`.

### 3. Verification of Installation
Check the post-install status to ensure the daemon is ready:
```bash
# Verify model storage
ls -lh /usr/share/aios/voice/models/whisper-medium.bin

# Check for active voice daemon status
systemctl status ai-voice-daemon
```

## Pitfalls & Troubleshooting
*   **Hardware Mismatch:** If `test-mic.sh` fails to produce sound, check `arecord -l` to ensure your microphone is mapped to the device expected by `plughw:1,0` or update the script to match the correct card/device index.
*   **Model Latency:** If dictation feels sluggish, downgrade the model in `voice/config.py` from `medium` to `small` or `base` to fit within available RAM/VRAM.
*   **Permission Denied:** Ensure the user is part of the `audio` group to access hardware inputs directly: `sudo usermod -aG audio $USER`.
