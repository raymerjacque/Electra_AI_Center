---
name: aspell-en
description: Skill for aspell-en (English word list for aspell)
---

# aspell-en Skill

This skill provides functionality for `aspell-en`, the English word list package for the aspell spell checker.

**Overview:**
- `aspell-en` contains the English dictionary for use with the aspell spell checker
- Provides comprehensive English vocabulary for spell checking
- Part of the `aspell-en` package on Debian/Ubuntu systems
- Required for English language spell checking with aspell

**Commands:**
- `aspell -d en_US` - Use the English dictionary (automatically loaded from aspell-en)
- `aspell -l` - List available languages (will show `en_US` after installing aspell-en)
- `aspell check <file>` - Spell check a file with English dictionary

**Usage examples:**
- Install: `apt-get install aspell-en`
- Check a file: `aspell check document.txt`
- Set English dictionary: `aspell -d en_US check document.txt`

**Note:**
- The `aspell-en` package must be installed separately from `aspell` for English spell checking to work
