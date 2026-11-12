---
name: cinnamon-disk-optimizer
description: Automates disk cleanup, intelligent SSD/HDD defragmentation detection, and directory structure enforcement using a custom Python script.
triggers: ["disk cleanup script", "ssd hdd defrag python", "folder structure enforcement", "disk optimizer"]
---

# Cinnamon Disk Optimizer

## Overview
This skill provides a Python-based automated solution for cleaning temporary files and system caches, intelligently checking storage types to safely handle HDDs versus SSDs (skipping TRIM-based or flash drives for defragmentation), and standardizing user directory structures.

## Proven Procedure
1. Create a script (e.g., `disk_optimizer.py`) with checks for root privileges, drive rotational status (`/sys/block/<dev>/queue/rotational`), and common temporary cache locations (`/tmp`, `~/.cache`, apt caches).
2. Implement safe deletion logic for old temporary files.
3. Implement conditional defragmentation targeting only rotational hard drives (`e4defrag` or similar utilities).
4. Run the optimization script via python:
   ```bash
   python3 /home/dd811162436/disk_optimizer.py
   ```

## Pitfalls & Troubleshooting
- **SSD Defragmentation:** Ensure the rotational check reads `/sys/block/.../rotational` properly to prevent unnecessary write wear on solid-state drives.
- **Permissions:** Some cache cleaning and defragmentation commands require `sudo` privileges. Ensure the script handles or prompts for elevated permissions gracefully.
