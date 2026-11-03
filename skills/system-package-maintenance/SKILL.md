---
name: system-package-maintenance
description: Procedures for safely updating system apt packages and user pip packages handling PEP 668 restrictions and xargs edge cases.
triggers: ["update system packages", "upgrade pip packages", "apt upgrade", "pip upgrade outdated"]
---

# System Package Maintenance

## Overview
This skill outlines the robust procedure for updating system packages via `apt` and user Python packages via `pip3`, accounting for modern Python environment restrictions (PEP 668 externally-managed-environment) and empty xargs input handling.

## Proven Procedure

### 1. System Packages (APT)
Run standard system upgrades non-interactively:
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. User Pip Packages (PEP 668 Compliant)
To upgrade user pip packages without failing on PEP 668 restrictions:
```bash
pip3 list --outdated --format=freeze 2>/dev/null | cut -d= -f1 | xargs -r -n1 pip3 install --upgrade --user --break-system-packages
```
*Note: Using `xargs -r` (or checking for empty input) prevents `pip3` from failing with `ERROR: You must give at least one requirement to install` when no outdated packages are returned.*

## Pitfalls & Troubleshooting
- **PEP 668 Externally Managed Environment:** Modern Linux distributions block global/user `pip install` unless `--break-system-packages` is explicitly supplied or a virtual environment is used.
- **Empty Xargs Input:** Piping `pip3 list --outdated` directly into `xargs -n1 pip3 install` fails if the list is empty. Always use `xargs -r` GNU extension or conditionally check if any packages are returned.
