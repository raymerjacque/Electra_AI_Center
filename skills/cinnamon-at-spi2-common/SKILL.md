---
name: cinnamon-at-spi2-common
description: Skill for at-spi2-common
---

# at-spi2-common Skill

This skill provides information about `at-spi2-common`, which contains common files for the Assistive Technology Service Provider Interface (AT-SPI) version 2.

**Overview:**
- `at-spi2-common` provides the common files used by the AT-SPI2 (Assistive Technology Service Provider Interface) framework
- AT-SPI2 is a D-Bus based accessibility framework that allows assistive technologies to interact with desktop applications
- Part of the GNOME accessibility infrastructure on Linux
- Essential for screen readers and other accessibility tools to work properly

**Usage:**
- The framework runs automatically in the background via D-Bus
- Assistive technologies like Orca screen reader connect via D-Bus to access application interfaces
- No command-line tools needed for typical usage
- Part of the core GNOME/Cinnamon desktop accessibility stack

**Package purpose:**
- Provides the shared data and configuration files needed by at-spi2-core and other AT-SPI2 components
- Architecture-independent files that work on all CPU types
- Part of the Debian/Ubuntu GNOME/Cinnamon desktop integration
