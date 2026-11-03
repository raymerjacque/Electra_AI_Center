---
name: aptitude
description: Skill for aptitude (advanced package manager)
---

# aptitude Skill

This skill provides functionality for `aptitude`, an advanced text-based package manager for Debian/Ubuntu systems.

**Overview:**
- `aptitude` is a curses-based (text UI) and command-line package manager
- Offers more features than `apt` including pattern-based package selection
- Handles complex dependency resolution and offers interactive conflict resolution
- Part of the `aptitude` package on Debian/Ubuntu systems

**Commands:**
- `aptitude update` - Refresh package index from repositories
- `aptitude upgrade` - Upgrade all installed packages
- `aptitude install <package>` - Install a new package
- `aptitude remove <package>` - Remove an installed package
- `aptitude search <term>` - Search for packages matching a term
- `aptitude show <package>` - Show package information
- `aptitude purge <package>` - Remove package and configuration files
- `aptitude why <package>` - Explain why a package is installed
- `aptitude why-not <package>` - Explain why a package cannot be installed
- `aptitude autoclean` - Clean old .deb packages

**Usage:**
- `aptitude` offers an interactive menu interface (press `i` to install, `u` to upgrade, etc.)
- Command-line usage similar to `apt` but with additional options
- Better at handling tricky dependency situations
- Can operate in non-interactive mode with `-q` flag

**Configuration:**
- Similar to `apt` configuration in `/etc/apt/sources.list`
- Profile management available for saving/loading package states
