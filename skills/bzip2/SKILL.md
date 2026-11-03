---
name: bzip2
description: Skill for bzip2
---

# bzip2 Skill

This skill provides functionality for `bzip2`, a high-quality data compression program.

**Overview:**
- `bzip2` is a free and open-source file compression program that uses the Burrows-Wheeler block sorting algorithm
- Provides better compression than gzip but at the cost of higher memory usage
- Part of the `bzip2` package on Debian/Ubuntu systems
- Creates .bz2 compressed files

**Commands:**
- `bzip2 <file>` - Compress a file (replaces original with .bz2)
- `bzip2 -d <file>` - Decompress a .bz2 file
- `bzip2 -k <file>` - Keep original file after compression
- `bzip2 -z <file>` - Compress a file
- `bunzip2 <file>` - Decompress a .bz2 file

**Usage examples:**
- Compress file: `bzip2 document.txt` → creates `document.txt.bz2`
- Decompress file: `bzip2 -d document.txt.bz2` → restores `document.txt`
- Keep original: `bzip2 -k document.txt` → keeps `document.txt` and creates `document.txt.bz2`
- List bzip2 version: `bzip2 -V`

**Package purpose:**
- Provides high-quality lossless data compression
- Often used for distributing software and archiving files
- Complements gzip with better compression ratio
