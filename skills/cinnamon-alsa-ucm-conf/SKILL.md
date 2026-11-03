---
name: cinnamon-alsa-ucm-conf
description: Skill for alsa-ucm-conf
---

# alsa-ucm-conf Skill

This skill provides information about the ALSA Use Case Manager (UCM) configuration files, which define audio hardware profiles and input/output routing for the Advanced Linux Sound Architecture (ALSA) system.

**Overview:**
- ALSA UCM configuration files define audio card profiles and device settings
- Used by the Advanced Linux Sound Architecture (ALSA) system for hardware detection
- Contains profile, device, and widget configurations
- Typically stored in `/usr/share/alsa/ucm/` or `/etc/alsa/ucm.conf`

**Usage:**
- Audio profiles are managed automatically by the system via PulseAudio/PipeWire
- Can list available profiles with: `pactl list cards short` or `amixer scontrols`
- Switch profiles with: `pactl set-card-profile <card_name> <profile>`
- Modify UCM files in `/usr/share/alsa/ucm2/` or `/etc/alsa/ucm.conf` for custom configurations

**Common profiles:**
- `analog-stereo`, `digital-stereo`, `headset-output`, `headset-input`
- `pro-audio`, `off` (disable audio card)
