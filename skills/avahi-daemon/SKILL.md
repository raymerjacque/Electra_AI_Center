---
name: avahi-daemon
description: Skill for avahi-daemon
---

# avahi-daemon Skill

This skill provides functionality for `avahi-daemon`, which is the mDNS/DNS-SD (Multicast DNS/Domain Name System Service Discovery) daemon for the Avahi suite.

**Overview:**
- `avahi-daemon` implements the mDNS (Multicast DNS) and DNS-SD (DNS-Based Service Discovery) specifications
- Allows programs to publish and discover services and hosts on a local network without a central DNS server
- Part of the `avahi-daemon` package on Debian/Ubuntu systems
- Essential for zero-configuration networking on Linux desktops

**Commands:**
- `systemctl start avahi-daemon` - Start the avahi daemon
- `systemctl stop avahi-daemon` - Stop the avahi daemon
- `systemctl restart avahi-daemon` - Restart the avahi daemon
- `systemctl status avahi-daemon` - Check avahi daemon status
- `avahi-browse _services._tcp.local` - Browse services on the local network
- `avahi-resolve -n hostname.local` - Resolve a hostname to an IP address

**Usage:**
- Automatically enables hostname resolution on local network (e.g., `computer.local`)
- Allows service discovery (e.g., printing, file sharing, media streaming)
- Works with NetworkManager to configure automatically
- Browse local services: `avahi-browse _workstation._tcp.local`
- Resolve a host: `avahi-resolve mycomputer.local`

**Configuration:**
- Main config: `/etc/avahi/avahi-daemon.conf`
- Automatically starts with NetworkManager or can be started manually with systemctl
- Essential for AirPlay, Chromecast, and other mDNS-based discovery on local networks
