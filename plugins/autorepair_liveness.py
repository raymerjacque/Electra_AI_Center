<think>Got it, let's tackle this. First, the user is asking "are you alive?" which is a simple liveness check. The error says the Proactive Scanner agent can't handle it, so we need a ROUTER plugin that catches these liveness check requests.

First, the plugin metadata. Let's name it something like "Liveness Check Handler" so PLUGIN_NAME is that. Version 1.0.0. Description: "Handles liveness check requests like 'are you alive?' to confirm the app is running." Author can be "Electra Plugin Community" maybe. PLUGIN_TYPE is ROUTER, right? Because it's intercepting routing for these triggers.

Triggers: what phrases would users use for liveness checks? Let's list common ones: "are you alive", "are you there", "are you working", "are you online", "is the app running", "liveness check", "ping". Yeah those cover it. PLUGIN_ROUTE_TOKEN should be something unique, like "LIVENESS" — wait, check existing plugins? The existing ones are autorepair_merhaba, autorepair_1785386250, autorepair_1785444278, so LIVENESS is safe. PLUGIN_COMMANDS can be ["/alive", "/ping"] so users can use slash commands too.

Now the run function. The prompt is the user's input. We need to check if the prompt matches any of the triggers, case-insensitive probably. Then return a friendly response confirming we're alive, maybe include some context like the current mode, session ID? Wait no, keep it simple but useful. Also, use the print_fn if needed? Wait no, the run function returns the string that's sent back to the user.

Wait also, make sure we don't crash. No external calls needed here, right? Because it's just a simple check. So no PLUGIN_REQUIRES needed, or empty list.

Wait let's structure it properly. First the required metadata variables. Then PLUGIN_TRIGGERS, PLUGIN_ROUTE_TOKEN, PLUGIN_COMMANDS. Then the run function.

Wait let's make the trigger matching case-insensitive. So in run, convert the prompt to lowercase, check if any trigger is in it. Wait but triggers are like "are you alive", so if the user types "Are you alive?" it should match. So yes, lowercase both.

What's a good response? Maybe something like "✅ Yes, I'm fully operational! Current session: {context['session_id'][:8]}... Active mode: {context['current_mode']}. How can I help you today?" That's friendly and gives useful info.

Wait also, make sure the plugin is enabled, PLUGIN_ENABLED = True. PLUGIN_TYPE is ROUTER. Let's check for clashes: existing route tokens? The existing plugins are merhaba, 1785386250, 1785444278, so LIVENESS is fine.

Wait let's write the code step by step. First the docstring? Or start with imports? Wait no, the metadata is first. Let's see:

First, the module docstring? Maybe not necessary, but can add a short one. Then the required metadata:

PLUGIN_NAME = "Liveness Check Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles liveness check requests (e.g. 'are you alive?') to confirm the app is running and responsive"
PLUGIN_AUTHOR = "Electra Plugin Community"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []  # No external dependencies needed

Then the router specific vars:
PLUGIN_TRIGGERS = [
    "are you alive",
    "are you there",
    "are you working",
    "are you online",
    "is the app running",
    "liveness check",
    "ping",
    "are you functional"
]
PLUGIN_ROUTE_TOKEN = "LIVENESS"
PLUGIN_COMMANDS = ["/alive", "/ping"]

Then the run function:
def run(prompt: str, context: dict) -> str:
    # Normalize prompt for case-insensitive matching
    normalized_prompt = prompt.lower().strip()
    # Check if any trigger matches
    if any(trigger in normalized_prompt for trigger in PLUGIN_TRIGGERS):
        # Build response with useful context
        session_short = context.get("session_id", "unknown")[:8]
        current_mode = context.get("current_mode", "unknown")
        response = (
            "✅ Yes, I'm fully operational!\n"
            f"• Session ID: {session_short}...\n"
            f"• Active mode: {current_mode}\n"
            "How can I assist you today?"
        )
        # Optional: print to console if needed via context print_fn
        # context["print_fn"](response)
        return response
    # If no trigger matches, return empty string to let other handlers process
    return ""

Wait that's good. Wait but what if the prompt doesn't match? Return empty string so the router passes it to other handlers. That's correct.

Wait also, make sure we don't have any external calls, so no try/except needed? Wait no, but maybe wrap in try/except just in case? Like:

def run(prompt: str, context: dict) -> str:
    try:
        normalized_prompt = prompt.lower().strip()
        if any(trigger in normalized_prompt for trigger in PLUGIN_TRIGGERS):
            session_short = context.get("session_id", "unknown")[:8]
            current_mode = context.get("current_mode", "unknown")
            return (
                "✅ Yes, I'm fully operational!\n"
                f"• Session ID: {session_short}...\n"
                f"• Active mode: {current_mode}\n"
                "How can I assist you today?"
            )
        return ""
    except Exception as e:
        # Fallback response if something goes wrong, don't crash the app
        return f"⚠️ Liveness check encountered an error: {str(e)}"

Yeah that's better, so even if something fails, it returns a string instead of crashing.

Wait also, check the context keys: session_id is available in v2.1, current_mode is v2.0, so that's fine. All context keys are available as per the spec.

Wait the plugin file name will be autorepair_liveness.py, right? Because the token is LIVENESS, lowercase is liveness. That's correct.

Wait let's make sure there are no hardcoded paths, no imports from ai_terminal, no external calls. Perfect, this plugin is self-contained, no dependencies, so PLUGIN_REQUIRES is empty.

Wait let's test the triggers: if user says "are you alive?" it matches, "Ping" matches, "is the app running?" matches, etc. That covers the user's request.

Is there anything missing? Let's check the spec: all required metadata is present, PLUGIN_TYPE is ROUTER, triggers are correct, route token is unique, commands are there, run function returns non-empty string on success, uses context correctly, has error handling, no hardcoded paths, no external dependencies. Yep,</think>
PLUGIN_NAME = "Liveness Check Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles liveness check requests (e.g. 'are you alive?') to confirm the app is running and responsive"
PLUGIN_AUTHOR = "Electra Plugin Community"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []

PLUGIN_TRIGGERS = [
    "are you alive",
    "are you there",
    "are you working",
    "are you online",
    "is the app running",
    "liveness check",
    "ping",
    "are you functional",
    "are you up"
]
PLUGIN_ROUTE_TOKEN = "LIVENESS"
PLUGIN_COMMANDS = ["/alive", "/ping"]

def run(prompt: str, context: dict) -> str:
    try:
        normalized_prompt = prompt.lower().strip()
        if any(trigger in normalized_prompt for trigger in PLUGIN_TRIGGERS):
            session_short = context.get("session_id", "unknown")[:8]
            current_mode = context.get("current_mode", "unknown")
            return (
                "✅ Yes, I'm fully operational!\n"
                f"• Session ID: {session_short}...\n"
                f"• Active mode: {current_mode}\n"
                "How can I assist you today?"
            )
        return ""
    except Exception as e:
        return f"⚠️ Liveness check encountered an error: {str(e)}"