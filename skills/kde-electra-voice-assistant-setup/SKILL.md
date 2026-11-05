---
name: kde-electra-voice-assistant-setup
description: Deploys a custom voice assistant pipeline (Wake word: "Hey Sarah") using Vosk for STT, Piper for TTS, and Systemd for background orchestration.
triggers: ["setup sarah assistant", "install electra voice", "hey sarah wake word", "configure voice commands"]
---

# KDE-Electra Voice Assistant Setup

## Overview
This skill deploys and manages a custom local voice assistant pipeline. It enables hands-free interaction using "Hey Sarah" as a wake word, powered by Vosk (STT), a text generation model (Ollama), and Piper (TTS). It handles the creation of systemd services for persistence and sets up utility aliases for management.

## Proven Procedure

### 1. Prerequisites (Core Components)
Ensure necessary tools are installed:
```bash
sudo apt install python3-pip python3-venv paplay -y
# Create the environment and install dependencies
mkdir -p ~/bin/electra-voice
python3 -m venv ~/bin/electra-voice/venv
source ~/bin/electra-voice/venv/bin/activate
pip install vosk piper-tts ollama sounddevice
```

### 2. Configure Text-to-Speech (Piper)
Download the female voice model (e.g., `en_US-lessac-medium.onnx`):
```bash
mkdir -p ~/.local/share/piper
# Download voice and config files (example path)
# wget -O ~/.local/share/piper/voice.onnx <URL>
# wget -O ~/.local/share/piper/voice.onnx.json <URL>
```

### 3. Create Voice Scripts
Create the speech script (`~/.local/bin/say-female`):
```bash
#!/bin/bash
echo "$1" | piper --model ~/.local/share/piper/voice.onnx --config ~/.local/share/piper/voice.onnx.json --output-raw | paplay --raw --channels=1 --rate=22050
```
Make it executable: `chmod +x ~/.local/bin/say-female`

### 4. Setup Wake-Word Service (Systemd)
Create the systemd service file at `~/.config/systemd/user/hey-sarah.service`:
```ini
[Unit]
Description=Hey Sarah Voice Assistant
After=default.target

[Service]
ExecStart=/home/user/bin/electra-voice/venv/bin/python /home/user/.local/bin/hey-sarah
Restart=always
RestartSec=5

[Install]
WantedBy=default.target
```

### 5. Deployment
Enable and start the service:
```bash
systemctl --user daemon-reload
systemctl --user enable hey-sarah.service
systemctl --user start hey-sarah.service
```

## Pitfalls & Troubleshooting
*   **Audio Output:** If the assistant is silent, ensure the user account is part of the `audio` group (`sudo usermod -aG audio $USER`) and the default sink in PipeWire/PulseAudio is correct (`pactl set-default-sink <id>`).
*   **Microphone Input:** If "Hey Sarah" is not detected, check `arecord -l` to ensure the correct hardware device ID matches the one configured in the Python script.
*   **Dependency Failures:** If `pip` installs fail due to system-wide constraints, always use a virtual environment (`venv`) to isolate `vosk` and `piper` dependencies.
*   **Performance:** For fast wake-word response, ensure the `vosk-model-small` is used rather than larger models, as it significantly reduces CPU load and latency.
