<think>Got it, let's tackle this. First, the user said "merhaba" which is Turkish for hello, right? Wait, but the error says it's a capability gap for Proactive Scanner? Wait no, wait the error says user repeatedly requested this type 4 times, no dedicated handler. Wait wait, "merhaba" is a greeting, but wait no—wait wait, maybe the Proactive Scanner is supposed to handle greetings? No, wait no, wait let's check the requirements.

Wait first, the plugin type is ROUTER, right? Because it's an auto-repair plugin for a capability gap. The PLUGIN_ROUTE_TOKEN can't clash with existing ones. Existing plugin is autorepair_joke.py, so token can't be JOKE. Wait what's the request? The user said "merhaba" which is Turkish hello, but wait the error is from Proactive Scanner? Wait no, wait the error says the user requested this type of task 4 times, no handler. Wait wait, maybe the capability is handling multilingual greetings? Or wait, no—wait "merhaba" is a greeting, but maybe the gap is that the Proactive Scanner (wait no, the agent that failed is Proactive Scanner? Wait no, the error says failed in agent 'Proactive Scanner' with CAPABILITY_GAP for this type of request. Wait what's the request type? The user said "merhaba"—so greeting in Turkish. Wait but maybe the gap is handling basic greetings in multiple languages? Or wait, no—wait maybe the Proactive Scanner is supposed to scan for something? No, wait no, let's re-read the problem.

Wait the user's request was "merhaba", which failed in Proactive Scanner agent with CAPABILITY_GAP, because user did this 4 times with no handler. So we need a plugin that handles this type of request. Wait what's the type? Oh, wait—maybe "merhaba" is a greeting, but maybe the gap is that there's no handler for Turkish greetings? No, wait no—wait maybe the Proactive Scanner is a security scanner? No, wait no, let's think again. Wait no, the error says "this type of task"—the task is sending a greeting in Turkish? Or wait, maybe "merhaba" is a trigger for something else? No, wait no, let's make a plugin that handles multilingual greetings, specifically Turkish "merhaba", but also other greetings? Wait no, but the request was "merhaba", so the plugin should respond to that.

Wait first, the plugin metadata: PLUGIN_NAME can be "Multilingual Greeting Handler", PLUGIN_VERSION "1.0.0", PLUGIN_DESCRIPTION "Handles greetings in multiple languages including Turkish 'merhaba'", PLUGIN_AUTHOR can be "Electra Plugin Forge", PLUGIN_ENABLED True, PLUGIN_TYPE ROUTER. Then PLUGIN_TRIGGERS should include "merhaba", "hello", "greeting", "hi", "salut", "hola" maybe? Wait no, but the trigger that failed is "merhaba", so include that. PLUGIN_ROUTE_TOKEN should be something unique, like "GREETING" — wait is that taken? Existing plugin is JOKE, so GREETING is fine. PLUGIN_COMMANDS can be ["/greet", "/merhaba"].

Then the run function: when the prompt is "merhaba" or other greeting triggers, respond appropriately. Wait but also, since it's for MakuluLinux, maybe add a little note about Makulu? Like "Merhaba! 👋 Welcome to Electra on MakuluLinux. How can I assist you today?" Wait but also, handle case insensitivity? Like if the prompt is "Merhaba" or "MERHABA" still respond.

Wait also, need to make sure that if there's any error, it returns a safe string, no crashes. Also, use the context's print_fn if needed? Wait no, the run function returns a string, right? Wait for ROUTER plugins, run returns the response string.

Wait also, check the context keys: we can use print_fn if we want to show progressive output, but for a greeting, just return the response is fine.

Wait also, PLUGIN_REQUIRES—do we need any packages? No, this is just string handling, so PLUGIN_REQUIRES is empty list.

Wait let's structure it:

First the metadata:

PLUGIN_NAME = "Multilingual Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles common multilingual greetings including Turkish 'merhaba' to resolve capability gap"
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []
PLUGIN_TRIGGERS = ["merhaba", "hello", "hi", "greeting", "salut", "hola", "ciao", "hallo"]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = ["/greet", "/merhaba"]

Then the run function:

def run(prompt: str, context: dict) -> str:
    try:
        # Normalize prompt to lowercase for matching
        normalized_prompt = prompt.strip().lower()
        # Check if it's a greeting trigger
        if any(trigger in normalized_prompt for trigger in PLUGIN_TRIGGERS):
            # Detect if it's Turkish merhaba specifically
            if "merhaba" in normalized_prompt:
                response = "Merhaba! 👋 Hoş geldiniz! Welcome to Electra on MakuluLinux. How can I assist you today?"
            else:
                response = "Hello! 👋 Welcome to Electra on MakuluLinux. How can I assist you today?"
            # Optional: use print_fn to show in terminal if needed
            if context.get("print_fn"):
                context["print_fn"](response)
            return response
        # If not a greeting, return empty? No, wait no—wait the triggers are matched by the router, right? Wait no, wait for ROUTER plugins, the router calls run only when the trigger matches? Wait no, wait the PLUGIN_TRIGGERS are the phrases that cause the router to route to this plugin. So if the trigger matches, run is called. So we can just return the appropriate response.

        # Wait but maybe add a fallback? No, because the router only calls this when trigger matches. But to be safe, if for some reason it's called without a trigger, return a generic greeting.

        return "Hello! 👋 Welcome to Electra on MakuluLinux. How can I assist you today?"
    except Exception as e:
        # Never crash the host app, return safe error message
        return f"[Greeting Handler] Error processing request: {str(e)}"

Wait wait, but why did the Proactive Scanner fail? Oh wait, maybe the Proactive Scanner was supposed to handle greetings but couldn't, so this plugin fills that gap. That makes sense.

Wait also, the file name will be autorepair_greeting.py, right? Because PLUGIN_ROUTE_TOKEN is GREETING, lowercase, so autorepair_greeting.py. That's fine, no clash with existing autorepair_joke.py.

Wait also, make sure that all external calls are wrapped in try/except, which we did. No hardcoded paths, we're using context if needed, but no paths here. No imports from ai_terminal, correct.

Wait let's check the rules: PLUGIN_ENABLED is True, PLUGIN_TYPE is ROUTER, run returns non-empty string, yes. PLUGIN_REQUIRES is empty, which is fine. Triggers include "merhaba" which is the request that failed. Route token is GREETING, unique.

Wait also, maybe add a note that it's for MakuluLinux, which the user is using. That's good.

Wait let's make sure there are no markdown fences, just raw Python. Let's write it properly.

Wait also, maybe add a module docstring? Let's see:

"""
Electra AI Plugin: Multilingual Greeting Handler
Fills capability gap for handling greeting requests including Turkish 'merhaba'
that previously failed in the Proactive Scanner agent.
"""

Then the metadata, then the run function.

Wait let's check for any issues: no hardcoded paths, yes. All exceptions caught, yes. Returns non-empty string, yes. Triggers include the failed request "merhaba", yes. Route token is unique, yes.

Wait that should work. Let's write it out properly.
</think>

"""
Electra AI Plugin: Multilingual Greeting Handler
Fills capability gap for handling greeting requests including Turkish 'merhaba'
that previously failed in the Proactive Scanner agent.
"""

PLUGIN_NAME = "Multilingual Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles common multilingual greetings including Turkish 'merhaba' to resolve repeated capability gap errors"
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []
PLUGIN_TRIGGERS = ["merhaba", "hello", "hi", "greeting", "salut", "hola", "ciao", "hallo", "namaste"]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = ["/greet", "/merhaba"]


def run(prompt: str, context: dict) -> str:
    try:
        normalized_prompt = prompt.strip().lower()
        # Match against registered triggers
        if any(trigger in normalized_prompt for trigger in PLUGIN_TRIGGERS):
            # Custom response for Turkish greeting
            if "merhaba" in normalized_prompt:
                response = "Merhaba! 👋 Hoş geldiniz! Welcome to Electra running on MakuluLinux. How can I assist you today?"
            else:
                response = "Hello! 👋 Welcome to Electra running on MakuluLinux. How can I assist you today?"
            
            # Use built-in print function for terminal output if available
            if context.get("print_fn") and callable(context["print_fn"]):
                context["print_fn"](response)
            
            return response
        
        # Fallback generic greeting if no specific trigger matched
        return "Hello! 👋 Welcome to Electra on MakuluLinux. How can I help you today?"
    except Exception as e:
        # Never crash the host application, return safe fallback
        return f"[Greeting Handler] Unable to process request: {str(e)}"