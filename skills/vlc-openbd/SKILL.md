---
name: vlc-openbd
description: Skill for VLC OpenBD Blu-ray plugin
---

# vlc-openbd Skill

# VLC OpenBD Plugin Skill

## Overview
VLC OpenBD plugin enables Blu-ray disc playback support in VLC media player.

## Commands
- `vlc` - Launch VLC with OpenBD support
- `vlc --bluray-device /dev/sr0` - Play Blu-ray disc
- `vlc dvdnav:/dev/sr0` - Play DVD with navigation

## Blu-ray Support
- Requires libaacs and libbluray packages
- AACS keys must be in `~/.config/aacs/keys.conf`
- For UHD Blu-ray, libbdplus may be needed
- Open source AACS keys available at https://www.aacsplus.com/knowledge-base/

## Configuration
- Key file location: `~/.config/aacs/keys.conf`
- VLC plugin path: `/usr/lib/x86_64-linux-gnu/vlc/plugins/`
- Environment variable: `LD_LIBRARY_PATH` may need adjustment

## Troubleshooting
- If Blu-ray doesn't play, verify AACS keys are correct
- Some newer discs require newer libaacs versions
- Debug with: `vlc --verbose bluray:`
