---
name: brave-browser
description: Skill for brave-browser
---

# brave-browser Skill

This skill provides functionality for `brave-browser`, a privacy-focused web browser built on Chromium.

**Overview:**
- `brave-browser` is a privacy-oriented web browser based on Chromium
- Blocks ads, trackers, and fingerprinting scripts by default
- Built-in Tor support and IPFS integration
- Faster browsing experience due to built-in tracker blocking
- Part of the `brave-browser` package on Debian/Ubuntu/MakuluLinux systems

**Commands:**
- `brave-browser` - Launch the Brave browser
- `brave-browser --incognito` - Open incognito window
- `brave-browser --new-window <url>` - Open URL in new window
- `brave-browser --profile-directory="Default"` - Specify profile
- `brave-browser --version` - Show version information

**Usage examples:**
- Launch Brave: `brave-browser`
- Private browsing: `brave-browser --incognito`
- Set as default: `brave-browser --default-browser`
- Open specific URL: `brave-browser https://example.com`

**Configuration:**
- Brave Shields for ad/tracker blocking settings
- `brave://settings` for browser configuration
- Profile located at `~/.config/brave-browser/Default/`
- Can import data from Chrome/Firefox on first launch
