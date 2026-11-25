---
name: flatpak-steam-external-drive
description: Fixes Flatpak Steam failing to recognize, mount, or write to external hard drives by configuring Flatpak filesystem overrides and correcting host mount permissions.
triggers: ["flatpak steam external drive", "steam library external disk error", "flatpak filesystem override media", "steam external drive permission denied"]
---

# Flatpak Steam External Drive Configuration

## Overview
When Steam is installed via Flatpak, strict sandboxing prevents it from accessing external drives mounted under `/media` or `/run/media` by default. This skill provides the exact procedure to grant Flatpak Steam host filesystem access to external drives and resolve underlying ownership/permission issues.

## Proven Procedure

1. **Grant Flatpak Filesystem Access to External Mounts:**
   Run the following commands to allow the Flatpak version of Steam to read and write to standard mount locations:
   ```bash
   flatpak override --user --filesystem=/media com.valvesoftware.Steam
   flatpak override --user --filesystem=/run/media com.valvesoftware.Steam
   ```

2. **Verify Host Mount Permissions:**
   Ensure the current user owns or has access to the target game library directory on the external drive:
   ```bash
   sudo chown -R $USER:$USER /media/$USER/<drive-uuid-or-name>
   ```

3. **Restart Flatpak Steam:**
   Completely quit Steam (or restart the flatpak instance) for the overrides to take effect:
   ```bash
   flatpak kill com.valvesoftware.Steam
   flatpak run com.valvesoftware.Steam
   ```

## Pitfalls & Troubleshooting
- **Sandboxing Limitations:** Even if `chmod 777` is applied to the drive on the host, Flatpak sandboxing blocks access unless explicit `--filesystem` overrides are added.
- **Removable Media Permissions:** If drives are auto-mounted by udisks2 under `/run/media/$USER/`, ensure the user has execution permissions along the entire path.
