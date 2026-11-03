---
name: bsdutils
description: Skill for bsdutils
---

# bsdutils Skill

This skill provides functionality for `bsdutils`, a collection of basic utility programs derived from 4.4BSD.

**Overview:**
- `bsdutils` contains basic system utility programs derived from the 4.4BSD operating system
- Includes essential tools for system administration and file management
- Part of the `bsdutils` package on Debian/Ubuntu/MakuluLinux systems
- Provides fundamental utilities that complement the GNU coreutils

**Commands:**
- `df` - Show disk free space (BSD version)
- `dmesg` - Display kernel ring buffer (often included)
- `last` - Show login history (sometimes included)
- `wall` - Write message to all users
- `cal` - Display calendar
- `who` - Show who is logged in
- `w` - Show who is logged in and what they are doing

**Usage examples:**
- Check disk space: `df -h`
- View system messages: `dmesg`
- Send message to all users: `wall "System maintenance"`
- Check calendar: `cal`
- View logged-in users: `who`

**Package purpose:**
- Provides BSD-derived system utilities
- Complements GNU coreutils with BSD-style implementations
- Essential system administration tools on Debian/Ubuntu systems
