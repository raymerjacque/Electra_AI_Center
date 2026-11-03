---
name: arp-scan
description: Skill for arp-scan
---

# arp-scan Skill

This skill provides functionality for `arp-scan`, a tool for scanning networks to discover hosts and their IP addresses using ARP requests.

**Overview:**
- `arp-scan` is used to discover active hosts on a local network by sending ARP requests
- Useful for network administration, security auditing, and inventory management
- Part of the `arp-scan` package on Debian/Ubuntu systems

**Commands:**
- `arp-scan <network>` - Scan a network range (e.g., `arp-scan 192.168.1.0/24`)
- `arp-scan -I <interface>` - Specify network interface (e.g., `arp-scan -I eth0 192.168.1.0/24`)
- `arp-scan -l` - List available network interfaces
- `arp-scan -r <rate>` - Set scan rate in packets per second

**Usage examples:**
- Basic scan: `arp-scan 192.168.1.0/24`
- Scan with specific interface: `arp-scan -I eth0 192.168.1.0/24`
- List interfaces: `arp-scan -l`
- Fast scan: `arp-scan -r 1000 192.168.1.0/24`
