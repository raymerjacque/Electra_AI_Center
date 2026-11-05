<think>Here's a thinking process:

1.  **Analyze User Input:**
   - User wants a plugin for Electra AI terminal app on MakuluLinux
   - The request is: "how do I configure makulu"
   - This failed in agent 'Proactive Scanner' with CAPABILITY_GAP, repeated 3 times
   - I need to write a complete, working plugin file that handles this request
   - Output must be raw Python source only, no markdown fences, no explanation, no preamble
   - Must follow the plugin specification provided

2.  **Identify Key Requirements:**
   - Plugin type: ROUTER (since it's filling a capability gap, and spec says `PLUGIN_TYPE = "ROUTER"` for auto-repair plugins)
   - Triggers should match "how do I configure makulu" or similar MakuluLinux configuration queries
   - PLUGIN_ROUTE_TOKEN should not clash with existing ones
   - Must return non-empty string
   - Must use `context["print_fn"]` for output
   - Must wrap external calls in try/except
   - Must declare dependencies if needed in `PLUGIN_REQUIRES`
   - Auto-named: `autorepair_<token_lowercase>.py`
   - Must not hardcode paths/usernames
   - Must use `context["user_home"]` or `os.path.expanduser("~")`

3.  **Determine Plugin Triggers & Route Token:**
   - Triggers: things like "configure makulu", "makulu setup", "makulu linux configure"
   - Route token: something like "MAKULU" or "MAKULU_CONFIG". Need to check existing ones? Not provided, but I'll pick something unlikely to clash. Maybe "MAKULU_CFG" or just "MAKULU". I'll use "MAKULU".
   - Commands: maybe "/makulu" or "/configure_makulu". I'll keep it simple.

4.  **Plugin Functionality:**
   - The request is "how do I configure makulu" - this is about MakuluLinux configuration guidance
   - Since it's a Linux distro config question, the plugin should provide helpful guidance/instructions for configuring MakuluLinux
   - It could open relevant docs, or just provide a structured response with common config steps
   - Since we can't actually run system commands safely without risk, and the plugin must just return a string, I'll make it provide a helpful formatted response with common MakuluLinux configuration tips, using `context["print_fn"]` for progressive output, or just return the string.
   - Actually, the `run` function returns a string. The `print_fn` is callable to print with Rich Markdown rendering. I should use `context["print_fn"]` to output progressive results, but the function must return a non-empty string.
   - Looking at the spec: `run(prompt: str, context: dict) -> str:` and "Use context["print_fn"](text) to show progressive output instead of print()". So I can call `context["print_fn"]` inside the function for output, and also return a string.

   - Let me design the plugin:
     - It's a ROUTER plugin
     - Triggers: ["configure makulu", "makulu setup", "how do i configure makulu", "makulu config"]
     - PLUGIN_ROUTE_TOKEN = "MAKULU"
     - PLUGIN_COMMANDS = ["/makulu"]
     - PLUGIN_REQUIRES might be empty or include `os` (standard lib)
     - The `run` function will provide MakuluLinux configuration guidance

   - Since this is an auto-repair plugin filling a capability gap, it should be robust, handle errors, and provide useful info.

   - Let me think about what "configure makulu" typically involves on MakuluLinux:
     - MakuluLinux is based on Ubuntu/Debian, uses Xfce/Cinnamon
     - Common config: display settings, keyboard, software sources, themes, etc.
     - I'll provide a concise, helpful guide string.

   - Plugin structure per spec:
     ```python
     PLUGIN_NAME        = "MakuluLinux Config Helper"
     PLUGIN_VERSION     = "1.0.0"
     PLUGIN_DESCRIPTION = "Handles MakuluLinux configuration questions"
     PLUGIN_AUTHOR      = "Auto-repair"
     PLUGIN_ENABLED     = True
     PLUGIN_TYPE        = "ROUTER"
     PLUGIN_TRIGGERS    = [...]
     PLUGIN_ROUTE_TOKEN = "MAKULU"
     PLUGIN_COMMANDS    = ["/makulu"]
     PLUGIN_REQUIRES    = []
     
     def run(prompt: str, context: dict) -> str:
         # use context["print_fn"] to output
         # return helpful string
     
   - I need to make sure I don't hardcode paths. Use `context["user_home"]` if needed.
   - I'll keep it simple: provide a formatted response with configuration steps for MakuluLinux.

   - Let me draft the actual code carefully:

   ```python
   """Autorepair plugin for MakuluLinux configuration guidance."""
   
   PLUGIN_NAME        = "MakuluLinux Config Helper"
   PLUGIN_VERSION     = "1.0.0"
   PLUGIN_DESCRIPTION = "Provides guidance for configuring MakuluLinux settings"
   PLUGIN_AUTHOR      = "Auto-repair System"
   PLUGIN_ENABLED     = True
   PLUGIN_TYPE        = "ROUTER"
   PLUGIN_TRIGGERS    = ["configure makulu", "makulu setup", "how do i configure makulu", "makulu config"]
   PLUGIN_ROUTE_TOKEN = "MAKULU"
   PLUGIN_COMMANDS    = ["/makulu"]
   PLUGIN_REQUIRES    = []
   
   def run(prompt: str, context: dict) -> str:
       try:
           user_home = context.get("user_home", "")
           print_fn = context.get("print_fn", print)
           
           print_fn("[MakuluLinux Config] Here are common configuration steps for MakuluLinux:")
           print_fn("• Display & Monitor: Use 'Display Settings' or `xrandr` for multi-monitor setup")
           print_fn("• Software Sources: Open 'Software & Updates' to configure repos, PPAs, and update sources")
           print_fn("• System Updates: Run `sudo apt update && sudo apt full-upgrade` in terminal")
           print_fn("• Desktop Theme: Right-click desktop → 'Change Desktop Background' or use 'Appearance' settings")
           print_fn("• Keyboard & Shortcuts: Configure via 'Keyboard' settings for custom shortcuts")
           print_fn("• Network: Use the system tray network applet or `nmcli` for command-line setup")
           print_fn("• For Cinnamon users: Additional tweaks are available via 'Cinnamon Settings'")
           print_fn("• Tip: MakuluLinux inherits Ubuntu/Debian package management, so all standard `apt` commands apply")
           
           return "[MakuluLinux Config Helper] Configuration guidance provided."
       except Exception as e:
           return f"[MakuluLinux Config Helper] Error: {str(e)}"
   
   - Wait, the spec says: "Output ONLY raw Python source. No markdown fences, no explanation, no preamble. Start directly with the module docstring or first import line."
   - So I need to output just the Python code, no triple backticks, no markdown, no explanation.
   - Also: "Start directly with the module docstring or first import line." So I can start with a docstring or directly with the metadata variables.
   - I'll structure it starting with the PLUGIN_* variables, or a module docstring then them. The spec shows the metadata dict-like variables at the top. I'll follow that pattern but as actual Python code.
   - Actually, the spec shows:
     ```python
     PLUGIN_NAME        = "My Plugin"         # Display name shown in /plugin list
     PLUGIN_VERSION     = "1.0.0"            # Semantic version string
     PLUGIN_DESCRIPTION = "One-line summary"  # Shown in router context + /plugin list
     PLUGIN_AUTHOR      = "Your Name"         # Optional
     PLUGIN_ENABLED     = True                # Set False to disable without deleting
     PLUGIN_TYPE        = "ROUTER"            # ROUTER | AGENT | HOOK | COMMAND | EVENT
     PLUGIN_TRIGGERS    = ["ask groq", "use groq", "groq:"]
     PLUGIN_ROUTE_TOKEN = "GROQ"
     PLUGIN_COMMANDS    = ["/groq"]
     
     def run(prompt: str, context: dict) -> str:
     
   - So I should output exactly that format, no markdown fences. I'll just write the Python code plain.

   - Let me double-check the "Output FORMAT" section: "Output ONLY raw Python source. No markdown fences, no explanation, no preamble. Start directly with the module docstring or first import line."
   - So I'll output the Python code plain, starting maybe with a comment or docstring, then the variables. To be safe, I'll start with the PLUGIN_NAME line directly, or a module docstring. The spec says "Start directly with the module docstring or first import line." I'll start with a brief module docstring, then the variables. Or I can just start with `PLUGIN_NAME = ...`. I think starting with the variables is fine, as they are the first lines in the spec example.

   - I'll make sure there are no markdown fences. Just plain text Python code.

   - One thing: The spec says `PLUGIN_TRIGGERS` is required for ROUTER. I'll set it.
   - `PLUGIN_ROUTE_TOKEN` must not clash. "MAKULU" seems fine.
   - `PLUGIN_COMMANDS` optional but I'll include `["/makulu"]`.
   - `PLUGIN_REQUIRES` optional, I'll leave `[]`.
   - The `run` function must use `context["print_fn"]` for output, and return a string.
   - I'll use `context.get("print_fn", print)` as fallback, but ideally use it directly.

   - Let me draft the exact code block:

   ```python
   """Autorepair plugin providing MakuluLinux configuration guidance."""
   
   PLUGIN_NAME        = "MakuluLinux Config Helper"
   PLUGIN_VERSION     = "1.0.0"
   PLUGIN_DESCRIPTION = "Provides guidance for configuring MakuluLinux settings and system setup"
   PLUGIN_AUTHOR      = "Auto-repair System"
   PLUGIN_ENABLED     = True
   PLUGIN_TYPE        = "ROUTER"
   PLUGIN_TRIGGERS    = ["configure makulu", "makulu setup", "how do i configure makulu", "makulu config"]
   PLUGIN_ROUTE_TOKEN = "MAKULU"
   PLUGIN_COMMANDS    = ["/makulu"]
   PLUGIN_REQUIRES    = []
   
   def run(prompt: str, context: dict) -> str:
       try:
           print_fn = context.get("print_fn", print)
           user_home = context.get("user_home", "")
           
           print_fn("[MakuluLinux Config] Providing configuration guidance for MakuluLinux:")
           print_fn("• Display & Monitor settings: Use the 'Display' settings panel or `xrandr` for multi-monitor configuration.")
           print_fn("• Software Sources & Updates: Open 'Software & Updates' to manage repos, PPAs, and update preferences.")
           print_fn("• System Updates: Run `sudo apt update && sudo apt full-upgrade` in the terminal.")
           print_fn("• Desktop Theme & Appearance: Right-click desktop → 'Change Desktop Background' or use 'Appearance' settings.")
           print_fn("• Keyboard Shortcuts & Input: Configure via 'Keyboard' settings in the main menu.")
           print_fn("• Network Configuration: Use the Network Manager applet or `nmcli` for command-line setup.")
           print_fn("• Cinnamon-specific tweaks: Access additional options via 'Cinnamon Settings' (MakuluLinux uses Cinnamon/Xfce).")
           print_fn("• Package Management: All standard `apt` commands apply, as MakuluLinux is Ubuntu/Debian-based.")
           
           return "[MakuluLinux Config Helper] Configuration guidance delivered successfully."
       except Exception as e:
           return f"[MakuluLinux Config Helper] An error occurred: {str(e)}"
   
   - Check against critical rules:
     - PLUGIN_ROUTE_TOKEN doesn't clash (MAKULU is fine)
     - PLUGIN_ENABLED = True
     - PLUGIN_TYPE = "ROUTER"
     - run returns non-empty string
     - Uses context["print_fn"] 
     - Uses context.get("user_home", "") not hardcoded paths
     - Wrapped in try/except
     - No import from ai_terminal
     - No hardcoded usernames
     - Declares PLUGIN_REQUIRES if needed (empty here)
     - File will be auto-named: autorepair_maakulu.py? Actually "autorepair_<token_lowercase>.py" so "autorepair_makulu.py"

   - Looks good. I'll output just the Python code plain, no markdown fences.

   - One adjustment: The spec says "Start directly with the module docstring or first import line." I'll start with a module docstring line, then the variables. Or I can just start with `PLUGIN_NAME = ...` as the first line. To be safe, I'll add a simple docstring at the top, then the variables. But the spec example starts directly with `PLUGIN_NAME ...`. I think it's fine to start with `PLUGIN_NAME`. I'll just start with the variables. The docstring is optional. I'll include a comment/docstring at the very top maybe, but to follow "start directly with the module docstring or first import line", I'll start with a module docstring `"""Autorepair plugin..."""` then the variables. Actually, the spec's "Required Metadata" section starts with `PLUGIN_NAME ...` without a docstring. I'll just start with `PLUGIN_NAME = ...` as the first line. That matches "first import line" or "module docstring". I'll just start with `PLUGIN_NAME`.

   - Wait, the output format says: "Output ONLY raw Python source. No markdown fences, no explanation, no preamble. Start directly with the module docstring or first import line."
   - I'll output:
   ```python
   """Autorepair plugin for MakuluLinux configuration guidance."""
   
   PLUGIN_NAME        = "MakuluLinux Config Helper"
   ...
   
   - But to be safe and minimal, I'll just start with the PLUGIN_NAME line. Actually, many Python plugins start with a docstring. I'll include a brief docstring, it's fine. The instruction says "or first import line", so either is fine. I'll do a docstring then the variables.

   - Let me just output the code without any markdown formatting. I'll make sure there's no triple backticks. I'll just write the text.

   - Final check of the code logic: The `run` function uses `context.get("print_fn", print)` then calls `print_fn(...)`. That's correct per spec: "Use context["print_fn"](text) to show progressive output instead of print()". I'm using it, with a fallback just in case.

   - One thing: The spec says `context["print_fn"]` — it's expected to be present. I'll just use `context["print_fn"]` directly, but adding `.get` with fallback is safer and still compliant. I'll stick with `.get` to avoid KeyError if somehow missing, but the spec implies it's always there. I'll use `context["print_fn"]` to be strict, but fallback is fine. I'll use `context.get("print_fn", print)`.

   - Actually, reading spec: "Use context["print_fn"](text) to show progressive output instead of print()" — it's a directive, but using `.get` is pragmatic. I'll use `context["print_fn"]` directly to match exactly, but wrap in try/except maybe. The outer try/except covers it.

   - I'll just use `print_fn = context["print_fn"]` to be exact. But if print_fn is missing, it'll crash, which is covered by the outer try/except? The spec says "Wrap ALL external calls in try/except — plugin must never crash the host app". So using `context["print_fn"]` could crash if key missing, but the try/except would catch it and return error string. That's acceptable. I'll use `context["print_fn"]` for strict compliance.

   - Let me finalize the code.

   - One more thing: The triggers should match the user request type. The user requested "how do I configure makulu". So triggers like `["how do i configure makulu", "configure makulu", "makulu setup", "makulu config"]` are good.

   - I'll output the code now.</think>
"""Autorepair plugin for MakuluLinux configuration guidance."""

PLUGIN_NAME        = "MakuluLinux Config Helper"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Provides guidance for configuring MakuluLinux settings and system setup"
PLUGIN_AUTHOR      = "Auto-repair System"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "ROUTER"
PLUGIN_TRIGGERS    = ["how do i configure makulu", "configure makulu", "makulu setup", "makulu config"]
PLUGIN_ROUTE_TOKEN = "MAKULU"
PLUGIN_COMMANDS    = ["/makulu"]
PLUGIN_REQUIRES    = []

def run(prompt: str, context: dict) -> str:
    try:
        print_fn = context["print_fn"]
        user_home = context.get("user_home", "")

        print_fn("[MakuluLinux Config] Providing configuration guidance for MakuluLinux:")
        print_fn("• Display & Monitor settings: Use the 'Display' settings panel or `xrandr` for multi-monitor configuration.")
        print_fn("• Software Sources & Updates: Open 'Software & Updates' to manage repos, PPAs, and update preferences.")
        print_fn("• System Updates: Run `sudo apt update && sudo apt full-upgrade` in the terminal.")
        print_fn("• Desktop Theme & Appearance: Right-click desktop → 'Change Desktop Background' or use 'Appearance' settings.")
        print_fn("• Keyboard Shortcuts & Input: Configure via 'Keyboard' settings in the main menu.")
        print_fn("• Network Configuration: Use the Network Manager applet or `nmcli` for command-line setup.")
        print_fn("• Cinnamon-specific tweaks: Access additional options via 'Cinnamon Settings' (MakuluLinux uses Cinnamon/Xfce).")
        print_fn("• Package Management: All standard `apt` commands apply, as MakuluLinux is Ubuntu/Debian-based.")

        return "[MakuluLinux Config Helper] Configuration guidance delivered successfully."
    except Exception as e:
        return f"[MakuluLinux Config Helper] An error occurred: {str(e)}"