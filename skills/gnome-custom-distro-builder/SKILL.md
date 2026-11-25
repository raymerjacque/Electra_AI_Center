---
name: gnome-custom-distro-builder
description: Guide and scripts to create a custom Ubuntu LTS Linux distribution with GNOME tailored for beginners using Cubic.
triggers: ["crear distribucion linux", "custom linux distro", "ubuntu lts gnome", "crear iso ubuntu", "cubic iso builder"]
---

# GNOME Custom Linux Distribution Builder

## Overview
This skill provides templates, package lists, and procedures for creating a beginner-friendly custom Ubuntu LTS Linux distribution featuring the GNOME desktop environment using tools like Cubic (Custom Ubuntu ISO Creator).

## Proven Procedure
1. Create a workspace directory for the custom distribution files.
2. Define a list of beginner-friendly software packages (`packages.list`).
3. Prepare configuration scripts for GNOME settings (`gnome-settings.sh`).
4. Use **Cubic** (Custom Ubuntu ISO Creator) to load an official Ubuntu LTS ISO, chroot into the environment, install the packages, apply the configurations, and generate the final ISO.

## Pitfalls & Troubleshooting
- Ensure you have enough disk space (at least 20GB free) when building ISOs with Cubic.
- Verify that the target Ubuntu LTS version matches the base ISO used in Cubic.
