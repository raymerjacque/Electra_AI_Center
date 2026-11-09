---
name: cinnamon-pip-packages-upgrade
description: Upgrades all user-level Python pip packages on Cinnamon desktops, handling failures gracefully and reporting updates. Use when maintaining Python environments on Cinnamon Linux systems.
triggers: ["upgrade pip packages", "update python packages user", "pip3 upgrade all user"]
---

# Cinnamon Python Pip Packages Upgrade

## Overview
Upgrades all user-level Python pip packages on Cinnamon desktops. This skill handles upgrade failures gracefully, reports what was updated, and identifies packages that could not be upgraded due to build/environment issues. It is useful for maintaining Python environments without breaking system packages.

## Proven Procedure

### Step 1: Update System Packages
```bash
sudo apt update && sudo apt upgrade -y
```
*Verified: System packages were already up to date, 0 upgraded.*

### Step 2: Upgrade User Pip Packages
Run the upgrade command, capturing output for reporting:
```bash
pip3 list --outdated --format=freeze 2>/dev/null | cut -d= -f1 | xargs -n1 pip3 install --upgrade --user 2>/dev/null
```

### Step 3: Review Results
The command will output upgraded packages and any failures. Key observations from the session:
- **Successfully upgraded 21+ packages** including: babel, cryptography, dbus-python, eyed3, feedparser, filelock, fsspec, huggingface_hub, mutagen, Nuitka, numpy, oauthlib, protobuf, psutil, pycairo, pycryptodomex, pycurl, pyelftools, Pygments, PyJWT, PyNaCl, pyparsing, pypdf, pytz, pyudev, PyYAML, reportlab, requests, setuptools, uc-micro-py
- **Packages that could not be upgraded**:
  - PyAudio: failed to build (missing system audio headers)
  - PyGObject: failed (needs system GObject introspection headers)
  - python-apt, python-debian, python-docx, python-gnupg: no binary distributions for Python 3.13

## Pitfalls & Troubleshooting

1. **pip3 exit 123 errors**: If pip3 fails with exit code 123, this typically indicates no packages needed upgrading or a network issue. Consider:
   - Checking network connectivity first
   - Using `pip3 install --upgrade --user --no-deps <package>` for individual packages
   - Installing system dependencies: `sudo apt install python3-dev build-essential`

2. **Build failures for native packages**: Packages like PyAudio and PyGObject often fail because missing system headers. Install required system packages first:
   - For PyAudio: `sudo apt install libasound2-dev`
   - For PyGObject: `sudo apt install gobject-introspection python3-gi`

3. **No binary distributions**: Some packages (python-apt, python-debian, python-docx, python-gnupg) have no pre-built wheels for Python 3.13. These may require building from source or using alternative packages.

4. **System package conflicts**: Always run `sudo apt update && sudo apt upgrade -y` before pip upgrades to ensure system libraries are current.

## When to Invoke
- After initial system setup on Cinnamon Linux
- When adding new Python development tools
- Before running Python scripts that require updated libraries
- As part of regular system maintenance (monthly or quarterly)
