<think>We are given a specific error: the user repeatedly requested "wake up electra" and it failed because there's no dedicated handler.
 We are to write a plugin that handles this type of request.

 The error says it's a CAPABILITY_GAP and that the user requested this 5 times.

 We are to write a ROUTER plugin (since the error came from an agent, but we are to intercept the trigger and handle it).

 Steps:
 1. We need to choose a PLUGIN_ROUTE_TOKEN that doesn't clash. Since the request is "wake up electra", we can choose something like "WAKE_UP" or "ELECTRA_WAKE".
    But note: the error says the agent 'Proactive Scanner' failed. We don't want to interfere with existing agents unless we are replacing the same functionality.

 However, note the specification: we are to write a plugin that handles this type of request. The error says the user requested "wake up electra" and it failed.

 Let's analyze: the user said "wake up electra". This might be a command to wake up the Electra AI from a dormant state? But note the context: the app is called Electra.

 Since the error says it's a CAPABILITY_GAP, it means the router didn't find a plugin that matches the trigger for this request.

 We are to write a ROUTER plugin that triggers on phrases like "wake up electra".

 But note: the existing plugin list includes:
   autorepair_token_login.py, autorepair_ollama_login.py, autorepair_greeting.py

 We are to write a new plugin that will be named: autorepair_<token_lowercase>.py

 We must choose a token that doesn't clash. Let's choose "WAKE_UP" as the token? But note the existing ones are about repair and login.

 However, the error says the request is "wake up electra". We can set:

   PLUGIN_TRIGGERS = ["wake up electra", "wake electra", "electra wake up", "electra wake"]

 But note: the error says the user repeatedly requested this type of task. So we want to catch variations.

 We are to return a string that indicates success.

 What should the plugin do? The request is to "wake up electra". Since Electra is the app itself, maybe we just need to respond that Electra is awake?

 However, note the context: the app is running (since we are in a plugin). So maybe the user is trying to wake up the AI from a sleep mode? But the app is already running.

 Alternatively, maybe the user is trying to activate the AI? But the app is an AI terminal.

 Since we don't have more context, we can simply respond with a message that Electra is awake and ready.

 But note: the error came from the 'Proactive Scanner' agent. Maybe the user is trying to wake up the Proactive Scanner? We don't know.

 However, the specification says we are to handle the request "wake up electra". So we'll just handle that.

 Let's design:

   PLUGIN_NAME = "Electra Wake Up"
   PLUGIN_VERSION = "1.0.0"
   PLUGIN_DESCRIPTION = "Handles 'wake up electra' requests"
   PLUGIN_AUTHOR = "Plugin Forge"
   PLUGIN_ENABLED = True
   PLUGIN_TYPE = "ROUTER"
   PLUGIN_TRIGGERS = ["wake up electra", "wake electra", "electra wake up", "electra wake", "wake up", "wake"]
   PLUGIN_ROUTE_TOKEN = "WAKE_UP"
   PLUGIN_COMMANDS = ["/wake_up"]

 But note: the triggers might be too broad. We don't want to catch every "wake" word. However, the error says the user said "wake up electra", so we can be specific.

 However, the user might say "wake up" alone? But that might be ambiguous. Since the error is about "wake up electra", we can focus on that.

 Let's adjust:

   PLUGIN_TRIGGERS = ["wake up electra", "wake electra", "electra wake up", "electra wake"]

 But note: the user might have said exactly "wake up electra". We'll catch that.

 However, the error says the user repeatedly requested this type of task. So we want to catch the same intent.

 We'll use:

   PLUGIN_TRIGGERS = [
        "wake up electra",
        "wake electra",
        "electra wake up",
        "electra wake",
        "wake up the electra",
        "wake the electra"
   ]

 But note: the trigger matching is probably exact or substring? The specification doesn't say. We assume it's a substring match? Or exact?

 Since the original error says the user said "wake up electra", we can assume the router does a case-insensitive substring match? We don't know.

 To be safe, we can use a list of phrases that we think the user might say.

 However, note: the plugin system might do a simple "if trigger in prompt" (case insensitive). So we can use:

   triggers = ["wake up electra", "wake electra", ...]

 But if the user says "can you wake up electra", then "wake up electra" is a substring? Yes.

 So we can use:

   PLUGIN_TRIGGERS = ["wake up electra", "wake electra", "electra wake up", "electra wake"]

 But note: the user might say "wake up, electra" with a comma. We can't catch every variation. We'll stick to the main ones.

 Alternatively, we can use a more flexible approach in the run function? But the triggers are used by the router to route to us.

 We are only called if one of our triggers matches. So we want to be as inclusive as possible without being too broad.

 Since the error is about "wake up electra", we'll focus on that.

 Let's set:

   PLUGIN_TRIGGERS = ["wake up electra", "wake electra", "electra wake up", "electra wake"]

 Now, what should the run function do?

 We are to return a string. We can say:

   "Electra is now awake and ready to assist!"

 But note: the user might be trying to wake up a specific agent? The error says the agent 'Proactive Scanner' failed.

 However, we are not told what the Proactive Scanner does. We are just to handle the request.

 Since we don't have more context, we'll just respond with a generic wake up message.

 But note: the context has a `print_fn` and `notify_panel`. We can use `print_fn` to show a message in the terminal and also maybe update a panel?

 However, the specification says we must return a string. So we return a string and also we can use `print_fn` for progressive output? But the run function returns the final response.

 We can do:

   context["print_fn"]("Electra is waking up...")
   ... then do something? But what?

 Since we don't have a specific action (like starting a service), we just return a string.

 However, note: the error says the user requested this 5 times. Maybe the user expects Electra to do something when woken up? We don't know.

 Given the ambiguity, we'll just return a string that confirms Electra is awake.

 But wait: the error says the agent 'Proactive Scanner' failed. Maybe the user is trying to wake up the Proactive Scanner? We don't have a way to start an agent.

 Since we are a ROUTER plugin, we are intercepting the request and handling it. We are not starting an agent.

 So we'll just respond:

   "Electra is awake. How can I help you?"

 However, note: the user might be expecting the Proactive Scanner to start. But we don't have information about that.

 Since we are writing a plugin to fill the capability gap, we are to handle the request in a way that satisfies the user.

 Without more context, we'll assume that the user just wants to know that Electra is awake.

 Let's code accordingly.

 But note: the plugin must be named `autorepair_wake_up.py` because the token is "WAKE_UP" and we lower it.

 However, the specification says: "File will be auto-named: autorepair_<token_lowercase>.py"

 So we set:

   PLUGIN_ROUTE_TOKEN = "WAKE_UP"

 Then the file should be named: autorepair_wake_up.py

 But note: the existing plugins are named:
   autorepair_token_login.py, autorepair_ollama_login.py, autorepair_greeting.py

 So we follow the pattern.

 Let's write the plugin accordingly.

 However, note: the user might have said "wake up electra" and we are handling it. But what if the user says "wake up" without "electra"? We don't want to catch that because it might be for something else.

 But the error says the user said "wake up electra". So we are safe with the triggers we have.

 We'll write:

   PLUGIN_TRIGGERS = ["wake up electra", "wake electra", "electra wake up", "electra wake"]

 But note: the user might have said "wake up, electra" or "wake up electra please". We are only matching exact phrases? The router might do a substring.

 We don't know. We'll assume the router does a case-insensitive substring match. So if the user says "please wake up electra", then "wake up electra" is a substring? Yes.

 So we are safe.

 Let's code the plugin.

 Important: We must not crash. So we'll wrap any code in try/except? But we don't have any external calls.

 We are just returning a string.

 However, we are allowed to use context["print_fn"] to print. We can do:

   context["print_fn"]("Electra is now awake!")

 But note: the run function must return a string. We can return the same string.

 We'll do:

   response = "Electra is now awake and ready to assist!"
   context["print_fn"](response)
   return response

 But note: the print_fn might be for progressive output. We are only printing one line.

 Alternatively, we can just return the string and let the app print it? The specification says we can use print_fn to show progressive output.

 Since we don't have progressive output, we can just return.

 However, the example in the specification uses:

   return f"[My Plugin] Got: {prompt}"

 So we can just return.

 But note: the user might be in a mode where the app expects a certain format? We don't know.

 We'll return a simple string.

 Let's code accordingly.

 However, note: the error says the agent 'Proactive Scanner' failed. Maybe the user expects the Proactive Scanner to start? We don't have a way to start an agent.

 Since we are a ROUTER plugin, we are replacing the routing for this trigger. We are not starting an agent.

 So we are just going to respond with a message.

 But wait: the error says the user requested this 5 times. Maybe the user is trying to wake up the entire system? We don't know.

 Given the lack of context, we'll just respond with a wake up message.

 Let's write the plugin.

 However, note: the plugin must be placed in ~/.config/ai_plugins and named autorepair_wake_up.py.

 We are to output the raw Python source.

 Let's code accordingly.</think>
