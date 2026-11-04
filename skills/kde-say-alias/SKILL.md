---
name: kde-say-alias
description: Creates a persistent English female TTS alias in KDE Plasma that works from any terminal. Triggers when user wants to use text-to-speech from command line without typing full Piper commands.
triggers: ["say", "text-to-speech", "tts voice"]
---

# English Female TTS Alias for KDE Plasma

## Overview
Sets up a persistent `say` alias in KDE Plasma that invokes Piper TTS with the English female `lessac` voice. This allows users to type `say "any text"` in any terminal and hear natural English female speech. The alias is added to `~/.bashrc` for persistence across sessions.

## Proven Procedure

### Step 1: Install Piper TTS Engine
```bash
sudo apt update
sudo apt install -y piper
```

### Step 2: Install English Female Voice Model
```bash
flatpak install flathub org.freedesktop.Platform.VAAPI.Intel -y  # Ensure VAAPI drivers
flatpak install flathub com.voicevox.voicevox-engine -y  # Alternative if needed
# Download Lessac voice model
wget -O /usr/share/piper/voices/en_US/lessac.onnx "https://huggingface.co/rhasspy/piper-voices/resolve/main/en_US/lessac/medium/lessac.onnx?download=true"
wget -O /usr/share/piper/voices/en_US/lessac.onnx.normalized "https://huggingface.co/rhasspy/piper-voices/resolve/main/en_US/lessac/medium/lessac.onnx.normalized?download=true"
```

### Step 3: Create the say Alias
Add to `~/.bashrc`:
```bash
echo 'alias say="piper -v /usr/share/piper/voices/en_US/lessac/medium/lessac.onnx"' >> ~/.bashrc
source ~/.bashrc
```

### Step 4: Test the Installation
```bash
say "Hello, this is an English female voice"
```

### Step 5: Create Local Bin Script (Optional)
```bash
mkdir -p ~/.local/bin
cat > ~/.local/bin/say-female << 'EOF'
#!/bin/bash
piper -v /usr/share/piper/voices/en_US/lessac/medium/lessac.onnx
EOF
chmod +x ~/.local/bin/say-female
```

## Pitfalls & Troubleshooting

- **Voice model not found**: Ensure the `.onnx` and `.onnx.normalized` files are in `/usr/share/piper/voices/en_US/lessac/medium/`
- **Permission errors**: Use `sudo` for installation paths; use `~/.local/bin/` for user-level scripts
- **Aliases not working**: Run `source ~/.bashrc` or restart the terminal
- **Piper not installed**: Install with `sudo apt install piper`
- **No sound output**: Check KDE Plasma audio settings and VAAPI driver configuration
