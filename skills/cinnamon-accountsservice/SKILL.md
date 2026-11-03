---
name: cinnamon-accountsservice
description: Skill for accountsservice user management daemon
---

# accountsservice Skill

This skill provides functionality for the accountsservice daemon on Linux systems, which manages user account information.

**Overview:**
- accountsservice is a D-Bus daemon that provides user account information to the desktop
- It integrates with the system to provide user details, pictures, and metadata
- Commonly used by desktop environments like GNOME, Cinnamon, etc.

**Commands:**
- `loginctl list-users` - List all users managed by systemd
- `loginctl show-user <username>` - Show user information
- `busctl list` - List D-Bus services (look for accountsservice)
- `systemctl status accountsservice` - Check accountsservice status

**Usage:**
- The service automatically runs in the background
- User information is available via D-Bus to desktop applications
- No manual command needed for typical usage
