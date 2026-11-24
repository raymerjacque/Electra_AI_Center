---
name: system-temporary-user-account
description: Creates a temporary, non-persistent system user account that leaves minimal trace (no home directory, disabled login shell, no persistent files or logs).
triggers: ["create temp user", "temporary user account", "ephemeral user", "non persistent user", "no trace user"]
---

# Temporary Non-Persistent User Account Creation

## Overview
This skill covers the creation of a temporary, non-persistent system user account designed to leave minimal trace on the system (no home directory, disabled login shell, no mail spool, and non-interactive access).

## Proven Procedure
To create a clean, non-persistent system user without leaving a home directory or active login shell:

```bash
# Create a system user with no home directory and nologin shell
sudo useradd --system --no-create-home --shell /usr/sbin/nologin --home-dir /nonexistent tempuser-temp
```

To clean up and remove the user completely afterwards:
```bash
sudo userdel tempuser-temp
```

## Pitfalls & Troubleshooting
- **Home Directory Creation:** Avoid using standard `useradd username` without flags, as it populates `/home/username` and creates persistent state. Use `--system` and `--no-create-home` (`-M`).
- **Login Shell:** Always set the shell explicitly to `/usr/sbin/nologin` or `/bin/false` to prevent interactive shell access.
