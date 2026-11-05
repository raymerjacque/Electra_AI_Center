---
name: cinnamon-ventoy-install
description: Downloads, installs, and integrates the Ventoy bootable USB tool into the system and Cinnamon application menu.
triggers: ["install ventoy", "setup ventoy", "add ventoy"]
---

# Cinnamon: Install and Integrate Ventoy

## Overview
Ventoy is not typically available in standard Debian/Ubuntu repositories. This skill automates the process of fetching the official release from GitHub, installing it into `/opt`, setting up system-wide symlinks, and creating a `.desktop`
