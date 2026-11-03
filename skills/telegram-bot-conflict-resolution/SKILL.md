---
name: telegram-bot-conflict-resolution
description: Resolves Telegram bot API Conflict: terminated by other getUpdates request errors by detecting and killing duplicate polling instances and implementing process locking.
triggers: ["telegram api conflict", "getupdates conflict terminated by other getupdates request", "telegram bot duplicate instances", "telegram long polling conflict"]
---

# Telegram Bot Conflict Resolution

## Overview
When a Telegram bot using long polling (`getUpdates`) has multiple instances running concurrently against the same bot token, Telegram's API returns a `Conflict: terminated by other getUpdates request` error. This skill outlines how to diagnose, terminate, and prevent duplicate bot instances.

## Proven Procedure

1. **Identify Duplicate Processes:**
   Search for running instances of the bot script or binary:
   ```bash
   pgrep -af <bot_name_or_keyword>
   # or
   ps aux | grep -E "telegram|bot"
   ```

2. **Terminate Rogue Instances:**
   Stop duplicate processes, keeping only the intended instance (or kill all and restart cleanly):
   ```bash
   kill -9 <PID_of_duplicate>
   ```

3. **Implement Startup Safeguards:**
   Add a pre-execution check in your startup script or wrapper to prevent multiple instances:
   ```bash
   if pgrep -f "ai_terminal.bin --telegram" > /dev/null; then
       echo "Bot is already running!"
       exit 1
   fi
   ```

4. **Use PID File Locking (Recommended):**
   In your bot's entry point, write the process ID to a lock file and check it on startup:
   ```python
   import os
   import sys

   PID_FILE = "/var/run/my_telegram_bot.pid"

   if os.path.exists(PID_FILE):
       with open(PID_FILE, "r") as f:
           pid = f.read().strip()
       if os.path.exists(f"/proc/{pid}"):
           print(f"Bot already running with PID {pid}")
           sys.exit(1)

   with open(PID_FILE, "w") as f:
       f.write(str(os.getpid()))
   ```

## Pitfalls & Troubleshooting
- **Webhook vs
