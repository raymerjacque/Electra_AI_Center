---
name: cinnamon-docker-containerd-repair
description: Fixes systemd service failures for Docker and containerd caused by corrupted or stale state directories.
triggers: ["docker-failed-to-start", "containerd-failed-to-start", "docker-service-crash", "repair-docker-daemon"]
---

# Docker and Containerd Service Repair

## Overview
This skill resolves situations where `docker.service` or `containerd.service` repeatedly fail to start upon system boot or manual invocation. This is frequently caused by a corrupted or stale state directory in `/var/lib/containerd` preventing the container runtime from initializing correctly.

## Proven Procedure
If Docker services are failing to start, perform these steps to clean the state and force a clean initialization:

1.  **Stop the services to ensure no processes are holding locks:**
    ```bash
    sudo systemctl stop docker
    sudo systemctl stop containerd
    ```

2.  **Backup and remove the problematic state directory:**
    *Moving the directory is safer than deleting it directly, allowing for recovery if needed.*
    ```bash
    sudo mv /var/lib/containerd /var/lib/containerd.bak
    ```

3.  **Restart the services:**
    *This forces containerd and Docker to recreate the necessary state files from scratch.*
    ```bash
    sudo systemctl start containerd
    sudo systemctl start docker
    ```

4.  **Verify status:**
    ```bash
    sudo systemctl status containerd docker
    ```

## Pitfalls & Troubleshooting
*   **Data Loss:** Moving the directory (`/var/lib/containerd`) effectively resets the container state on the host. While images remain, existing containers might need to be recreated or restarted.
*   **Persistent Failures:** If the services still fail, check for conflicting configurations in `/etc/docker/daemon.json`.
*   **AppArmor:** Ensure that AppArmor profiles are not blocking the docker-default profile (check `dmesg | grep apparmor`).
