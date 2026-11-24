---
name: kde-workspace-listing
description: Lists the contents of the workspace directory in the user's home folder, useful for verifying project structure or file presence before operations.
triggers: ["cd workspace", "list workspace contents", "check home directory files"]
---

# KDE Workspace Listing

## Overview
This skill lists the contents of the `workspace` directory located in the user's home folder. It is triggered when navigating to or inspecting the workspace directory to verify project structure or file presence.

## Proven Procedure
```bash
cd workspace
ls -la /home/ai-besefmaker/workspace
```

## Pitfalls & Troubleshooting
- If the `workspace` directory does not exist, verify the correct path or create it with `mkdir workspace`.
- Ensure proper permissions to read the directory contents.
