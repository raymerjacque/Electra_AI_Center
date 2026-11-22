---
name: python-pep668-venv
description: Resolves Python PEP 668 externally-managed-environment errors by installing venv packages and creating local virtual environments.
triggers: ["externally-managed-environment", "pep 668", "pip install error break-system-packages", "python venv setup"]
---

# Python PEP 668 Externally-Managed-Environment Fix

## Overview
Modern Debian and Ubuntu-based Linux distributions (including MakuluLinux) enforce PEP 668, blocking direct system-wide `pip install` commands to protect the OS package manager. When encountering `error: externally-managed-environment`, this skill provides the standard procedure to set up and use a local Python virtual environment.

## Proven Procedure
1. Install required virtual environment packages via APT:
   ```bash
   sudo apt update && sudo apt install -y python3-full python3-venv
   ```
2. Create a virtual environment in the project directory:
   ```bash
   python3 -m venv venv
   ```
3. Activate the virtual environment or run pip directly from it:
   ```bash
   source venv/bin/activate
   # Or use ./venv/bin/pip and ./venv/bin/python
   ```
4. Upgrade pip inside the virtual environment:
   ```bash
   pip install --upgrade pip
   ```

## Pitfalls & Troubleshooting
- Do NOT pass `--break-system-packages` unless strictly necessary, as it can break system python packages managed by APT.
- Ensure `python3-full` is installed if `python3-venv` fails to include essential headers or modules.
