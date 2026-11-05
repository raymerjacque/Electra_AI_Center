---
name: pip-safe-upgrade
description: Safely upgrade user-level Python packages by ensuring build dependencies exist and filtering out problematic, system-managed packages.
triggers: ["update python packages", "fix pip upgrade error", "upgrade pip packages safely"]
---

# Pip Safe Upgrade & Dependency Management

## Overview
Upgrading Python packages via `pip` on Debian-based distributions (like MakuluLinux) often fails due to PEP 668 ("externally-managed-environment") or missing C-headers for compiled libraries (like `cairo` or `portaudio`). This skill provides a reliable workflow to identify missing build dependencies and perform safe batch upgrades while ignoring packages managed by the system (like `dbus-python`).

## Proven Procedure

### 1. Install Required Build Dependencies
Before running pip upgrades, ensure the system has the necessary compilation tools and headers. If pip fails with "missing header" or "failed to build wheel" errors, run:

```bash
sudo apt update
sudo apt install -y build-essential python3-dev pkg-config \
    libcairo2-dev libgire
