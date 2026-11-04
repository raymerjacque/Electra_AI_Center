---
name: cinnamon-install-winbind
description: Installs winbind and libntlm0 on Debian/Trixie systems when libntlm-auth-0 is not found. Useful for Samba/Active Directory integration on Cinnamon desktops.
triggers: ["apt-get install winbind", "libntlm-auth-0 not found", "winbind package missing"]
---

# Install winbind and libntlm0 on Debian Trixie

## Overview
When attempting to install `libntlm-auth-0` on Debian 13 (Trixie), the package does not exist. The correct packages are `winbind` (which includes `ntlmauth`) and `libntlm0`. This skill resolves the package name mismatch for Samba/Active Directory integration.

## Proven Procedure

### Step 1: Update package lists
```bash
sudo apt-get update
```

### Step 2: Install the correct packages
```bash
sudo apt-get install winbind libntlm0
```

### Step 3: Verify installation
```bash
which winbind
ntlm_auth --version
```

## Pitfalls & Troubleshooting
- **Old package name**: `libntlm-auth-0` does not exist in Debian Trixie. Use `winbind` which provides `ntlmauth`.
- **Signature errors**: If `sudo` fails with missing GPG keys, run `sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D43F640145369C51D786DDEA76F1A20FF987672F` or remove problematic repos.
- **Package not found**: Ensure `apt-get update` ran successfully before installing.
