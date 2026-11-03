---
name: bubblewrap
description: Skill for bubblewrap
---

# bubblewrap Skill

This skill provides functionality for `bubblewrap`, an unprivileged sandboxing tool for Linux.

**Overview:**
- `bubblewrap` (bwrap) is a tool for creating unprivileged sandboxes
- Used to run applications in isolated environments without root privileges
- Part of the `bubblewrap` package on Debian/Ubuntu systems
- Commonly used by Flatpak and other container technologies

**Commands:**
- `bwrap` - Run a command in a bubblewrap sandbox
- `bwrap --ro-bind <src> <dst>` - Bind mount a directory read-only
- `bwrap --bind <src> <dst>` - Bind mount a directory read-write
- `bwrap --proc <path>` - Mount proc filesystem
- `bwrap --dev <path>` - Mount dev filesystem
- `bwrap --unshare-all` - Unshare all namespaces
- `bwrap --die-with-parent` - Die when parent process dies

**Usage examples:**
- Simple sandbox: `bwrap --ro-bind / / --proc /proc --dev /dev -- /bin/sh`
- With writable tmp: `bwrap --ro-bind / / --proc /proc --dev /dev --tmpfs /tmp -- /bin/sh`
- Flatpak uses bubblewrap internally for application sandboxing

**Package purpose:**
- Provides unprivileged user namespace sandboxing
- Essential for Flatpak application isolation
- Lightweight alternative to full container runtimes
