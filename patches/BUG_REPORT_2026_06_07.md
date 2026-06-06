# Bug Report & Fix Log — 2026-06-07

**Audit type:** Full codebase review  
**Files audited:** `ai_terminal.py`, `finance_bot.py`, `electra_bar_qt.py`, `electra_bar_launcher.py`, `heartbeat_agent.py`, `compile.sh`, `docker.sh`  
**Patch script:** [`patches/bugfix_2026_06_07.py`](patches/bugfix_2026_06_07.py)  
**Total bugs found:** 14 (2 Critical · 4 High · 5 Medium · 3 Low)  
**Total bugs fixed in this patch:** 9 (all Critical + High + key Medium)

---

## How to apply

```bash
# From your Electra source directory (where ai_terminal.py lives):
python3 /path/to/bugfix_2026_06_07.py

# Review the changes:
git diff ai_terminal.py finance_bot.py electra_bar_qt.py

# Recompile:
bash docker.sh
sudo cp ai_terminal.bin /usr/share/MakuluSetup/tools/
```

Backups of original files are written to `.patch_backups/bugfix_2026_06_07/` before any edits.

---

## Critical Bugs

### BUG-01 — Duplicate `_novel_api_call()` silently shadows itself
**File:** `ai_terminal.py` · **Lines:** ~7641 and ~8575  
**Severity:** Critical — silent wrong behavior  

Two top-level `def _novel_api_call(...)` definitions exist in the file. Python replaces the first with the second at import time with no warning. The first definition is the correct full SSE-streaming implementation (longer, handles `thinking` tokens, proper error reporting). The second is a shorter stub that shadows it permanently. Any difference in behavior between the two means the first version's logic is permanently discarded.

**Fix:** The patch detects both definitions, compares their length to determine which is the complete implementation, and removes the shorter one. The surviving definition is the full streaming version.

---

### BUG-02 — Finance GUI `ChatWorker` uses `verify=False` and disables SSL warnings
**File:** `finance_bot.py` · **Location:** `ChatWorker.run()`  
**Severity:** Critical — security vulnerability  

