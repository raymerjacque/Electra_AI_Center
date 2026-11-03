---
name: bind9-dnsutils
description: Skill for bind9-dnsutils
---

# bind9-dnsutils Skill

This skill provides functionality for `bind9-dnsutils`, a collection of DNS utilities from the ISC BIND9 package.

**Overview:**
- `bind9-dnsutils` contains essential DNS diagnostic and query tools
- Part of the ISC BIND9 package on Debian/Ubuntu systems
- Used for troubleshooting DNS, looking up records, and network diagnostics

**Commands:**
- `dig <domain>` - DNS lookup (most commonly used)
- `dig @<server> <domain>` - Query specific DNS server
- `host <domain>` - Simple DNS lookup
- `nslookup <domain>` - Alternative DNS lookup tool
- `dig -x <IP>` - Reverse DNS lookup
- `dig axfr <domain>` - Zone transfer (if permitted)

**Usage examples:**
- Basic DNS lookup: `dig example.com`
- Check A record: `dig example.com A`
- Reverse lookup: `dig -x 8.8.8.8`
- Short answer only: `dig +short example.com`
- Query specific server: `dig @8.8.8.8 example.com`

**Package purpose:**
- Provides the dnsutils tools from the BIND9 distribution
- Essential for system administrators and network troubleshooting
