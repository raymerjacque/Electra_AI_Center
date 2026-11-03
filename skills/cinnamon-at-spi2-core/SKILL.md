---
name: cinnamon-at-spi2-core
description: Skill for at-spi2-core
---

# at-spi2-core Skill

This skill provides functionality for `at-spi2-core`, which contains the core implementation of the Assistive Technology Service Provider Interface (AT-SPI) version 2.

**Overview:**
- `at-spi2-core` is the core component of the AT-SPI2 (Assistive Technology Service Provider Interface) framework
- Provides the D-Bus daemon and implementation that assistive technologies communicate with
- Part of the GNOME accessibility infrastructure on Linux
- Essential for screen readers (like Orca) and other accessibility tools to interact with desktop applications

**Commands:**
- `at-spi-bus-launch --domain` - Launch the AT-SPI2 bus (usually not needed manually)
- `ls -la /usr/lib/at-spi2/` - List AT-SPI2 core components
- `dbus-send --system --dest=org.a11y.Bus /org/a11y/Bus org.a11y.Bus.ListObjects` - Query the AT-SPI2 bus

**Usage:**
- The AT-SPI2 core runs automatically in the background via the system D-Bus session
- Assistive technologies connect to the D-Bus to discover and interact with application accessibility trees
- No manual command needed for typical usage
- Part of the core GNOME/Cinnamon desktop accessibility stack

**Package purpose:**
- Provides the main AT-SPI2 daemon and implementation files
- Works alongside at-spi2-common to provide complete accessibility support
- Part of the Debian/Ubuntu GNOME/Cinnamon desktop integration
