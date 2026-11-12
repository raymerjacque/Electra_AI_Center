---
name: vlc-opencda
description: Skill for VLC Audio CD plugin
---

# vlc-opencda Skill

# VLC Audio CD Plugin Skill

## Overview
VLC Audio CD plugin enables Audio CD (CDDA) playback in VLC media player.

## Commands
- `vlc /dev/sr0` - Play Audio CD from optical drive
- `vlc cdda:/dev/sr0` - Alternative CDDA path

## Audio CD Support
- Standard Audio CD (CDDA) format
- Track selection via GUI or command
- Ripping support with proper codec selection

## Configuration
- Default device: `/dev/sr0`
- Can specify alternate device: `vlc /dev/sr1`
- Audio output settings in VLC preferences

## Troubleshooting
- If CD not recognized, verify `/dev/sr0` exists with `ls /dev/sr*`
- Some drives may need `eject`/`cdtowav` for ripping
- Audio sync issues may require output driver adjustment
