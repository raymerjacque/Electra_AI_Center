---
name: cinnamon-system-pip-updates
description: Updates system packages and user pip packages on Cinnamon desktops, handling common pip upgrade failures due to missing system dependencies or package name mismatches.
triggers: ["sudo apt update && sudo apt upgrade -y", "pip3 list --outdated", "pip3 install --upgrade --user"]
---

# System Package and Pip User Updates (Cinnamon)

## Overview
This skill performs full system package updates on MakuluLinux Cinnamon and upgrades user-installed pip packages. It handles common pip upgrade failures by detecting when a pip package name is mangled (e.g., `dbus-python` → `dbus-python3`) or when a required system build dependency is missing, and falls back to the system package manager (apt) for those components.

## Proven Procedure

### 1. Update System Packages
```bash
sudo apt update && sudo apt upgrade -y
```
*All system packages are already up to date (0 upgraded, 0 installed, 0 removed).*

### 2. Upgrade User Pip Packages
Run the standard upgrade command:
```bash
pip3 list --outdated --format=freeze 2>/dev/null | cut -d= -f1 | xargs -n1 pip3 install --upgrade --user 2>/dev/null
```

### 3. Handle Pip Upgrade Failures
If pip install fails (e.g., `ERROR: Could not find a version that satisfies the requirement dbus-python3`), take the following steps:

**For `dbus-python`:**
- The pip package name may be mangled. Install the system package instead:
  ```bash
  sudo apt install python3-dbus -y
  ```
- Verify the system package is at the latest apt version (1.4.0-1 on this system).

**For `pycairo`:**
- If pip install fails due to missing Cairo dependencies, install the system build dependency first:
  ```bash
  sudo apt install libcairo2-dev -y
  pip3 install --user --break-system-packages pycairo
  ```

**For `python3-gi` / `PyGObject`:**
- If pip upgrade fails due to missing `girepository-2.0` pkg-config file, install the system package:
  ```bash
  sudo apt install python3-gi -y
  ```

### 4. Report Updated Packages
After upgrades, list what was successfully updated:
- `pycairo`: Successfully upgraded from 1.27.0 → 1.29.2 (installed via pip --user --break-system-packages after installing libcairo2-dev build dependency).
- `dbus-python` (1.4.0 → 1.5.1): Could not upgrade via pip — package name mangled to "dbus-python3" which doesn't exist on PyPI. System package `python3-dbus` is already at latest apt version (1.4.0-1).
- `PyGObject` (3.50.0 → 3.58.1): Could not upgrade via pip — missing `girepository-2.0` pkg-config file (not provided by libgirepository1.0-dev on this system). System package `python3-gi` is already at latest apt version (3.50.0-4+b1).

The two remaining packages are at their latest versions available via the system package manager (apt).

## Pitfalls & Troubleshooting

| Issue | Resolution |
|-------|------------|
| `ERROR: Could not find a version that satisfies the requirement dbus-python3` | `dbus-python` is not available on PyPI under that name. Install via apt: `sudo apt install python3-dbus -y` |
| `ERROR: You must give at least one requirement to install` | Ensure `pip3 list --outdated` returns at least one package; the `xargs` command may pass an empty list if no packages are outdated. |
| `pycairo` install fails with missing `libcairo2-dev` | Install the build dependency first: `sudo apt install libcairo2-dev -y` then retry `pip3 install --user --break-system-packages pycairo` |
| `PyGObject` upgrade fails with `girepository-2.0` missing | Install system package: `sudo apt install python3-gi -y`. Pip upgrade is not required; the system package is already at the latest version. |
| `pip3 install --upgrade --user` hangs or errors on other packages | Try `pip3 install --user --break-system-packages <package>` or fall back to `apt` for system-managed Python packages. |
