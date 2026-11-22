---
name: cinnamon-system-info-gathering
description: Collects core hardware, session, and process information for Cinnamon desktop systems. Useful for diagnostics, performance monitoring, and system profiling.
triggers: ["system profiling", "hardware diagnostics", "cinnamon process monitoring", "performance assessment"]
---

# Cinnamon System Information Gathering

## Overview
This skill automates the collection of core hardware, session type, and process information on Cinnamon Linux desktops. It provides a quick diagnostic snapshot useful for performance monitoring, troubleshooting, and system profiling. Execute when needing to identify CPU, memory, session type, active processes, and audio/connection status on Cinnamel systems.

## Proven Procedure
Run the following commands in the terminal to gather system information:

**1. CPU and Memory Overview:**
```bash
lscpu && free -h
```

**2. Session Type and Desktop Environment:**
```bash
echo "Session type: $XDG_SESSION_TYPE"
echo "DE: $XDG_CURRENT_DESKTOP"
```

**3. Active Processes (Cinnamon-specific):**
```bash
ps aux | grep -E 'cinnamon|muffin' | grep -v grep
```

**4. System Resource Summary:**
```bash
uptime
```

**5. Audio Status (PipeWire/PulseAudio):**
```bash
pactl list sinks | grep -A 3 "Name: .*output" | head -n 6
```

**6. Network Connection:**
```bash
ip -4 addr show | grep inet | grep -v docker | head -n 2
```

**7. Disk Usage:**
```bash
df -h / /home
```

## Pitfalls & Troubleshooting
- **No output from `lscpu`**: Ensure `util-linux` package is installed (`sudo apt install util-linux`).
- **Empty process list**: Verify you're running in a Cinnamon session (check `echo $XDG_CURRENT_DESKTOP`).
- **Audio showing 0%**: May indicate PipeWire not running; start with `pipewire-media-session` or restart the service.
- **Network showing only docker IPs**: The `grep -v docker` filter excludes container interfaces; remove it to see all interfaces.
- **Disk usage unexpectedly high**: Check for large hidden files or logs with `sudo du -sh /var/log`.

This skill is reusable for any future Cinnamon desktop diagnostics and eliminates the need to recall individual commands for system profiling.
