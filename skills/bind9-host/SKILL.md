---
name: bind9-host
description: Skill for bind9-host
---

# bind9-host Skill

This skill provides functionality for `bind9-host`, a utility for DNS lookups that is part of the ISC BIND9 package.

**Overview:**
- `bind9-host` is a simple DNS lookup utility that was traditionally part of the BIND distribution
- Provides quick DNS resolution without the full feature set of `dig`
- Part of the `bind9-host` package on Debian/Ubuntu systems
- Simpler alternative to `dig` for basic DNS queries

**Commands:**
- `host <domain>` - Simple DNS lookup
- `host -t <type> <domain>` - Lookup specific record type (A, AAAA, MX, etc.)
- `host -l <domain> <server>` - List DNS zone (axfr)
- `host -C <domain>` - Show SOA record information

**Usage examples:**
- Basic DNS lookup: `host example.com`
- Lookup A record: `host -t example.com A`
- Check MX records: `host -t mx example.com`
- Reverse lookup: `host 8.8.8.8`

**Package purpose:**
- Provides a simple DNS query tool from the BIND9 distribution
- Lightweight alternative to dig for quick lookups
