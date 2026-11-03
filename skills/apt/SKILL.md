---
name: apt
description: Skill for apt package manager
---

# apt Skill

This skill provides functionality for apt (Advanced Package Tool), the primary package management system on Debian/Ubuntu and derivative Linux distributions.

**Overview:**
- apt is the command-line tool for installing, updating, removing, and managing software packages
- Works with .deb packages and remote repositories
- Front-end to dpkg for higher-level package management operations
- Part of the core system on Debian/Ubuntu/MakuluLinux systems

**Commands:**
- `apt update` - Refresh package index from repositories
- `apt upgrade` - Upgrade all installed packages to latest versions
- `apt install <package>` - Install a new package
- `apt remove <package>` - Remove an installed package
- `apt search <term>` - Search for packages matching a term
- `apt show <package>` - Show package information and description
- `apt list --installed` - List installed packages
- `apt autoremove` - Remove automatically installed dependency packages
- `apt clean` - Remove downloaded package files from cache
- `apt full-upgrade` - Smart upgrade that handles dependency changes

**Usage examples:**
- Update and upgrade: `apt update && apt upgrade`
- Install package: `apt install vim`
- Search for package: `apt search text editor`
- Remove package: `apt remove firefox`
- Auto-remove dependencies: `apt autoremove`

**Configuration:**
- `/etc/apt/sources.list` - Repository configuration
- `/etc/apt/sources.list.d/` - Additional repository files
- `/etc/apt/apt.conf.d/` - APT configuration snippets
