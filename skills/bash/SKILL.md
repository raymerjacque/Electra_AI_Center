---
name: bash
description: Skill for bash
---

# bash Skill

This skill provides functionality for bash (Bourne Again SHell), the default shell on most Linux systems including Debian/Ubuntu/MakuluLinux.

**Overview:**
- bash is the GNU Bourne Again SHell, an sh-compatible shell with extensive features
- It's the default login shell for most Linux users
- Provides command line editing, history, job control, and programmable completion
- Part of the core system on virtually all Linux distributions

**Commands:**
- `bash` - Start a bash shell
- `bash -c "command"` - Execute a command and exit
- `bash -i` - Enter interactive mode
- `exit` - Exit the current shell
- `cd <directory>` - Change directory
- `pwd` - Print working directory
- `ls` - List directory contents
- `man <page>` - Show manual page

**Usage examples:**
- Basic command execution: `ls -la`
- Navigate directories: `cd /home/user`
- View history: `history`
- Run last command: `!!`
- Tab completion: Type part of a command/file and press Tab

**Configuration:**
- `~/.bashrc` - Per-user bash configuration
- `~/.bash_profile` - Login shell configuration
- `/etc/bash.bashrc` - System-wide bash configuration
- PS1 - Customize the prompt
