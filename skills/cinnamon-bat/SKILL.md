---
name: cinnamon-bat
description: Skill for bat
---

# bat Skill

This skill provides functionality for `bat`, a cat(1) clone with wings that visualizes syntax, git integration, and themes.

**Overview:**
- `bat` is a modern cat command replacement with syntax highlighting, Git integration, and themes
- Provides a more user-friendly way to view file contents in the terminal
- Part of the `bat` package on Debian/Ubuntu/MakuluLinux systems
- Can act as a pager for `less` and other commands

**Commands:**
- `bat <file>` - Display file contents with syntax highlighting
- `bat --theme <theme>` - Set color theme
- `bat --list-themes` - List available themes
- `bat --color always` - Always use colors
- `bat --plain` - Disable syntax highlighting
- `bat` can also be used as a pager: `bat file.txt | less`

**Usage examples:**
- View a file: `bat document.txt`
- View with theme: `bat --theme=OneHalfDark file.py`
- Check available themes: `bat --list-themes`
- Git integration shows changes: `bat file.py` when file is in a git repo

**Configuration:**
- `~/.config/bat/config` - Bat configuration file
- Theme files in `/usr/share/bat/themes/`
- Can set BAT_THEME environment variable
