<think>We need to output a plugin file content only, raw Python source, no markdown fences. It should be placed in ~/.config/ai_plugins. It should handle "hello" request. Probably a ROUTER plugin with triggers like ["hello", "hi", "hey"]? Or maybe it's a COMMAND? The request is just "hello". The plugin should respond appropriately. Provide metadata, triggers, route token, commands maybe. Should be self-contained, handle errors, use context.print_fn maybe. Provide PLUGIN_REQUIRES empty.

We need to output only raw Python source, starting with module docstring or import line. Provide the required metadata and run function.

Let's craft a plugin named "AutoReply Hello". Use PLUGIN_TYPE = "ROUTER". PLUGIN_TRIGGERS = ["hello", "hi", "hey", "greetings"] maybe. PLUGIN_ROUTE_TOKEN = "HELLO". PLUGIN_COMMANDS = ["/hello"].

In run(prompt, context): if prompt.strip().lower() in ["hello","hi","hey"]: return "Hello! How can I assist you today?" Use context["print_fn"] to output maybe progressive. But must return a non-empty string.

Also need to handle capability gap detection: maybe the plugin should detect repeated requests and respond accordingly. But simple.

We'll include PLUGIN_REQUIRES = [].

Write code:

"""
AutoHello Plugin
"""

PLUGIN_NAME = "AutoHello"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles greeting requests like 'hello' and provides a friendly response."
PLUGIN_AUTHOR = "Jacque"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["hello", "hi", "hey", "greetings"]
PLUGIN_ROUTE_TOKEN = "HELLO"
PLUGIN_COMMANDS = ["/hello"]
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    # Normalize prompt
    lowered = prompt.strip().lower()
    greetings = {"hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"}
    if lowered in greetings:
        # Use Rich rendering via print_fn if available
        if "print_fn" in context:
            context["print_fn"]("[bold green]Bot:[/bold green] Hello! How can I help you today?")
        else:
            print("Bot: Hello! How can I help you today?")
        return "Hello! How can I help you today?"
    # Not a greeting, let other plugins handle
    return ""

But must return non-empty string on success; if not a greeting, maybe return empty? Might cause failure. But we can just return a default friendly message? Probably only handle greetings.

We need to ensure we don't crash. Use try/except.

Add try/except around everything.

Let's produce final code.
</think>
"""
AutoHello Plugin
"""
PLUGIN_NAME        = "AutoHello"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Handles greeting requests like 'hello' and provides a friendly response."
PLUGIN_AUTHOR      = "Jacque"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "ROUTER"
PLUGIN_TRIGGERS    = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
PLUGIN_ROUTE_TOKEN = "HELLO"
PLUGIN_COMMANDS    = ["/hello"]
PLUGIN_REQUIRES    = []

def run(prompt: str, context: dict) -> str:
    try:
        lowered = prompt.strip().lower()
        greetings = {
            "hello",
            "hi",
            "hey",
            "greetings",
            "good morning",
            "good afternoon",
            "good evening",
        }
        if lowered in greetings:
            # Use Rich rendering if print_fn is available
            if "print_fn" in context and callable(context["print_fn"]):
                context["print_fn"]("[bold green]Bot:[/bold green] Hello! How can I help you today?")
            else:
                # Fallback simple print
                print("Bot: Hello! How can I help you today?")
            # Return a non‑empty response to signal successful handling
            return "Hello! How can I help you today?"
        # Not a greeting – let other plugins or the default router handle it
        return ""
    except Exception as e:
        # Never let the plugin crash the host application
        if "print_fn" in context and callable(context["print_fn"]):
            context["print_fn"]("[bold red]AutoHello[/bold red] Error: {}".format(str(e)))
        return ""