---
name: python-pep668-management
description: Safely resolve PEP 668 (externally-managed-environment) errors when upgrading Python packages by verifying system-level package alternatives.
triggers: ["pip update error", "externally-managed-environment", "pip install failure", "python module conflict"]
---

# Python PEP 668 Management

## Overview
Modern Linux distributions (including MakuluLinux) use PEP 668 to prevent `pip` from overwriting system-installed Python packages, which can break the OS. This skill provides the workflow to identify why a package update is failing and how to verify or install the correct system-level equivalent using `apt` instead of forcing a `pip` install.

## Proven Procedure

### 1. Identify Outdated Packages
To safely list packages that might be outdated without breaking the system:
```bash
pip3 list --outdated --format=freeze 2>/dev/null
```

### 2. Handling the "Externally Managed Environment" Error
If a `pip install` command fails with `error: externally-managed-environment`, **do not** use `--break-system-packages`. Instead, check if the
