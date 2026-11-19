---
name: cinnamon-docker-installation
description: Install Docker engine via APT on Debian-based systems, resolve snap package conflicts, configure non-root user permissions, and verify functionality.
triggers: ["install docker", "setup docker", "docker engine", "docker.io"]
---

# Docker Installation & Setup

## Overview
This skill handles the installation of Docker on Debian-based systems (like MakuluLinux), bypassing broken Snap alternatives in favor of the reliable native APT package (`docker.io`), configuring user group permissions, and verifying daemon status.

## Proven Procedure
1. Check if Docker is already installed or if conflicting snap packages exist:
   ```bash
   snap list | grep docker
   dpkg -l | grep docker
   ```
2. Remove conflicting snap versions if present:
   ```bash
   sudo snap remove docker
   ```
3. Update package lists and install the native APT package:
   ```bash
   sudo apt update
   sudo apt install docker.io -y
   ```
4. Start and enable the Docker service:
   ```bash
   sudo systemctl enable --now docker
   ```
5. Add the current user to the `docker` group to run commands without `sudo`:
   ```bash
   sudo usermod -aG docker $USER
   ```
6. Verify the installation (requires a new shell session or `newgrp docker`):
   ```bash
   newgrp docker
   docker run hello-world
   ```

## Pitfalls & Troubleshooting
- **Snap Profile Timeouts:** The Snap version of Docker can sometimes fail with confinement or system profile timeout errors on custom kernels. Always fall back to the native APT package (`docker.io`).
- **Permission Denied (`/var/run/docker.sock`):** If running `docker` commands fails with permission errors, ensure the user has been added to the `docker` group and the group session has been refreshed using `newgrp docker`.
