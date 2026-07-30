<think>We need to output a plugin file content only, raw Python source, no markdown fences. It should be placed in ~/.config/ai_plugins, auto-named autorepair_<token_lowercase>.py. Need to fill capability gap: user asks "czy zapamatasz wszystko co ci powiem?" (Polish: "do you remember everything I tell you?"). This is a capability gap: need a plugin that handles this request. Likely an AGENT or ROUTER? The request is a question about memory. Could be handled as an AGENT that answers. Or a HOOK? Probably an AGENT plugin that responds to that phrase. But the spec says for capability gap fill, use ROUTER plugin with PLUGIN_TYPE = "ROUTER" and PLUGIN_TRIGGERS include phrases like "czy zapamatasz wszystko co ci powiem?" or maybe "czy zapamitasz wszystko co ci powiem?" Use PLUGIN_ROUTE_TOKEN unique. Provide run(prompt, context) returning answer.

We need to output only raw Python source, starting with module docstring or import lines. Must include required metadata: PLUGIN_NAME, PLUGIN_VERSION, PLUGIN_DESCRIPTION, PLUGIN_AUTHOR optional, PLUGIN_ENABLED True, PLUGIN_TYPE = "ROUTER", PLUGIN_TRIGGERS = [...], PLUGIN_ROUTE_TOKEN = "...". Also PLUGIN_COMMANDS maybe not needed for ROUTER? In spec example they used PLUGIN_COMMANDS = ["/groq"] but not required. We can include.

We need to handle the request: answer in Polish maybe: "Nie, nie mam pamięci długotrwałej, tylko krótkoterminową w obrębie aktualnej sesji." Something like that.

Also need to include PLUGIN_REQUIRES maybe empty.

We must not crash, wrap calls in try/except. Use context["print_fn"] to output progressive output? Could just use print_fn.

We'll write a plugin that intercepts triggers: "czy zapamatasz wszystko co ci powiem?" and maybe also "czy zapamitasz wszystko co ci powiem?" (typo). Provide triggers list with both.

Write run function: if prompt contains that phrase (case-insensitive?), respond accordingly.

We'll use context["print_fn"](answer) to display.

We'll also maybe add a small memory note: we can store in electra_state? But not needed.

We'll output the plugin file content.

Make sure no markdown fences. Just raw Python code.

Let's craft:

"""
Plugin to handle memory queries.
"""

PLUGIN_NAME = "Memory Helper"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Answers questions about short-term memory capabilities."
PLUGIN_AUTHOR = "Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["czy zapamatasz wszystko co ci powiem?", "czy zapamitasz wszystko co ci powiem?"]
PLUGIN_ROUTE_TOKEN = "memoryhelper"
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    try:
        # Normalize prompt
        lowered = prompt.lower()
        if "czy zapamatasz wszystko co ci powiem" in lowered or "czy zapamitasz wszystko co ci powiem" in lowered:
            answer = (
                "Nie, nie mam trwałej pamięci poza bieżącą sesją. "
                "Mogę recordar tylko to, o czym rozmawiamy w tej chwili."
            )
            context["print_fn"](answer)
            return answer
    except Exception as e:
        # Should never crash the host
        context["print_fn"](f"[Memory Helper] Błąd: {e}")
    return ""

But need to ensure run returns non-empty string on success. If we used print_fn, we still need to return something. Could return answer.

Also need to import anything? Not needed.

Make sure we don't hardcode paths.

Thus final output is the plugin source.

Let's produce final answer.
</think>
"""
Plugin to handle Polish queries about short‑term memory.
"""

PLUGIN_NAME = "Memory Helper"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Answers questions about short‑term memory capabilities."
PLUGIN_AUTHOR = "Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = [
    "czy zapamatasz wszystko co ci powiem?",
    "czy zapamitasz wszystko co ci powiem?"
]
PLUGIN_ROUTE_TOKEN = "memoryhelper"
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    try:
        lowered = prompt.lower()
        if ("czy zapamatasz wszystko co ci powiem" in lowered or
            "czy zapamitasz wszystko co ci powiem" in lowered):
            answer = (
                "Nie, nie mam trwałej pamięci poza bieżącą sesją. "
                "Mogę recordar tylko to, o czym rozmawiamy w tej chwili."
            )
            context["print_fn"](answer)
            return answer
    except Exception as exc:
        # Never let the plugin crash the host application
        context["print_fn"](f"[Memory Helper] Błąd: {exc}")
    return ""