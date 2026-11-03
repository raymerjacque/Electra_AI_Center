---
name: aspell
description: Skill for aspell (spell checker)
---

# aspell Skill

This skill provides functionality for `aspell`, a spell checker and replacement for ispell on Linux systems.

**Overview:**
- `aspell` is a free and open-source spell checker that provides better suggestions and faster performance than ispell
- Can be used interactively or as a filter for other programs
- Part of the `aspell` package on Debian/Ubuntu systems
- Supports multiple languages

**Commands:**
- `aspell -l` - List available languages
- `aspell -d <language>` - Set dictionary language (e.g., `aspell -d en_US`)
- `aspell check <file>` - Spell check a file interactively
- `aspell list` - Read words from stdin and output misspelled ones
- `aspell -a` - Interactive mode showing misspelled words with suggestions

**Usage examples:**
- Check a file: `aspell check document.txt`
- Set dictionary: `aspell -d en_US check document.txt`
- Filter misspelled words: `cat file.txt | aspell list`
- Interactive mode: `aspell -a`

**Language support:**
- Install additional dictionaries with: `apt-get install aspell-es` (Spanish), `apt-get install aspell-fr` (French), etc.
