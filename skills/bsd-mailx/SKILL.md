---
name: bsd-mailx
description: Skill for bsd-mailx
---

# bsd-mailx Skill

This skill provides functionality for `bsd-mailx`, a BSD mail user agent (MUA) based on the `mailx` package.

**Overview:**
- `bsd-mailx` is a mail user agent based on the 4.4BSD `mailx` command
- Provides email reading, sending, and management capabilities from the command line
- Part of the `bsd-mailx` package on Debian/Ubuntu systems
- Designed as a lightweight, efficient mail client for terminal use

**Commands:**
- `mail` - Read and send mail
- `bsd-mailx` - Start the mail user agent
- `sendmail` - Send mail (often symlinked from bsd-mailx)
- `mailx` - Alternative command name (often symlinked)

**Usage examples:**
- Send mail: `echo "body" | mail -s "subject" user@example.com`
- Read mail: `mail` (interactive mode)
- List mail: `mail -f` (read mail from mbox)
- Quick send: `mail user@example.com < message.txt`

**Package purpose:**
- Provides command-line email functionality
- Lightweight alternative to graphical email clients
- Based on BSD mailx tradition, common on Debian/Ubuntu systems
