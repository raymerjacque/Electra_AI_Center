<think>We need to output a plugin file content only, raw Python source, no markdown fences. It should be placed in ~/.config/ai_plugins. It must handle "merhaba" request, which is Turkish for "hello". The user repeatedly requested this type of task (4 times) with no dedicated handler. So we need a plugin that intercepts greeting-like requests in Turkish? Probably handle "merhaba", "selam", "hi", etc. Provide a response. It should be a ROUTER plugin with triggers like "merhaba", "selam", "hello", etc. Provide PLUGIN_NAME, version, description, author, enabled, type, requires maybe none. Provide PLUGIN_TRIGGERS list. Provide run function that returns appropriate response using context["print_fn"] maybe. Should not crash. Should use context keys. Should be self-contained.

We need to output only raw Python source, starting with module docstring or import lines. Probably start with docstring then metadata then run function.

Make sure to include PLUGIN_TYPE = "ROUTER". Provide PLUGIN_TRIGGERS = ["merhaba", "selam", "hello", "hi"] maybe. Provide PLUGIN_ROUTE_TOKEN unique, e.g., "MERHABA". Provide PLUGIN_COMMANDS maybe ["/merhaba"].

Implement run(prompt, context) that checks if any trigger in prompt (case-insensitive). Return a friendly greeting in Turkish maybe. Use context["print_fn"] to output progressive? Could just return string.

Also need to declare PLUGIN_REQUIRES = [].

Make sure not to import anything that may not be installed; maybe just use built-in.

Write plugin file content.

Let's craft:

"""
Plugin: Turkish Greeting Handler
Version: 1.0.0
Description: Handles Turkish greeting requests like "merhaba" to provide a friendly response.
Author: AI Plugin Developer
"""

PLUGIN_NAME = "Turkish Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles Turkish greeting requests such as 'merhaba' to provide a friendly response."
PLUGIN_AUTHOR = "AI Plugin Developer"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["merhaba", "selam", "hello", "hi", "günaydın", "good morning"]
PLUGIN_ROUTE_TOKEN = "MERHABA"
PLUGIN_COMMANDS = ["/merhaba"]
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    # Normalize prompt
    lowered = prompt.strip().lower()
    # Check if any trigger phrase is present
    for trigger in PLUGIN_TRIGGERS:
        if trigger in lowered:
            # Friendly Turkish response
            greeting = "Merhaba! Size nasıl yardımcı olabilirim?"
            # Use Rich markdown print if available
            context["print_fn"](f"**{greeting}**")
            return greeting
    # If no trigger matched, let the router continue
    return None

But need to ensure that if no trigger matches, we return None or empty string? The plugin should only handle when trigger matches; otherwise return None to let other plugins handle.

Make sure to not crash.

Also need to include the metadata at module level.

Thus final output is raw python code.

Let's produce final answer.
</think>
"""
Turkish Greeting Handler
Version: 1.0.0
Description: Handles Turkish greeting requests such as "merhaba" to provide a friendly response.
Author: AI Plugin Developer
"""
PLUGIN_NAME = "Turkish Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles Turkish greeting requests such as 'merhaba' to provide a friendly response."
PLUGIN_AUTHOR = "AI Plugin Developer"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["merhaba", "selam", "hello", "hi", "günaydın", "good morning"]
PLUGIN_ROUTE_TOKEN = "MERHABA"
PLUGIN_COMMANDS = ["/merhaba"]
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    # Normalize the incoming prompt for case‑insensitive matching
    lowered = prompt.strip().lower()

    # Check if any of the configured trigger phrases appear in the prompt
    for trigger in PLUGIN_TRIGGERS:
        if trigger in lowered:
            # Compose a friendly Turkish greeting
            greeting = "Merhaba! Size nasıl yardımcı olabilirim?"
            # Use the provided print function for Rich‑styled output
            context["print_fn"](f"**{greeting}**")
            return greeting

    # No trigger matched – let the router continue processing
    return None