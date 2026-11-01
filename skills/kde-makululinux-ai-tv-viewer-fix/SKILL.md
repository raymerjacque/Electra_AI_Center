---
name: kde-makululinux-ai-tv-viewer-fix
description: Troubleshoot and resolve startup crashes in MakuluLinux-AI-TV-Viewer by installing missing wxWidgets runtime dependencies.
triggers: ["MakuluLinux-AI-TV-Viewer crashes", "AI TV Viewer closes immediately", "missing libwxgtk runtime", "wxWidgets application startup crash"]
---

# MakuluLinux-AI-TV-Viewer Startup Crash Fix

## Overview
Use this skill when MakuluLinux-AI-TV-Viewer or similar desktop media/AI applications close immediately after launch due to missing shared libraries or runtime dependencies.

## Proven Procedure
1. Test launching the application via terminal to observe stderr/stdout errors:
   ```bash
   makululinux-ai-tv-viewer
   ```
2. Identify missing shared libraries (e.g., `libwx_gtk3u_core-3.2.so` or similar wxWidgets errors).
3. Install the required runtime package via apt:
   ```bash
   sudo apt update
   sudo apt install -y libwxgtk3.2-1t64
   ```
4. Verify application launch post-installation.

## Pitfalls & Troubleshooting
- Ensure package manager lists are updated before installing packages (`sudo apt update`).
- Package names may vary slightly across Debian/Ubuntu versions (e.g., `libwxgtk3.0-gtk3` vs `libwxgtk3.2-1t64`). Check `apt-cache search libwxgtk` if necessary.
