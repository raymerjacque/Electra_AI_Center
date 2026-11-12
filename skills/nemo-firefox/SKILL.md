---
name: nemo-firefox
description: Skill for Firefox web browser
---

# firefox Skill

# Firefox Web Browser Skill

## Overview
Firefox is a free and open-source web browser developed by Mozilla that offers a secure and customizable browsing experience.

## Commands
- `firefox` - Launch Firefox GUI
- `firefox <url>` - Open a specific URL
- `firefox --private-window <url>` - Open private browsing
- `firefox --new-window <url>` - Open new window
- `firefox --new-private-window <url>` - Open new private window

## Common Operations
- Open URL: `firefox https://example.com`
- Open private window: `firefox --private-window https://example.com`
- Open new window: `firefox --new-window https://example.com`
- Open new private window: `firefox --new-private-window https://example.com`
- Open specific file: `firefox file:///home/user/document.pdf`

## Configuration
- Config file: `~/.mozilla/firefox/*.default-release/firefox.cfg`
- Profile manager: `firefox -ProfileManager`
- Reset config: delete `~/.mozilla/firefox/*.default-release/firefox.cfg`

## Plugins & Extensions
- Add-ons: `about:addons` in Firefox
- Extension management: `~/.mozilla/firefox/*.default-release/extensions/`
- Themes: `~/.mozilla/firefox/*.default-release/themes/`

## Troubleshooting
- If Firefox crashes, check for conflicting extensions
- Clear cache: `firefox --clear-cache`
- Reset Firefox: `firefox --reset`
- Debug with: `firefox --debug`

## Security Features
- Tracking protection: enabled by default
- Enhanced Tracking Protection: Standard, Strict, or Custom
- HTTPS-Only Mode: enabled by default
- Container tabs: isolates websites for security
