---
name: apparmor
description: Skill for apparmor security module
---

# apparmor Skill

This skill provides functionality for AppArmor, a Linux security module that implements mandatory access control (MAC) through program-specific profiles.

**Overview:**
- AppArmor protects the system by confining programs to a limited set of resources
- Each program has a profile that describes what files and capabilities it can access
- Profiles can be enforced (strict) or complain (permissive/monitoring mode)
- Part of the `apparmor` package on Debian/Ubuntu systems
- Complements SELinux (which is more common on Red Hat systems)

**Commands:**
- `aa-status` - Show AppArmor status and enforced profiles
- `aa-disable <profile>` - Disable AppArmor for a specific profile
- `aa-enforce <profile>` - Enforce a specific profile
- `aa-complain <profile>` - Set profile to complain mode (logging only)
- `apparmor_parser` - Load or update profiles
- `ls -la /etc/apparmor.d/` - List available profiles

**Profile locations:**
- `/etc/apparmor.d/` - System profiles (e.g., firefox, chromium, firewalld)
- `/var/lib/apparmor/` - Profile state and cache

**Usage:**
- Most common profiles are pre-installed for popular applications
- Profiles can be customized by editing files in `/etc/apparmor.d/`
- Switch between complain and enforce modes for testing
- `aa-status` shows which processes are currently confined
