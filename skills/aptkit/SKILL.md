---
name: aptkit
description: Skill for aptkit
---

# aptkit Skill

This skill provides information about `aptkit`, which is a Python kit for working with apt packages programmatically.

**Overview:**
- `aptkit` is a Python library for working with apt packages programmatically
- Provides an API for package installation, removal, and information retrieval
- Useful for scripts and applications that need to manage packages
- Part of the `aptkit` package on Debian/Ubuntu systems

**Usage:**
- Import `aptkit` in Python scripts: `import aptkit`
- Use `aptkit.install('<package>')` to install packages
- Use `aptkit.remove('<package>')` to remove packages
- Use `aptkit.list_installed()` to list installed packages
- Good for automation scripts and custom package management tools

**Python example:**
```python
import aptkit

# Install a package
aptkit.install('vim')

# List installed packages
pkgs = aptkit.list_installed()
for pkg in pkgs:
    print(pkg)
```
