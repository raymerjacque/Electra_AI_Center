---
name: bc
description: Skill for bc
---

# bc Skill

This skill provides functionality for `bc`, an arbitrary precision calculator language.

**Overview:**
- `bc` is a command-line calculator that supports arbitrary precision numbers
- Has a math mode with standard mathematical functions
- Can be used interactively or in shell scripts
- Part of the `bc` package on Debian/Ubuntu systems

**Commands:**
- `bc` - Start the bc interactive calculator
- `echo "scale=5; 22/7" | bc` - Calculate with scale (precision)
- `bc <<< "10 + 5"` - Calculate using here-string
- `man bc` - Show bc manual page

**Usage examples:**
- Simple calculation: `echo "2 + 3" | bc` → 5
- With scale/precision: `echo "scale=3; 1/3" | bc` → .333
- Square root: `echo "sqrt(16)" | bc` → 4
- Programmatic use in scripts: `result=$(echo "2^10" | bc)`

**Configuration:**
- `bc` supports mathematical functions like `s` (sine), `c` (cosine), `a` (arctangent), `l` (natural log)
- `scale` variable controls the number of decimal places
