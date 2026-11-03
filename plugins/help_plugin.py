PLUGIN_NAME        = "Help & Plugin Manager"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Handles /help and /plugin slash commands — lists commands, plugins, and plugin status."
PLUGIN_AUTHOR      = "Electra AI Team"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "COMMAND"
PLUGIN_TRIGGERS    = []
PLUGIN_ROUTE_TOKEN = "HELP"
PLUGIN_COMMANDS    = ["/help", "/plugin"]
PLUGIN_REQUIRES    = []
import json
import os


def setup(config: dict) -> bool:
    """Called at load time with JSON config. Return False to disable plugin."""
    return True


def run(prompt: str, context: dict) -> str:
    """Not used for routing — COMMAND plugins return empty string."""
    return ""


def handle_command(command: str, args: str) -> bool:
    """Handle /help and /plugin slash commands. Return True if handled."""
    cmd = command.strip().lower()
    args = args.strip() if args else ""

    if cmd == "/help":
        _print_help(args)
        return True

    if cmd == "/plugin":
        _handle_plugin_subcommand(args)
        return True

    return False


def _print_help(args: str) -> None:
    """Print general help text."""
    help_text = (
        "Electra AI — Available Commands\n"
        "===============================\n"
        "/help              — Show this help message\n"
        "/plugin list       — List all loaded plugins\n"
        "/plugin reload     — Hot-reload all plugins\n"
        "/plugin <name>     — Show help for a specific plugin\n"
    )
    print(help_text)


def _handle_plugin_subcommand(args: str) -> None:
    """Handle /plugin subcommands: list, reload, or show plugin help."""
    if not args:
        print("Usage: /plugin list | /plugin reload | /plugin <plugin_name>")
        return

    sub = args.strip().lower()

    if sub == "list":
        _list_plugins()
    elif sub == "reload":
        print("[HELP] Plugin reload requested — use the app's /plugin reload command.")
    else:
        _show_plugin_help(sub)


def _list_plugins() -> None:
    """List all loaded plugins by introspecting this directory."""
    plugin_dir = os.path.dirname(os.path.abspath(__file__))
    print("Loaded Plugins:\n---------------")

    found_any = False
    for filename in sorted(os.listdir(plugin_dir)):
        if not filename.endswith(".py") or filename.startswith("_"):
            continue
        if filename.endswith(".disabled"):
            continue

        filepath = os.path.join(plugin_dir, filename)
        metadata = _parse_plugin_metadata(filepath)
        if metadata:
            found_any = True
            status = "enabled" if metadata.get("PLUGIN_ENABLED", True) else "disabled"
            ptype = metadata.get("PLUGIN_TYPE", "ROUTER")
            commands = metadata.get("PLUGIN_COMMANDS", [])
            cmds_str = ", ".join(commands) if commands else "(none)"
            print(
                f"  {metadata['PLUGIN_NAME']} v{metadata['PLUGIN_VERSION']} "
                f"[{ptype}] — {status}\n"
                f"    Commands: {cmds_str}\n"
                f"    {metadata.get('PLUGIN_DESCRIPTION', '')}\n"
            )

    if not found_any:
        print("  (no plugins found)")


def _show_plugin_help(name: str) -> None:
    """Show help for a specific plugin by name."""
    plugin_dir = os.path.dirname(os.path.abspath(__file__))
    for filename in sorted(os.listdir(plugin_dir)):
        if not filename.endswith(".py") or filename.startswith("_"):
            continue
        if filename.endswith(".disabled"):
            continue

        filepath = os.path.join(plugin_dir, filename)
        metadata = _parse_plugin_metadata(filepath)
        if metadata and metadata.get("PLUGIN_NAME", "").lower() == name.lower():
            print(
                f"{metadata['PLUGIN_NAME']} v{metadata['PLUGIN_VERSION']}\n"
                f"Type: {metadata.get('PLUGIN_TYPE', 'ROUTER')}\n"
                f"Description: {metadata.get('PLUGIN_DESCRIPTION', '')}\n"
                f"Author: {metadata.get('PLUGIN_AUTHOR', 'Unknown')}\n"
                f"Enabled: {metadata.get('PLUGIN_ENABLED', True)}\n"
                f"Commands: {', '.join(metadata.get('PLUGIN_COMMANDS', [])) or '(none)'}\n"
                f"Triggers: {', '.join(metadata.get('PLUGIN_TRIGGERS', [])) or '(none)'}\n"
            )
            return

    print(f"[HELP] Plugin '{name}' not found.")


def _parse_plugin_metadata(filepath: str) -> dict:
    """Parse PLUGIN_* metadata variables from a plugin source file."""
    metadata = {}
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line.startswith("PLUGIN_"):
                    if "=" in line:
                        key, _, value = line.partition("=")
                        key = key.strip()
                        value = value.strip().strip('"').strip("'")
                        # Try to parse list literals like ["a", "b"]
                        if value.startswith("[") and value.endswith("]"):
                            try:
                                value = json.loads(value.replace("'", '"'))
                            except Exception:
                                value = [v.strip().strip('"').strip("'") for v in value[1:-1].split(",") if v.strip()]
                        elif value == "True":
                            value = True
                        elif value == "False":
                            value = False
                        metadata[key] = value
    except Exception:
        return {}
    return metadata if metadata else None


def get_help() -> str:
    """Shown in /plugin list."""
    return f"{PLUGIN_NAME} v{PLUGIN_VERSION}: {PLUGIN_DESCRIPTION}"
