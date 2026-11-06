---
name: cinnamon-fdupes-duplicate-search
description: Use the fdupes tool to find and count duplicate files across directories on external drives or mounted volumes in Cinnamon.
triggers: ["find duplicate files", "search for duplicates", "count duplicate files", "fdupes external drive"]
---

# Find Duplicate Files Using fdupes

## Overview
This skill outlines how to install and use `fdupes` to scan mounted drives or directories for duplicate files, saving storage space by identifying redundant data.

## Proven Procedure
1. Install `fdupes` if not already present on the system:
   ```bash
   sudo apt-get update && sudo apt-get install -y fdupes
   ```
2. Run a recursive scan on the target directory to find duplicate files:
   ```bash
   fdupes -r "/path/to/directory"
   ```
3. To count duplicate files or summarize them without cluttering the output, you can pipe the results or use flags such as `-S` for a size summary:
   ```bash
   fdupes -r -S "/path/to/directory"
   ```

## Pitfalls & Troubleshooting
- **Large Drives:** Scanning massive external SSDs recursively can take significant time depending on I/O speeds and the number of files. Run inside a `tmux` or `screen` session if necessary.
- **Permissions:** Ensure the user has read permissions for all subdirectories on the mounted volume.
