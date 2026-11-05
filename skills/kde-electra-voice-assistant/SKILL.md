---
name: kde-electra-voice-assistant
description: Configure custom English female voice synthesis (Piper TTS) and wake-word voice assistant (Vosk STT) with "Hey Sarah" trigger for the Electra AI system on KDE Plasma.
triggers: ["install english female voice", "hey sarah wake word", "voice assistant setup", "electra text to speech"]
---

# Electra Voice Assistant and Wake Word Setup (KDE Plasma)

## Overview
This skill covers setting up a complete local offline voice assistant system in KDE Plasma, including text-to-speech (TTS) via Piper, speech-to-text (STT) wake-word detection ("Hey Sarah") via Vosk, and LLM command integration.

## Proven Procedure
1. Install dependencies for audio, TTS, and STT:
   ```bash
   sudo apt-get update && sudo apt-get install -y python3-pip python3-venv espeak-ng alsa-utils pulseaudio-utils
   ```
2. Download and set up Piper TTS with an English female voice (`en_US-lessac-medium`):
   ```bash
   mkdir -p ~/.local/share/piper/voices ~/.local/bin
   # Download piper binary and voice models into ~/.local/share/piper/
   ```
3. Create the text-to-speech helper script at `~/.local/bin/say-female`:
   ```bash
   #!/usr/bin/env bash
   echo "$*" | ~/.local/share/piper/piper --model ~/.local/share/piper/voices/en_US-lessac-medium.onnx --output-file /tmp/speech.wav
   aplay /tmp/speech.wav 2>/dev/null
   ```
   Make it executable: `chmod +x ~/.local/bin/say-female`
4. Configure Vosk-based wake-word service for "Hey Sarah" under `~/.config/systemd/user/hey-sarah.service`.

## Pitfalls & Troubleshooting
- Ensure audio routing is correct (`pulseaudio` or `pipewire` active) so `aplay` or `paplay` can access the sound card without conflicts.
- Python packages like `vosk` may require a virtual environment or `--break-system-packages` on modern PEP 668 distributions.
