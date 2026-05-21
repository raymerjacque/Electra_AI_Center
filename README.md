# Electra AI Center — Plugin System Guide
**Connect with us on Discord:** https://discord.gg/rYdcWz3Ch6  
**A Project by MakuluLinux.com** | **HTML Guide:** https://makululinux.us/ai-terminal-guide.html

---

**Electra AI Terminal** is the AI assistant built into MakuluLinux. The core application is distributed as a compiled binary (`ai_terminal.bin`) to protect proprietary backend credentials. The **plugin system** is the open extension layer that allows the community to contribute new features, connect third-party APIs, and extend Electra's capabilities — all without access to the source code.

This is the **v2.0** plugin API. It is fully backward-compatible — all v1.0 plugins continue to work with zero changes.

---

## Table of Contents

1. [How the Plugin System Works](#1-how-the-plugin-system-works)
2. [Plugin Types — Overview](#2-plugin-types--overview)
3. [Plugin Directory](#3-plugin-directory)
4. [Required Fields — All Plugin Types](#4-required-fields--all-plugin-types)
5. [The context Dict — Full Reference](#5-the-context-dict--full-reference)
6. [ROUTER Plugin — Intercept Routing](#6-router-plugin--intercept-routing)
7. [AGENT Plugin — First-Class Routing Target](#7-agent-plugin--first-class-routing-target)
8. [HOOK Plugin — Lifecycle Events](#8-hook-plugin--lifecycle-events)
9. [COMMAND Plugin — Slash Commands Only](#9-command-plugin--slash-commands-only)
10. [Optional Functions — All Types](#10-optional-functions--all-types)
11. [Config Files — Storing API Keys](#11-config-files--storing-api-keys)
12. [Dependency Declaration — PLUGIN_REQUIRES](#12-dependency-declaration--plugin_requires)
13. [GUI Integration — Sidebar Panels & Toolbar Actions](#13-gui-integration--sidebar-panels--toolbar-actions)
14. [Inter-Plugin Communication](#14-inter-plugin-communication)
15. [How Plugins Connect to the Router](#15-how-plugins-connect-to-the-router)
16. [Managing Plugins](#16-managing-plugins)
17. [Plugin Coder Mode — Let AI Write Your Plugin](#17-plugin-coder-mode--let-ai-write-your-plugin)
18. [Writing Plugins Manually](#18-writing-plugins-manually)
19. [Complete Plugin Examples](#19-complete-plugin-examples)
20. [Testing and Debugging](#20-testing-and-debugging)
21. [Plugin Ideas and Use Cases](#21-plugin-ideas-and-use-cases)
22. [Rules and Best Practices](#22-rules-and-best-practices)
23. [Reserved Tokens](#23-reserved-tokens)
24. [Contributing](#24-contributing)

---

## 1. How the Plugin System Works

When Electra starts, it automatically scans `~/.config/ai_plugins/` and loads every `.py` file it finds. Each plugin is registered with the **routing agent** — the AI brain that decides what to do with every message you send — and optionally with the **lifecycle hook system**.

```
User types a message
        │
        ▼
  on_message_pre hooks  ← HOOK plugins can transform the prompt here
        │
        ▼
   Routing Agent
  (AI + keyword scan)
        │
        ├─── Core mode?      (Chat / Coder / Command / Google / etc.)
        ├─── AGENT plugin?   (first-class, same priority as core agents)
        └─── ROUTER plugin?  (community trigger match)
                    │
                    ▼
             Plugin's run()
                    │
                    ▼
  on_message_post hooks ← HOOK plugins observe the completed response
                    │
                    ▼
             Response to user
```

**Key properties:**
- Plugins are hot-reloadable — no restart needed (`/plugin reload`)
- `run()` returning `""` falls through to normal chat
- Plugin errors are caught per-plugin — they never crash the app
- AGENT plugins are indistinguishable from built-in agents to the router
- HOOK plugins run on lifecycle events without intercepting any routing

---

## 2. Plugin Types — Overview

v2.0 introduces five plugin types, declared with the `PLUGIN_TYPE` field (default: `"ROUTER"`).

| Type | Purpose | Intercepts routing? |
|---|---|---|
| `ROUTER` | Intercepts routing when trigger phrases match | Yes |
| `AGENT` | First-class routing target — identical to built-in agents (Google, Discord, etc.) | Yes |
| `HOOK` | Lifecycle events: startup, shutdown, mode change, file writes, pre/post message | No |
| `COMMAND` | Registers slash commands only, no routing involvement | No |
| `EVENT` | Responds to app events, never appears in the router | No |

All existing v1.0 plugins are treated as `PLUGIN_TYPE = "ROUTER"` automatically.

---

## 3. Plugin Directory

All plugins live in:

```
~/.config/ai_plugins/
```

This directory is created automatically the first time Electra runs.

| File | Purpose |
|---|---|
| `PLUGIN_SPEC.md` | Full API spec (auto-generated on first run) |
| `example_plugin.py.disabled` | Skeleton template (rename to `.py` to enable) |
| `your_plugin.py` | Your plugin file |
| `YOUR_TOKEN.json` | Config/credentials for your plugin |

**File name rules:**
- Must end in `.py`
- Files starting with `_` are ignored (use for private helper modules)
- Files ending in `.disabled` are ignored
- The file name is cosmetic — the plugin identifies itself via `PLUGIN_ROUTE_TOKEN`

---

## 4. Required Fields — All Plugin Types

Every plugin must declare these variables regardless of type:

| Field | Type | Description |
|---|---|---|
| `PLUGIN_NAME` | `str` | Human-readable display name |
| `PLUGIN_VERSION` | `str` | Semantic version string, e.g. `"1.0.0"` |
| `PLUGIN_DESCRIPTION` | `str` | One-line summary injected into the router AI's context |
| `PLUGIN_AUTHOR` | `str` | Optional author name or GitHub handle |
| `PLUGIN_ENABLED` | `bool` | `False` disables without deleting the file |
| `PLUGIN_TYPE` | `str` | `"ROUTER"` \| `"AGENT"` \| `"HOOK"` \| `"COMMAND"` \| `"EVENT"` — defaults to `"ROUTER"` |
| `PLUGIN_TRIGGERS` | `list[str]` | Routing phrases. Use `[]` for HOOK/COMMAND/EVENT types |
| `PLUGIN_ROUTE_TOKEN` | `str` | Unique ALL_CAPS identifier. Must be unique across all plugins |
| `PLUGIN_COMMANDS` | `list[str]` | Slash commands registered to this plugin. Use `[]` for none |
| `PLUGIN_REQUIRES` | `list[str]` | Optional. Pip packages needed, e.g. `["feedparser>=6.0"]` |

---

## 5. The `context` Dict — Full Reference

Every `run()` call receives a `context` dict. v2.0 adds 8 new keys (all backward-compatible):

```python
def run(prompt: str, context: dict) -> str:
    # ── Original keys (v1.0) ───────────────────────────────────────────────
    context["user_home"]        # str  — os.path.expanduser("~")
    context["plugin_dir"]       # str  — ~/.config/ai_plugins
    context["chat_history"]     # list — recent [{role, content}] dicts (read-only)
    context["conversation_id"]  # str  — current session conversation ID
    context["model"]            # str  — currently selected model ID

    # ── New keys (v2.0) ────────────────────────────────────────────────────
    context["current_mode"]     # str  — active phase: CHAT, CODER, WRITER, PLUGIN…
    context["cwd"]              # str  — current working directory
    context["gui_active"]       # bool — True when GUI (electra_gui) is running
    context["telegram_active"]  # bool — True when Telegram bridge is running
    context["session_id"]       # str  — unique UUID for this app launch
    context["print_fn"]         # callable(str) — print with Rich Markdown rendering
    context["notify_panel"]     # callable — register/update a GUI sidebar panel
    context["plugins"]          # dict — {TOKEN: module} of all loaded plugins
```

### Using `print_fn` for progressive output

Instead of building a full response string, use `print_fn` to output progressively (streaming feel):

```python
def run(prompt: str, context: dict) -> str:
    out = context["print_fn"]
    out("Fetching data…")
    data = fetch_something()
    out(f"**Result:** {data}")
    return ""   # already printed — return empty to skip double output
```

---

## 6. ROUTER Plugin — Intercept Routing

The original plugin type. When the routing agent matches a trigger phrase, your `run()` is called.

```python
"""
A minimal ROUTER plugin.
"""
import requests

PLUGIN_NAME        = "My Router Plugin"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "One-line summary shown in the router and /plugin list"
PLUGIN_AUTHOR      = "YourName"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "ROUTER"          # default — can be omitted for v1 compat

PLUGIN_TRIGGERS    = ["ask groq", "use groq", "groq:"]
PLUGIN_ROUTE_TOKEN = "GROQ"
PLUGIN_COMMANDS    = ["/groq"]
PLUGIN_REQUIRES    = ["requests"]      # optional — requests is always available

def run(prompt: str, context: dict) -> str:
    """
    Called when the router sends traffic here.
    Return a response string (Markdown supported), or "" to fall through to chat.
    """
    return f"[My Plugin] You asked: {prompt}"
```

### Choosing good trigger phrases

Triggers are matched using substring matching against the lowercased user input. Choose phrases specific enough that they won't intercept messages meant for core modes.

```python
# ✅ Good — specific, unlikely to conflict
PLUGIN_TRIGGERS = ["ask groq", "use groq", "groq:", "via groq"]

# ⚠️  Too broad — will steal normal chat messages
PLUGIN_TRIGGERS = ["ask", "search", "help"]

# ✅ Good — product name + action verb
PLUGIN_TRIGGERS = ["openai:", "use gpt", "ask gpt", "gpt-4o"]
```

---

## 7. AGENT Plugin — First-Class Routing Target

AGENT plugins are indistinguishable from built-in agents (Google, Discord, Spotify, etc.) from the router's perspective. They get the same routing priority, the same label in routing output, and no "community plugin" label. Use this type when your plugin is a full feature agent rather than a quick intercept.

```python
"""
An AGENT plugin — first-class routing target.
"""
import requests

PLUGIN_NAME        = "OpenWeatherMap Agent"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Live weather and 7-day forecast via OpenWeatherMap"
PLUGIN_AUTHOR      = "YourName"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "AGENT"           # ← makes this first-class

PLUGIN_TRIGGERS    = ["weather", "forecast", "temperature outside",
                      "will it rain", "how hot", "how cold"]
PLUGIN_ROUTE_TOKEN = "MY_WEATHER"
PLUGIN_COMMANDS    = ["/weather"]
PLUGIN_REQUIRES    = ["requests"]

_API_KEY = ""
_BASE    = "https://api.openweathermap.org/data/2.5"

def setup(config: dict) -> bool:
    global _API_KEY
    _API_KEY = config.get("api_key", "")
    return bool(_API_KEY)

def run(prompt: str, context: dict) -> str:
    out = context["print_fn"]
    out("Checking weather…")
    try:
        city = _extract_city(prompt) or "London"
        r = requests.get(f"{_BASE}/weather",
                         params={"q": city, "appid": _API_KEY, "units": "metric"},
                         timeout=10)
        r.raise_for_status()
        d = r.json()
        return (
            f"## Weather in {d['name']}\n"
            f"**{d['weather'][0]['description'].title()}**  \n"
            f"Temp: {d['main']['temp']}°C  |  "
            f"Feels like: {d['main']['feels_like']}°C  \n"
            f"Humidity: {d['main']['humidity']}%  |  "
            f"Wind: {d['wind']['speed']} m/s"
        )
    except Exception as e:
        return f"[Weather] Error: {e}"

def _extract_city(prompt: str) -> str:
    import re
    m = re.search(r'(?:in|for|at)\s+([A-Za-z\s]+)', prompt)
    return m.group(1).strip() if m else ""

def handle_command(command: str, args: str) -> bool:
    if command == "/weather":
        print(run(args or "weather London", {}))
        return True
    return False
```

**What the router sees (after loading this plugin):**

```
# AGENT PLUGINS — first-class routing targets (treat like GOOGLE/DISCORD):
MY_WEATHER             — Live weather and 7-day forecast. Triggers: "weather", "forecast"...

# COMMUNITY PLUGINS — route to these tokens when triggers match:
GROQ                   — Route queries to Groq API. Triggers: "ask groq", "use groq"...
```

---

## 8. HOOK Plugin — Lifecycle Events

HOOK plugins never intercept routing. They listen to app lifecycle events and can run code on startup, shutdown, mode changes, file writes, and before/after every message. Set `PLUGIN_TRIGGERS = []` — the router ignores them completely.

### Available lifecycle functions

Define only the ones you need — all are optional:

| Function | Signature | When called |
|---|---|---|
| `on_startup` | `(context: dict)` | Once after all plugins finish loading |
| `on_shutdown` | `(context: dict)` | On clean app exit (via `atexit`) |
| `on_mode_change` | `(old_mode: str, new_mode: str)` | Every time the active mode switches |
| `on_file_write` | `(path: str, content: str)` | After every successful file write in Coder mode |
| `on_message_pre` | `(prompt: str) -> str` | Before routing — return modified prompt or `""` to leave unchanged |
| `on_message_post` | `(prompt: str, response: str)` | After each completed response |

```python
"""
Example HOOK plugin — activity logger.
Logs every mode switch, file write, and message to ~/.electra/plugin_activity.log
"""
import os
import datetime

PLUGIN_NAME        = "Activity Logger"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Logs mode changes, file writes, and messages to a log file"
PLUGIN_AUTHOR      = "YourName"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "HOOK"

PLUGIN_TRIGGERS    = []        # ← HOOK plugins never intercept routing
PLUGIN_ROUTE_TOKEN = "ACTIVITY_LOG"
PLUGIN_COMMANDS    = []
PLUGIN_REQUIRES    = []

_LOG_FILE = os.path.join(os.path.expanduser("~"), ".electra", "plugin_activity.log")

def _log(msg: str):
    try:
        os.makedirs(os.path.dirname(_LOG_FILE), exist_ok=True)
        ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(_LOG_FILE, "a") as f:
            f.write(f"[{ts}] {msg}\n")
    except Exception:
        pass

def run(prompt: str, context: dict) -> str:
    return ""   # HOOK plugins always return "" — they don't handle routing

def on_startup(context: dict):
    _log(f"App started — session {context.get('session_id', '')[:8]}  "
         f"model={context.get('model', '?')}  "
         f"gui={context.get('gui_active', False)}")

def on_shutdown(context: dict):
    _log("App exiting cleanly.")

def on_mode_change(old_mode: str, new_mode: str):
    _log(f"Mode: {old_mode} → {new_mode}")

def on_file_write(path: str, content: str):
    lines = len(content.splitlines())
    _log(f"File written: {path}  ({lines} lines)")

def on_message_pre(prompt: str) -> str:
    """
    Example: silently strip a profanity word before routing.
    Return "" to leave the prompt unchanged, or a modified string.
    """
    return ""   # pass through unchanged

def on_message_post(prompt: str, response: str):
    words = len(response.split())
    _log(f"Response: {words} words  |  prompt[:60]={prompt[:60]!r}")
```

---

## 9. COMMAND Plugin — Slash Commands Only

Use COMMAND type when you only need slash commands and no routing involvement.

```python
"""
Quick system shortcuts as slash commands.
"""
import subprocess

PLUGIN_NAME        = "Dev Tools"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Developer shortcuts — git status, docker ps, etc."
PLUGIN_AUTHOR      = "YourName"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "COMMAND"

PLUGIN_TRIGGERS    = []        # no routing
PLUGIN_ROUTE_TOKEN = "DEVTOOLS"
PLUGIN_COMMANDS    = ["/gs", "/dp", "/sysinfo"]
PLUGIN_REQUIRES    = []

def run(prompt: str, context: dict) -> str:
    return ""   # COMMAND plugins don't handle routing

def _sh(cmd: str) -> str:
    try:
        return subprocess.check_output(
            cmd, shell=True, stderr=subprocess.STDOUT,
            timeout=10, text=True
        ).strip() or "(no output)"
    except Exception as e:
        return f"Error: {e}"

def handle_command(command: str, args: str) -> bool:
    if command == "/gs":
        print(_sh("git status"))
        return True
    if command == "/dp":
        print(_sh("docker ps --format 'table {{.Names}}\t{{.Status}}'"))
        return True
    if command == "/sysinfo":
        print(_sh("uptime && free -h && df -h /"))
        return True
    return False

def get_help() -> str:
    return (
        "Dev Tools: quick system shortcuts\n"
        "  /gs       — git status\n"
        "  /dp       — docker ps\n"
        "  /sysinfo  — uptime, memory, disk"
    )
```

---

## 10. Optional Functions — All Types

These functions can be defined in any plugin type:

### `setup(config: dict) -> bool`

Called once at load time (and on `/plugin reload`). `config` is loaded automatically from `~/.config/ai_plugins/<TOKEN>.json`.

```python
_API_KEY = ""

def setup(config: dict) -> bool:
    global _API_KEY
    _API_KEY = config.get("api_key", "")
    if not _API_KEY:
        print("[My Plugin] No api_key in config — plugin disabled.")
        return False
    return True
```

Returning `False` disables the plugin silently.

### `handle_command(command: str, args: str) -> bool`

Intercepts slash commands from `PLUGIN_COMMANDS`. Return `True` if handled, `False` to fall back to `run()`.

```python
def handle_command(command: str, args: str) -> bool:
    if command == "/groq":
        if not args:
            print("[Groq] Usage: /groq <question>")
        else:
            print(run(args, {}))
        return True
    return False
```

### `get_help() -> str`

Return a multi-line string shown in `/plugin list`.

```python
def get_help() -> str:
    return (
        f"{PLUGIN_NAME} v{PLUGIN_VERSION}: {PLUGIN_DESCRIPTION}\n"
        f"  Triggers : {', '.join(PLUGIN_TRIGGERS)}\n"
        f"  Commands : {', '.join(PLUGIN_COMMANDS)}"
    )
```

---

## 11. Config Files — Storing API Keys

Never hardcode credentials in your plugin. Store them in a JSON file:

**Location:** `~/.config/ai_plugins/<PLUGIN_ROUTE_TOKEN>.json`

**Example** for `PLUGIN_ROUTE_TOKEN = "GROQ"`:

`~/.config/ai_plugins/GROQ.json`:
```json
{
    "api_key": "gsk_yourkeyhere",
    "base_url": "https://api.groq.com/openai/v1",
    "default_model": "llama3-8b-8192",
    "temperature": 0.7
}
```

The `config` dict is loaded automatically and passed to `setup()`. You do not need to open the file yourself.

---

## 12. Dependency Declaration — PLUGIN_REQUIRES

Declare any non-standard packages your plugin needs. The loader checks them at load time and warns the user if they're missing — without crashing the load.

```python
PLUGIN_REQUIRES = ["feedparser>=6.0", "beautifulsoup4"]
```

The loader strips version specifiers to check import availability and prints a clear install hint:

```
[Plugins] ⚠  RSS Reader: missing deps ['feedparser>=6.0'] — install with:
              pip install feedparser>=6.0
```

Always install in the plugin `setup()` or document the requirement:

```python
PLUGIN_REQUIRES = ["feedparser"]

def setup(config: dict) -> bool:
    try:
        import feedparser  # noqa
    except ImportError:
        print("[RSS] Install feedparser:  pip3 install feedparser")
        return False
    return True
```

**Always available (no declaration needed):**  
Full Python 3 standard library · `requests` · `json` · `os` · `re` · `subprocess` · `threading` · `datetime` · `uuid`

---

## 13. GUI Integration — Sidebar Panels & Toolbar Actions

When the user runs Electra in GUI mode (`/gui` or `--gui`), plugins can add a **sidebar panel** and **header bar buttons**.

### Sidebar panel

Call `context["notify_panel"]()` from any hook or `run()` function:

```python
def on_startup(context: dict):
    if context.get("gui_active"):
        context["notify_panel"](
            token        = PLUGIN_ROUTE_TOKEN,
            label        = "Weather",        # tab label (≤14 chars)
            content      = get_panel_text,   # callable() -> str, or a plain str
            refresh_s    = 300,              # auto-refresh every 5 minutes (0 = manual)
        )

def get_panel_text() -> str:
    # Called every time the panel refreshes
    return "🌤 London: 18°C  |  Partly cloudy"
```

The panel appears as a tab in the **PLUGINS** section at the bottom of the sidebar. A refresh button lets the user manually update it. The separator and header are hidden when no plugins have registered panels.

You can also register a panel from `run()` to update it after every response:

```python
def run(prompt: str, context: dict) -> str:
    result = do_work(prompt)
    # Update the sidebar with latest status
    if context.get("gui_active"):
        context["notify_panel"](
            PLUGIN_ROUTE_TOKEN,
            "My Plugin",
            f"Last query: {prompt[:40]}\nResult: {result[:80]}",
        )
    return result
```

### Header bar toolbar buttons

Pass a `toolbar_actions` list to `notify_panel`:

```python
def on_startup(context: dict):
    if context.get("gui_active"):
        context["notify_panel"](
            token           = PLUGIN_ROUTE_TOKEN,
            label           = "Weather",
            content         = get_panel_text,
            refresh_s       = 300,
            toolbar_actions = [
                {"label": "Weather Now", "icon": "weather-clear-symbolic", "command": "/weather now"},
                {"label": "Forecast",    "icon": "x-office-calendar-symbolic", "command": "/weather forecast"},
            ]
        )
```

Each action renders as a small button in the header bar. Clicking it sends the `command` string to the backend exactly as if the user had typed it.

### `get_gui_panel()` — declarative alternative

Alternatively, declare the panel statically:

```python
def get_gui_panel() -> dict:
    return {
        "label":      "My Panel",
        "content_fn": lambda: f"Status: {_get_live_status()}",
        "refresh_s":  60,
    }
```

---

## 14. Inter-Plugin Communication

Plugins can call each other via `context["plugins"]` — a read-only dict of `{TOKEN: module}` for all currently loaded plugins.

```python
def run(prompt: str, context: dict) -> str:
    plugins = context.get("plugins", {})

    # Check if another plugin is loaded before calling it
    groq = plugins.get("GROQ")
    if groq and hasattr(groq, "run"):
        return groq.run(prompt, context)

    # Fall through if the other plugin isn't available
    return "[My Plugin] Groq plugin not loaded."
```

This is useful for orchestrator plugins that delegate to specialised plugins depending on the prompt content.

---

## 15. How Plugins Connect to the Router

### Strategy 1 — Fast local keyword scan

The app scans every message against all loaded plugin `PLUGIN_TRIGGERS` lists instantly, with no AI call. AGENT plugin triggers are checked alongside built-in agent triggers.

### Strategy 2 — AI router with full plugin context

If the keyword scan is inconclusive, the router AI is called. The app dynamically appends all loaded plugins to the router's system prompt in two sections:

```
# AGENT PLUGINS — first-class routing targets (treat like GOOGLE/DISCORD):
MY_WEATHER             — Live weather and forecast. Triggers: "weather", "forecast"...

# COMMUNITY PLUGINS — route to these tokens when triggers match:
GROQ                   — Route queries to Groq API. Triggers: "ask groq", "use groq"...
CRYPTO                 — Live crypto prices from CoinGecko. Triggers: "btc price"...
```

HOOK, COMMAND, and EVENT plugins are never shown to the router — they have no routing presence whatsoever.

---

## 16. Managing Plugins

All plugin management happens via the `/plugin` command.

### Quick Reference

| Command | Action |
|---|---|
| `/plugin` | Enter Plugin Coder Mode (AI writes/edits plugins) |
| `/plugin list` | Show all loaded plugins with type, triggers, and commands |
| `/plugin reload` | Hot-reload all plugins — no restart needed |
| `/plugin test GROQ hello` | Directly call `GROQ.run("hello", ctx)` |
| `/plugin install <file>` | Download a plugin from the community GitHub repo |
| `/plugin publish <file>` | Submit a plugin to the community GitHub repo |
| `/plugin sync` | Pull all new community plugins from GitHub |
| `/plugin community` | Browse the community plugin hub |
| `/plugin spec` | Open the full API spec |
| `/plugin dir` | Open `~/.config/ai_plugins/` in Nemo |

### Installing a plugin manually

1. Place your `.py` file in `~/.config/ai_plugins/`
2. If it needs credentials, create `~/.config/ai_plugins/<TOKEN>.json`
3. Type `/plugin reload` — done

### Disabling a plugin

- Set `PLUGIN_ENABLED = False` in the plugin file, then `/plugin reload`
- Rename the file to `pluginname.py.disabled`
- Delete the file entirely

---

## 17. Plugin Coder Mode — Let AI Write Your Plugin

Plugin Coder Mode is a specialized AI coding environment where Electra knows the full v2.0 plugin API and writes complete, working plugins for you.

### Entering Plugin Coder Mode

**Option A — Enter mode, then describe:**
```
/plugin
> write a HOOK plugin that logs every file the AI writes to a CSV file
```

**Option B — Inline:**
```
/plugin create a weather AGENT plugin using OpenWeatherMap API
```

**Option C — Edit an existing plugin:**
```
/plugin edit my groq plugin and add on_mode_change support to pause it in Coder mode
```

The AI knows all five plugin types, all lifecycle hooks, the full context dict, and all v2.0 features. Just describe what you want in plain English.

### Example session

```
> /plugin
[Plugin Coder Mode activated]

> write an AGENT plugin for crypto prices that also shows a GUI sidebar panel

[AI writes crypto_agent.py and saves it]

> add on_startup so it registers the panel automatically when GUI loads

[AI edits the file]

> /plugin reload
[2 plugin(s) loaded]

> btc price
[Your AGENT plugin responds, panel appears in GUI sidebar]

> /chat
[Returns to normal chat]
```

---

## 18. Writing Plugins Manually

### Step 1 — Create the file

```bash
nano ~/.config/ai_plugins/my_plugin.py
```

### Step 2 — Choose your type and write the plugin

Use the templates in Sections 6–9 as your starting point.

### Step 3 — Create config if needed

```bash
nano ~/.config/ai_plugins/MY_PLUGIN.json
```
```json
{ "api_key": "your-key-here" }
```

### Step 4 — Load it

```
/plugin reload
```

### Step 5 — Test it

```
/plugin test MY_PLUGIN hello world
```

Or type one of your trigger phrases normally.

---

## 19. Complete Plugin Examples

### Example 1 — Groq API Connector (ROUTER)

`~/.config/ai_plugins/GROQ.json`:
```json
{
    "api_key": "gsk_your_key_here",
    "default_model": "llama3-8b-8192"
}
```

`~/.config/ai_plugins/groq_connector.py`:
```python
"""
Plugin Name: Groq Connector
Author: Community
Description: Route queries to Groq's fast inference API.

Setup:
  1. Get a free API key at https://console.groq.com
  2. Create ~/.config/ai_plugins/GROQ.json:
     {"api_key": "gsk_your_key_here"}
  3. /plugin reload

Triggers: ask groq | use groq | groq: | via groq
Commands: /groq
"""
import requests

PLUGIN_NAME        = "Groq Connector"
PLUGIN_VERSION     = "1.1.0"
PLUGIN_DESCRIPTION = "Route queries to Groq API (llama3, mixtral, gemma)"
PLUGIN_AUTHOR      = "Community"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "ROUTER"

PLUGIN_TRIGGERS    = ["ask groq", "use groq", "via groq", "groq:"]
PLUGIN_ROUTE_TOKEN = "GROQ"
PLUGIN_COMMANDS    = ["/groq"]
PLUGIN_REQUIRES    = ["requests"]

_API_KEY = ""
_MODEL   = "llama3-8b-8192"
_URL     = "https://api.groq.com/openai/v1/chat/completions"

def setup(config: dict) -> bool:
    global _API_KEY, _MODEL
    _API_KEY = config.get("api_key", "")
    _MODEL   = config.get("default_model", _MODEL)
    return bool(_API_KEY)

def run(prompt: str, context: dict) -> str:
    clean = prompt
    for t in PLUGIN_TRIGGERS:
        if clean.lower().startswith(t):
            clean = clean[len(t):].strip(" :")

    messages = []
    for turn in context.get("chat_history", [])[-4:]:
        if turn.get("role") in ("user", "assistant"):
            messages.append(turn)
    messages.append({"role": "user", "content": clean})

    try:
        resp = requests.post(
            _URL,
            json={"model": _MODEL, "messages": messages, "temperature": 0.7},
            headers={"Authorization": f"Bearer {_API_KEY}"},
            timeout=60,
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[Groq] Error: {e}"

def handle_command(command: str, args: str) -> bool:
    if command == "/groq":
        if not args:
            print(f"[Groq] Usage: /groq <question>  |  Model: {_MODEL}")
        else:
            print(run(args, {}))
        return True
    return False

def get_help() -> str:
    return f"Groq Connector: fast llama3/mixtral inference. Model: {_MODEL}"
```

**Usage:** `ask groq what is quantum computing?` · `/groq explain binary trees`

---

### Example 2 — CoinGecko Crypto Prices (AGENT + GUI Panel)

`~/.config/ai_plugins/crypto_agent.py`:
```python
"""
Plugin Name: Crypto Agent
Description: Live crypto prices from CoinGecko with GUI sidebar panel.
No API key required.
"""
import requests

PLUGIN_NAME        = "Crypto Agent"
PLUGIN_VERSION     = "2.0.0"
PLUGIN_DESCRIPTION = "Live cryptocurrency prices from CoinGecko"
PLUGIN_AUTHOR      = "Community"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "AGENT"           # first-class routing — same as GOOGLE/DISCORD

PLUGIN_TRIGGERS    = ["crypto price", "bitcoin price", "btc price",
                      "eth price", "ethereum price", "coin price",
                      "price of btc", "price of eth", "how much is btc"]
PLUGIN_ROUTE_TOKEN = "CRYPTO"
PLUGIN_COMMANDS    = ["/crypto"]
PLUGIN_REQUIRES    = []

PLUGIN_TOOLBAR_ACTIONS = [
    {"label": "BTC Price", "icon": "go-up-symbolic",  "command": "btc price"},
    {"label": "ETH Price", "icon": "go-up-symbolic",  "command": "eth price"},
]

_COIN_MAP = {
    "btc": "bitcoin",  "bitcoin": "bitcoin",
    "eth": "ethereum", "ethereum": "ethereum",
    "sol": "solana",   "solana": "solana",
    "bnb": "binancecoin", "xrp": "ripple",
    "ada": "cardano",  "doge": "dogecoin",
}
_last_prices = {}

def on_startup(context: dict):
    if context.get("gui_active"):
        context["notify_panel"](
            token           = PLUGIN_ROUTE_TOKEN,
            label           = "Crypto",
            content         = _panel_content,
            refresh_s       = 120,
            toolbar_actions = PLUGIN_TOOLBAR_ACTIONS,
        )

def _panel_content() -> str:
    if not _last_prices:
        return "No prices fetched yet.\nType 'btc price' to start."
    lines = []
    for coin, info in _last_prices.items():
        chg   = info.get("usd_24h_change", 0)
        arrow = "↑" if chg >= 0 else "↓"
        lines.append(f"{coin.title()}: ${info['usd']:,.2f}  {arrow}{abs(chg):.1f}%")
    return "\n".join(lines)

def run(prompt: str, context: dict) -> str:
    p = prompt.lower()
    found = None
    for symbol, coin_id in _COIN_MAP.items():
        if symbol in p:
            found = coin_id
            break
    if not found:
        return "[Crypto] Couldn't identify coin. Try: 'btc price' or '/crypto eth'"
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": found, "vs_currencies": "usd",
                    "include_24hr_change": "true"},
            timeout=10,
        )
        r.raise_for_status()
        data = r.json().get(found, {})
        _last_prices[found] = data
        price = data.get("usd", "N/A")
        chg   = data.get("usd_24h_change", 0)
        arrow = "📈" if chg >= 0 else "📉"
        # Refresh the GUI panel with latest data
        if context.get("gui_active"):
            context["notify_panel"](PLUGIN_ROUTE_TOKEN, "Crypto", _panel_content)
        return (
            f"**{found.title()}**\n"
            f"  Price : ${price:,.2f} USD\n"
            f"  24h   : {arrow} {chg:+.2f}%"
        )
    except Exception as e:
        return f"[Crypto] Error: {e}"

def handle_command(command: str, args: str) -> bool:
    if command == "/crypto":
        print(run(args or "btc price", {}))
        return True
    return False
```

**Usage:** `btc price` · `ethereum price` · `/crypto sol` · GUI panel auto-updates every 2 min

---

### Example 3 — Session Logger (HOOK)

`~/.config/ai_plugins/session_logger.py`:
```python
"""
Logs every mode change and file write for the current session.
No routing involvement — pure HOOK plugin.
"""
import os, datetime

PLUGIN_NAME        = "Session Logger"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Logs mode switches and file writes to ~/.electra/session.log"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "HOOK"
PLUGIN_TRIGGERS    = []
PLUGIN_ROUTE_TOKEN = "SESSION_LOG"
PLUGIN_COMMANDS    = []

_LOG = os.path.join(os.path.expanduser("~"), ".electra", "session.log")

def _w(msg):
    os.makedirs(os.path.dirname(_LOG), exist_ok=True)
    ts = datetime.datetime.now().strftime("%H:%M:%S")
    with open(_LOG, "a") as f:
        f.write(f"[{ts}] {msg}\n")

def run(prompt, context): return ""

def on_startup(context):
    _w(f"=== Session started  model={context.get('model','?')} "
       f"gui={context.get('gui_active',False)} ===")

def on_shutdown(context):
    _w("=== Session ended ===")

def on_mode_change(old, new):
    _w(f"Mode: {old} → {new}")

def on_file_write(path, content):
    _w(f"Wrote: {path}  ({len(content.splitlines())} lines)")
```

---

## 20. Testing and Debugging

### Test directly

```
/plugin test GROQ what is machine learning?
/plugin test CRYPTO btc price
/plugin test MY_HOOK on_startup
```

### Check if your plugin loaded

```
/plugin list
```

If it isn't listed, check the terminal output for load errors:

```bash
/usr/share/MakuluSetup/tools/ai_terminal.bin
# or
python3 /path/to/ai_terminal.py
```

**Common load failures:**

| Symptom | Cause |
|---|---|
| Missing from `/plugin list` | Missing required variable or `run()` |
| `setup() failed` | `setup()` returned `False` — usually missing API key |
| `missing deps [...]` | `PLUGIN_REQUIRES` package not installed |
| Duplicate token warning | Another plugin uses the same `PLUGIN_ROUTE_TOKEN` |
| Syntax error | Python syntax error in plugin file |

### Hot reload after edits

```
/plugin reload
```

No restart needed. Changes to any plugin file take effect immediately. `on_startup` hooks fire again for newly loaded HOOK plugins.

### Open plugin directory

```
/plugin dir
```

Opens `~/.config/ai_plugins/` in Nemo.

### Error output

If `run()` raises an exception, it's caught and shown:
```
[Plugin: My Plugin] Error in run(): ConnectionTimeout
```
The app falls through to normal chat. Your plugin can never crash Electra.

---

## 21. Plugin Ideas and Use Cases

### AGENT Plugins (first-class features)
- **OpenAI** — GPT-4o, o1, o3 models
- **Anthropic** — Claude models directly
- **Groq** — Ultra-fast llama3 / mixtral inference
- **Together AI** — 50+ open-source models
- **Perplexity** — Web-grounded answers
- **Weather** — OpenWeatherMap / WeatherAPI
- **News** — NewsAPI with GUI panel showing headlines

### HOOK Plugins (observability & automation)
- **Session logger** — Log all mode changes, file writes, prompts
- **Backup trigger** — Run a backup when Coder writes to certain paths
- **Prompt guard** — Sanitise or translate prompts in `on_message_pre`
- **Analytics** — Track usage patterns per mode
- **Notification** — Push phone notification on Coder session complete

### ROUTER/COMMAND Plugins (quick integrations)
- **Crypto prices** — CoinGecko, Binance
- **Stock ticker** — Yahoo Finance, Alpha Vantage
- **Earthquake alerts** — USGS live feed
- **Home Assistant** — Lights, switches, climate
- **Tasmota / MQTT** — Generic IoT
- **Notion / Obsidian** — Read/write notes
- **Todoist / Taskwarrior** — Task management
- **Plex / Jellyfin** — Media server control
- **Jira / Linear** — Ticket lookup

### MakuluLinux-Specific
- **System monitor** — CPU/RAM/disk with GUI panel
- **Timeshift** — Snapshot info and trigger
- **Package watcher** — Pending updates notification
- **Nemo integration** — File operations via chat

---

## 22. Rules and Best Practices

### Always do these

```python
# ✅ Read credentials from config — never hardcode
def setup(config: dict) -> bool:
    global _API_KEY
    _API_KEY = config.get("api_key", "")
    return bool(_API_KEY)

# ✅ Wrap all external calls in try/except
def run(prompt: str, context: dict) -> str:
    try:
        resp = requests.get("https://api.example.com/data", timeout=10)
        resp.raise_for_status()
        return resp.json()["result"]
    except requests.exceptions.Timeout:
        return "[My Plugin] Request timed out."
    except Exception as e:
        return f"[My Plugin] Error: {e}"

# ✅ Return "" to fall through when you can't handle it
def run(prompt: str, context: dict) -> str:
    if "my trigger" not in prompt.lower():
        return ""   # let normal chat handle it
    return do_work(prompt)

# ✅ Use context["print_fn"] for progressive output
def run(prompt: str, context: dict) -> str:
    out = context["print_fn"]
    out("Fetching data…")
    result = fetch_slowly()
    out(f"**Done:** {result}")
    return ""

# ✅ Use context["user_home"] — never hardcode paths or usernames
log = os.path.join(context["user_home"], ".electra", "my_plugin.log")

# ✅ Declare external packages in PLUGIN_REQUIRES
PLUGIN_REQUIRES = ["feedparser>=6.0"]

# ✅ For HOOK/COMMAND/EVENT: set PLUGIN_TRIGGERS = []
PLUGIN_TYPE    = "HOOK"
PLUGIN_TRIGGERS = []
```

### Never do these

```python
# ❌ Never hardcode credentials
_API_KEY = "sk-abc123..."

# ❌ Never use broad triggers (will steal normal chat)
PLUGIN_TRIGGERS = ["the", "what", "how", "search", "help"]

# ❌ Never use a reserved token
PLUGIN_ROUTE_TOKEN = "CHAT"     # core mode
PLUGIN_ROUTE_TOKEN = "GOOGLE"   # built-in agent

# ❌ Never import from ai_terminal — it's a closed binary
from ai_terminal import something

# ❌ Never hardcode usernames or absolute user paths
open("/home/jacque/.myfile")    # use context["user_home"] instead
```

---

## 23. Reserved Tokens

Do not use any of the following as your `PLUGIN_ROUTE_TOKEN` — they are taken by core modes and built-in agents:

```
CHAT          CODER         WRITER        COMMAND       LIVE
IMAGE         VIDEO         AUDIO         TRAVEL        NOVEL
PLAN          PLUGIN        GOOGLE        HOME_ASSISTANT
RSS           GITHUB_AGENT  SPOTIFY       DISCORD       REDDIT
FINANCE       TELEGRAM_SERVICE            AGENT_SERVICE
ISO_AGENT     APP_AGENT     NVIDIA_AGENT  TROUBLESHOOT
ASK_COMMAND   ASK_CODER
```

---

## 24. Contributing

### Submitting a plugin

1. Test your plugin locally and confirm it works
2. Strip any personal API keys from the plugin file
3. Include a clear docstring header (see template below)
4. Submit a PR to the Electra plugins repository
5. Or use `/plugin publish <filename.py>` to submit directly from the terminal

### Plugin docstring template for submissions

```python
"""
Plugin Name   : Your Plugin Name
Author        : YourName / GitHub handle
Version       : 1.0.0
Plugin Type   : ROUTER | AGENT | HOOK | COMMAND
Description   : What it does in one sentence.

Setup:
  1. Get an API key at https://...
  2. Create ~/.config/ai_plugins/<TOKEN>.json:
     {"api_key": "your-key-here"}
  3. /plugin reload

Requires: pip3 install somepackage   (if applicable)

Triggers : phrase one | phrase two
Commands : /mycommand
"""

---

*Electra AI — MakuluLinux*  
*Plugin System v2.0*  
*© MakuluLinux.com — Community contributions welcome*
