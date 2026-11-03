---
name: apt-file
description: Skill for apt-file (search package contents)
---

# apt-file Skill

This skill provides functionality for `apt-file`, which searches for files within packages even if the packages are not installed.

**Overview:**
- `apt-file` is a complement to `apt` for finding which package provides a specific file
- Useful when you know you need a certain file/program but don't know which package contains it
- Part of the `apt-file` package on Debian/Ubuntu systems
- Must run `apt-file update` first to refresh the file database

**Commands:**
- `apt-file update` - Download and install the package file database
- `apt-file search <filename>` - Search which package provides a file
- `apt-file list <package>` - List all files provided by a package
- `apt-file install <package>` - Install a package via apt-file (deprecated, use apt)

**Usage examples:**
- Find which package contains `vim`: `apt-file search /usr/bin/vim`
- List all files in `vim` package: `apt-file list vim`
- Search for a Python module: `apt-file search numpy.py`

**Setup:**
- First time: run `apt-file update` to download the package database
- Then use `apt-file search` to find packages by filename
