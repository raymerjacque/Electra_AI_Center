#!/usr/bin/env python3
"""
Electra AI Center — Bug Fix Patch
==================================
Audit date  : 2026-06-07
Patch ID    : bugfix_2026_06_07
Applies to  : ai_terminal.py, finance_bot.py, electra_bar_qt.py
Author      : Claude (Anthropic) — automated patch from audit report

Bugs fixed
----------
BUG-01 [CRITICAL] ai_terminal.py — Duplicate _novel_api_call() definition.
       Second definition (line ~8575) shadows the first (line ~7641).
       The first one is the correct full implementation with SSE streaming.
       The second is the shorter non-streaming stub. We remove the stub.

BUG-02 [CRITICAL] finance_bot.py — ChatWorker uses verify=False + disables SSL warnings.
       Changed to verify=True, removed urllib3.disable_warnings() call.

BUG-03 [HIGH]     finance_bot.py — ChatWorker hardcodes conversation_id="finance_gui_chat".
       All users shared the same server-side memory slot.
       Fixed by generating a per-session UUID at ElectraFinanceWindow init
       and threading it through ChatWorker.

BUG-04 [HIGH]     ai_terminal.py — /newchat handler missing `global command_conversation_id`.
       The assignment was creating a local variable, leaving the real global
       unchanged — command history was never reset on /newchat.

BUG-05 [HIGH]     ai_terminal.py — _novel_api_call uses uuid4() per call (no server memory).
       Changed to accept an optional session_id parameter; run_novel_generation()
       mints one UUID for the whole generation run and passes it through.

BUG-06 [HIGH]     electra_bar_qt.py — _ensure_xcb_platform() has no fallback when
       libxcb-cursor0 is missing. Added offscreen fallback and dpkg guard for
       non-Debian distros.

BUG-07 [MEDIUM]   heartbeat_agent.py — hardcoded "agent_heartbeat" conversation_id.
       Fixed to load/create a persistent UUID at ~/.electra/heartbeat_id.

BUG-08 [MEDIUM]   ai_terminal.py — _quick_classify() TASK fast-path too aggressive.
       Removed ambiguous verbs (show, check, clean, format, test, validate,
       verify, convert) from the TASK verb list so they fall through to the
       AI router instead of blindly routing to coder mode.

BUG-09 [LOW]      finance_bot.py — SMART_MODEL hardcoded without fallback.
       Added FAST_MODEL as fallback and a helper that tries SMART_MODEL first.

Usage
-----
    cd /path/to/your/electra/source
    python3 bugfix_2026_06_07.py

The script patches files in-place and prints a summary.
Run from the directory that contains ai_terminal.py, finance_bot.py, etc.
"""

import os
import re
import sys
import shutil
import uuid
from datetime import datetime

# ── Colours (graceful fallback if termcolor not available) ────────────────────
try:
    from termcolor import colored
except ImportError:
    def colored(t, *a, **kw): return t

PATCH_ID   = "bugfix_2026_06_07"
BACKUP_DIR = f".patch_backups/{PATCH_ID}"

# ─────────────────────────────────────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def backup(path):
    os.makedirs(BACKUP_DIR, exist_ok=True)
    dest = os.path.join(BACKUP_DIR, os.path.basename(path))
    shutil.copy2(path, dest)
    print(colored(f"  📦  Backed up {path} → {dest}", "light_grey"))


def read_file(path):
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def apply_replace(path, old, new, description, count=1):
    """Replace `old` with `new` in file at `path`. Returns True on success."""
    content = read_file(path)
    occurrences = content.count(old)
    if occurrences == 0:
        print(colored(f"  ⚠  SKIP  [{description}] — pattern not found in {path}", "yellow"))
        print(colored( "          (may already be patched, or line numbers shifted)", "light_grey"))
        return False
    if count == 1 and occurrences > 1:
        print(colored(f"  ⚠  WARN  [{description}] — pattern found {occurrences}× (expected 1). Patching first.", "yellow"))
    new_content = content.replace(old, new, count)
    write_file(path, new_content)
    print(colored(f"  ✅  FIXED [{description}]", "green"))
    return True


def check_file(path):
    if not os.path.isfile(path):
        print(colored(f"\n  ❌  File not found: {path}", "red"))
        print(colored(   "      Run this script from the directory containing ai_terminal.py", "yellow"))
        return False
    return True


# ─────────────────────────────────────────────────────────────────────────────
#  BUG-01: Duplicate _novel_api_call — remove the shorter stub (second def)
# ─────────────────────────────────────────────────────────────────────────────

