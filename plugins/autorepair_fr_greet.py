<think>We need to write a plugin that handles "bonjour" requests. The user says "bonjour". The error indicates capability gap: user repeatedly requested this type of task (3 times) with no dedicated handler. So we need to create a plugin that handles "bonjour" requests. Likely "bonjour" is a greeting in French. The plugin should respond appropriately. We need to choose a PLUGIN_ROUTE_TOKEN that does not clash. Let's pick "FR_GREET". The plugin type is ROUTER. Triggers: ["bonjour", "salut", "coucou"] maybe. The plugin should respond with a friendly greeting. Use context["print_fn"] to output. Return a string. No external dependencies needed. So PLUGIN_REQUIRES empty. Provide metadata. Ensure PLUGIN_ENABLED True. Provide run function. Use context["print_fn"] to show progressive output. Return a greeting string. That's it.

We need to output raw Python source. Let's write the plugin file content. Use docstring maybe. Provide metadata. Provide run. Use context["print_fn"] to print "Bonjour! Comment puis-je vous aider aujourd'hui?" or similar. Return that string. Ensure non-empty. No external imports. Use try/except around any potential errors, but none. Just safe.

Let's produce.</think>
PLUGIN_NAME        = "French Greeting Handler"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Handles French greeting requests like 'bonjour', 'salut', 'coucou'"
PLUGIN_AUTHOR      = "AutoRepair Bot"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "ROUTER"
PLUGIN_TRIGGERS    = ["bonjour", "salut", "coucou"]
PLUGIN_ROUTE_TOKEN = "FR_GREET"
PLUGIN_COMMANDS    = []

def run(prompt: str, context: dict) -> str:
    try:
        greeting = "Bonjour! Comment puis-je vous aider aujourd'hui?"
        context["print_fn"](greeting)
        return greeting
    except Exception as e:
        error_msg = f"[French Greeting Handler] Error: {e}"
        context["print_fn"](error_msg)
        return error_msg