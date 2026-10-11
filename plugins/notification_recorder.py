"""Notification Recorder Plugin - Records system notifications to file for AI access."""

import json
import os
import time
import threading
from datetime import datetime, timedelta
from pathlib import Path

PLUGIN_NAME = "Notification Recorder"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Records system notifications to file, lists last 24h, clears old unacknowledged"
PLUGIN_AUTHOR = "AI Assistant"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "HOOK"
PLUGIN_REQUIRES = ["dbus-python", "pygobject"]

# Notification storage file
NOTIFICATION_FILE = Path(__file__).parent / "notifications.json"
_lock = threading.Lock()


def setup(config: dict) -> bool:
    """Initialize notification recording on startup."""
    try:
        # Start notification listener in background thread
        thread = threading.Thread(target=_start_notification_listener, daemon=True)
        thread.start()
        return True
    except Exception as e:
        print(f"[NotificationRecorder] Setup failed: {e}")
        return False


def _start_notification_listener():
    """Listen for system notifications via DBus."""
    try:
        import dbus
        from dbus.mainloop.glib import DBusGMainLoop
        from gi.repository import GLib
        
        # Set up DBus main loop
        DBusGMainLoop(set_as_default=True)
        bus = dbus.SessionBus()
        
        # Listen to NotificationClosed and ActionInvoked signals
        bus.add_signal_receiver(
            _notification_handler,
            signal_name="Notify",
            dbus_interface="org.freedesktop.Notifications",
            path="/org/freedesktop/Notifications"
        )
        
        # Run the main loop
        loop = GLib.MainLoop()
        loop.run()
    except ImportError:
        print("[NotificationRecorder] DBus/PyGObject not available - using fallback polling")
        _fallback_polling_listener()
    except Exception as e:
        print(f"[NotificationRecorder] Listener error: {e}")


def _notification_handler(*args, **kwargs):
    """Handle incoming notification from DBus."""
    try:
        # Extract notification data
        app_name = args[0] if len(args) > 0 else "Unknown"
        replaces_id = args[1] if len(args) > 1 else 0
        app_icon = args[2] if len(args) > 2 else ""
        summary = args[3] if len(args) > 3 else ""
        body = args[4] if len(args) > 4 else ""
        
        if summary or body:
            _record_notification({
                "timestamp": datetime.now().isoformat(),
                "app": str(app_name),
                "summary": str(summary),
                "body": str(body),
                "icon": str(app_icon),
                "acknowledged": False,
                "reported": False
            })
    except Exception as e:
        print(f"[NotificationRecorder] Handler error: {e}")


def _fallback_polling_listener():
    """Fallback: poll journalctl for notifications."""
    try:
        import subprocess
        
        last_check = datetime.now()
        while True:
            time.sleep(5)  # Check every 5 seconds
            try:
                # Get recent notifications from journalctl
                result = subprocess.run(
                    ["journalctl", "--user", "-u", "notify*", "--since", "5 seconds ago", "--output=json"],
                    capture_output=True,
                    text=True,
                    timeout=2
                )
                
                if result.stdout:
                    for line in result.stdout.strip().split('\n'):
                        if line:
                            try:
                                entry = json.loads(line)
                                _record_notification({
                                    "timestamp": entry.get("__REALTIME_TIMESTAMP", datetime.now().isoformat()),
                                    "app": entry.get("SYSLOG_IDENTIFIER", "System"),
                                    "summary": entry.get("MESSAGE", ""),
                                    "body": "",
                                    "icon": "",
                                    "acknowledged": False,
                                    "reported": False
                                })
                            except json.JSONDecodeError:
                                continue
            except Exception:
                pass
    except Exception as e:
        print(f"[NotificationRecorder] Fallback listener error: {e}")


def _record_notification(notification: dict):
    """Write notification to JSON file."""
    with _lock:
        try:
            notifications = []
            if NOTIFICATION_FILE.exists():
                with open(NOTIFICATION_FILE, 'r') as f:
                    notifications = json.load(f)
            
            notifications.append(notification)
            
            with open(NOTIFICATION_FILE, 'w') as f:
                json.dump(notifications, f, indent=2)
        except Exception as e:
            print(f"[NotificationRecorder] Record error: {e}")


def on_pre_message(prompt: str, context: dict) -> str:
    """Check for notification-related commands before message processing."""
    prompt_lower = prompt.lower().strip()
    
    # Check for notification commands
    if prompt_lower.startswith("/notifications"):
        return _handle_notification_command(prompt_lower)
    elif "notification" in prompt_lower and ("list" in prompt_lower or "show" in prompt_lower or "update" in prompt_lower):
        return _handle_notification_command("/notifications list")
    elif "clear notification" in prompt_lower:
        return _handle_notification_command("/notifications clear")
    elif "acknowledge notification" in prompt_lower:
        return _handle_notification_command("/notifications acknowledge")
    
    return ""


