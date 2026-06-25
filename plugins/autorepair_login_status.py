"""Login Status Plugin for Electra AI Terminal.
Handles user login/session information requests on MakuluLinux (Ubuntu/Cinnamon).
"""

import subprocess
import os

PLUGIN_NAME        = "Login Status Handler"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Provides user login status, session info, and authentication details"
PLUGIN_AUTHOR      = "Electra AI"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "ROUTER"
PLUGIN_REQUIRES    = []

PLUGIN_TRIGGERS    = [
    "login", "whoami", "who am i", "current user", "user info",
    "session info", "login status", "who is logged in", "logged in users",
    "login history", "recent logins", "check login", "my login"
]
PLUGIN_ROUTE_TOKEN = "LOGIN_STATUS"
PLUGIN_COMMANDS    = ["/login", "/whoami", "/sessions"]

def run(prompt: str, context: dict) -> str:
    """Return formatted login and session information for the current system."""
    print_fn = context.get("print_fn", print)

    result_parts = []
    result_parts.append("=== Login & Session Status ===\n")

    # 1. Current username
    try:
        whoami_proc = subprocess.run(
            ["whoami"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False
        )
        if whoami_proc.returncode == 0:
            result_parts.append(f"Current User: {whoami_proc.stdout.strip()}")
    except Exception:
        result_parts.append("Current User: [unavailable]")

    # 2. Detailed identity info
    try:
        id_proc = subprocess.run(
            ["id"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False
        )
        if id_proc.returncode == 0:
            result_parts.append(f"\nUser Details:\n{id_proc.stdout.strip()}")
    except Exception:
        pass

    # 3. Active user sessions
    try:
        loginctl = subprocess.run(
            ["loginctl", "list-sessions", "--no-legend"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False
        )
        if loginctl.returncode == 0 and loginctl.stdout.strip():
            result_parts.append("\nActive Sessions:")
            for line in loginctl.stdout.strip().split('\n'):
                line = line.strip()
                if line:
                    parts = line.split()
                    if len(parts) >= 2:
                        user_field = parts[2] if len(parts) > 2 else "unknown"
                        tty_field  = parts[4] if len(parts) > 4 else "?"
                        result_parts.append(f"  • Session {parts[0]}: {user_field} (TTY: {tty_field})")
        else:
            # Fallback to 'who'
            who_proc = subprocess.run(
                ["who"],
                capture_output=True,
                text=True,
                timeout=5,
                check=False
            )
            if who_proc.returncode == 0 and who_proc.stdout.strip():
                result_parts.append("\nCurrently Logged In:")
                for line in who_proc.stdout.strip().split('\n'):
                    result_parts.append(f"  • {line}")
    except Exception:
        result_parts.append("\nActive Sessions: [unavailable]")

    # 4. Recent login history
    try:
        last_proc = subprocess.run(
            ["last", "-n", "5", "-F"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False
        )
        if last_proc.returncode == 0 and last_proc.stdout.strip():
            result_parts.append("\nRecent Login History:")
            for line in last_proc.stdout.strip().split('\n')[:5]:
                line = line.strip()
                if line and not line.startswith("wtmp begins"):
                    result_parts.append(f"  • {line}")
    except Exception:
        pass

    # 5. Session environment details
    try:
        display       = os.environ.get("DISPLAY", "none")
        xdg_session   = os.environ.get("XDG_SESSION_TYPE", "unknown")
        result_parts.append(f"\nEnvironment: Display={display}, SessionType={xdg_session}")
    except Exception:
        pass

    result_parts.append("\n" + "="*30)

    return "\n".join(result_parts)