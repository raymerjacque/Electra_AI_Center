---
name: ca-certificates-java
description: Skill for ca-certificates-java
---

# ca-certificates-java Skill

This skill provides functionality for `ca-certificates-java`, which installs CA certificates into the Java keystore.

**Overview:**
- `ca-certificates-java` installs the system's CA certificates into the Java keystore (cacerts)
- Allows Java applications to trust the same certificate authorities as the rest of the system
- Part of the `ca-certificates-java` package on Debian/Ubuntu systems
- Required for Java applications to make HTTPS connections to sites using system-trusted CAs

**Commands:**
- `update-ca-certificates -f` - Force update of Java keystore with system CA certificates
- `keytool -list -keystore /etc/ssl/certs/java/cacerts` - List certificates in Java keystore
- `keytool -import -file <cert.pem> -alias <name> -keystore /etc/ssl/certs/java/cacerts` - Import a certificate

**Usage examples:**
- Update Java keystore: `sudo update-ca-certificates -f`
- List Java keystore certs: `keytool -list -keystore /etc/ssl/certs/java/cacerts`
- Java keystore location: `/etc/ssl/certs/java/cacerts`

**Package purpose:**
- Bridges system CA certificates with Java's keystore
- Ensures Java applications can verify SSL/TLS connections using system-trusted CAs
