"""
Autorepair plugin for handling status inquiries like 'How are you?'.
Fills capability gap by intercepting greeting/status routing requests.
"""

import os
import platform
from datetime import datetime

PLUGIN_NAME = "How Are You Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles greeting and status inquiries like 'How are you?'"
PLUGIN_AUTHOR = "Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"

PLUGIN_TRIGGERS = [
    "how are you",
    "how are you doing",
    "how do you do",
    "how is it going",
    "what's up",
    "how are things",
    "are you well",
    "how are you today",
    "how are you feeling"
]

PLUGIN_ROUTE_TOKEN = "HOWAREYOU"
PLUGIN_COMMANDS = ["/howareyou", "/status"]
PLUGIN_REQUIRES = []


def run(prompt: str, context: dict) -> str:
    """Handle status inquiries with system information and friendly response."""
    try:
        print_fn = context.get("print_fn", print)
        
        print_fn("Checking status...")
        system_info = _get_system_info()
        
        hour = datetime.now().hour
        time_greeting = _get_time_greeting(hour)
        
        response = (
            f"I'm doing well, thanks for asking! {time_greeting}\n\n"
            f"System Status:\n"
            f"  OS: {system_info['os']}\n"
            f"  Uptime: {system_info['uptime']}\n"
            f"  Memory: {system_info['memory']}\n"
            f"  Disk: {system_info['disk']}\n\n"
            f"I'm ready to help with anything you need!"
        )
        
        return response
        
    except Exception as e:
        return "I'm doing great, thanks for asking! (Error getting system details)"


def _get_time_greeting(hour: int) -> str:
    """Return appropriate time-based greeting."""
    if 5 <= hour < 12:
        return "Good morning!"
    elif 12 <= hour < 17:
        return "Good afternoon!"
    elif 17 <= hour < 22:
        return "Good evening!"
    else:
        return "Good night!"


def _get_system_info() -> dict:
    """Gather basic system information safely."""
    info = {
        "os": "MakuluLinux",
        "uptime": "N/A",
        "memory": "N/A",
        "disk": "N/A"
    }
    
    try:
        if os.path.exists("/etc/os-release"):
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("PRETTY_NAME="):
                        info["os"] = line.split("=", 1)[1].strip().strip('"')
                        break
    except:
        pass
    
    try:
        if os.path.exists("/proc/uptime"):
            with open("/proc/uptime") as f:
                seconds = float(f.read().split()[0])
            hours = int(seconds // 3600)
            minutes = int((seconds % 3600) // 60)
            info["uptime"] = f"{hours}h {minutes}m"
    except:
        pass
    
    try:
        with open("/proc/meminfo") as f:
            meminfo = {}
            for line in f:
                parts = line.split()
                if len(parts) >= 2 and parts[0].endswith(":"):
                    key = parts[0].rstrip(":")
                    meminfo[key] = int(parts[1])
        
        total = meminfo.get("MemTotal", 0) // 1024
        available = meminfo.get("MemAvailable", 0) // 1024
        if total > 0:
            used = total - available
            percent = int((used / total) * 100)
            info["memory"] = f"{used}MB / {total}MB ({percent}%)"
    except:
        pass
    
    try:
        stat = os.statvfs(os.path.expanduser("~"))
        total = (stat.f_frsize * stat.f_blocks) // (1024**3)
        free = (stat.f_frsize * stat.f_bfree) // (1024**3)
        if total > 0:
            used = total - free
            percent = int((used / total) * 100)
            info["disk"] = f"{used}GB / {total}GB ({percent}%)"
    except:
        pass
    
    return info