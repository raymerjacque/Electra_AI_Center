---
name: 7zip
description: Skill for 7zip file archiver
---

# 7zip Skill

This skill provides functionality for the 7zip file archiver on Linux systems.

**Commands:**
- `7z` - Main 7zip command line tool for creating, extracting, and managing archives
- `7z a <archive> <files>` - Create a new 7z archive
- `7z x <archive>` - Extract archive
- `7z l <archive>` - List contents of archive
- `7z t <archive>` - Test archive integrity

**Usage examples:**
- Create archive: `7z a archive.7z file1 file2`
- Extract archive: `7z x archive.7z`
- List contents: `7z l archive.7z`
- Add files to existing archive: `7z u archive.7z newfile.txt`
