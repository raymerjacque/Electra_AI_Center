---
name: kde-appstream
description: Skill for appstream
---

# appstream Skill

This skill provides functionality for appstream, which provides a standard for describing application metadata and streamlining application discovery and installation on Linux desktops.

**Overview:**
- appstream provides a standardized format for describing application metadata (name, description, screenshots, categories, etc.)
- Part of the modern Linux desktop infrastructure (freedesktop.org specification)
- Replaces older .desktop file metadata standards
- Used by software centers, application menus, and package managers

**Commands:**
- `appstreamcli list -s <repo>` - List applications from a repository
- `appstreamcli validate -f <file.xml>` - Validate an appstream metadata file
- `grep -R 'com\.example' /usr/share/appdata/` - Search application data

**Usage:**
- Application stores (GNOME Software, KDE Discover, etc.) use appstream data
- Developers package their apps with appstream.xml metadata
- Part of the freedesktop.org specification for application discovery
- Metadata files typically located in `/usr/share/appdata/`

**Format:**
- XML-based format following the Application Stream specification
- Includes name, summary, description, screenshots, URL, and category information