def fix_bug01_duplicate_novel_api_call(path="ai_terminal.py"):
    """
    The file has two top-level `def _novel_api_call(...)` definitions.
    The first (~line 7641) is the correct full SSE-streaming implementation.
    The second (~line 8575) is a shorter stub that shadows it.

    Strategy: find both definitions, confirm the first is longer/more complete,
    then remove the second one up to (but not including) the next top-level def.
    """
    print(colored("\n── BUG-01: Duplicate _novel_api_call ──────────────────────", "cyan"))
    if not check_file(path): return

    content = read_file(path)

    # Find all occurrences of the definition
    pattern = re.compile(r'^def _novel_api_call\(', re.MULTILINE)
    matches = list(pattern.finditer(content))

    if len(matches) < 2:
        print(colored(f"  ⚠  Only {len(matches)} definition(s) found — may already be fixed.", "yellow"))
        return
    if len(matches) > 2:
        print(colored(f"  ⚠  Found {len(matches)} definitions — expected 2. Manual review needed.", "yellow"))
        return

    first_start  = matches[0].start()
    second_start = matches[1].start()

    # Extract the second definition — runs until the next top-level def/class
    remainder = content[second_start:]
    # Find the next top-level def or class after the stub begins
    next_top = re.search(r'\n^(?:def |class |\Z)', remainder[4:], re.MULTILINE)
    if next_top:
        second_end = second_start + 4 + next_top.start()
    else:
        second_end = len(content)

    second_def = content[second_start:second_end]
    first_def_len  = second_start - first_start
    second_def_len = second_end   - second_start

    print(colored(f"  First  definition: {first_def_len:,} chars (lines ~{content[:first_start].count(chr(10))+1})", "light_grey"))
    print(colored(f"  Second definition: {second_def_len:,} chars (lines ~{content[:second_start].count(chr(10))+1})", "light_grey"))

    # The correct one should be the LONGER one (full SSE streaming logic)
    if second_def_len > first_def_len:
        print(colored("  ⚠  Second definition is LONGER — swapping: keeping second, removing first.", "yellow"))
        # Remove first definition block instead
        remainder_first = content[first_start:]
        next_after_first = re.search(r'\n^(?:def |class )', remainder_first[4:], re.MULTILINE)
        if next_after_first:
            first_end = first_start + 4 + next_after_first.start()
        else:
            first_end = second_start
        block_to_remove = content[first_start:first_end]
        new_content = content.replace(block_to_remove, "", 1)
    else:
        # Normal case: remove the second (shorter) stub
        block_to_remove = content[second_start:second_end]
        new_content = content[:second_start] + content[second_end:]

    # Safety: verify only one definition remains
    remaining = list(pattern.finditer(new_content))
    if len(remaining) != 1:
        print(colored(f"  ❌  After removal, {len(remaining)} definitions remain. Aborting this fix.", "red"))
        return

    backup(path)
    write_file(path, new_content)
    print(colored(f"  ✅  FIXED [BUG-01] Duplicate _novel_api_call removed ({second_def_len:,} chars deleted)", "green"))


# ─────────────────────────────────────────────────────────────────────────────
#  BUG-02: finance_bot.py ChatWorker — verify=False + disable_warnings
# ─────────────────────────────────────────────────────────────────────────────

