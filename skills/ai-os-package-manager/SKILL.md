---
name: ai-os-package-manager
description: Safely updates system-wide APT packages and user-level Python (pip) packages, handling common pip versioning and formatting constraints.
triggers: ["update system packages", "upgrade python packages", "pip update all packages", "run system and python updates"]
---

# AI OS Package Manager

## Overview
This skill handles the dual requirement of updating system-level dependencies via `apt` and user-space Python packages via `pip`. It accounts for common pitfalls, such as `pip`'s incompatibility between `--format=freeze` and `--outdated` flags, and ensures robust handling of potentially empty package lists.

## Proven Procedure
To safely update both system and user-space dependencies:

1.  **Update APT Packages:**
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

2.  **Update User-Space PIP Packages:**
    Use this command pipeline to accurately identify outdated packages, strip the header, extract names, and perform an upgrade without erroring on incompatible format flags:
    ```bash
    pip3 list --outdated | tail -n +3 | awk '{print $1}' | xargs -r -n1 pip3 install --upgrade --user
    ```

## Pitfalls & Troubleshooting
*   **PIP Format Errors:** Do not use `pip3 list --outdated --format=freeze`. It will return an exit code 123. Always use the default table format and filter with `tail` and `awk` as shown above.
*   **PEP 668 (Externally Managed Environment):** If the system has enabled PEP 668 protection, `pip install` might block global updates. Always include `--user` when updating packages in user-space to avoid this conflict. The provided command pipeline inherently includes `--user`.
*   **Empty Lists:** The `-r` flag in `xargs` ensures that if no packages are found to be outdated, `xargs` will not execute `pip3 install` with an empty argument list, preventing unnecessary command errors.
