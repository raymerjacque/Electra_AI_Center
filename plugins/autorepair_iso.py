<think>We need to output a plugin file content only, raw Python source, no markdown. Must follow spec. Plugin should handle request "create an iso from my linux". Provide triggers maybe "create iso", "make iso", "iso". Provide route token unique, e.g., "ISO". Provide run function that uses appropriate commands to create ISO, maybe using genisoimage or xorriso. Use subprocess. Must handle errors gracefully. Provide setup maybe reading config? Not needed. Provide PLUGIN_TRIGGERS list. Provide PLUGIN_ROUTE_TOKEN = "ISO". Provide PLUGIN_COMMANDS maybe ["/iso"]. Provide get_help. Provide run that checks context maybe for user_home and runs appropriate command. Should be self-contained. Must not import ai_terminal. Use only standard library and subprocess. Provide try/except.

Write plugin file content as raw python. No markdown fences. Ensure file starts with module docstring? Not required but can include comments. Must output only raw source.

Let's craft:

# Plugin metadata
PLUGIN_NAME = "ISO Creator"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Creates an ISO image from the user's home directory"
PLUGIN_AUTHOR = "Your Name"
PLUGIN_ENABLED = True

PLUGIN_TRIGGERS = ["create iso", "make iso", "iso image", "generate iso"]
PLUGIN_ROUTE_TOKEN = "ISO"
PLUGIN_COMMANDS = ["/iso"]

def run(prompt: str, context: dict) -> str:
    """
    Handles prompts that request ISO creation.
    Uses xorriso (or genisoimage) to generate an ISO of the home directory.
    Returns a success message or an error description.
    """
    import os, subprocess, shlex

    user_home = context.get("user_home", os.path.expanduser("~"))
    # Determine which ISO tool is available
    for tool in ("xorriso", "genisoimage"):
        tool_path = shutil.which(tool)
        if tool_path:
            iso_tool = tool
            break
    else:
        return "Error: No ISO creation tool (xorriso or genisoimage) found in PATH."

    # Destination ISO file in the home directory
    iso_path = os.path.join(user_home, "makulu_backup.iso")
    # Build command
    cmd = [iso_tool, "-output", iso_path, "-volid", "MAKULU_BACKUP", "-joliet", "-rock", user_home]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"ISO created successfully at {iso_path}."
    except subprocess.CalledProcessError as e:
        return f"Failed to create ISO: {e.stderr.strip()}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def setup(config: dict) -> bool:
    # No external config needed, but keep function signature
    return True

def get_help() -> str:
    return f"{PLUGIN_NAME} v{PLUGIN_VERSION}: {PLUGIN_DESCRIPTION}"
But need to import shutil for which; shutil is standard. Also need to import shutil at top. Also need to import os, subprocess already imported. Use shutil.which.

Add import shutil.

Make sure no stray prints.

Make sure function signatures exactly as spec: run(prompt: str, context: dict) -> str. setup(config: dict) -> bool. handle_command maybe not needed.

Add handle_command returning False.

Add PLUGIN_TRIGGERS list.

Make sure PLUGIN_ROUTE_TOKEN is unique; "ISO" likely not used.

Make sure file ends with maybe nothing.

Now produce raw python source only, no markdown.
</think>
# Plugin metadata
PLUGIN_NAME = "ISO Creator"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Creates an ISO image from the user's home directory"
PLUGIN_AUTHOR = "Your Name"
PLUGIN_ENABLED = True

PLUGIN_TRIGGERS = ["create iso", "make iso", "iso image", "generate iso", "iso from", "iso of"]
PLUGIN_ROUTE_TOKEN = "ISO"
PLUGIN_COMMANDS = ["/iso"]

import os, subprocess, shutil

def run(prompt: str, context: dict) -> str:
    """
    Handles prompts that request ISO creation.
    Uses the first available ISO tool (xorriso or genisoimage) to generate an ISO
    of the user's home directory.
    Returns a success message or an error description.
    """
    user_home = context.get("user_home", os.path.expanduser("~"))
    # Find a suitable ISO creation utility
    iso_tool = None
    for tool in ("xorriso", "genisoimage"):
        path = shutil.which(tool)
        if path:
            iso_tool = path            break
    if not iso_tool:
        return "Error: No ISO creation tool (xorriso or genisoimage) found in PATH."

    # Destination ISO file (placed in the home directory)
    iso_path = os.path.join(user_home, "makulu_backup.iso")
    # Build the command; -volid sets the volume label, -joliet and -rock add Windows compatibility
    cmd = [iso_tool, "-output", iso_path, "-volid", "MAKULU_BACKUP", "-joliet", "-rock", user_home]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        return f"ISO created successfully at {iso_path}."
    except subprocess.CalledProcessError as e:
        return f"Failed to create ISO: {e.stderr.strip()}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def setup(config: dict) -> bool:
    """
    Optional initialization hook. Called once when the plugin is loaded.
    Return True to keep the plugin enabled.
    """
    return True

def handle_command(command: str, args: str) -> bool:
    """
    Optional: handle a slash command directly.
    Return True if the command was handled, False to let the router continue processing.
    """
    return False

def get_help() -> str:
    """Text shown in the /plugin list."""
    return f"{PLUGIN_NAME} v{PLUGIN_VERSION}: {PLUGIN_DESCRIPTION}"