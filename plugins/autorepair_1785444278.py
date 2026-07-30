<think>We need to output a plugin file content only, raw Python source, no markdown fences. It should be placed in ~/.config/ai_plugins, named autorepair_<token>.py where token is unique. Must include metadata: PLUGIN_NAME, PLUGIN_VERSION, PLUGIN_DESCRIPTION, PLUGIN_AUTHOR optional, PLUGIN_ENABLED True, PLUGIN_TYPE "ROUTER" (since it's auto-repair plugin filling capability gap). Also PLUGIN_TRIGGERS maybe? The spec says for ROUTER plugin we need PLUGIN_TRIGGERS and PLUGIN_ROUTE_TOKEN and PLUGIN_COMMANDS. The example shows PLUGIN_TRIGGERS = ["ask groq", ...] etc. For this plugin we need to handle request "how to run an app". So triggers could be ["how to run", "run an app", "execute an app"] maybe. Provide PLUGIN_ROUTE_TOKEN unique not colliding. Let's pick "runapp". So token lowercase "runapp". File will be named autorepair_runapp.py (but spec says file will be auto-named: autorepair_<token_lowercase>.py). So we need to output the plugin source code that includes metadata and run function.

We need to handle the request successfully. The run function receives prompt and context, returns a non-empty string. Should use print_fn for progressive output maybe. Should not crash. Should check if the user is asking how to run an app, maybe detect keywords. Provide instructions generic for MakuluLinux (Ubuntu/Cinnamon). Could check if .desktop file exists, use "gtk-launch" or "xdg-open". Provide steps.

We must include PLUGIN_REQUIRES maybe empty.

Write full plugin source: start with module docstring? Not required but okay. Must include metadata variables at top.

Let's craft:

"""
Auto-repair plugin for "how to run an app" queries.
"""

PLUGIN_NAME = "App Runner"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles 'how to run an app' queries on MakuluLinux"
PLUGIN_AUTHOR = "David"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["how to run", "run an app", "execute an app", "how do i run"]
PLUGIN_ROUTE_TOKEN = "runapp"
PLUGIN_COMMANDS = ["/runapp"]
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    # Detect if the user is asking how to run an application
    lowered = prompt.lower()
    if not any(phrase in lowered for phrase in PLUGIN_TRIGGERS):
        return ""  # not our scope

    # Determine the target application name (simple heuristic)
    import re, os
    # Extract possible .desktop or executable name after "run" keywords
    match = re.search(r'(?:run|execute|start)\s+([^\s]+)', lowered)
    if not match:
        return "I couldn't identify the application you want to run."

    app_name = match.group(1).strip('".\'')
    # Try to locate a .desktop file or executable in PATH
    from shutil import which
    desktop_file = os.path.expanduser(f"~/.local/share/applications/{app_name.replace(' ', '_').lower()}.desktop")
    if os.path.isfile(desktop_file):
        # Use gtk-launch if available
        cmd = ["gtk-launch", app_name.replace(' ', '_')]
    else:
        cmd = ["which", app_name]
    executable = which(app_name)
    if executable:
        # Run the executable
        import subprocess
        try:
            result = subprocess.run([executable], capture_output=True, text=True, timeout=30)
            if result.returncode == 0:
                return f"✔️  Successfully started {app_name}. Output:\n{result.stdout}"
            else:
                return f"⚠️  Started {app_name} but it exited with code {result.returncode}.\n{result.stderr}"
        except subprocess.TimeoutExpired:
            return f"⏱️  Starting {app_name} timed out."
    else:
        return f"❓  Could not find an executable or .desktop entry for '{app_name}'."
But need to use context["print_fn"] for progressive output instead of print(). The spec says use context["print_fn"](text) to show progressive output instead of print(). So we should use that. Also we must not import from ai_terminal. Use only standard library.

We should use context["print_fn"] to output maybe step by step. But we can just return a string; but to be safe, we can use print_fn to send messages. However run must return a non-empty string. Using print_fn may not return anything. The spec says use context["print_fn"](text) to show progressive output instead of print(). So we can do:

context["print_fn"]("Looking for application...")
...
context["print_fn"]("Found executable.")
...
return "Done."
But we need to return something. Could return "Operation completed.".

Better to use print_fn for user feedback and then return a final message.

Let's implement:

def run(prompt: str, context: dict) -> str:
    lowered = prompt.lower()
    if not any(phrase in lowered for phrase in PLUGIN_TRIGGERS):
        return ""

    import re, os, subprocess, sys
    from shutil import which

    # Extract application name
    match = re.search(r'(?:run|execute|start)\s+([^\s]+)', lowered)
    if not match:
        context["print_fn"]("I couldn't identify the application you want to run.")
        return "I couldn't identify the application."

    app_name = match.group(1).strip('".\'')
    context["print_fn"](f"Attempting to run '{app_name}'...")

    # Look for .desktop file
    desktop_path = os.path.expanduser(f"~/.local/share/applications/{app_name.replace(' ', '_').lower()}.desktop")
    if os.path.isfile(desktop_path):
        cmd = ["gtk-launch", app_name.replace(' ', '_')]
    else:
        executable = which(app_name)
        if executable:
            cmd = [executable]
        else:
            context["print_fn"](f"❓  No executable or .desktop found for '{app_name}'.")
            return f"Cannot find '{app_name}'."
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            context["print_fn"](f"✔️  Successfully started {app_name}.")
            context["print_fn"](result.stdout.strip() or "Application launched.")
        else:
            context["print_fn"](f"⚠️  {app_name} exited with code {result.returncode}.")
            context["print_fn"](result.stderr.strip() or "See above for details.")
        return f"Launched {app_name}."
    except subprocess.TimeoutExpired:
        context["print_fn"]("⏱️  Starting the application timed out.")
        return "Timeout while launching."
Make sure to not hardcode username. Use os.path.expanduser.

Add PLUGIN_REQUIRES maybe ["subprocess"] but that's built-in; no external packages.

Now ensure metadata includes PLUGIN_COMMANDS maybe not needed but okay.

Now output only raw python source, no markdown fences. Ensure no extra explanation.

Let's produce final answer.
</think>
"""
Auto‑repair plugin for “how to run an app” queries on MakuluLinux.
"""

PLUGIN_NAME = "App Runner"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles 'how to run an app' queries on MakuluLinux"
PLUGIN_AUTHOR = "David"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["how to run", "run an app", "execute an app", "how do i run"]
PLUGIN_ROUTE_TOKEN = "runapp"
PLUGIN_COMMANDS = ["/runapp"]
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    # Normalise the prompt for trigger detection
    lowered = prompt.lower()
    if not any(phrase in lowered for phrase in PLUGIN_TRIGGERS):
        return ""  # not our scope

    import os, re, subprocess
    from shutil import which

    # Extract the target application name
    match = re.search(r'(?:run|execute|start)\s+([^\s]+)', lowered)
    if not match:
        context["print_fn"]("I couldn't identify the application you want to run.")
        return "I couldn't identify the application."

    app_name = match.group(1).strip('".\'')
    context["print_fn"](f"Attempting to run '{app_name}'...")

    # Look for a .desktop file first
    desktop_path = os.path.expanduser(
        f"~/.local/share/applications/{app_name.replace(' ', '_').lower()}.desktop"
    )
    if os.path.isfile(desktop_path):
        # Use gtk-launch for desktop entries
        cmd = ["gtk-launch", app_name.replace(' ', '_')]
    else:
        # Fall back to checking the PATH for an executable
        exe_path = which(app_name)
        if exe_path:
            cmd = [exe_path]
        else:
            context["print_fn"](f"❓  No executable or .desktop entry found for '{app_name}'.")
            return f"Cannot find '{app_name}'."

    # Execute the command safely
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            context["print_fn"](f"✔️  Successfully started {app_name}.")
            context["print_fn"](result.stdout.strip() or "Application launched.")
        else:
            context["print_fn"](f"⚠️  {app_name} exited with code {result.returncode}.")
            context["print_fn"](result.stderr.strip() or "See error above.")
        return f"Launched {app_name}."
    except subprocess.TimeoutExpired:
        context["print_fn"]("⏱️  Starting the application timed out.")
        return "Timeout while launching."