---
name: cinnamon-pip-upgrade-workaround
description: Upgrades user pip packages on Cinnamon/MakuluLinux systems where system Python is externally managed (PEP 668). Handles incompatibility of `pip3 list --outdated` with xargs and resolves dbus-python naming conflicts. Use when standard pip upgrade commands fail due to externally managed Python or missing PyPI packages.
triggers: ["pip3 upgrade fails with PEP 668 error", "pip3 list --outdated | xargs pip3 install upgrade fails", "upgrading pycairo or other system-critical Python packages on Cinnamon"]
---

# Cinnamon Pip Upgrade Workaround

## Overview
On Cinnamon (MakuluLinux) and other Debian/Ubuntu systems with externally managed Python (PEP 668), the standard `pip3 list --outdated --format=freeze | xargs -n1 pip3 install --upgrade --user` command fails. This skill provides a working approach to upgrade specific user pip packages while respecting system Python constraints. It identifies which packages can be upgraded via `--break-system-packages` flag and which are better installed via apt.

## Proven Procedure

### Step 1: Update system packages first
```bash
sudo apt update && sudo apt upgrade -y
```

### Step 2: Check for outdated user packages (suppress PEP 668 warning)
```bash
PIP_REQUIRE_VIRTUALENV= pip3 list --outdated --format=freeze 2>/dev/null | grep -v '^$' | cut -d= -f1
```

### Step 3: Upgrade specific packages with --break-system-packages
For packages that don't have a system equivalent or where pip upgrade is preferred:
```bash
PIP_REQUIRE_VIRTUALENV= pip3 install --upgrade --user --break-system-packages <package_name>
```

### Step 4: Verify apt alternatives first
Before using pip with `--break-system-packages`, check if the package is available via apt:
```bash
apt search <package_name>
```
If available, prefer `sudo apt install python3-<package_name>` instead.

### Step 5: Handle dbus-python naming conflict
The PyPI package `dbus-python` maps to system package `python3-dbus`. Do not attempt `pip3 install dbus-python` as it will fail with "version not found". Use the system package instead.

**Example - Upgrade pycairo:**
```bash
pip3 install --upgrade --user --break-system-packages pycairo
```

**Example - Verify python3-dbus is installed (provides dbus functionality):**
```bash
apt policy python3-dbus
```

### Step 6: List currently installed pip packages to confirm upgrades
```bash
pip3 list --format=columns 2>/dev/null | grep -i cairo
```

## Pitfalls & Troubleshooting

1. **"You must give at least one requirement to install" error**: 
   - Cause: `pip3 list --outdated` returns empty output when all packages are up to date
   - Fix: Check output first, or upgrade packages individually by name

2. **dbus-python3 not found on PyPI**:
   - The pip package name is mangled; the correct system package is `python3-dbus`
   - Never use `pip3 install dbus-python3` — it doesn't exist

3. **PyGObject / gir-repository errors**:
   - System package `python3-gi` provides GObject introspection
   - If missing: `sudo apt install python3-gi`
   - Do not attempt pip install for GI-related packages

4. **PEP 668 externally managed flag**:
   - System Python on MakuluLinux/Cinnamon is externally managed
   - Use `--break-system-packages` flag or set `PIP_REQUIRE_VIRTUALENV=`
   - Consider creating a virtual environment for isolated Python package management

5. **Package-specific build failures**:
   - Some packages require development headers (e.g., `libpango1.0-dev`, `libjpeg-dev`)
   - Install build dependencies: `sudo apt build-dep python3-<package_name>`
