---
name: flatpak-steam-secondary-drives
description: Configure and troubleshoot Flatpak Steam permissions to access secondary and external hard drives.
triggers: ["flatpak steam secondary drives", "steam can't see second drive flatpak", "flatpak steam storage devices"]
---

# Flatpak Steam Secondary Drives

## Overview
Flatpak applications run in a sandboxed environment and often cannot access secondary internal or external drives by default. This skill covers configuring filesystem overrides and permissions so Flatpak Steam can detect and use secondary drives (e.g., 4TB data drives).

## Proven Procedure
1. Grant Flatpak Steam access to host filesystems or specific mount points using `flatpak override`:
   ```bash
   flatpak --user override --filesystem=/path/to/drive com.valvesoftware.Steam
   # Or to grant access to all mounted media/external drives:
   flatpak --user override --filesystem=/media com.valvesoftware.Steam
   flatpak --user override --filesystem=/mnt com.valvesoftware.Steam
   ```
2. Alternatively, use Flatseal (GUI permission manager) to toggle filesystem access under the Steam application settings.
3. Restart Steam completely (`flatpak kill com.valvesoftware.Steam` followed by launching it again) to apply permissions.
4. Inside Steam, go to **Settings > Storage**, click the drop-down/plus icon, and add the directory on the secondary drive (e.g., `/media/username/4TB-Drive/SteamLibrary`).

## Pitfalls & Troubleshooting
- **Permission Denied / Drive Not Visible**: Ensure the mount point is correctly owned by the current user or readable, and that Flatpak has explicit `--filesystem=` permissions for that exact path or parent directory (`/media` or `/mnt`).
- **Symlink issues**: Flatpak apps sometimes fail to traverse symlinks pointing outside their sandbox container unless the target path is explicitly allowed via overrides.
