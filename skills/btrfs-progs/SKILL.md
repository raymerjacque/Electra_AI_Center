---
name: btrfs-progs
description: Skill for btrfs-progs
---

# btrfs-progs Skill

This skill provides functionality for `btrfs-progs`, the B-tree filesystem utilities for Linux systems.

**Overview:**
- `btrfs-progs` is the set of utilities and commands for managing Btrfs (B-tree filesystem) file systems
- Btris is a copy-on-write (CoW) filesystem designed for fault tolerance, repair, and easy administration
- Part of the `btrfs-progs` package on Debian/Ubuntu systems

**Commands:**
- `mkfs.btrfs` - Create a new Btrfs filesystem
- `mount -t btrfs <device> <mountpoint>` - Mount a Btrfs filesystem
- `btrfs filesystem show` - Show Btrfs filesystem information
- `btrfs filesystem df <mount>` - Show disk space usage
- `btrfs balance <mount>` - Balance data across devices
- `btrfs scrub <mount>` - Check and repair filesystem
- `btrfs subvolume create <path>` - Create a subvolume
- `btrfs send <path>` - Send a subvolume to a stream

**Usage examples:**
- Format a drive: `mkfs.btrfs /dev/sdx`
- Mount a filesystem: `mount -t btrfs /dev/sdx /mnt`
- Check filesystem: `btrfs scrub /mnt`
- Create subvolume: `btrfs subvolume create /mnt/mydir`

**Package purpose:**
- Essential tools for managing Btrfs filesystem on Linux systems
- Provides both command-line utilities and some GUI options
