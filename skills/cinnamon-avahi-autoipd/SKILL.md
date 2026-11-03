---
name: cinnamon-avahi-autoipd
description: Skill for avahi-autoipd
---

# avahi-autoipd Skill

This skill provides functionality for `avahi-autoipd`, which is the IPv4LL (Link Local) address configuration daemon for the Avahi mDNS/DNS-SD suite.

**Overview:**
- `avahi-autoipd` implements IPv4LL (Internet Protocol Version 4 Link Local) addressing as defined in RFC 3927
- Provides automatic private IP address configuration when no DHCP server is available
- Part of the `avahi-autoipd` package on Debian/Ubuntu systems
- Works alongside avahi-daemon for mDNS and DNS-SD services

**Commands:**
- `avahi-autoipd -D` - Run in background as daemon
- `avahi-autoipd -t` - Test the IPv4LL configuration
- `avahi-autoipd -k` - Kill running instance
- `avahi-autoipd -4` - Use IPv4 only

**Usage:**
- Automatically runs when a network interface is configured without a DHCP server
- Provides APIPA (Automatic Private IP Addressing) addresses in the 169.254.0.0/16 range
- Works alongside avahi-daemon for service discovery on local networks
- No manual intervention typically needed on modern systems with NetworkManager

**Configuration:**
- Works with NetworkManager to provide IPv4LL addressing
- Can be configured in `/etc/avahi/avahi-autoipd.conf`
- Typically enabled automatically on interfaces set to DHCP
