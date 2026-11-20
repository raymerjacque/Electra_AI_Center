---
name: nemo-archive-permissions
description: Fixes incorrect file and directory permissions after extracting ZIP or compressed archives via the Nemo file manager.
triggers: ["extract archive permissions wrong", "unzip chmod fix file manager", "nemo extract permissions", "fix permissions after extraction"]
---

# Nemo Archive Permissions Fixer

## Overview
When compressing and extracting files using the graphical Nemo file manager (especially standard `.zip` archives), file permissions can sometimes be lost or restricted due to the local `umask` settings (often resulting in restrictive `600` or `700` permissions). This skill provides a quick way to restore standard POSIX permissions (`644` for files, `755` for directories).

## Proven Procedure
To fix permissions recursively in the target directory where the archive was extracted:

1. Open a terminal inside the extracted folder.
2. Fix all file permissions to `644` (read/write for owner, read-only for others):
   ```bash
   find . -type f -exec chmod 644 {} +
   ```
3. Fix all directory permissions to `755` (read/write/execute for owner, read/execute for others):
   ```bash
   find . -type d -exec chmod 755 {} +
   ```

## Pitfalls & Troubleshooting
- **Tarballs vs Zips:** Standard `.tar.gz` or `.tar.xz` archives preserve Unix permissions much better than `.zip` files. Prefer using tar archives when transferring executable scripts or code repositories.
