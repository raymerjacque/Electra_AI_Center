---
name: cinnamon-ai-os-auto-skill-generator
description: Dynamically scans the system PATH to discover executables and auto-generates corresponding skill definition files based on a standardized Python template.
triggers: ["auto-generate skills", "scan system for skills", "generate skill files", "discover all programs"]
---

# AI OS Auto-Skill Generator

## Overview
This skill automates the integration of new command-line tools into the AI's orchestration framework. Instead of manually writing a wrapper for every utility on the system, this system scans the `$PATH`, identifies executables, and auto-generates Python-based skill definition files using a provided template.

## Proven Procedure
To trigger the automated discovery and generation process:

1.  **Preparation**: Ensure the `manager.py` orchestration script is located at `/home/guy/workspace/manager.py` and the base class definition exists at `/home/guy/workspace/skills/base.py`.
2.  **Execution**: Run the manager script from the workspace directory:
    ```bash
    cd /home/guy/workspace/
    python3 manager.py
    ```
3.  **Mechanism**: 
    *   The `manager.py` iterates through all directories listed in `$PATH`.
    *   It filters for files that are executable.
    *   It sanitizes program names (e.g., converting hyphens to CamelCase for class names and prefixing digits to avoid syntax errors).
    *   It generates a corresponding Python file in `/home/guy/workspace/skills/generated/` for every discovered program.

## Pitfalls & Troubleshooting
*   **Naming Collisions**: The generator handles hyphens and digit prefixes automatically by using string sanitization (e.g., `7z` becomes `_7z`, `run-parts` becomes `RunParts`). If a collision occurs (two binaries mapped to the same class name), the script will overwrite existing files—ensure backup if customization is required.
*   **Path Permissions**: The scanner will only generate skills for binaries readable by the current user. Running the script with `sudo` might generate skills for root-only binaries that the user cannot execute, causing "permission denied" errors when the AI attempts to use them later. It is recommended to run as the standard user.
*   **Performance**: Scanning thousands of binaries and generating files takes several seconds. Avoid running this in a loop; trigger it only when new software packages are installed.
