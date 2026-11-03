---
name: binutils
description: Skill for binutils
---

# binutils Skill

This skill provides functionality for `binutils`, the collection of binary utilities for the GNU assembler, linker, and other tools.

**Overview:**
- `binutils` is a collection of binary tools for the GNU toolchain
- Includes `as` (assembler), `ld` (linker), `objdump`, `readelf`, `size`, `nm`, and many others
- Essential for compiling and linking programs on Linux systems
- Part of the `binutils` package on Debian/Ubuntu systems

**Commands:**
- `as` - Assembler for machine code
- `ld` - Linker for object files
- `objdump` - Display information from object files
- `readelf` - Display information about ELF files
- `size` - Show section sizes of object files
- `nm` - List symbols from object files
- `strip` - Remove symbols and debugging information from object files

**Usage examples:**
- Compile assembly: `as file.s -o file.o`
- Link object files: `ld file.o -o program`
- Inspect ELF: `readelf -h program`
- Check symbols: `nm file.o`
- Show section sizes: `size program`

**Package purpose:**
- Core development tools for compiling software
- Required for building C/C++ programs and many other languages
- Provides the GNU assembler and linker
