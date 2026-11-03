---
name: apg
description: Skill for apg (Automatic Password Generator)
---

# apg Skill

This skill provides functionality for `apg` (Automatic Password Generator), which generates random passwords for use on Linux systems.

**Overview:**
- `apg` generates random, pronounceable, or completely random passwords
- Useful for creating strong passwords for user accounts, services, or encryption
- Part of the `apg` package on Debian/Ubuntu systems
- Can generate passwords with various character sets and constraints

**Commands:**
- `apg` - Generate a random password interactively
- `apg -a 1` - Generate automatic password (default)
- `apg -a 2` - Generate completely random password
- `apg -a 3` - Generate pronounceable password
- `apg -a 4` - Generate password with custom characters
- `apg -m 12 -n 5` - Generate 5 passwords of 12 characters each
- `apg -x -m 8 -n 3` - Generate 3 passwords minimum 8 chars with special chars

**Usage examples:**
- Generate one password: `apg`
- Generate 5 passwords of 12 chars: `apg -m 12 -n 5`
- Generate pronounceable password: `apg -a 3`
- Generate with specific character set: `apg -a 4 -m 10 -n 2 -c 'abc123'`
