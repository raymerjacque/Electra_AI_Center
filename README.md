# Electra_AI_Center  - connect with us on Discord : https://discord.gg/rYdcWz3Ch6
# A Project Developed by MakuluLinux.com

# Plugin System Guide for Intergated AI system on AI-OS

**Html Guide :** https://makululinux.us/ai-terminal-guide.html

**Electra AI Terminal** is the AI assistant built into MakuluLinux. The core application is distributed as a compiled binary (`ai_terminal.bin`) to protect proprietary backend credentials. The **plugin system** is the open extension layer that allows the community to contribute new features, connect third-party APIs, and extend Electra's capabilities — all without access to the source code.

---

## Table of Contents

1. [How the Plugin System Works](#1-how-the-plugin-system-works)
2. [Plugin Directory](#2-plugin-directory)
3. [Plugin File Structure — Full API Reference](#3-plugin-file-structure--full-api-reference)
4. [Required Fields](#4-required-fields)
5. [Optional Functions](#5-optional-functions)
6. [Config Files — Storing API Keys](#6-config-files--storing-api-keys)
7. [How Plugins Connect to the Router](#7-how-plugins-connect-to-the-router)
8. [Managing Plugins](#8-managing-plugins)
9. [Plugin Coder Mode — Let AI Write Your Plugin](#9-plugin-coder-mode--let-ai-write-your-plugin)
10. [Writing Plugins Manually](#10-writing-plugins-manually)
11. [Complete Plugin Examples](#11-complete-plugin-examples)
12. [Testing and Debugging](#12-testing-and-debugging)
13. [Plugin Ideas and Use Cases](#13-plugin-ideas-and-use-cases)
14. [Rules and Best Practices](#14-rules-and-best-practices)
15. [Contributing](#15-contributing)

---

## 1. How the Plugin System Works

When Electra starts, it automatically scans `~/.config/ai_plugins/` and loads every `.py` file it finds. Each plugin registers itself with the **routing agent** — the AI brain that decides what to do with every message you send.

The flow looks like this:

```
User types a message
        │
        ▼
   Routing Agent
  (AI + keyword scan)
        │
        ├─── Core mode? (Chat / Coder / Command / Travel / etc.)
        │
        └─── Plugin trigger match?
                    │
                    ▼
             Plugin's run() function
                    │
                    ▼
             Response to user
```

The routing agent is dynamically taught about all loaded plugins at startup. When the user types something that matches a plugin's trigger phrases, the router sends the message straight to that plugin's `run()` function. The plugin processes it and returns a response string.

**Key properties:**
- Plugins are hot-reloadable — no restart needed (use `/plugin reload`)
- A plugin returning an empty string `""` falls through to normal chat
- Plugin errors are caught and shown as warnings — they never crash the app
- Core modes (Chat, Coder, Command, etc.) always take priority over plugin triggers

---

## 2. Plugin Directory

All plugins live in:

```
~/.config/ai_plugins/
```

This directory is created automatically the first time Electra runs. It contains:

| File | Purpose |
|---|---|
| `PLUGIN_SPEC.md` | This spec (auto-generated on first run) |
| `example_plugin.py.disabled` | A skeleton template (rename to `.py` to enable) |
| `your_plugin.py` | Your plugin file |
| `YOUR_PLUGIN_TOKEN.json` | Config/credentials for your plugin |

**Rules for file names:**
- Must end in `.py`
- Files starting with `_` are ignored (use for shared helper modules)
- Files ending in `.disabled` are ignored
- The file name is just a label — the plugin identifies itself via `PLUGIN_ROUTE_TOKEN`

---

## 3. Plugin File Structure — Full API Reference

A plugin is a standard Python file. The only dependencies available by default are the Python standard library and the `requests` package. Here is the complete structure:

```python
"""
Optional module docstring describing your plugin.
"""

import requests  # available by default
import os        # standard library always available
import json      # standard library always available

# ── Required metadata ──────────────────────────────────────────────────────────
PLUGIN_NAME        = "My Plugin"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "One-line summary shown in the router and plugin list"
PLUGIN_AUTHOR      = "Your Name or GitHub handle"
PLUGIN_ENABLED     = True   # Set to False to disable without deleting the file

# ── Router integration ─────────────────────────────────────────────────────────
PLUGIN_TRIGGERS    = ["trigger phrase one", "trigger two", "keyword"]
PLUGIN_ROUTE_TOKEN = "MY_PLUGIN"   # Unique, ALL_CAPS, no spaces
PLUGIN_COMMANDS    = ["/myplugin"] # Slash commands this plugin handles (can be [])

# ── Required: main entry point ─────────────────────────────────────────────────
def run(prompt: str, context: dict) -> str:
    """
    Called by the router when a trigger phrase is matched.

    Args:
        prompt  : The full message the user typed.
        context : Runtime information from the app. Keys:
                    "user_home"       — os.path.expanduser("~")
                    "plugin_dir"      — ~/.config/ai_plugins
                    "chat_history"    — list of recent {role, content} dicts (read-only)
                    "conversation_id" — current session ID string
                    "model"           — currently selected model ID string

    Returns:
        str  : Response to display to the user (supports Markdown).
        ""   : Empty string = fall through to normal chat mode.
    """
    return f"[My Plugin] You asked: {prompt}"

# ── Optional: called once when the plugin loads ────────────────────────────────
def setup(config: dict) -> bool:
    """
    Called once at startup (or on /plugin reload).

    Args:
        config : Dict loaded from ~/.config/ai_plugins/<PLUGIN_ROUTE_TOKEN>.json
                 Returns {} if the file doesn't exist.

    Returns:
        True  : Plugin loaded successfully, register it.
        False : Plugin not ready (missing API key, etc.) — disable it.
    """
    return True

# ── Optional: handle slash commands ───────────────────────────────────────────
def handle_command(command: str, args: str) -> bool:
    """
    Called when the user types one of the commands in PLUGIN_COMMANDS.

    Args:
        command : The slash command typed, e.g. "/myplugin"
        args    : Everything after the command (stripped), e.g. "hello world"

    Returns:
        True  : You handled it — stop processing.
        False : Pass through to default plugin dispatch.
    """
    if command == "/myplugin":
        print(f"[My Plugin] Args: {args}")
        return True
    return False

# ── Optional: custom help text ─────────────────────────────────────────────────
def get_help() -> str:
    """Shown when the user runs /plugin list."""
    return (
        f"{PLUGIN_NAME} v{PLUGIN_VERSION}: {PLUGIN_DESCRIPTION}\n"
        f"  Triggers : {', '.join(PLUGIN_TRIGGERS)}\n"
        f"  Commands : {', '.join(PLUGIN_COMMANDS)}"
    )
```

---

## 4. Required Fields

| Field | Type | Description |
|---|---|---|
| `PLUGIN_NAME` | `str` | Human-readable display name |
| `PLUGIN_VERSION` | `str` | Semantic version, e.g. `"1.0.0"` |
| `PLUGIN_DESCRIPTION` | `str` | One-line summary. Also injected into the router AI's context |
| `PLUGIN_ENABLED` | `bool` | `False` disables the plugin without deleting it |
| `PLUGIN_TRIGGERS` | `list[str]` | Phrases/keywords that route messages to this plugin |
| `PLUGIN_ROUTE_TOKEN` | `str` | Unique ALL_CAPS identifier. Must be unique across all plugins |
| `PLUGIN_COMMANDS` | `list[str]` | Slash commands registered to this plugin. Use `[]` for none |
| `run(prompt, context)` | `function` | **Required.** Main entry point |

### Choosing good trigger phrases

Triggers are matched using simple substring matching against the lowercased user input. Choose phrases specific enough that they won't accidentally intercept messages meant for core modes.

```python
# ✅ Good — specific, unlikely to conflict
PLUGIN_TRIGGERS = ["ask groq", "use groq", "groq:", "via groq"]

# ⚠️  Too broad — will intercept many normal chat messages
PLUGIN_TRIGGERS = ["ask", "search", "help"]

# ✅ Good — product name + action
PLUGIN_TRIGGERS = ["openai:", "use gpt", "ask gpt", "gpt-4o"]
```

---

## 5. Optional Functions

### `setup(config: dict) -> bool`

Use this to load credentials and validate your plugin before it's registered. If you return `False`, the plugin is silently disabled.

```python
_API_KEY = ""

def setup(config: dict) -> bool:
    global _API_KEY
    _API_KEY = config.get("api_key", "")
    if not _API_KEY:
        print("[My Plugin] No api_key found in config — plugin disabled.")
        return False
    return True
```

### `handle_command(command: str, args: str) -> bool`

Intercepts slash commands registered in `PLUGIN_COMMANDS`. If you return `False`, the app falls back to calling `run(args, {})`.

```python
def handle_command(command: str, args: str) -> bool:
    if command == "/groq":
        if not args:
            print("[Groq] Usage: /groq <your question>")
        else:
            result = run(args, {})
            print(result)
        return True
    return False
```

### `get_help() -> str`

Return a multi-line string. Shown in `/plugin list` output.

---

## 6. Config Files — Storing API Keys

Never hardcode API keys in your plugin file. Instead, store credentials in a JSON config file:

**Location:** `~/.config/ai_plugins/<PLUGIN_ROUTE_TOKEN>.json`

**Example** for a plugin with `PLUGIN_ROUTE_TOKEN = "GROQ"`:

File: `~/.config/ai_plugins/GROQ.json`
```json
{
    "api_key": "gsk_yourkeyhere",
    "base_url": "https://api.groq.com/openai/v1",
    "default_model": "llama3-8b-8192",
    "temperature": 0.7
}
```

Then read it in `setup()`:

```python
_API_KEY = ""
_MODEL   = "llama3-8b-8192"

def setup(config: dict) -> bool:
    global _API_KEY, _MODEL
    _API_KEY = config.get("api_key", "")
    _MODEL   = config.get("default_model", _MODEL)
    return bool(_API_KEY)
```

The `config` dict is automatically loaded from the JSON file and passed to `setup()` at load time. You don't need to open the file yourself.

---

## 7. How Plugins Connect to the Router

The router is the component that decides what to do with every message. It uses two strategies:

### Strategy 1 — Fast local keyword scan
The app scans every message against each loaded plugin's `PLUGIN_TRIGGERS` list. This happens instantly, no AI call needed. Core mode triggers (Chat, Coder, Command, Travel, etc.) are checked first, so they always win.

### Strategy 2 — AI router with plugin context
If the keyword scan is inconclusive, the router AI model is called. Before calling it, the app dynamically appends a list of all loaded plugins and their trigger phrases to the router's system prompt. So the AI literally knows "Plugin GROQ is available — if the user wants to use Groq, return GROQ." This means your plugin is automatically discovered by the AI router the moment it's loaded.

### What the router sees (example)

```
# LOADED PLUGINS — route to these tokens when triggers match:
GROQ                 — Route queries to Groq API. Triggers: "ask groq", "use groq"
OPENAI               — Route queries to OpenAI API. Triggers: "ask openai", "gpt-4o"
HOME_ASSISTANT       — Control smart home devices. Triggers: "turn on the lights", "set thermostat"
```

The router returns your `PLUGIN_ROUTE_TOKEN` and the app calls your `run()` function.

---

## 8. Managing Plugins

All plugin management happens through the `/plugin` command in the Electra terminal.

### Quick Reference

| Command | Action |
|---|---|
| `/plugin` | Enter Plugin Coder mode (AI writes/edits plugins) |
| `/plugin list` | Show all loaded plugins with triggers and commands |
| `/plugin reload` | Hot-reload all plugins — no restart needed |
| `/plugin test GROQ hello` | Directly call GROQ plugin's `run("hello", ctx)` |
| `/plugin spec` | Open the plugin specification in your file manager |
| `/plugin dir` | Open `~/.config/ai_plugins/` in Nemo file manager |

### Installing a plugin manually

1. Place your `.py` file in `~/.config/ai_plugins/`
2. If it needs credentials, create `~/.config/ai_plugins/<TOKEN>.json`
3. Type `/plugin reload` in Electra — done

### Disabling a plugin

Either:
- Set `PLUGIN_ENABLED = False` in the plugin file, then `/plugin reload`
- Rename the file to `pluginname.py.disabled`
- Delete the file entirely

### Enabling a plugin from the skeleton

```bash
cd ~/.config/ai_plugins/
cp example_plugin.py.disabled my_plugin.py
# Edit my_plugin.py ...
```
Then type `/plugin reload` in Electra.

---

## 9. Plugin Coder Mode — Let AI Write Your Plugin

Plugin Coder Mode is a specialized AI coding environment where Electra knows the full plugin API and writes plugins for you. It's the easiest way to create new plugins.

### How to enter Plugin Coder Mode

**Option A — Enter mode first, then describe your plugin:**
```
/plugin
```
You'll see the Plugin Coder Mode banner. Then just describe what you want:
```
write a plugin that connects to the Groq API using the llama3-70b model
```

**Option B — Describe inline:**
```
/plugin create a weather plugin that uses the OpenWeatherMap API
```

The AI will:
1. Write a complete, valid plugin file
2. Save it to `~/.config/ai_plugins/`
3. Confirm the file is written

Then you type `/plugin reload` to activate it.

### What you can ask Plugin Coder Mode to do

**Create new plugins:**
```
write a plugin that lets me query the Anthropic API directly
```
```
create a plugin that connects to my Home Assistant instance at 192.168.1.100
```
```
make a plugin that fetches crypto prices from CoinGecko — triggers: "crypto price", "btc price"
```
```
build a plugin that translates text using LibreTranslate API
```
```
create a Telegram notification plugin that sends messages to my bot
```

**Edit existing plugins:**
```
edit the groq_connector.py plugin and add support for the gemma2-9b model
```
```
update the openai plugin to also support o1-mini model, add "o1" as a trigger
```
```
fix the home_assistant plugin — the lights endpoint changed to /api/services/light/turn_on
```

**Add features:**
```
add conversation history support to the groq plugin so it remembers context across messages
```
```
add a /groqmodels command to the groq plugin that lists available models
```

**The AI stays in Plugin Coder Mode** until you type `/chat`. This means you can have a full conversation:
```
> write a groq plugin
[AI writes the file]

> actually, add mixtral-8x7b as the default model instead
[AI edits the file]

> also add /groq list to show available models
[AI edits again]

> /plugin reload
[Plugins hot-reloaded — your new plugin is live]

> ask groq what is the capital of France
[Your new plugin answers]
```

---

## 10. Writing Plugins Manually

If you prefer to write plugins by hand, here's everything you need to know.

### Step 1 — Create the file

```bash
nano ~/.config/ai_plugins/my_plugin.py
```

### Step 2 — Write the plugin

Use the template in Section 3. At minimum you need the 7 required variables and the `run()` function.

### Step 3 — Create config if needed

```bash
nano ~/.config/ai_plugins/MY_PLUGIN.json
```
```json
{
    "api_key": "your-key-here"
}
```

### Step 4 — Load it

In the Electra terminal:
```
/plugin reload
```

### Step 5 — Test it

```
/plugin test MY_PLUGIN hello world
```
Or just type one of your trigger phrases normally.

---

## 11. Complete Plugin Examples

### Example 1 — Groq API Connector

Connects Electra to [Groq](https://groq.com)'s fast inference API.

Config file `~/.config/ai_plugins/GROQ.json`:
```json
{
    "api_key": "gsk_your_key_here",
    "default_model": "llama3-8b-8192"
}
```

Plugin file `~/.config/ai_plugins/groq_connector.py`:
```python
import requests

PLUGIN_NAME        = "Groq Connector"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Route queries to Groq API (llama3, mixtral, gemma)"
PLUGIN_AUTHOR      = "Community"
PLUGIN_ENABLED     = True

PLUGIN_TRIGGERS    = ["ask groq", "use groq", "via groq", "groq:"]
PLUGIN_ROUTE_TOKEN = "GROQ"
PLUGIN_COMMANDS    = ["/groq"]

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

    messages = [{"role": "user", "content": clean}]
    for turn in context.get("chat_history", [])[-4:]:
        if turn.get("role") in ("user", "assistant"):
            messages.insert(-1, turn)

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

**Usage:**
```
ask groq what is quantum computing?
/groq explain binary search trees
```

---

### Example 2 — CoinGecko Crypto Price Plugin

No API key required.

Plugin file `~/.config/ai_plugins/crypto_prices.py`:
```python
import requests

PLUGIN_NAME        = "Crypto Prices"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Fetch live cryptocurrency prices from CoinGecko"
PLUGIN_AUTHOR      = "Community"
PLUGIN_ENABLED     = True

PLUGIN_TRIGGERS    = ["crypto price", "bitcoin price", "btc price",
                      "eth price", "ethereum price", "coin price",
                      "price of btc", "price of eth"]
PLUGIN_ROUTE_TOKEN = "CRYPTO"
PLUGIN_COMMANDS    = ["/crypto"]

_COIN_MAP = {
    "btc": "bitcoin", "bitcoin": "bitcoin",
    "eth": "ethereum", "ethereum": "ethereum",
    "sol": "solana", "solana": "solana",
    "bnb": "binancecoin", "xrp": "ripple",
    "ada": "cardano", "doge": "dogecoin",
}

def setup(config: dict) -> bool:
    return True

def _fetch_price(coin_id: str) -> dict:
    url = f"https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": "usd", "include_24hr_change": "true"}
    resp = requests.get(url, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()

def run(prompt: str, context: dict) -> str:
    p = prompt.lower()
    found = None
    for symbol, coin_id in _COIN_MAP.items():
        if symbol in p:
            found = coin_id
            break

    if not found:
        # Try to extract any word after "price of"
        import re
        m = re.search(r'price of (\w+)', p)
        if m:
            found = _COIN_MAP.get(m.group(1), m.group(1))

    if not found:
        return "[Crypto] Couldn't identify which coin. Try: 'btc price' or '/crypto eth'"

    try:
        data = _fetch_price(found)
        if found not in data:
            return f"[Crypto] No data for '{found}'. Check the coin name."
        info  = data[found]
        price = info.get("usd", "N/A")
        chg   = info.get("usd_24h_change", 0)
        arrow = "📈" if chg >= 0 else "📉"
        return (
            f"**{found.title()}**\n"
            f"  Price  : ${price:,.2f} USD\n"
            f"  24h    : {arrow} {chg:+.2f}%"
        )
    except Exception as e:
        return f"[Crypto] Error: {e}"

def handle_command(command: str, args: str) -> bool:
    if command == "/crypto":
        print(run(args or "btc price", {}))
        return True
    return False
```

**Usage:**
```
btc price
ethereum price
/crypto sol
price of dogecoin
```

---

### Example 3 — Simple Custom Command Plugin

A plugin that adds domain-specific slash commands without any API.

Plugin file `~/.config/ai_plugins/dev_tools.py`:
```python
import subprocess
import os

PLUGIN_NAME        = "Dev Tools"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Quick developer shortcuts — git status, docker ps, etc."
PLUGIN_AUTHOR      = "Community"
PLUGIN_ENABLED     = True

PLUGIN_TRIGGERS    = ["quick git status", "show docker containers", "dev status"]
PLUGIN_ROUTE_TOKEN = "DEVTOOLS"
PLUGIN_COMMANDS    = ["/gs", "/dp", "/devstatus"]

def setup(config: dict) -> bool:
    return True

def _run_cmd(cmd: str) -> str:
    try:
        out = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT,
                                      timeout=10, text=True)
        return out.strip() or "(no output)"
    except subprocess.CalledProcessError as e:
        return e.output.strip() or f"(exit {e.returncode})"
    except Exception as e:
        return f"Error: {e}"

def run(prompt: str, context: dict) -> str:
    p = prompt.lower()
    if "git" in p:
        return f"```\n{_run_cmd('git status --short')}\n```"
    if "docker" in p:
        return f"```\n{_run_cmd('docker ps --format \"table {{.Names}}\\t{{.Status}}\"')}\n```"
    return _run_cmd("git status --short && echo '---' && df -h / | tail -1")

def handle_command(command: str, args: str) -> bool:
    if command == "/gs":
        print(_run_cmd("git status"))
        return True
    if command == "/dp":
        print(_run_cmd("docker ps"))
        return True
    if command == "/devstatus":
        print(_run_cmd("git status --short && uptime && free -h"))
        return True
    return False
```

**Usage:**
```
quick git status
/gs
/dp
/devstatus
```

---

## 12. Testing and Debugging

### Test a plugin directly

```
/plugin test GROQ what is machine learning?
/plugin test CRYPTO btc price
```

This calls the plugin's `run()` function directly, bypassing the router.

### Check if your plugin loaded

```
/plugin list
```

If your plugin isn't listed, it either failed validation or `setup()` returned `False`. Run Electra from a terminal to see error output:

```bash
python3 /path/to/ai_terminal.py
# or
/usr/share/MakuluSetup/tools/ai_terminal.bin
```

Common reasons a plugin fails to load:
- Missing a required variable (`PLUGIN_NAME`, `PLUGIN_ROUTE_TOKEN`, etc.)
- Missing `run()` function
- `setup()` returned `False` (usually missing API key)
- Syntax error in the plugin file
- Duplicate `PLUGIN_ROUTE_TOKEN` (last file loaded wins)

### Hot reload after edits

```
/plugin reload
```

No restart needed. Changes to any plugin file take effect immediately.

### View the plugin directory

```
/plugin dir
```

Opens `~/.config/ai_plugins/` in Nemo.

### Read error output

If a plugin's `run()` raises an exception, the error is caught and displayed:
```
[Plugin: My Plugin] Error in run(): ConnectionTimeout
```
The app then falls through to normal chat. Your plugin will never crash Electra.

---

## 13. Plugin Ideas and Use Cases

Here are plugin categories and specific ideas ready to build:

### AI Model Connectors
- **OpenAI** — GPT-4o, o1, o3 via OpenAI API
- **Groq** — Ultra-fast llama3, mixtral inference
- **Anthropic** — Claude models directly
- **Ollama** — Local models (llama3, mistral, phi3)
- **Together AI** — 50+ open-source models
- **Perplexity AI** — Web-grounded answers

### Data & Finance
- **Stock prices** — Yahoo Finance or Alpha Vantage
- **Crypto** — CoinGecko, Binance API
- **Currency exchange** — Open Exchange Rates
- **News feed** — NewsAPI, RSS aggregator
- **Earthquake alerts** — USGS live data

### Home & IoT
- **Home Assistant** — Control lights, switches, climate
- **Philips Hue** — Direct bulb control
- **Tasmota** — ESP8266/ESP32 smart plugs
- **MQTT** — Generic IoT message bus

### Productivity
- **Notion** — Read/write database entries
- **Obsidian** — Create notes from the terminal
- **Todoist / Taskwarrior** — Task management
- **Calendar** — Google Calendar or CalDAV
- **Email** — Send via SMTP or read via IMAP

### Communication
- **Telegram** — Send messages to a bot
- **Discord** — Post to a webhook
- **Slack** — Post to a channel
- **Pushover / Gotify** — Push notifications to phone

### Media & Entertainment
- **Plex** — Now playing, library search
- **Spotify** — Now playing, search (via OAuth)
- **Jellyfin** — Local media server control

### Developer Tools
- **GitHub** — List issues, PRs, repo stats
- **GitLab** — Pipelines, merge requests
- **Jira** — Ticket lookup and creation
- **Docker** — Container status and control
- **Prometheus** — Query metrics

### MakuluLinux Specific
- **System monitor** — CPU/RAM/disk with alerting thresholds
- **Backup status** — Timeshift snapshot info
- **Package watcher** — New updates available check
- **Nemo integration** — File operations via chat

---

## 14. Rules and Best Practices

### Always do these

```python
# ✅ Read credentials from config, never hardcode
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

# ✅ Return "" to fall through to chat when you can't handle it
def run(prompt: str, context: dict) -> str:
    if "relevant keyword" not in prompt.lower():
        return ""  # Let normal chat handle this
    # ... handle it yourself
```

### Never do these

```python
# ❌ Never hardcode credentials
_API_KEY = "sk-abc123..."

# ❌ Never use broad triggers
PLUGIN_TRIGGERS = ["the", "what", "how", "search"]

# ❌ Never let exceptions propagate (already caught, but don't rely on it)
def run(prompt, context):
    return requests.get("...").json()["data"]  # Will crash if network fails

# ❌ Never use duplicate PLUGIN_ROUTE_TOKEN
PLUGIN_ROUTE_TOKEN = "CHAT"  # Conflicts with core mode!
PLUGIN_ROUTE_TOKEN = "COMMAND"  # Conflicts with core mode!
```

### Reserved tokens (do not use as PLUGIN_ROUTE_TOKEN)

```
CHAT  COMMAND  CODER  LIVE  TRAVEL  IMAGE  VIDEO  AUDIO
APP_AGENT  NVIDIA_AGENT  TROUBLESHOOT  ASK_COMMAND  ASK_CODER
```

### Available Python packages

The following are reliably available in the Electra environment:
- Full Python 3 standard library
- `requests` — HTTP client
- `json`, `os`, `re`, `subprocess`, `threading`, `datetime`, `uuid`

If your plugin needs additional packages, check availability with:
```bash
python3 -c "import package_name"
```
And document the install requirement in your plugin's docstring:
```python
"""
Requires: pip3 install somepackage
"""
```

---

## 15. Contributing

### Submitting a plugin

1. Make sure your plugin works locally
2. Strip any personal API keys from the plugin file
3. Include a `README` block in the docstring explaining what it does, what API it uses, and how to get credentials
4. Submit a PR to the Electra plugins repository

### Plugin file template for submissions

```python
"""
Plugin Name: Groq Connector
Author: YourName
Version: 1.0.0
Description: Connect Electra to Groq's fast inference API.

Setup:
  1. Get a free API key at https://console.groq.com
  2. Create ~/.config/ai_plugins/GROQ.json:
     {"api_key": "gsk_your_key_here"}
  3. /plugin reload

Triggers: ask groq | use groq | groq: | via groq
Commands: /groq
"""
# ... plugin code below
```

### Guidelines for accepted plugins
- Must work without modifying the core `ai_terminal.py`
- Must read credentials from config file — zero hardcoded keys
- Must handle all exceptions inside `run()` and return an error string
- Must not use `PLUGIN_ROUTE_TOKEN` that conflicts with core modes
- Must include usage examples in the docstring
- Prefer the Python standard library + `requests` over heavy dependencies

---

*Electra AI — MakuluLinux*
*Plugin System v1.0*
