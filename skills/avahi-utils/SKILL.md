---
name: avahi-utils
description: Skill for avahi-utils
---

# avahi-utils Skill

This skill provides functionality for `avahi-utils`, a collection of utility commands for the Avahi mDNS/DNS-SD suite.

**Overview:**
- `avahi-utils` contains various command-line tools for querying and controlling the Avahi mDNS/DNS-SD daemon
- Works alongside `avahi-daemon` for service discovery on local networks
- Part of the `avahi-utils` package on Debian/Ubuntu systems

**Commands:**
- `avahi-browse _services._tcp.local` - Browse services on the local network
- `avahi-resolve -n hostname.local` - Resolve a hostname to an IP address
- `avahi-info hostname.local` - Get information about a local host
- `avahi-send -r` - Send a signal to the avahi daemon
- `avahi-domainname` - Get the current domain name
- `avahi-publish -s "service name" _service._tcp.local` - Publish a service

**Usage examples:**
- Browse local services: `avahi-browse _services._tcp.local`
- Resolve a hostname: `avahi-resolve mycomputer.local`
- Get host information: `avahi-info mycomputer.local`
- Publish a custom service: `avahi-publish -s "MyService" _workstation._tcp.local`

**Package purpose:**
- Provides command-line utilities for interacting with and testing the Avahi mDNS/DNS-SD infrastructure
- Complements the avahi-daemon for network service discovery
