---
name: cinnamon-btrfs-maintenance-optimization
description: Standardized procedure for safely performing Btrfs maintenance, including balancing (defragmenting/reclaiming space) and scrubbing (data integrity checks) on mounted partitions.
triggers: ["btrfs maintenance", "optimize btrfs drive", "btrfs scrub disk", "btrfs balance filesystem"]
---

# Btrfs Maintenance and Optimization

## Overview
This skill provides a reliable, non-destructive workflow for maintaining Btrfs filesystems. Btrfs requires periodic "scrubbing" to verify data integrity and "balancing" to reclaim space from unused chunks, especially when files are frequently deleted or modified. Unlike typical filesystem commands, Btrfs tools operate on the **mount point**, not the raw block device (e.g., `/dev/sdX1`).

## Proven Procedure

### 1. Identify Btrfs Mount Points
Before running maintenance, identify which partitions are Btrfs and where they are mounted.
```bash
lsblk -f | grep btrfs
```

### 2. Check Filesystem Usage
Run the usage command against the **mount point** (e.g., `/` or `/mnt/data`), not the `/dev/` node.
```bash
# Correct syntax:
sudo btrfs filesystem usage /mount/point
```

### 3. Perform a Scrub (Integrity Check)
Run a scrub to detect and repair data corruption. This can be done while the system is in use.
```bash
# Start a scrub in the background
sudo btrfs scrub start /mount/point

# Check the status of a running scrub
sudo btrfs scrub status /mount/point
```

### 4. Perform a Balance (Optimization)
A balance moves data chunks to free up space. Use `dusage` (data usage) or `musage` (metadata usage) filters to avoid unnecessary wear by only processing chunks that are partially full.
```bash
# Targeted balance (only reclaims chunks with < 30% usage)
sudo btrfs balance start -dusage=30 -musage=30 /mount/point

# Full balance (Use with caution, high I/O impact)
sudo btrfs balance start /mount/point
```

### 5. Verify Mount Options (Optional but Recommended)
To ensure optimal performance, verify that compression (e.g., `compress=zstd`) and `space_cache=v2` are enabled in `/etc/fstab`.
```bash
# Check current mount options
findmnt -T /mount/point
```

## Pitfalls & Troubleshooting
*   **"ERROR: not a btrfs filesystem":** Ensure you are pointing to the directory where the drive is mounted (e.g., `/`), not the block device (e.g., `/dev/sda1`).
*   **"Balance" High I/O:** Running a full balance on a near-full drive is extremely resource-intensive. Always use the `-dusage` flag first to reclaim space efficiently without unnecessary rewrites.
*   **Permission Denied:** Btrfs maintenance commands always require `sudo`.