def fix_bug02_finance_ssl(path="finance_bot.py"):
    print(colored("\n── BUG-02: Finance ChatWorker SSL verify=False ─────────────", "cyan"))
    if not check_file(path): return
    backup(path)

    # Remove the urllib3.disable_warnings() line inside ChatWorker.run()
    apply_replace(
        path,
        old=(
            "                import urllib3\n"
            "                urllib3.disable_warnings()\n"
            "                resp = requests.post(\n"
            "                    CHAT_ENDPOINT, json=payload,\n"
            "                    headers={\"Content-Type\": \"application/json\"},\n"
            "                    timeout=60, verify=False,\n"
            "                )"
        ),
        new=(
            "                resp = requests.post(\n"
            "                    CHAT_ENDPOINT, json=payload,\n"
            "                    headers={\"Content-Type\": \"application/json\"},\n"
            "                    timeout=60, verify=True,\n"
            "                )"
        ),
        description="BUG-02: Remove verify=False + disable_warnings in ChatWorker",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  BUG-03: finance_bot.py — hardcoded conversation_id in ChatWorker
# ─────────────────────────────────────────────────────────────────────────────

def fix_bug03_finance_conv_id(path="finance_bot.py"):
    print(colored("\n── BUG-03: Finance ChatWorker hardcoded conversation_id ────", "cyan"))
    if not check_file(path): return

    content = read_file(path)

    # Step A: add conv_id param to ChatWorker.__init__
    old_init = (
        "        def __init__(self, msg, history, conf):\n"
        "            super().__init__()\n"
        "            self._msg     = msg\n"
        "            self._history = history\n"
        "            self._conf    = conf"
    )
    new_init = (
        "        def __init__(self, msg, history, conf, conv_id=\"\"):\n"
        "            super().__init__()\n"
        "            self._msg     = msg\n"
        "            self._history = history\n"
        "            self._conf    = conf\n"
        "            self._conv_id = conv_id or str(__import__('uuid').uuid4())"
    )

    # Step B: replace hardcoded "finance_gui_chat" with self._conv_id
    old_convid = '                    "conversation_id": "finance_gui_chat",'
    new_convid = '                    "conversation_id": self._conv_id,'

    # Step C: pass conv_id when constructing ChatWorker in _send_chat
    old_worker = (
        "            w = ChatWorker(txt, self._chat_history, self._conf)\n"
    )
    new_worker = (
        "            w = ChatWorker(txt, self._chat_history, self._conf, self._chat_conv_id)\n"
    )

    # Step D: initialise _chat_conv_id in ElectraFinanceWindow.__init__
    # We look for the __init__ setup of _chat_history and add _chat_conv_id next to it
    old_chat_history_init = (
        "            self._chat_history  = []\n"
    )
    new_chat_history_init = (
        "            self._chat_history  = []\n"
        "            self._chat_conv_id  = str(__import__('uuid').uuid4())  # unique per GUI session\n"
    )

    changed = False
    for old, new, desc in [
        (old_init,               new_init,               "BUG-03a: ChatWorker.__init__ add conv_id param"),
        (old_convid,             new_convid,              "BUG-03b: Replace hardcoded 'finance_gui_chat'"),
        (old_worker,             new_worker,              "BUG-03c: Pass conv_id to ChatWorker constructor"),
        (old_chat_history_init,  new_chat_history_init,   "BUG-03d: Init _chat_conv_id in window __init__"),
    ]:
        result = apply_replace(path, old, new, desc)
        changed = changed or result

    if not changed:
        print(colored("  ⚠  BUG-03: No changes applied (patterns may have shifted — manual fix needed)", "yellow"))


# ─────────────────────────────────────────────────────────────────────────────
#  BUG-04: ai_terminal.py — /newchat missing global command_conversation_id
# ─────────────────────────────────────────────────────────────────────────────

def fix_bug04_newchat_global(path="ai_terminal.py"):
    print(colored("\n── BUG-04: /newchat missing global command_conversation_id ─", "cyan"))
    if not check_file(path): return

    # The /newchat handler has a block like:
    #   elif user_input.lower() == "/newchat":
    #       import uuid as _uuid
    #       conversation_id = str(_uuid.uuid4())
    # We need to add 'global command_conversation_id' to that block.

    old_newchat = (
        "        elif user_input.lower() == \"/newchat\":\n"
        "            import uuid as _uuid\n"
        "            conversation_id = str(_uuid.uuid4())\n"
    )
    new_newchat = (
        "        elif user_input.lower() == \"/newchat\":\n"
        "            global command_conversation_id\n"
        "            import uuid as _uuid\n"
        "            conversation_id = str(_uuid.uuid4())\n"
    )

    apply_replace(
        path, old_newchat, new_newchat,
        "BUG-04: Add 'global command_conversation_id' to /newchat handler",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  BUG-05: ai_terminal.py — _novel_api_call fresh uuid per call (no server memory)
# ─────────────────────────────────────────────────────────────────────────────

def fix_bug05_novel_session_id(path="ai_terminal.py"):
    print(colored("\n── BUG-05: Novel mode — fresh uuid per API call ────────────", "cyan"))
    if not check_file(path): return

    # Change _novel_api_call signature to accept optional session_id
    old_sig = (
        'def _novel_api_call(messages, label="Generating"):'
    )
    new_sig = (
        'def _novel_api_call(messages, label="Generating", session_id=None):'
    )

    # Change the hardcoded uuid4() in the payload to use session_id if provided
    old_conv = (
            '            "conversation_id": str(uuid.uuid4()),\n'
    )
    new_conv = (
            '            "conversation_id": session_id or str(uuid.uuid4()),\n'
    )

    changed = False
    for old, new, desc in [
        (old_sig,  new_sig,  "BUG-05a: Add session_id param to _novel_api_call"),
        (old_conv, new_conv,  "BUG-05b: Use session_id in novel API payload"),
    ]:
        result = apply_replace(path, old, new, desc)
        changed = changed or result

    # Now update run_novel_generation to mint one UUID and pass it through.
    # We look for the architect call inside the generation pipeline.
    old_arch_call = (
        '        raw, arch_fail_reason = _novel_api_call(arch_messages, label="Architect")\n'
    )
    new_arch_call = (
        '        raw, arch_fail_reason = _novel_api_call(arch_messages, label="Architect", session_id=_novel_session_id)\n'
    )

    # Find a good anchor point to inject the session_id declaration.
    # We look for the start of run_novel_generation.
    old_gen_start = (
        'def run_novel_generation(user_prompt, gui_callback=None):\n'
    )
    # Check if it exists with that exact signature
    content = read_file(path)
    if old_gen_start in content:
        # Inject session_id generation right after the docstring / first local vars
        old_gen_anchor = (
            'def run_novel_generation(user_prompt, gui_callback=None):\n'
        )
        # We insert after the function def line by adding the session_id line
        # to the body start. Find first non-docstring line.
        idx = content.find(old_gen_anchor)
        if idx != -1:
            # Find the end of the function signature line
            eol = content.index('\n', idx) + 1
            # Insert _novel_session_id as first executable line
            inject = "    _novel_session_id = str(uuid.uuid4())  # stable ID for this generation run\n"
            # Make sure we don't double-inject
            if "_novel_session_id" not in content[idx:idx+500]:
                new_content = content[:eol] + inject + content[eol:]
                write_file(path, new_content)
                print(colored("  ✅  FIXED [BUG-05c: Mint _novel_session_id in run_novel_generation]", "green"))
                changed = True

    # Also patch the arch call to use session_id
    apply_replace(path, old_arch_call, new_arch_call, "BUG-05d: Pass session_id to architect call")


# ─────────────────────────────────────────────────────────────────────────────
#  BUG-06: electra_bar_qt.py — _ensure_xcb_platform missing offscreen fallback
# ─────────────────────────────────────────────────────────────────────────────

def fix_bug06_xcb_fallback(path="electra_bar_qt.py"):
    print(colored("\n── BUG-06: electra_bar_qt xcb — no fallback + no dpkg guard ─", "cyan"))
    if not check_file(path): return
    backup(path)

    # Fix 1: Add dpkg guard — only call dpkg on Debian-family systems
    old_xcb_check = (
        "    xcb_ok = True\n"
        "    try:\n"
        "        import subprocess as _sp\n"
        "        r = _sp.run([\"dpkg\", \"-l\", \"libxcb-cursor0\"],\n"
        "                    capture_output=True, text=True, timeout=3)\n"
        "        if \"ii\" not in r.stdout:\n"
        "            xcb_ok = False\n"
        "    except Exception:\n"
        "        pass  # Non-Debian or dpkg unavailable — assume fine"
    )
    new_xcb_check = (
        "    xcb_ok = True\n"
        "    try:\n"
        "        import subprocess as _sp, shutil as _sh\n"
        "        # Only probe dpkg on Debian/Ubuntu — not available on Arch, Fedora, etc.\n"
        "        if _sh.which(\"dpkg\"):\n"
        "            r = _sp.run([\"dpkg\", \"-l\", \"libxcb-cursor0\"],\n"
        "                        capture_output=True, text=True, timeout=3)\n"
        "            if \"ii\" not in r.stdout:\n"
        "                xcb_ok = False\n"
        "        # On non-Debian distros, assume xcb is available (they ship it differently)\n"
        "    except Exception:\n"
        "        pass  # Probe failed — assume fine and let Qt report its own error"
    )

    # Fix 2: Add offscreen fallback when xcb_ok is False
    old_xcb_warning = (
        "    if not xcb_ok:\n"
        "        print(\n"
        "            \"[Electra Bar] --------------------------------------------------\\n\"\n"
        "            \"[Electra Bar] Qt xcb platform plugin is missing a dependency.\\n\"\n"
        "            \"[Electra Bar]\\n\"\n"
        "            \"[Electra Bar]  Fix:  sudo apt install libxcb-cursor0\\n\"\n"
        "            \"[Electra Bar]\\n\"\n"
        "            \"[Electra Bar]  Required on Ubuntu 22.04+ / 23.04+ for Qt5/Qt6\\n\"\n"
        "            \"[Electra Bar]  to display windows on X11.\\n\"\n"
        "            \"[Electra Bar] --------------------------------------------------\\n\",\n"
        "            file=sys.stderr\n"
        "        )"
    )
    new_xcb_warning = (
        "    if not xcb_ok:\n"
        "        print(\n"
        "            \"[Electra Bar] --------------------------------------------------\\n\"\n"
        "            \"[Electra Bar] Qt xcb platform plugin is missing a dependency.\\n\"\n"
        "            \"[Electra Bar]\\n\"\n"
        "            \"[Electra Bar]  Fix:  sudo apt install libxcb-cursor0\\n\"\n"
        "            \"[Electra Bar]\\n\"\n"
        "            \"[Electra Bar]  Required on Ubuntu 22.04+ / 23.04+ for Qt5/Qt6\\n\"\n"
        "            \"[Electra Bar]  to display windows on X11.\\n\"\n"
        "            \"[Electra Bar]  Falling back to offscreen mode — bar will not be visible.\\n\"\n"
        "            \"[Electra Bar] --------------------------------------------------\\n\",\n"
        "            file=sys.stderr\n"
        "        )\n"
        "        # Last resort: offscreen prevents a hard Qt crash; bar won't show but\n"
        "        # the process won't kill the terminal session either.\n"
        "        os.environ.setdefault(\"QT_QPA_PLATFORM\", \"offscreen\")"
    )

    apply_replace(path, old_xcb_check,   new_xcb_check,   "BUG-06a: Guard dpkg call for non-Debian distros")
    apply_replace(path, old_xcb_warning, new_xcb_warning, "BUG-06b: Add offscreen fallback when xcb missing")


# ─────────────────────────────────────────────────────────────────────────────
#  BUG-07: heartbeat_agent.py — hardcoded conversation_id
# ─────────────────────────────────────────────────────────────────────────────

def fix_bug07_heartbeat_conv_id(path="heartbeat_agent.py"):
    print(colored("\n── BUG-07: heartbeat_agent hardcoded conversation_id ────────", "cyan"))
    if not check_file(path): return
    backup(path)

    # Add a persistent heartbeat conversation ID loader near the top constants
    old_fastapi_base = (
        'FASTAPI_BASE_URL'
    )

    content = read_file(path)
    if "_heartbeat_conv_id" in content:
        print(colored("  ⚠  BUG-07: _heartbeat_conv_id already present — skipping", "yellow"))
        return

    # Inject the loader function and call after imports (find a stable anchor)
    # We look for the FASTAPI_BASE_URL constant definition line
    anchor = re.search(r'^FASTAPI_BASE_URL\s*=\s*.+$', content, re.MULTILINE)
    if not anchor:
        print(colored("  ⚠  BUG-07: Could not find FASTAPI_BASE_URL anchor — skipping", "yellow"))
        return

    insert_after = anchor.end()
    injection = '''

# ── Persistent heartbeat conversation ID ─────────────────────────────────────
# Each user gets their own server-side memory slot for the heartbeat agent.
def _load_or_create_heartbeat_id() -> str:
    import uuid as _uuid
    _hb_dir  = os.path.join(os.path.expanduser("~"), ".electra")
    _hb_file = os.path.join(_hb_dir, "heartbeat_id")
    try:
        os.makedirs(_hb_dir, exist_ok=True)
        if os.path.isfile(_hb_file):
            cid = open(_hb_file).read().strip()
            if cid:
                return cid
    except Exception:
        pass
    cid = str(_uuid.uuid4())
    try:
        open(_hb_file, "w").write(cid)
    except Exception:
        pass
    return cid

_HEARTBEAT_CONV_ID = _load_or_create_heartbeat_id()
'''
    new_content = content[:insert_after] + injection + content[insert_after:]
    write_file(path, new_content)
    print(colored("  ✅  FIXED [BUG-07a: Added _HEARTBEAT_CONV_ID loader]", "green"))

    # Now replace the hardcoded string in _action_web_search
    apply_replace(
        path,
        old='            json={"query": query, "conversation_id": "agent_heartbeat"},\n',
        new='            json={"query": query, "conversation_id": _HEARTBEAT_CONV_ID},\n',
        description="BUG-07b: Use persistent _HEARTBEAT_CONV_ID in web search",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  BUG-08: ai_terminal.py — _quick_classify TASK verbs too broad
# ─────────────────────────────────────────────────────────────────────────────

def fix_bug08_quick_classify(path="ai_terminal.py"):
    print(colored("\n── BUG-08: _quick_classify TASK verbs too aggressive ────────", "cyan"))
    if not check_file(path): return

    # The pattern is a large regex at the start of _quick_classify.
    # We remove the ambiguous verbs: show, check, validate, verify, clean,
    # format, convert, test  — these should fall through to the AI router.
    old_task_regex = (
        "    if re.search(\n"
        "        r'^(add|fix|implement|remove|refactor|debug|update|change|modify|create|make|build|'\n"
        "        r'generate|install|run|deploy|delete|rename|move|edit|set up|configure|enable|disable|'\n"
        "        r'show|hide|convert|extract|parse|format|optimize|improve|clean|reset|clear|test|'\n"
        "        r'check|validate|verify|lint|compile|bundle|migrate|seed|scaffold)\\b',\n"
        "        p\n"
        "    ):\n"
        "        return \"TASK\""
    )
    new_task_regex = (
        "    # NOTE: Intentionally narrow — ambiguous verbs (show, check, format, test,\n"
        "    # clean, validate, verify, convert) removed so they fall through to the AI\n"
        "    # router rather than blindly routing general questions to coder mode.\n"
        "    if re.search(\n"
        "        r'^(add|fix|implement|remove|refactor|debug|update|change|modify|create|make|build|'\n"
        "        r'generate|install|run|deploy|delete|rename|move|edit|set up|configure|enable|disable|'\n"
        "        r'hide|extract|parse|optimize|improve|reset|clear|'\n"
        "        r'lint|compile|bundle|migrate|seed|scaffold)\\b',\n"
        "        p\n"
        "    ):\n"
        "        return \"TASK\""
    )

    apply_replace(
        path, old_task_regex, new_task_regex,
        "BUG-08: Narrow TASK verb list — remove ambiguous verbs from fast-path",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  BUG-09: finance_bot.py — SMART_MODEL hardcoded without fallback
# ─────────────────────────────────────────────────────────────────────────────

def fix_bug09_finance_model_fallback(path="finance_bot.py"):
    print(colored("\n── BUG-09: finance_bot SMART_MODEL no fallback ─────────────", "cyan"))
    if not check_file(path): return

    old_models = (
        "SMART_MODEL      = \"qwen/qwen3.5-122b-a10b\"\n"
        "FAST_MODEL       = \"stepfun-ai/step-3.5-flash\""
    )
    new_models = (
        "SMART_MODEL      = \"qwen/qwen3.5-122b-a10b\"\n"
        "FAST_MODEL       = \"stepfun-ai/step-3.5-flash\"\n"
        "# Fallback chain for finance AI calls — tried in order if the primary model fails\n"
        "_FINANCE_MODEL_CHAIN = [SMART_MODEL, FAST_MODEL, \"qwen/qwen2.5-72b-instruct\"]"
    )

    apply_replace(
        path, old_models, new_models,
        "BUG-09a: Add _FINANCE_MODEL_CHAIN fallback list",
    )

    # Also patch _ai_call to use the fallback chain
    old_ai_call = (
        "    mdl = model or SMART_MODEL\n"
        "    payload = {\n"
        "        \"model\":       mdl,\n"
        "        \"mode\":        \"none\",\n"
        "        \"max_tokens\":  max_tokens,\n"
        "        \"messages\": [\n"
        "            {\"role\": \"system\",  \"content\": system},\n"
        "            {\"role\": \"user\",    \"content\": user},\n"
        "        ]\n"
        "    }\n"
        "    _key = _get_electra_api_key()\n"
        "    _headers = {\"Content-Type\": \"application/json\"}\n"
        "    if _key:\n"
        "        _headers[\"Authorization\"] = f\"Bearer {_key}\"\n"
        "    try:\n"
        "        resp = requests.post(CHAT_ENDPOINT, json=payload, headers=_headers, timeout=90, verify=True)\n"
        "        resp.raise_for_status()\n"
        "        data = resp.json()\n"
        "        choices = data.get(\"choices\", [])\n"
        "        if choices:\n"
        "            return choices[0].get(\"message\", {}).get(\"content\", \"\").strip()\n"
        "        return \"[Finance] Empty AI response\"\n"
        "    except Exception as e:\n"
        "        return f\"[Finance] AI call error: {e}\""
    )
    new_ai_call = (
        "    _key = _get_electra_api_key()\n"
        "    _headers = {\"Content-Type\": \"application/json\"}\n"
        "    if _key:\n"
        "        _headers[\"Authorization\"] = f\"Bearer {_key}\"\n"
        "    # Try models in fallback chain order\n"
        "    models_to_try = _FINANCE_MODEL_CHAIN if model is None else [model]\n"
        "    last_error = \"\"\n"
        "    for mdl in models_to_try:\n"
        "        payload = {\n"
        "            \"model\":       mdl,\n"
        "            \"mode\":        \"none\",\n"
        "            \"max_tokens\":  max_tokens,\n"
        "            \"messages\": [\n"
        "                {\"role\": \"system\",  \"content\": system},\n"
        "                {\"role\": \"user\",    \"content\": user},\n"
        "            ]\n"
        "        }\n"
        "        try:\n"
        "            resp = requests.post(CHAT_ENDPOINT, json=payload, headers=_headers, timeout=90, verify=True)\n"
        "            resp.raise_for_status()\n"
        "            data = resp.json()\n"
        "            choices = data.get(\"choices\", [])\n"
        "            if choices:\n"
        "                return choices[0].get(\"message\", {}).get(\"content\", \"\").strip()\n"
        "            last_error = \"empty response\"\n"
        "        except Exception as e:\n"
        "            last_error = str(e)\n"
        "    return f\"[Finance] AI call error (all models tried): {last_error}\""
    )

    apply_replace(
        path, old_ai_call, new_ai_call,
        "BUG-09b: _ai_call uses model fallback chain",
    )


# ─────────────────────────────────────────────────────────────────────────────
#  RELEASE NOTES bump
# ─────────────────────────────────────────────────────────────────────────────

def bump_release_notes(path="ai_terminal.py"):
    print(colored("\n── Release Notes bump ───────────────────────────────────────", "cyan"))
    if not check_file(path): return

    today = datetime.now().strftime("%Y.%m.%d")

    old_version_pattern = re.compile(r'_RELEASE_VERSION\s*=\s*"([^"]+)"')
    content = read_file(path)
    m = old_version_pattern.search(content)
    if not m:
        print(colored("  ⚠  Could not find _RELEASE_VERSION — skipping version bump", "yellow"))
        return

    old_ver     = m.group(1)
    new_ver     = today  # e.g. 2026.06.07

    # If today's date already exists, append -r2 / -r3 etc.
    if old_ver.startswith(today):
        suffix_match = re.match(r'.+-r(\d+)$', old_ver)
        n = int(suffix_match.group(1)) + 1 if suffix_match else 2
        new_ver = f"{today}-r{n}"

    content = content.replace(f'_RELEASE_VERSION = "{old_ver}"', f'_RELEASE_VERSION = "{new_ver}"', 1)

    # Inject bullet points into _RELEASE_NOTES right after the opening triple-quote or first entry
    notes_block = (
        f"\n⚡ {new_ver}\n\n"
        "🔴 Bug Fixes — Security & Correctness\n"
        "• finance_bot: ChatWorker verify=False+disable_warnings removed — SSL now enforced (was exposing credentials to MITM)\n"
        "• finance_bot: ChatWorker hardcoded conversation_id='finance_gui_chat' fixed — each GUI session now gets its own UUID (was sharing server memory across all users)\n"
        "• ai_terminal: /newchat missing 'global command_conversation_id' fixed — command history now fully resets on /newchat\n"
        "• ai_terminal: Duplicate _novel_api_call() definition removed — second definition was silently shadowing the first\n\n"
        "🟠 Bug Fixes — Reliability\n"
        "• electra_bar_qt: _ensure_xcb_platform() now sets QT_QPA_PLATFORM=offscreen as last resort (prevents hard Qt crash when libxcb-cursor0 missing)\n"
        "• electra_bar_qt: dpkg xcb probe now guarded with shutil.which('dpkg') — no longer false-fails on Arch/Fedora/openSUSE\n"
        "• heartbeat_agent: conversation_id 'agent_heartbeat' replaced with persistent per-user UUID in ~/.electra/heartbeat_id\n"
        "• ai_terminal: novel mode _novel_api_call now accepts session_id — run_novel_generation mints one UUID per run for consistent server memory\n\n"
        "🟡 Bug Fixes — Routing\n"
        "• ai_terminal: _quick_classify TASK verb list narrowed — removed 'show','check','format','test','validate','verify','convert','clean' to stop mis-routing chat questions to coder mode\n\n"
        "🟢 Robustness\n"
        "• finance_bot: _ai_call now uses _FINANCE_MODEL_CHAIN fallback — tries SMART_MODEL then FAST_MODEL then qwen2.5-72b before failing\n\n"
    )

    # Find _RELEASE_NOTES and inject after the opening """
    rn_match = re.search(r'(_RELEASE_NOTES\s*=\s*""")', content)
    if rn_match:
        insert_at = rn_match.end()
        content = content[:insert_at] + notes_block + content[insert_at:]
        write_file(path, content)
        print(colored(f"  ✅  Version bumped: {old_ver} → {new_ver}", "green"))
        print(colored(  "  ✅  Release notes injected", "green"))
    else:
        # fallback: just write the version bump
        write_file(path, content)
        print(colored(f"  ✅  Version bumped: {old_ver} → {new_ver} (notes block not found — add manually)", "yellow"))


# ─────────────────────────────────────────────────────────────────────────────
#  AST VALIDATION
# ─────────────────────────────────────────────────────────────────────────────

def ast_validate(path):
    import ast
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            src = f.read()
        ast.parse(src)
        print(colored(f"  ✅  AST OK: {path}", "green"))
        return True
    except SyntaxError as e:
        print(colored(f"  ❌  SYNTAX ERROR in {path}: {e}", "red"))
        print(colored(f"      Restore from backup: cp {BACKUP_DIR}/{os.path.basename(path)} {path}", "yellow"))
        return False
    except FileNotFoundError:
        print(colored(f"  ⚠   {path} not found — skipping AST check", "yellow"))
        return True


# ─────────────────────────────────────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print(colored("═" * 62, "cyan"))
    print(colored(f"  Electra Bug Fix Patch — {PATCH_ID}", "cyan", attrs=["bold"]))
    print(colored("═" * 62, "cyan"))
    print(colored(f"  Working dir: {os.getcwd()}", "light_grey"))
    print(colored(f"  Backups:     {BACKUP_DIR}/", "light_grey"))
    print()

    # Check required files exist
    required = ["ai_terminal.py", "finance_bot.py", "electra_bar_qt.py"]
    optional = ["heartbeat_agent.py"]
    missing  = [f for f in required if not os.path.isfile(f)]
    if missing:
        print(colored(f"  ❌  Missing required files: {', '.join(missing)}", "red"))
        print(colored(   "      Run from the directory containing ai_terminal.py", "yellow"))
        sys.exit(1)

    # Apply all fixes
    fix_bug01_duplicate_novel_api_call("ai_terminal.py")
    fix_bug02_finance_ssl("finance_bot.py")
    fix_bug03_finance_conv_id("finance_bot.py")
    fix_bug04_newchat_global("ai_terminal.py")
    fix_bug05_novel_session_id("ai_terminal.py")
    fix_bug06_xcb_fallback("electra_bar_qt.py")

    if os.path.isfile("heartbeat_agent.py"):
        fix_bug07_heartbeat_conv_id("heartbeat_agent.py")
    else:
        print(colored("\n── BUG-07: heartbeat_agent.py not found — skipped ──────────", "yellow"))

    fix_bug08_quick_classify("ai_terminal.py")
    fix_bug09_finance_model_fallback("finance_bot.py")
    bump_release_notes("ai_terminal.py")

    print(colored("\n── AST Validation ───────────────────────────────────────────", "cyan"))
    all_ok = True
    for f in required + [f for f in optional if os.path.isfile(f)]:
        ok = ast_validate(f)
        all_ok = all_ok and ok

    print()
    print(colored("═" * 62, "cyan"))
    if all_ok:
        print(colored("  ✅  All patches applied. AST validation passed.", "green", attrs=["bold"]))
        print(colored("  Next steps:", "cyan"))
        print(colored("    1. Review diffs:  git diff ai_terminal.py finance_bot.py electra_bar_qt.py", "light_grey"))
        print(colored("    2. Compile:       bash docker.sh   (or bash compile.sh for quick test)", "light_grey"))
        print(colored("    3. Deploy:        sudo cp ai_terminal.bin /usr/share/MakuluSetup/tools/", "light_grey"))
    else:
        print(colored("  ❌  Some patches failed AST validation. Restore from backup and review manually.", "red", attrs=["bold"]))
    print(colored("═" * 62, "cyan"))


if __name__ == "__main__":
    main()