Inside `ChatWorker.run()` (the finance GUI's AI chat), the code does:
```python
import urllib3
urllib3.disable_warnings()
resp = requests.post(CHAT_ENDPOINT, json=payload, ..., verify=False)
```

This disables SSL certificate verification globally on that thread and suppresses the warning that would otherwise alert the developer. Any man-in-the-middle attack between the user's machine and `makululinux.us:2007` is completely silent. This is particularly dangerous because the finance chat sends earnings context, API credentials configuration, and income stream data.

The inconsistency is striking: the main `_ai_call()` helper in the same file correctly uses `verify=True`. Only the GUI worker is wrong.

**Fix:** Removed `urllib3.disable_warnings()` entirely and changed `verify=False` → `verify=True`.

---

## High Bugs

### BUG-03 — Finance GUI `ChatWorker` hardcodes `conversation_id="finance_gui_chat"`
**File:** `finance_bot.py` · **Location:** `ChatWorker.run()` payload  
**Severity:** High — all users share one server-side memory slot  

The AI chat payload contains:
```python
"conversation_id": "finance_gui_chat",
```

Per project rule #1, the backend uses `conversation_id` to store and retrieve conversation history in ChromaDB. With a static hardcoded string, every user on every machine writes to the same server-side memory bucket. This means:
- User A can have their finance context bleed into User B's chat
- The local `_history` list maintained in the GUI is redundant/inconsistent with the server's view
- Clearing chat in the GUI does not clear server-side memory

**Fix:** `ElectraFinanceWindow.__init__` now generates `self._chat_conv_id = str(uuid.uuid4())` once per GUI session. This UUID is passed through `ChatWorker.__init__` and used in the payload.

---

### BUG-04 — `/newchat` handler missing `global command_conversation_id`
**File:** `ai_terminal.py` · **Location:** `/newchat` command handler  
**Severity:** High — command history never resets on /newchat  

The `/newchat` handler contains:
```python
elif user_input.lower() == "/newchat":
    import uuid as _uuid
    conversation_id = str(_uuid.uuid4())   # ← updates chat global ✓
    ...
    command_conversation_id = str(_uuid.uuid4())  # ← BUG: local variable!
```

The `conversation_id` assignment works because it's declared `global` higher up in the same scope. But `command_conversation_id` has no `global` declaration in this block — Python treats the assignment as creating a brand-new local variable that disappears when the block exits. The actual global `command_conversation_id` used by `process_command_message()` is never touched. After `/newchat`, command mode silently continues on the old server conversation thread.

**Fix:** Added `global command_conversation_id` at the top of the `/newchat` handler block.

---

### BUG-05 — `_novel_api_call` generates a fresh `uuid4()` on every call
**File:** `ai_terminal.py` · **Location:** `_novel_api_call()` payload  
**Severity:** High — no server-side novel memory accumulates  

The comment in the code says *"Fresh conversation_id per call"* and the payload does:
```python
"conversation_id": str(uuid.uuid4()),
```

A new UUID per API call means the backend sees each architect/chapter/scene call as a completely isolated session. The server's MemPalace never accumulates novel context. If the chain fails mid-generation and the user retries, the server has no memory of what was already written. Consistency between scenes relies entirely on the local `messages` arrays passed by the client.

**Fix:** `_novel_api_call` now accepts an optional `session_id` parameter. `run_novel_generation()` mints one UUID at the start of the full generation run and passes it to every API call, giving the server a stable handle for the entire novel session.

---

### BUG-06 — `electra_bar_qt.py` `_ensure_xcb_platform()` has no offscreen fallback
**File:** `electra_bar_qt.py` · **Location:** `_ensure_xcb_platform()`  
**Severity:** High — standalone bar hard-crashes when libxcb-cursor0 missing  

`electra_bar_launcher.py` and `electra_bar_qt.py` both implement xcb detection. The launcher version (which runs when going through `electra_bar.bin`) sets `QT_QPA_PLATFORM=offscreen` as a last resort to prevent a hard crash. The bar's own internal copy only prints a warning message and does nothing — if the bar runs standalone or the env var isn't set before `QApplication.__init__`, Qt crashes unconditionally with no recovery.

Additionally, both implementations call `subprocess.run(["dpkg", "-l", "libxcb-cursor0"])` unconditionally. On non-Debian distributions (Arch, Fedora, openSUSE, Alpine), `dpkg` doesn't exist, so the exception handler catches it and assumes xcb is fine — but on some systems it might still fail for a different reason, leading to confusing behavior.

**Fix:**
1. Added `shutil.which("dpkg")` guard — only probe with dpkg on Debian/Ubuntu
2. Added `os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")` when xcb_ok is False, preventing the hard crash

---

## Medium Bugs (documented, patched where straightforward)

### BUG-07 — `heartbeat_agent.py` hardcodes `conversation_id="agent_heartbeat"`
**File:** `heartbeat_agent.py` · **Location:** `_action_web_search()`  
**Severity:** Medium — privacy: all users share one server memory slot  

All heartbeat agent tasks across all users write to the same `"agent_heartbeat"` bucket on the server. One user's task research context bleeds into another user's heartbeat session.

**Fix:** Added `_load_or_create_heartbeat_id()` which persists a UUID in `~/.electra/heartbeat_id` (same pattern as chat and coder IDs). All web search calls now use `_HEARTBEAT_CONV_ID`.

---

### BUG-08 — `_quick_classify()` TASK fast-path routes common chat phrases to coder
**File:** `ai_terminal.py` · **Location:** `_quick_classify()`  
**Severity:** Medium — mis-routing degrades user experience  

The TASK verb fast-path matched: `show`, `check`, `validate`, `verify`, `clean`, `format`, `convert`, `test`. These are extremely common in chat questions:
- *"show me how recursion works"* → routed to CODER (wrong)
- *"check if my understanding is right"* → routed to CODER (wrong)
- *"format this text as a list"* → routed to CODER (wrong)

**Fix:** Removed the ambiguous verbs from the regex. They now fall through to the AI router call which correctly classifies them as CHAT.

---

### BUG-09 — `finance_bot.py` `SMART_MODEL` hardcoded with no fallback
**File:** `finance_bot.py` · **Location:** `_ai_call()`  
**Severity:** Low-Medium — silent empty responses when model unavailable  

If `qwen/qwen3.5-122b-a10b` is removed, rate-limited, or overloaded, `_ai_call()` returns `"[Finance] Empty AI response"` with no retry. Unlike the main app which has a full fallback chain, the finance bot had none.

**Fix:** Added `_FINANCE_MODEL_CHAIN = [SMART_MODEL, FAST_MODEL, "qwen/qwen2.5-72b-instruct"]`. `_ai_call()` now iterates the chain, returning the first successful response.

---

## Remaining Items (not patched — require manual review)

### BUG-10 — `finance_bot` `_ai_call()` non-streaming POST may fail if server always streams
**File:** `finance_bot.py` · **Severity:** Medium  
If the server returns `text/event-stream` regardless of the `stream` field, `resp.json()` will fail. Add `"stream": False` explicitly to the payload and add a content-type check before calling `.json()`. Verify with the server owner whether the `/v1/chat/completions` endpoint can be called without streaming.

### BUG-11 — `electra_gui.py` mode switch clears chat UI but not backend `conversation_id`
**File:** `electra_gui.py` · **Severity:** Medium  
Switching Chat→Coder→Chat in the GUI calls `clearChat()` in JavaScript but does not signal `ai_terminal` to reset the relevant `conversation_id`. The server-side history from the previous mode remains active and can contaminate the new mode's context. Requires a `MODE_CHANGE` signal handler in `ai_terminal` that resets (or rotates) the appropriate conversation ID file.

### BUG-12 — `compile.sh` bar target may fail silently if `gi` bindings not in Docker env
**File:** `compile.sh` · **Severity:** Medium  
The `--enable-plugin=gi` flag requires `python3-gi` accessible at compile time inside the Docker container. `docker.sh` installs GTK system packages but does not explicitly verify `python3 -c "import gi"` before triggering Nuitka. A pre-flight `python3 -c "import gi; print('gi OK')" || exit 1` before the Nuitka call in `compile.sh`'s bar target would catch this early.

### BUG-13 — `electra_bar_qt.py` and `electra_bar_launcher.py` duplicate `_find_qt_plugin_path()`
**File:** Both bar files · **Severity:** Low  
Identical function in two places. Any path candidate update must be made in both. Consolidate into one location when doing the next bar refactor.

### BUG-14 — Release notes must be bumped before every compile
**File:** `ai_terminal.py` · **Severity:** Low (process)  
The developer notice requires `_RELEASE_VERSION` and `_RELEASE_NOTES` to be updated with every change. The patch script handles this automatically for the current patch, but future changes require manual attention.

---

## Files Changed by This Patch

| File | Changes |
|---|---|
| `ai_terminal.py` | BUG-01, BUG-04, BUG-05, BUG-08, release notes bump |
| `finance_bot.py` | BUG-02, BUG-03, BUG-09 |
| `electra_bar_qt.py` | BUG-06 |
| `heartbeat_agent.py` | BUG-07 |

---

## Verification Checklist

After running the patch and recompiling, verify:

- [ ] `/newchat` in terminal resets both chat and command history (check with `/github status` after)
- [ ] Finance GUI chat — open two instances, confirm they don't share AI context
- [ ] Finance GUI chat — confirm no SSL warning in console output
- [ ] Novel generation (`/novel`) completes without duplicate-function errors
- [ ] Electra Bar launches on Arch/Fedora without xcb crash
- [ ] "show me how X works" routes to Chat, not Coder
- [ ] "check my wifi" routes to Command/Troubleshoot, not Coder blindly
- [ ] `python3 -c "import ast; ast.parse(open('ai_terminal.py').read())"` passes
