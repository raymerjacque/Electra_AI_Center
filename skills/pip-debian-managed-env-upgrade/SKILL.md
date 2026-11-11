---
name: pip-debian-managed-env-upgrade
description: Handles Python package upgrades on Debian/MakuluLinux by bypassing the externally-managed-environment PEP 668 restriction.
triggers: ["pip externally-managed-environment error", "pip install upgrade debian 13", "pip3 break-system-packages"]
---

# pip-debian-managed-env-upgrade

## Overview
Modern Debian-based systems (like MakuluLinux on Debian 13+) enforce PEP 668, preventing direct `pip install` commands from modifying system Python packages to protect OS integrity. This skill provides the standardized, safe procedure to update user-space or system-level Python packages when the `externally-managed-environment` error is encountered.

## Proven Procedure
When a `pip install` command fails with "error: externally-managed-environment", follow these steps:

1. **Assess the package requirement:** 
   Determine if the package should be installed in a Virtual Environment (recommended) or globally. If you must update a system package:

2. **Run the upgrade with the safety flag:**
   Use the `--break-system-packages` flag explicitly to allow modification of the system Python environment.

   ```bash
   # Syntax for upgrading a specific package
   pip3 install --upgrade --break-system-packages <package-name>
   
   # Example for a specific version
   pip3 install --break-system-packages <package-name>==<version>
   ```

3. **Verify the installation:**
   ```bash
   pip3 show <package-name>
   ```

## Pitfalls & Troubleshooting
* **Virtual Environments:** Always prefer `python3 -m venv .venv` and activating it (`source .venv/bin/activate`) before installing packages to avoid breaking the OS Python dependencies. Use this skill ONLY when you are absolutely certain the package must be installed globally.
* **Package Conflicts:** Using `--break-system-packages` can potentially destabilize OS components that rely on specific Python versions. If an `apt` managed package breaks, use `sudo apt install --reinstall python3-<package-name>` to restore the system version.
