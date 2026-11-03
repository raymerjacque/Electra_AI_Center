---
name: anacron
description: Skill for anacron - periodic command execution
---

# anacron Skill

This skill provides functionality for anacron, which executes commands periodically based on calendar days rather than continuous system uptime.

**Overview:**
- anacron runs commands periodically (daily, weekly, monthly) even if the system is not continuously running
- Designed for laptops and desktops that are not always on
- Replaces cron for daily/weekly/monthly tasks on systems that are not 24/7 online
- Reads `/etc/anacrontab` for configuration

**Commands:**
- `anacron` - Run pending cron jobs
- `anacct -d` - Show anacron accounting
- `grep -E '^SHELL|^PATH|^RANDOM_DELAY' /etc/anacrontab` - View anacron config
- `ls -la /etc/cron.daily/` - List daily cron jobs

**Usage:**
- anacron automatically runs daily/weekly/monthly jobs at startup
- System administrators add scripts to `/etc/cron.daily/` for daily execution
- Unlike cron, anacron counts days from the last run, not system uptime
- Check status with: `systemctl status anacron`
