---
name: vlc-openvcd
description: Skill for VLC VCD plugin
---

# vlc-openvcd Skill

# VLC VCD Plugin Skill

## Overview
VLC VCD plugin enables Video CD (VCD) playback in VLC media player.

## Commands
- `vlc /dev/dvd` - Play VCD from optical drive (same device as DVD)
- `vlc vcd:/dev/dvd` - Alternative VCD path

## VCD Support
- MPEG-1 format Video CDs
- Compatible with legacy DVD players
- Limited menu support compared to DVD

## Configuration
- Device path: `/dev/dvd` or `/dev/sr0`
- MPEG-1 playback settings in VLC

## Troubleshooting
- VCD ISO files can also be played: `vlc video.mpg`
- Some VCDs may have compatibility issues
- Verify with: `ls /dev/sr*`
