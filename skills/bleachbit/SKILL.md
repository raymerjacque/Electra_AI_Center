---
name: bleachbit
description: Skill for bleachbit
---

# bleachbit Skill

This skill provides functionality for `bleachbit`, a system cleaner that frees disk space and protects privacy.

**Overview:**
- `bleachbit` is a system cleaner that frees disk space and protects privacy by deleting cache, cookies, logs, and other unnecessary files
- Can clean system files and application caches for many popular programs
- Part of the `bleachbit` package on Debian/Ubuntu/MakuluLinux systems
- Provides both GUI and command-line interfaces

**Commands:**
- `bleachbit` - Launch the GUI cleaner
- `bleachbit <cleaner1> <cleaner2> ...` - Clean specific areas from command line
- `bleachbit --list-cleaners` - List available cleaners
- `bleachbit --clean system` - Clean system files
- `bleachbit --clean firefox chrome` - Clean browser caches

**Usage examples:**
- Clean all: `bleachbit --clean all`
- Clean system files: `bleachbit --clean system`
- Clean browser caches: `bleachbit --clean firefox chrome`
- List available cleaners: `bleachbit --list-cleaners`

**Configuration:**
- Cleaners are configured in `/usr/share/bleachbit/` directory
- Can select which cleaners to run via command line or GUI
- Safe to use - creates backups before cleaning when possible
