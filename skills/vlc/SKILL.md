---
name: vlc
description: Skill for VLC media player
---

# vlc Skill

# VLC Media Player Skill

## Overview
VLC is a free and open-source cross-platform multimedia player and framework that plays most multimedia files, DVDs, audio CDs, VCDs, and streaming protocols.

## Commands
- `vlc` - Launch VLC GUI
- `vlc <file>` - Play a specific media file
- `vlc --fullscreen <file>` - Play in fullscreen
- `cvlc` - Command-line (ncurses) interface
- `vlc --intf qt` - Force Qt interface

## Common Operations
- Play file: `vlc movie.mkv`
- Play audio only: `vlc --no-video song.mp3`
- Stream/transcode: `vlc input.mp4 --sout '#transcode{vcodec=h264}:standard{access=file,mux=mp4,dst=out.mp4}'`
- Adjust volume: `vlc --volume 70 file.mp3`
- Subtitle delay: use `j`/`k` keys in GUI

## Plugins & Extensions
VLC supports Lua and native plugins:
- Lua extensions: `~/.local/share/vlc/lua/extensions/`
- Lua playlists/parsers: `~/.local/share/vlc/lua/playlist/`
- System plugins: `/usr/lib/x86_64-linux-gnu/vlc/plugins/`
- List loaded modules: `vlc --list` or `vlc -H`

## Configuration
- Config file: `~/.config/vlc/vlcrc`
- Reset config: delete `~/.config/vlc/vlcrc`

## Pitfalls
- Hardware acceleration may fail on some Intel GPUs; try `--avcodec-hw=none`
- For Blu-ray playback, libbluray/aacs keys must be installed
