---
name: apt-utils
description: Skill for apt-utils
---

# apt-utils Skill

This skill provides functionality for `apt-utils`, a collection of utility programs for the apt package management system.

**Overview:**
- `apt-utils` contains various utility programs that complement the main `apt` command
- Provides additional functionality for package management tasks
- Part of the `apt-utils` package on Debian/Ubuntu systems

**Commands:**
- `apt-get -h` - Show help (includes apt-utils utilities)
- `apt-ftparchive` - Generate package indexes for apt repositories
- `dpkg-deb` - Install, unpack, and information about .deb packages
- `dpkg-query` - Query dpkg database (often used by apt-utils)
- `apt-cache` - Query apt cache (some functions overlap)

**Usage examples:**
- Check package availability: `apt-cache show <package>`
- Inspect .deb packages: `dpkg-deb -I <package>.deb`
- Extract .deb packages: `dpkg-deb -x <package>.deb <target-dir>`

**Utility functions:**
- Package information and verification
- Repository index generation
- .deb package manipulation
- Dependency and version querying
