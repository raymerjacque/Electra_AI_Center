---
name: alsa-utils
description: Skill for alsa-utils
---

# alsa-utils Skill

This skill provides functionality for the ALSA utilities, which are command-line tools for managing sound cards and audio devices on Linux systems.

**Overview:**
- `alsa-utils` is a package containing various utilities for ALSA (Advanced Linux Sound Architecture)
- Works with PulseAudio and PipeWire on modern systems
- Provides tools for controlling volume, switching inputs/outputs, and troubleshooting audio

**Commands:**
- `alsamixer` - Interactive NCurses mixer for sound card control
- `amixer` - Command-line mixer control (e.g., `amixer sset Master 50%`)
- `amixer scontrols` - List available sound controls
- `alsactl init` - Initialize sound card settings
- `alsactl store` - Store current settings to persistent memory
- `speaker-test` - Test speaker output
- `arecord` - Record audio from command line
- `aplay` - Play audio files from command line

**Usage examples:**
- Open mixer: `alsamixer`
- Set master volume: `amixer sset Master 75%`
- Capture audio: `arecord -d 5 -f cd -t wav test.wav`
- Play audio: `aplay test.wav`
- List controls: `amixer scontrols`
