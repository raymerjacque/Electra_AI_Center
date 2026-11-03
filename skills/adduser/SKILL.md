---
name: adduser
description: Skill for adduser command
---

# adduser Skill

This skill provides functionality for the `adduser` command on Linux systems, which is a friendly interface for adding users to the system.

**Overview:**
- `adduser` is a friendly wrapper around `useradd` that asks interactive questions
- Part of the `adduser` package on Debian/Ubuntu systems
- Creates home directories, sets up defaults, and configures the new user

**Commands:**
- `adduser <username>` - Add a new user interactively
- `adduser <username> <group>` - Add user to a specific group
- `adduser --system <username>` - Create a system user
- `adduser <username> --ingroup <group>` - Add user to existing group
- `adduser <username> --shell /bin/zsh` - Create user with specific shell

**Usage examples:**
- Add new user: `adduser john`
- Add system user: `adduser --system john`
- Add user with custom shell: `adduser john --shell /bin/zsh`
- Add user to group: `adduser john sudo`
