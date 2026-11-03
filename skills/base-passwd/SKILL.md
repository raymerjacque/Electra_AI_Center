---
name: base-passwd
description: Skill for base-passwd
---

# base-passwd Skill

This skill provides information about `base-passwd`, which contains the Debian base system master password and group files.

**Overview:**
- `base-passwd` contains the essential system configuration files that define user accounts and groups
- Includes `/etc/passwd`, `/etc/group`, `/etc/shadow`, and `/etc/gshadow`
- Part of the core `base-passwd` package on Debian/Ubuntu systems
- Provides the foundation for user account management

**Files included:**
- `/etc/passwd` - User account information
- `/etc/group` - Group membership information
- `/etc/shadow` - Encrypted user passwords
- `/etc/gshadow` - Encrypted group passwords

**Usage:**
- System files are managed by the package manager and system administrators
- `/etc/passwd` and `/etc/group` can be viewed/edited with appropriate tools
- Use `vipw` to safely edit `/etc/passwd`
- Use `vigr` to safely edit `/etc/group`
