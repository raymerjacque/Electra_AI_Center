---
name: kde-voice-assistant-setup
description: Configures an offline voice-activated AI assistant using Vosk for wake-word detection, Piper for female TTS, and Ollama for LLM processing.
triggers: ["setup voice assistant", "install wake word", "configure hey sarah", "setup female voice tts"]
---

# KDE Voice Assistant Setup

## Overview
This skill automates the configuration of a custom offline voice assistant environment. It installs and links the necessary services (Vosk for wake-word detection, Piper for TTS, and Ollama for LLM) to allow voice interaction with an AI agent.

## Proven Procedure
1. **Ensure Dependencies:**
   - Install essential voice tools:
     ```bash
     sudo apt update && sudo apt install -y python3-pip pipx
     pipx install vosk piper-tts
     ```
   - Ensure `ollama` is installed and the `qwen2.5:3b` model is pulled.

2. **Setup Wake Word (Vosk):**
   - Create the detection script `~/.local/bin/hey-sarah` to monitor microphone input using Vosk's model.
   - Configure a `systemd` user service `~/.config/systemd/user/hey-sarah.service` to run the detection script on login.

3. **Configure TTS (Piper):**
   - Download the preferred female voice model (e.g., `en_US-lessac-medium`).
   - Create a helper script `~/.local/bin/say-female` that pipes text to the Piper binary.

4. **Service Activation:**
   ```bash
   systemctl --user daemon-reload
   systemctl --user enable --now hey-sarah.service
   ```

## Pitfalls & Troubleshooting
- **Vosk Import Errors:** If `import vosk` fails, ensure the Python environment is correctly linked in your `PATH` or use `pipx` to isolate the dependencies.
- **Audio Device Issues:** Ensure `pulseaudio` or `pipewire` is correctly configured and the user has permissions to access the microphone. Use `pactl info` to verify the default sink/source.
- **Service Loops:** If the system attempts to process its own output as a wake word, add a small "sleep" delay or a conditional mute logic in the `hey-sarah` script during active AI response.
