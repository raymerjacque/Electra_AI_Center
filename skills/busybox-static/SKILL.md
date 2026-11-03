---
name: busybox-static
description: Skill for busybox-static
---

# busybox-static Skill

This skill provides functionality for `busybox-static`, a collection of many common Unix utilities into a single executable.

**Overview:**
- `busybox-static` combines tiny versions of many standard Unix utilities (ls, cp, mv, cat, etc.) into a single small executable
- Designed for embedded systems and minimal installations
- Part of the `busybox` package on Debian/Ubuntu systems
- The static version provides all utilities without dynamic library dependencies

**Commands:**
- `busybox <command>` - Run a specific busybox utility
- `busybox ls` - List files
- `busybox cp` - Copy files
- `busybox cat` - Display file contents
- `busybox ping` - Ping network hosts
- `busybox wget` - Download files
- `busybox vi` - Text editor

**Usage examples:**
- Minimal system: `busybox ls -la`
- Download file: `busybox wget http://example.com/file`
- Text editing: `busybox vi file.txt`

**Package purpose:**
- Provides essential Unix utilities in a single small binary
- Ideal for embedded systems, rescue disks, and minimal Linux installations
