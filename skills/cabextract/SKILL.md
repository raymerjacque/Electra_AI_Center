---
name: cabextract
description: Skill for cabextract
---

# cabextract Skill

This skill provides functionality for `cabextract`, a tool for extracting files from Microsoft Cabinet (.cab) archives.

**Overview:**
- `cabextract` extracts files from Microsoft Cabinet (.cab) archive files
- Cabinet files are used by Microsoft for software distribution and Windows installers
- Part of the `cabextract` package on Debian/Ubuntu systems
- Useful for extracting Windows driver files, fonts, and other resources from .cab archives

**Commands:**
- `cabextract <archive.cab>` - Extract all files from a cabinet archive
- `cabextract -d <directory> <archive.cab>` - Extract to a specific directory
- `cabextract -l <archive.cab>` - List contents of a cabinet archive
- `cabextract -F <pattern> <archive.cab>` - Extract only files matching pattern

**Usage examples:**
- Extract all: `cabextract driver.cab`
- List contents: `cabextract -l archive.cab`
- Extract to directory: `cabextract -d /tmp/extract archive.cab`
- Extract specific files: `cabextract -F "*.dll" archive.cab`

**Package purpose:**
- Provides extraction support for Microsoft Cabinet archive format
- Useful for accessing Windows software components on Linux
