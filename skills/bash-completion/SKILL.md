---
name: bash-completion
description: Skill for bash-completion
---

# bash-completion Skill

This skill provides functionality for bash-completion, which adds tab completion capabilities to the bash shell.

**Overview:**
- bash-completion provides additional tab completion for commands, options, and arguments in bash
- Makes using the command line faster and reduces typos
- Part of the `bash-completion` package on Debian/Ubuntu systems
- Automatically loads for bash on most modern distributions

**Usage:**
- Tab completion is automatic - start typing a command and press Tab
- Completes commands, options, filenames, package names, service names, etc.
- Works with most commands including apt, systemctl, docker, etc.
- Can be disabled by sourcing /etc/profile.d/bash-completion.sh or removing the package

**Configuration:**
- `/etc/profile.d/bash-completion.sh` - System-wide bash completion setup
- `~/.bash_completion` - User-specific bash completion
- Can be tested with: `complete -C '/usr/bin/aws_completer' aws`
