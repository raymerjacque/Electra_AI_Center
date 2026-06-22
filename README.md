# Electra AI Center

[![Electra AI Center](https://makululinux.us/ai-os.png)](https://makululinux.us/ai-os.html)

**Fully integrated into:** https://makululinux.us/ai-os.html

**PUBLIC API Access:** https://makululinux.us/

**Connect with us on Discord:** https://discord.gg/rYdcWz3Ch6  
**A Project by MakuluLinux.com** | **HTML Guide:** https://makululinux.us/ai-terminal-guide.html

---

## Install

### 🖥️ Desktop / Laptop (with GUI)

For Ubuntu/Debian/Fedora/Arch desktops, laptops, and MakuluLinux. Installs both the terminal and the floating bar widget with full voice, GUI, and audio support:

```bash
curl -fsSL https://raw.githubusercontent.com/raymerjacque/Electra_AI_Center/main/install.sh | bash
```

### 🖧 Headless / Server (no GUI)

For VPS, cloud servers, WSL, or any SSH-only machine with no desktop environment. Installs the terminal backend only — no GTK, no audio, no display required:

```bash
curl -fsSL https://raw.githubusercontent.com/raymerjacque/Electra_AI_Center/main/install-headless.sh | bash
```

That's it. Electra AI Center will be running on your system within minutes.

---

## What is The AI Center?

Electra AI Center is MakuluLinux's flagship all-in-one AI productivity suite — a **Jarvis-style AI operating layer for Linux**. Delivered as a single compiled binary, it combines the conversational power of a chat assistant, the autonomous file-editing muscle of a full coding agent, the depth of a professional writing suite, the imagination of a novel-generation pipeline, and the system-level authority of a natural-language command executor — all in one application.

Think of it as your personal AI engineer, writer, shell expert, home-automation controller, finance bot, music controller, news reader, and research assistant — all accessible from one terminal window, from your desktop via the lightweight Electra Bar widget (Super+E), or through the full Electra GUI IDE.

**Unique capabilities no other tool has:**
- 🧠 **Screen awareness** — reads any focused app's content via AT-SPI (no copy-paste needed)
- 🔌 **D-Bus desktop control** — any app or script can send queries *to* Electra via the session bus
- 💰 **Autonomous finance engine** — earns money while you sleep (affiliate, print-on-demand, freelance)
- 💓 **Heartbeat background agent** — runs scheduled tasks 24/7 with Telegram notifications
- 🐝 **Agent Swarm** — up to 6 parallel AI agents working on different files simultaneously
- 📦 **Single binary** — everything compiled with Nuitka; no Python, no dependencies, just run it

In a nutshell: an **all-in-one autonomous AI control center** specially designed for Linux.

---

## AI Models — 80+ Available

Electra connects to **80+ AI models** across 11 providers — all through a single backend, no individual API keys needed for most. Models are ranked live by speed every time you check.

### 🏆 Headline Models

| Model | Provider | Best For |
|---|---|---|
| **DeepSeek V4 Pro** `671B` | DeepSeek | Deep reasoning, complex code, research |
| **DeepSeek V4 Flash** `671B` | DeepSeek | Fast reasoning, coding, general tasks |
| **DeepSeek R1-0528** `671B` | DeepSeek | Extended chain-of-thought reasoning |
| **Kimi K2.6** `1T MoE` | Moonshot AI | 1M context, agents, long-form analysis |
| **Step 3.7 Flash** `196B` | StepFun | Long-form writing, novel generation, research |
| **Step 3.5 Flash** `196B` | StepFun | Coding, chat, fast general use — primary backbone |
| **Qwen3-Coder 480B** `MoE` | Alibaba | Elite code generation across all languages |
| **Qwen3.5 397B** `MoE` | Alibaba | Frontier reasoning and coding |
| **Mistral Large 3** `675B` | Mistral | Enterprise reasoning, multilingual |
| **Devstral 2** `123B` | Mistral | Agentic software engineering |
| **GPT-OSS 120B** | OpenAI | OpenAI open-weight, tool use |
| **Nemotron 3 Super 120B** | NVIDIA | Agentic reasoning, tool calling |
| **Nemotron 3 Nano 30B** | NVIDIA | Fast chat, always-on |
| **Gemma 4 31B** | Google | Efficient multimodal reasoning |
| **MiniMax M3** | MiniMax | 1M context, agentic tasks |
| **MiniMax M2.7** | MiniMax | Long context, fast |
| **GLM-4.7** | Zhipu AI (Cerebras) | Ultra-fast wafer-scale (~3000 tok/s) |
| **Mistral Medium 3.5** | Mistral | Balanced quality and speed |

> Models span **11 providers** — Electra automatically picks the fastest live instance via composite scoring (60% capability + 40% speed). Pro tier unlocks the full catalogue.

### Provider Prefixes

| Prefix | Provider | Notes |
|---|---|---|
| `step-` | StepFun | Primary backbone — most stable cross-run |
| `qc-` | QwenCloud / DashScope | Web search + function calling |
| `mis-` | Mistral Direct | 5 keys, 10,000 req/day budget |
| `cb-` | Cerebras | Ultra-fast (~3000 tok/s), wafer-scale |
| `llm7-` | LLM7 | Community free inference |
| `ms-` | ModelScope | 1 RPS cap, manual selection only |
| `opr-` | OpenRouter | Manual selection only (daily limits) |
| `ol-` | Ollama Cloud | 20+ large models — Major+ tier |
| `ds-` | DeepSeek Direct | Paid per-token — Major+ tier |
| `bt-` | ByteDance Ark | Paid per-token — Major+ tier |
| `sf-` | SiliconFlow | Manual selection only (excluded from auto-routing) |

### Access Tiers

| Tier | Daily Limit | Premium Providers | Agent Swarm |
|---|---|---|---|
| **Free** | 50 / day | Standard pool | ✗ |
| **Private** | 500 / day | Standard pool | ✗ |
| **Corporal** | 1,500 / day | Standard pool | ✗ |
| **Sergeant** | 4,000 / day | Standard pool | ✗ |
| **Major** — $40/mo | 10,000 / day | `ds-` `bt-` `ol-` unlocked + auto-prioritised | ✓ |
| **Commander** — $100/mo | Unlimited ∞ | `ds-` `bt-` `ol-` unlocked + auto-prioritised | ✓ |

- Free users see all available models; locked models are marked `🔒 [Major+]`
- Major/Commander subscribers get paid providers **automatically prioritised** in Coder and Command mode routing — no manual switching needed
- Upgrade at: https://patreon.com/c/makululinux/membership
- Token holders: use `/unlock` to enter your token and immediately unlock access

Browse the full live-ranked list anytime inside Electra:
```
/model
```

---

## What Gets Installed

| Component | Desktop | Headless |
|---|---|---|
| `ai_terminal.bin` | ✅ `/usr/share/MakuluSetup/tools/` | ✅ `/usr/share/MakuluSetup/tools/` |
| `electra_bar.bin` | ✅ floating input bar (Super+E) | ❌ requires display |
| Autostart on login | ✅ `~/.config/autostart/` | ❌ no desktop session |
| `electra` symlink | ✅ `/usr/local/bin/electra` | ✅ `/usr/local/bin/electra` |
| Voice input | ✅ faster-whisper + pyaudio | ❌ no microphone |
| GUI mode (`/gui`) | ✅ GTK3 IDE interface | ❌ requires display |
| AT-SPI daemon | ✅ screen awareness daemon | ❌ requires display |
| D-Bus daemon | ✅ `org.makululinux.Electra` | ❌ requires session bus |
| Nemo context actions | ✅ right-click AI actions | ❌ no file manager |

---

## System Requirements

- **x86_64 architecture** — ARM/aarch64 not currently supported
- **glibc 2.35 or newer** — compiled on Ubuntu 22.04 (glibc 2.35)
- **Runtime libraries** — `libportaudio2` and `ffmpeg` must be present (the installer handles this)
- Internet connection for AI features (offline mode available via local Ollama)

> **How the binary works:** Electra is compiled with Nuitka into a single self-contained binary. At launch it extracts to `/tmp/electra/` — your system needs write access to `/tmp` and glibc ≥ 2.35. The installer auto-detects your distro and package manager.

> **Not sure about your glibc version?** Run `ldd --version` in your terminal. If the first line shows `2.35` or higher, you're good.

---

## Supported Distributions

| Family | Package Manager | Works | Confirmed Distros |
|---|---|---|---|
| **Debian / Ubuntu** | `apt-get` | ✅ Full support | Ubuntu 22.04+, Debian 12+, MakuluLinux, Linux Mint 21+, Pop!\_OS 22.04+, Zorin OS 16+, Elementary OS 7+, Kali Linux, MX Linux 23+, Raspberry Pi OS (Bookworm), Deepin, Neon, Devuan |
| **Fedora / RHEL** | `dnf` / `dnf5` | ✅ Full support | Fedora 37+, RHEL 9+, CentOS Stream 9+, Rocky Linux 9+, AlmaLinux 9+, Amazon Linux 2023, Nobara, Ultramarine |
| **Arch Linux** | `pacman` | ✅ Full support | Arch Linux, Manjaro, EndeavourOS, Garuda, ArcoLinux, Artix, CachyOS, XeroLinux |
| **openSUSE** | `zypper` | ✅ Full support | openSUSE Tumbleweed, SLES 15 SP5+ |
| **Void Linux** | `xbps-install` | ✅ Full support | Void Linux (glibc build — **not** the musl build) |
| **Gentoo** | `emerge` | ⚠️ Best-effort | Gentoo, Funtoo, Calculate Linux — installer works; binary compatibility depends on your glibc version |
| **Slackware** | `slackpkg` | ⚠️ Best-effort | Slackware 15+, Salix — installer attempts install; limited testing |
| **Alpine Linux** | `apk` | ❌ Binary fails | Alpine uses musl libc — the glibc binary will not execute |
| **WSL2** | (distro's) | ✅ Terminal mode | Use a Ubuntu 22.04+ WSL2 image; GUI requires WSLg |

### Not Supported

| Distro / Setup | Status | Reason |
|---|---|---|
| **Ubuntu 20.04 / Debian 11** | ❌ Binary fails | glibc 2.31 — too old. Binary requires glibc ≥ 2.35 |
| **RHEL 8 / Rocky 8 / AlmaLinux 8** | ❌ Binary fails | glibc 2.28 — too old |
| **CentOS 7** | ❌ Binary fails | glibc 2.17 — far too old |
| **openSUSE Leap 15.4 / 15.5** | ❌ Binary fails | glibc 2.31 — too old |
| **Alpine Linux** | ❌ Binary fails | musl libc — fundamentally incompatible |
| **Void Linux (musl build)** | ❌ Binary fails | musl libc — use the glibc Void build instead |
| **ARM / aarch64 / any non-x86\_64** | ❌ Not supported | Binary compiled for x86\_64 only |
| **NixOS** | ❌ Binary fails | NixOS patched glibc paths break standard ELF binaries |
| **WSL1** | ❌ Not supported | WSL1 lacks full Linux syscall support required by Nuitka onefile |
| **macOS** | ❌ Not supported | Linux ELF binary — does not run on macOS |
| **Windows (native)** | ❌ Not supported | Use WSL2 with Ubuntu 22.04+ |

---

## Starting Electra

```bash
# Desktop — after install:
/usr/share/MakuluSetup/tools/ai_terminal.bin

# Or via symlink (desktop + headless):
electra

# Start directly in GUI mode:
electra --gui
```

The **floating Electra Bar** (desktop only) starts automatically on every login — press **Super+E** or type anything into it and press Enter.

---

## Modes

Electra has seven core operating modes. Type the command to switch at any time:

| Mode | Command | What it does |
|---|---|---|
| **Chat** | `/chat` | Conversational AI — general questions, research, brainstorming |
| **Coder** | `/coder` | Autonomous coding agent — reads, writes, edits, runs your code |
| **Writer** | `/writer` | Content generation — articles, blogs, essays, documents, emails |
| **Novel** | `/novel` | Full long-form book pipeline — 25-chapter novels with scene-by-scene generation |
| **Command** | `/command` | Natural-language Linux commands — no shell knowledge needed |
| **GUI / IDE** | `/gui` | Full desktop IDE — file tree, editor, chat panel, activity log, git panel |
| **Finance** | `/finance` | Autonomous income engine — affiliate, print-on-demand, freelance scanner |
| **Voice** | mic button | Voice input via faster-whisper (desktop only) |

The **routing agent** automatically detects intent — just type naturally and Electra picks the right mode. You don't need to switch manually.

---

## Usage — Quick Start

### Chat Mode
```
▶ what is a Makefile and when should I use one?
▶ explain docker networking to me like I'm 10
▶ compare rust vs go for systems programming
```

### Coder Mode
```
▶ /coder
▶ build me a FastAPI app with JWT auth and SQLite
▶ /swarm         ← parallel agents work on multiple files at once (Major+)
▶ /plan          ← structured architect → developer → reviewer workflow
▶ /debug         ← AI analyses the last error output
▶ /delegate fix the auth module | add tests for the API  ← parallel tasks
▶ /research async patterns in Python
```
> In Coder mode, Electra reads your actual files, writes changes, runs commands, and iterates autonomously. Point it at a project with `/set /path/to/project`. The AI sees your full file tree, open tabs, and live editor content.

### Writer Mode
```
▶ /writer
▶ write a blog post about the future of open source AI
▶ draft a cover letter for a senior DevOps role at a startup
▶ /outline The Ethics of Autonomous Vehicles
▶ /translate French
▶ /refine make it more formal and cut 20%
▶ /export pdf
```

### Novel Mode
```
▶ /novel
▶ write a novel, 25 chapters, 3 scenes each — a family surviving on a lunar colony. Call it Moon Walkers
```
> Novel mode generates a complete structured book: blueprint → book overview → chapter outlines → scene-by-scene writing → full manuscript. All files are saved to `~/workspace/`.

### Command Mode
```
▶ /command
▶ find all files larger than 500MB in my home folder
▶ set up a cron job to backup ~/Documents every night at 2am
▶ show me what's using the most RAM right now
▶ install docker and add me to the docker group
```

### GUI / IDE Mode
```bash
electra --gui          # Launch directly in GUI mode
# Or from inside terminal:
/gui
```
The GUI provides a VS Code-style interface: file tree on the left, editor in the centre, AI chat panel on the right, and a status bar at the bottom. Features include:
- **Streaming diff preview** — see AI file changes before they apply
- **Agent Swarm panel** — live status of parallel agents (Major/Commander)
- **Git panel** — stage, commit, and view diff from the sidebar
- **Ghost text completions** — inline AI suggestions as you type (Tab to accept)
- **Open VSX extensions** — install VS Code-compatible extensions, themes, and snippets
- **Command palette** — Ctrl+Shift+P
- **Quick file open** — Ctrl+P
- **Inline edit** — select code, press Ctrl+K for AI to rewrite the selection
- **Test generation** — Ctrl+Shift+G generates tests for the current file
- **Voice input** — mic button in the chat panel

### Finance Mode
```
▶ /finance
▶ /hustle
```
> Finance mode activates the autonomous income engine: affiliate content generation, print-on-demand design & upload (Redbubble), and freelance job scanner. Results are tracked in a local SQLite ledger. Telegram notifications keep you updated while tasks run in the background.

---

## Built-in Services & Integrations

Electra ships with a suite of always-available integrations. No extra setup for most — just use them:

| Service | Command | What it does |
|---|---|---|
| **Codeberg** | `/codeberg` or `/cb` | Repos, PRs, issues, notifications on the privacy-first Git host |
| **GitHub** | `/github` | Repo management, issue tracking, PR summaries |
| **Weather** | `/weather London` | Live weather and forecasts for any city |
| **Telegram Bridge** | `/telegram` | Control Electra via Telegram — send prompts from your phone |
| **Discord Bot** | `/discord` | Discord channel integration with slash commands |
| **Reddit** | `/reddit` | Browse, summarise, and interact with Reddit |
| **Spotify** | `/spotify play chill beats` | Spotify playback control |
| **RSS / News** | `/rss` | Subscribe to and summarise RSS feeds |
| **Home Assistant** | `/ha` | Control your smart home devices |
| **Finance / Hustle** | `/hustle` or `/finance` | Autonomous income engine — affiliate, print-on-demand, freelance |
| **Blog Publisher** | `/blog` | AI-assisted blog writing and auto-publishing via Dev.to / Beehiiv |
| **Travel Planner** | `/travel plan a 5-night trip to Tokyo` | Full itinerary planning |
| **Image Generation** | `/image a neon city at night` | AI image generation |
| **QR Codes** | `/qr https://makululinux.us` | Generate QR codes instantly |
| **Screenshots / OCR** | `/screenshot` `/ocr` | Capture screen and extract or explain text |
| **SSH Manager** | `/ssh add home user@192.168.1.1` | Save and connect to SSH hosts |
| **Docker** | `/docker ps` | Manage Docker containers naturally |
| **System Monitor** | `/monitor cpu=85 ram=90` | Alerts when CPU/RAM cross thresholds |
| **Package Manager** | `/pkg install neovim` | Natural language apt/dnf/pacman/snap/flatpak |
| **Reminders** | `/remind 30m take a break` | Set timed reminders |
| **Clipboard AI** | `/clip explain` | Analyse whatever is in your clipboard |
| **Heartbeat Agent** | `/heartbeat` | Background autonomous task runner daemon |
| **AT-SPI Screen** | `/atspi` | Screen context daemon — AI reads any focused app |
| **D-Bus Control** | `/dbus` | Two-way D-Bus desktop integration daemon |
| **Agent Swarm** | `/swarm` | Parallel multi-agent multi-file editing (Major/Commander) |

---

## Desktop Integration (Linux-Exclusive Features)

### AT-SPI Screen Awareness
Electra can **read the content of any app you have focused** — a browser showing a stack trace, a PDF of API docs, a terminal with build output — and inject that context into every AI prompt automatically. No copy-paste needed.

```
# Control the AT-SPI daemon:
/atspi status|start|stop|restart|install|uninstall|logs|on|off
```

### D-Bus Two-Way Desktop Control
Any application, script, or keyboard shortcut on your desktop can send queries **to** Electra and receive responses via the standard Linux D-Bus session bus (`org.makululinux.Electra`).

```bash
# Send a query to Electra from any script:
dbus-send --session --print-reply --dest=org.makululinux.Electra \
  /org/makululinux/Electra org.makululinux.Electra.ExecuteIntent string:"what time is it"

# Control the D-Bus daemon:
/dbus status|start|stop|restart|install|uninstall|logs|ping
```

**Exposed D-Bus methods:** `Ping()`, `ExecuteIntent(query)`, `GetContext()`, `Notify(title, body)`, `TileWindows(layout)`

### Nemo Right-Click Actions
Right-click any file or folder in the Nemo file manager to access 25+ AI-powered context menu actions — summarise a file, explain code, generate tests, refactor, translate, and more. Installed automatically on first launch.

### Electra Bar Widget
A lightweight floating input bar (Super+E) gives you system-wide AI access from anywhere on your desktop without opening the full GUI.

---

## Key Commands Reference

### Navigation & Session
| Command | Description |
|---|---|
| `/help` | Show all commands |
| `/model` | Browse and select AI models |
| `/newchat` | Start a fresh conversation |
| `/cls` or `/clear` | Clear the terminal |
| `/refresh` | Re-check server and update model list |
| `/set <path>` | Set working directory |
| `/cd <path>` | Change directory |
| `/mode` | Show or switch current mode |
| `/offline` | Check offline/fallback mode status |

### AI & Models
| Command | Description |
|---|---|
| `/model` | List all models with speed rankings, select one |
| `/think` | Toggle extended reasoning/thinking mode |
| `/ghost [on\|off]` | Toggle inline AI ghost-text completions in GUI editor |
| `/providers` | Manage third-party API keys (OpenAI, Anthropic, Gemini, Kimi, Mistral, Grok, Groq…) |
| `/openai` | Add/update your OpenAI API key |
| `/claude` | Add/update your Anthropic API key |
| `/gemini` | Add/update your Google Gemini key |
| `/kimi` | Add/update your Moonshot (Kimi) key |
| `/mistral` | Add/update your Mistral key |
| `/grok` | Add/update your xAI Grok key |
| `/deepseek` | Add/update your DeepSeek Direct key |
| `/cerebras` | Add/update your Cerebras key |
| `/openrouter` | Add/update your OpenRouter key |

### Coding & Projects
| Command | Description |
|---|---|
| `/plan` | Activate structured planning: Architect → Developer → Reviewer |
| `/swarm [on\|off]` | Toggle Agent Swarm — parallel multi-agent multi-file editing (Major+) |
| `/delegate <task1> \| <task2>` | Run parallel coder tasks simultaneously |
| `/debug [error]` | AI diagnoses the last error or a pasted error |
| `/research <topic>` | Deep research pass before starting code |
| `/init [type] [name]` | Scaffold a new project (e.g. `/init flask myapi`) |
| `/template list` | List available project templates |
| `/index` | Re-index the current project for AI context |
| `/lint [file]` | Run linter + AI fix suggestions |
| `/sandbox` | Isolated test environment |
| `/dry-run [on\|off]` | Preview commands before executing |
| `/rollback [N\|all]` | Roll back the last N AI file changes |
| `/undo [all]` | Undo last edit |
| `/autowrite [on\|off]` | Toggle auto file-write (no confirmation prompt) |
| `/dp` | Toggle diff preview for autonomous operations |
| `/docker` | Manage Docker containers |
| `/pk` | View project knowledge base (`.electra_project.md`) |
| `/pk init` | Create a project knowledge base in current workspace |
| `/pk add <Section> \| <note>` | Quick-add a note to the project knowledge base |
| `/vec-index` | Force full semantic vector index rebuild (ChromaDB) |

### Writing & Content
| Command | Description |
|---|---|
| `/outline <topic>` | Generate a structured outline |
| `/refine <instructions>` | Rewrite last output with new instructions |
| `/translate <lang>` | Translate last output to any language |
| `/style [file]` | Apply a style guide to writing |
| `/format <rules>` | Reformat content by rules |
| `/wordcount` or `/wc` | Show word count and progress toward target |
| `/export <fmt> [file]` | Export to pdf / docx / md / txt |
| `/import <file>` | Import a document for editing |
| `/append <file>` | Append AI content to an existing file |
| `/inspect` | Novel inspector — check completeness and consistency |
| `/blog post` | Start a guided blog writing session |

### Memory & Context
| Command | Description |
|---|---|
| `/memory` | View and manage conversation memory |
| `/remember [note]` | Pin a note to persistent memory |
| `/pin <file>` | Pin a file as always-in-context |
| `/pins` | List pinned files |
| `/unpin <file>` | Remove a pinned file |
| `/compact` | Summarise and compress conversation history |
| `/history export` | Export full conversation history |
| `/context` | Show current context usage and token budget |
| `/offline-memory` | View local offline memory (`.electra_memory.md`) |
| `/clear-offline-memory` | Clear local offline memory |

### System & Utilities
| Command | Description |
|---|---|
| `/screenshot [q]` | Capture screen, optionally ask AI about it |
| `/ocr <image>` | Extract and explain text from an image |
| `/clip explain` | Analyse clipboard content with AI |
| `/atspi [status\|on\|off\|install]` | Manage AT-SPI screen awareness daemon |
| `/dbus [status\|ping\|install]` | Manage D-Bus desktop integration daemon |
| `/encrypt` / `/decrypt` | Encrypt or decrypt text |
| `/notify [on\|off]` | Toggle desktop notifications |
| `/remind <t> <msg>` | Set a timed reminder (e.g. `/remind 1h check build`) |
| `/schedule add <t> <msg>` | Add a scheduled reminder |
| `/search <q>` | Web search from the terminal |
| `/fetch <url>` | Fetch and summarise a URL |
| `/qr <text\|url>` | Generate a QR code |
| `/share` | Share last output |
| `/open [file]` | Open a file in the default application |
| `/repair` | AI self-repair — diagnose and fix broken Electra config |
| `/repair forge <desc>` | AI generates a custom repair tool |
| `/patterns` or `/gaps` | View error pattern log and stability report |
| `/tasks` | View heartbeat background task list |

### Account & Access
| Command | Description |
|---|---|
| `/account` or `/whoami` | Show your current account, tier, and daily limits |
| `/login` | Log in to your Patreon/Electra account |
| `/logout` | Log out |
| `/unlock` | Enter an access token to unlock Pro models |
| `/profile` | View your usage profile |

### Git & Code Hosting
| Command | Description |
|---|---|
| `/github` | GitHub agent — repos, issues, PRs, releases |
| `/codeberg` or `/cb` | Codeberg agent — Forgejo/Gitea repos, issues, PRs |
| `/cb connect` | Set up your Codeberg Personal Access Token |
| `/cb repos` | List your repositories |
| `/cb issues` | Open issues in active repo |
| `/cb prs` | Open pull requests |
| `/cb notifications` | Unread notifications |

### Plugins
| Command | Description |
|---|---|
| `/plugin list` | List all loaded plugins |
| `/plugin reload` | Hot-reload plugins after editing |
| `/plugin install <file>` | Install a plugin from a file |
| `/plugin publish <file>` | Submit a plugin to the community repo |
| `/plugin community` | Browse community plugins |
| `/plugin test <TOKEN> <q>` | Test a plugin directly |
| `/plugin dir` | Open plugin folder in file manager |

---

## Plugin System Guide

**Electra AI Center** is distributed as a compiled binary to protect proprietary backend credentials. The **plugin system** is the open extension layer that allows the community to contribute new features, connect third-party APIs, and extend Electra's capabilities — all without access to the source code.

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

AGENT plugins are indistinguishable from built-in agents (Google, Discord, Spotify, etc.) from the router's perspective. They get the same routing priority and no "community plugin" label. Use this type when your plugin is a full feature agent rather than a quick intercept.

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
from datetime import datetime

PLUGIN_NAME        = "Activity Logger"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Logs mode switches, file writes, and messages"
PLUGIN_AUTHOR      = "YourName"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "HOOK"

PLUGIN_TRIGGERS    = []   # HOOK — no routing involvement
PLUGIN_ROUTE_TOKEN = "ACTIVITY_LOGGER"
PLUGIN_COMMANDS    = []
PLUGIN_REQUIRES    = []

_log_path = ""

def on_startup(context: dict):
    global _log_path
    _log_path = os.path.join(context["user_home"], ".electra", "plugin_activity.log")
    _write(f"Electra started — session {context.get('session_id', '?')}")

def on_mode_change(old_mode: str, new_mode: str):
    _write(f"Mode: {old_mode} → {new_mode}")

def on_file_write(path: str, content: str):
    _write(f"File written: {path}  ({len(content.split())} words)")

def on_message_post(prompt: str, response: str):
    _write(f"Q: {prompt[:60]}…  A: {len(response)} chars")

def _write(msg: str):
    if not _log_path:
        return
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(_log_path, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {msg}\n")
```

---

## 9. COMMAND Plugin — Slash Commands Only

COMMAND plugins register slash commands without any routing involvement. They are not visible to the router at all.

```python
PLUGIN_NAME        = "Custom Commands"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Adds /greet and /bye commands"
PLUGIN_AUTHOR      = "YourName"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "COMMAND"

PLUGIN_TRIGGERS    = []
PLUGIN_ROUTE_TOKEN = "MY_COMMANDS"
PLUGIN_COMMANDS    = ["/greet", "/bye"]
PLUGIN_REQUIRES    = []

def handle_command(command: str, args: str) -> bool:
    if command == "/greet":
        print(f"Hello, {args or 'world'}!")
        return True
    if command == "/bye":
        print("Goodbye!")
        return True
    return False
```

---

## 10. Optional Functions — All Types

| Function | Signature | Purpose |
|---|---|---|
| `setup` | `(config: dict) -> bool` | Called at load — return `False` to disable plugin (e.g. missing API key) |
| `handle_command` | `(command: str, args: str) -> bool` | Handle slash commands registered in `PLUGIN_COMMANDS` |
| `get_panel_content` | `() -> str` | GUI sidebar panel content (Markdown supported) |
| `get_toolbar_actions` | `() -> list[dict]` | GUI toolbar buttons |
| `on_startup` | `(context: dict)` | Post-load lifecycle event (HOOK type mainly, but all types support it) |
| `on_shutdown` | `(context: dict)` | Clean shutdown event |
| `on_mode_change` | `(old: str, new: str)` | Mode switch event |
| `on_file_write` | `(path: str, content: str)` | File write event (Coder mode) |
| `on_message_pre` | `(prompt: str) -> str` | Pre-routing prompt transformer |
| `on_message_post` | `(prompt: str, response: str)` | Post-response observer |

---

## 11. Config Files — Storing API Keys

Store credentials in `~/.config/ai_plugins/YOUR_TOKEN.json` (replace `YOUR_TOKEN` with your `PLUGIN_ROUTE_TOKEN`, lowercased):

```json
{
    "api_key": "sk-your-key-here",
    "default_model": "llama3-8b-8192",
    "region": "us-east-1"
}
```

Electra loads this automatically and passes it to your `setup(config)` function. **Never hardcode credentials in the plugin file itself.**

---

## 12. Dependency Declaration — PLUGIN_REQUIRES

Declare pip packages your plugin needs:

```python
PLUGIN_REQUIRES = ["feedparser>=6.0", "beautifulsoup4", "pillow"]
```

Electra checks these at load time. If a package is missing, a warning is shown and the plugin is disabled. Users can install them with:

```bash
pip install feedparser beautifulsoup4 pillow
```

The following packages are **always available** (bundled): `requests`, `json`, `os`, `re`, `datetime`, `threading`.

---

## 13. GUI Integration — Sidebar Panels & Toolbar Actions

Register a live sidebar panel that updates automatically:

```python
def on_startup(context: dict):
    if context.get("gui_active"):
        context["notify_panel"](
            token      = PLUGIN_ROUTE_TOKEN,
            label      = "My Panel",
            content    = get_panel_content,   # callable, called on each refresh
            refresh_s  = 30,                  # refresh every 30 seconds
        )

def get_panel_content() -> str:
    return "**Status:** OK\nLast check: just now"
```

Register toolbar buttons:

```python
def get_toolbar_actions() -> list:
    return [
        {"label": "Refresh", "icon": "view-refresh", "callback": _on_refresh},
        {"label": "Settings", "icon": "preferences-system", "callback": _on_settings},
    ]

def _on_refresh():
    pass  # called when user clicks the Refresh button
```

---

## 14. Inter-Plugin Communication

Plugins can call each other via `context["plugins"]`:

```python
def run(prompt: str, context: dict) -> str:
    plugins = context.get("plugins", {})
    crypto  = plugins.get("CRYPTO")
    if crypto:
        price = crypto.run("btc price", context)
        return f"From Crypto plugin: {price}"
    return "Crypto plugin not loaded."
```

---

## 15. How Plugins Connect to the Router

The router AI sees your plugin like this (from its system prompt):

```
# AGENT PLUGINS — treat these as first-class built-in agents:
CRYPTO        — Live crypto prices from CoinGecko. Triggers: "crypto price", "btc price"...

# COMMUNITY PLUGINS — route to these when triggers match:
GROQ          — Route queries to Groq LLM API. Triggers: "ask groq", "use groq"...
MY_COMMANDS   — Custom slash commands (no routing involvement)
```

The router uses this context to decide whether to send a message to your plugin. AGENT plugins appear in the primary routing section alongside `GOOGLE`, `DISCORD`, `SPOTIFY`, etc.

---

## 16. Managing Plugins

```
/plugin list                  # list all loaded plugins with status
/plugin reload                # hot-reload all plugins (no restart needed)
/plugin install <file.py>     # install a plugin from a local file
/plugin sync                  # sync community plugin list
/plugin community             # browse available community plugins
/plugin publish <file.py>     # submit your plugin to the community
/plugin test GROQ hello       # call a plugin's run() directly for testing
/plugin dir                   # open ~/.config/ai_plugins in file manager
```

---

## 17. Plugin Coder Mode — Let AI Write Your Plugin

The fastest way to create a plugin — describe what you want and Electra writes it:

```
/plugin build a plugin that fetches live stock prices from Yahoo Finance
```

The AI will:
1. Ask clarifying questions (API key needed? slash commands? GUI panel?)
2. Generate a complete, ready-to-use plugin file
3. Install it to `~/.config/ai_plugins/`
4. Hot-reload automatically

You can also ask Electra to modify an existing plugin:

```
/plugin update GROQ to support streaming responses
```

---

## 18. Writing Plugins Manually

Minimum viable plugin (copy this skeleton):

```python
"""
Plugin Name: My Plugin
Description: What this plugin does
Author: YourName
Version: 1.0.0
"""

PLUGIN_NAME        = "My Plugin"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "One-line description for the router"
PLUGIN_AUTHOR      = "YourName"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "ROUTER"

PLUGIN_TRIGGERS    = ["my trigger phrase", "another trigger"]
PLUGIN_ROUTE_TOKEN = "MY_PLUGIN"     # must be unique, ALL_CAPS
PLUGIN_COMMANDS    = ["/myplugin"]
PLUGIN_REQUIRES    = []

def setup(config: dict) -> bool:
    # Load credentials from config file — return False to disable
    return True

def run(prompt: str, context: dict) -> str:
    # Main handler — return Markdown string or "" to fall through
    return f"My plugin received: {prompt}"

def handle_command(command: str, args: str) -> bool:
    if command == "/myplugin":
        print(run(args, {}))
        return True
    return False
```

Save as `~/.config/ai_plugins/my_plugin.py` and run `/plugin reload`.

---

## 19. Complete Plugin Examples

### Example 1 — Groq LLM (ROUTER + slash command)

```python
"""
Plugin Name: Groq Agent
Description: Route queries to Groq's ultra-fast LLM API.
Requires: GROQ.json with {"api_key": "gsk_..."}
"""
import requests

PLUGIN_NAME        = "Groq Agent"
PLUGIN_VERSION     = "2.0.0"
PLUGIN_DESCRIPTION = "Route queries to Groq LLM API (ultra-fast inference)"
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
        print(run(args or "", {}))
        return True
    return False
```

---

### Example 2 — CoinGecko Crypto Prices (AGENT + GUI Panel)

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
PLUGIN_TYPE        = "AGENT"

PLUGIN_TRIGGERS    = ["crypto price", "bitcoin price", "btc price",
                      "eth price", "ethereum price", "coin price",
                      "price of btc", "price of eth", "how much is btc"]
PLUGIN_ROUTE_TOKEN = "CRYPTO"
PLUGIN_COMMANDS    = ["/crypto"]
PLUGIN_REQUIRES    = []

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
            token        = PLUGIN_ROUTE_TOKEN,
            label        = "Crypto",
            content      = _panel_content,
            refresh_s    = 120,
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
    found = next((cid for sym, cid in _COIN_MAP.items() if sym in p), None)
    if not found:
        return "[Crypto] Couldn't identify coin. Try: 'btc price' or '/crypto eth'"
    try:
        r = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={"ids": found, "vs_currencies": "usd", "include_24hr_change": "true"},
            timeout=10,
        )
        r.raise_for_status()
        data = r.json().get(found, {})
        _last_prices[found] = data
        price = data.get("usd", "N/A")
        chg   = data.get("usd_24h_change", 0)
        arrow = "📈" if chg >= 0 else "📉"
        return f"**{found.title()}**\n  Price : ${price:,.2f} USD\n  24h   : {arrow} {chg:+.2f}%"
    except Exception as e:
        return f"[Crypto] Error: {e}"

def handle_command(command: str, args: str) -> bool:
    if command == "/crypto":
        print(run(args or "btc price", {}))
        return True
    return False
```

---

## 20. Testing and Debugging

```
/plugin list                          # confirm it loaded
/plugin test GROQ what is ML?         # call run() directly
/plugin reload                        # hot-reload after edits
/plugin dir                           # open plugin folder in Nemo
```

**Common load failures:**

| Symptom | Cause |
|---|---|
| Missing from `/plugin list` | Missing required variable or `run()` |
| `setup() failed` | `setup()` returned `False` — usually missing API key |
| `missing deps [...]` | `PLUGIN_REQUIRES` package not installed |
| Duplicate token warning | Another plugin uses the same `PLUGIN_ROUTE_TOKEN` |
| Syntax error | Python syntax error in plugin file |

---

## 21. Plugin Ideas and Use Cases

**AGENT Plugins** — OpenAI, Anthropic, Groq, Perplexity, Weather, News, Stock ticker  
**HOOK Plugins** — Session logger, backup trigger, prompt guard, phone notifications  
**ROUTER/COMMAND** — Crypto prices, Home Assistant, Notion, Todoist, Plex, Jira  
**MakuluLinux-specific** — System monitor panel, Timeshift snapshots, package watcher

---

## 22. Rules and Best Practices

```python
# ✅ Read credentials from config
def setup(config: dict) -> bool:
    global _API_KEY
    _API_KEY = config.get("api_key", "")
    return bool(_API_KEY)

# ✅ Wrap all external calls in try/except with timeout
r = requests.get("https://api.example.com", timeout=10)

# ✅ Return "" to fall through when you can't handle it
def run(prompt, context):
    if "my trigger" not in prompt.lower():
        return ""

# ✅ Use context["user_home"] — never hardcode paths
log = os.path.join(context["user_home"], ".electra", "my_plugin.log")

# ❌ Never hardcode credentials or broad triggers
# ❌ Never import from ai_terminal (closed binary)
# ❌ Never hardcode /home/username paths
```

---

## 23. Reserved Tokens

Do not use these as your `PLUGIN_ROUTE_TOKEN`:

```
CHAT  CODER  WRITER  COMMAND  LIVE  IMAGE  VIDEO  AUDIO  TRAVEL  NOVEL
PLAN  PLUGIN  GOOGLE  HOME_ASSISTANT  RSS  GITHUB_AGENT  SPOTIFY
DISCORD  REDDIT  FINANCE  TELEGRAM_SERVICE  AGENT_SERVICE  ISO_AGENT
APP_AGENT  NVIDIA_AGENT  TROUBLESHOOT  ASK_COMMAND  ASK_CODER  WEATHER
CODEBERG  SOURCE_CODE  BLOG  SWARM  DBUS  ATSPI  HEARTBEAT
```

---

## 24. Contributing

1. Test your plugin locally and confirm it works
2. Strip any personal API keys from the plugin file
3. Include a clear docstring header with name, author, version, setup instructions
4. Submit a PR to the Electra plugins repository
5. Or use `/plugin publish <filename.py>` to submit directly from the terminal

---

*Electra AI Center — MakuluLinux*  
*Plugin System v2.0 · Binary v2026.06.21-r5*  
*© MakuluLinux.com — Community contributions welcome*
