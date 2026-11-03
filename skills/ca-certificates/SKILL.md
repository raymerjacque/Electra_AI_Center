---
name: ca-certificates
description: Skill for ca-certificates
---

# ca-certificates Skill

This skill provides functionality for `ca-certificates`, which contains common CA certificates for SSL/TLS verification.

**Overview:**
- `ca-certificates` contains a set of common Certificate Authority (CA) certificates
- Used by SSL/TLS applications to verify the authenticity of HTTPS connections
- Part of the `ca-certificates` package on Debian/Ubuntu systems
- Certificates are stored in `/etc/ssl/certs/`

**Commands:**
- `update-ca-certificates` - Update the CA certificate bundle
- `ls /etc/ssl/certs/` - List available CA certificates
- `cat /etc/ssl/certs/ca-certificates.crt` - View the combined CA bundle

**Usage examples:**
- Update certificates: `sudo update-ca-certificates`
- View available certificates: `ls /etc/ssl/certs/`
- Check a specific certificate: `openssl x509 -in /etc/ssl/certs/ca-certificates.crt -noout -subject`

**Package purpose:**
- Provides trusted root CA certificates for SSL/TLS connections
- Essential for secure web browsing, email, and other encrypted communications
- Automatically updated through system package updates
