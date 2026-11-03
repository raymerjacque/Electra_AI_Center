---
name: amd64-microcode
description: Skill for AMD64 microcode
---

# amd64-microcode Skill

This skill provides functionality for the AMD64 microcode update on Linux systems.

**Overview:**
- AMD64 microcode (CPU firmware) updates security vulnerabilities and stability issues
- Automatically applied by the kernel at boot time
- Part of the `amd64-microcode` package on Debian/Ubuntu systems
- Also available as `intel-microcode` for Intel CPUs

**Commands:**
- `grep microcode /var/log/dmesg` - Check microcode loading at boot
- `dmesg | grep microcode` - Verify microcode is loaded
- `apt-cache policy amd64-microcode` - Check package version
- `apt-get install amd64-microcode` - Install/upgrade microcode

**Usage:**
- Microcode updates are applied automatically during system boot
- No manual intervention typically needed
- Check `dmesg` after boot to verify microcode is loaded
- Keep system updated with `apt update && apt upgrade` to get latest microcode
