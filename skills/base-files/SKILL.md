---
name: base-files
description: Skill for base-files
---

# base-files Skill

This skill provides information about `base-files`, which contains the fundamental filesystem and system configuration files for Debian/Ubuntu Linux systems.

**Overview:**
- `base-files` contains the essential system configuration files that define the Linux filesystem hierarchy
- Includes `/etc/passwd`, `/etc/group`, `/etc/debian_version`, and other fundamental system files
- Part of the core `base-files` package on Debian/Ubuntu systems
- Provides the foundation for the entire system's file structure

**Files included:**
- `/etc/passwd` - User account information
- `/etc/group` - Group membership information
- `/etc/debian_version` - Debian version information
- `/etc/hostname` - System hostname
- `/etc/motd` - Message of the day (displayed at login)
- `/etc/fstab` - File system mount points (sometimes included)
- `/etc/issue` - Login greeting text

**Usage:**
- System files are managed by the package manager and system administrators
- `/etc/passwd` and `/etc/group` can be viewed/edited with appropriate tools
- `/etc/debian_version` shows the current Debian version
- `/etc/motd` can be customized for login messages

**Package purpose:**
- Provides the fundamental filesystem configuration that all other packages depend on
- Architecture-independent core system files
- Part of the Debian base system installation