def _handle_notification_command(command: str) -> str:
    """Process notification commands."""
    parts = command.split(maxsplit=2)
    action = parts[1] if len(parts) > 1 else "list"
    
    if action == "list":
        return _list_notifications()
    elif action == "clear":
        return _clear_old_notifications()
    elif action == "acknowledge":
        notif_id = parts[2] if len(parts) > 2 else ""
        return _acknowledge_notification(notif_id)
    else:
        return "Unknown command. Use: /notifications [list|clear|acknowledge <id>]"


def _list_notifications() -> str:
    """List notifications from last 24 hours."""
    try:
        if not NOTIFICATION_FILE.exists():
            return "No notifications recorded yet."
        
        with _lock:
            with open(NOTIFICATION_FILE, 'r') as f:
                notifications = json.load(f)
        
        # Filter to last 24 hours
        cutoff = datetime.now() - timedelta(hours=24)
        recent = []
        
        for i, notif in enumerate(notifications):
            try:
                ts = datetime.fromisoformat(notif["timestamp"])
                if ts >= cutoff:
                    recent.append((i, notif))
            except (ValueError, KeyError):
                continue
        
        if not recent:
            return "No notifications in the last 24 hours."
        
        # Format output
        lines = ["📬 **Recent Notifications (Last 24h)**\n"]
        for idx, (i, notif) in enumerate(recent, 1):
            status = "✅" if notif.get("acknowledged") else ("📢" if notif.get("reported") else "⏳")
            app = notif.get("app", "Unknown")
            summary = notif.get("summary", "")
            body = notif.get("body", "")
            ts = notif.get("timestamp", "")[:16].replace("T", " ")
            
            lines.append(f"**{idx}.** {status} [{ts}] **{app}**")
            if summary:
                lines.append(f"   {summary}")
            if body:
                lines.append(f"   {body[:200]}")
            lines.append("")
        
        lines.append(f"Total: {len(recent)} notifications")
        lines.append("Use `/notifications acknowledge <id>` to mark as read")
        lines.append("Use `/notifications clear` to remove old notifications")
        
        # Mark as reported
        _mark_as_reported([i for i, _ in recent])
        
        return "\n".join(lines)
    except Exception as e:
        return f"Error listing notifications: {e}"


def _clear_old_notifications() -> str:
    """Clear notifications older than 24h that are acknowledged or reported."""
    try:
        if not NOTIFICATION_FILE.exists():
            return "No notifications to clear."
        
        with _lock:
            with open(NOTIFICATION_FILE, 'r') as f:
                notifications = json.load(f)
        
        cutoff = datetime.now() - timedelta(hours=24)
        kept = []
        cleared = 0
        
        for notif in notifications:
            try:
                ts = datetime.fromisoformat(notif["timestamp"])
                # Keep if: less than 24h old, OR not acknowledged AND not reported
                if ts >= cutoff or (not notif.get("acknowledged") and not notif.get("reported")):
                    kept.append(notif)
                else:
                    cleared += 1
            except (ValueError, KeyError):
                kept.append(notif)  # Keep if can't parse timestamp
        
        with open(NOTIFICATION_FILE, 'w') as f:
            json.dump(kept, f, indent=2)
        
        return f"Cleared {cleared} old notifications. {len(kept)} remaining."
    except Exception as e:
        return f"Error clearing notifications: {e}"


def _acknowledge_notification(notif_id: str) -> str:
    """Mark a notification as acknowledged."""
    try:
        if not notif_id:
            return "Please specify notification ID. Use: /notifications acknowledge <id>"
        
        try:
            idx = int(notif_id) - 1  # Convert 1-based to 0-based
        except ValueError:
            return "Invalid notification ID. Use a number."
        
        if not NOTIFICATION_FILE.exists():
            return "No notifications recorded yet."
        
        with _lock:
            with open(NOTIFICATION_FILE, 'r') as f:
                notifications = json.load(f)
            
            if 0 <= idx < len(notifications):
                notifications[idx]["acknowledged"] = True
                with open(NOTIFICATION_FILE, 'w') as f:
                    json.dump(notifications, f, indent=2)
                return f"Notification {notif_id} marked as acknowledged ✅"
            else:
                return f"Notification ID {notif_id} not found."
    except Exception as e:
        return f"Error acknowledging notification: {e}"


def _mark_as_reported(indices: list):
    """Mark notifications as reported after listing."""
    try:
        if not NOTIFICATION_FILE.exists():
            return
        
        with _lock:
            with open(NOTIFICATION_FILE, 'r') as f:
                notifications = json.load(f)
            
            for idx in indices:
                if 0 <= idx < len(notifications):
                    notifications[idx]["reported"] = True
            
            with open(NOTIFICATION_FILE, 'w') as f:
                json.dump(notifications, f, indent=2)
    except Exception as e:
        print(f"[NotificationRecorder] Mark reported error: {e}")


def on_shutdown(context: dict):
    """Cleanup on shutdown."""
    # Auto-clear old notifications on shutdown
    _clear_old_notifications()


def get_help() -> str:
    return """Notification Recorder: Records system notifications to file.
Commands:
  /notifications list - Show notifications from last 24h
  /notifications clear - Clear old acknowledged/reported notifications
  /notifications acknowledge <id> - Mark notification as acknowledged
Or just ask: "show notifications", "notification update", "clear notifications"
"""