"""
Electra Wake Up Handler - Handles 'wake up electra' requests
Plugin Type: ROUTER | Token: WAKE_UP
"""

PLUGIN_NAME = "Electra Wake Up"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles 'wake up electra' requests to activate Electra AI"
PLUGIN_AUTHOR = "Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = [
    "wake up electra",
    "wake electra",
    "electra wake up",
    "electra wake",
    "wake up, electra",
    "electra, wake up",
    "wake up the electra",
    "wake the electra"
]
PLUGIN_ROUTE_TOKEN = "WAKE_UP"
PLUGIN_COMMANDS = ["/wake_up"]
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    """
    Handles wake up requests for Electra AI.
    Returns confirmation message and optionally activates GUI/notifications.
    """
    try:
        # Use print_fn for Rich Markdown rendering if available
        print_fn = context.get("print_fn")
        if print_fn:
            print_fn(":sparkles: **Electra is now awake and ready!**")
        
        # If GUI is active, update status panel
        notify_panel = context.get("notify_panel")
        if notify_panel and callable(notify_panel):
            try:
                notify_panel(
                    "Electra Status",
                    "✅ **Awake** - Ready to assist",
                    "status"
                )
            except:
                pass  # Silent fail if panel update fails
        
        # Check if we're in a specific mode and acknowledge
        current_mode = context.get("current_mode", "CHAT")
        session_id = context.get("session_id", "unknown")
        
        response = (
            "**Electra is awake!** 🚀\n\n"
            f"Session: `{session_id[:8]}...`\n"
            f"Mode: `{current_mode}`\n"
            f"Workspace: `{context.get('cwd', '~')}`\n\n"
            "I'm ready to assist with any tasks. What would you like to do?"
        )
        
        return response
        
    except Exception as e:
        return f"⚠️ Wake sequence encountered an issue: {str(e)}"