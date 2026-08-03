<think>Got it, let's tackle this. First, the user's request was "hello" and it failed because there's no Proactive Scanner handler? Wait no, wait the error says capability gap for repeated requests, wait no, wait the user said the request was hello, but the error is from Proactive Scanner? Wait no, wait the task is to write a plugin that handles this type of request. Wait wait, let's re-read.

Wait the user's request was "hello", but the error says CAPABILITY_GAP because user repeatedly requested this type 3 times with no dedicated handler. Oh right, so we need a plugin that handles greeting/hello requests? Wait no, wait wait, no—wait the error was in agent 'Proactive Scanner'? Wait no, wait the error says "This failed in agent 'Proactive Scanner' with: Error type: CAPABILITY_GAP Error message: User repeatedly requested this type of task (3 times) with no dedicated handler." Oh right, so the Proactive Scanner agent doesn't have a handler for this, so we need to create a plugin that acts as a handler for this? Wait no, wait the plugin type: since it's filling a capability gap, PLUGIN_TYPE is ROUTER? Wait no, wait the spec says for auto-repair plugins that fill a capability gap, PLUGIN_TYPE is ROUTER. Wait but what's the trigger? Wait the user's request was "hello", so triggers for greetings? Wait no, wait wait—wait the error was that the Proactive Scanner couldn't handle the request, so maybe the plugin is for the Proactive Scanner? No, wait no, let's think again.

Wait first, the required metadata. Let's set PLUGIN_NAME to something like "Greeting Handler" because the user said hello. Wait no, wait the error was from Proactive Scanner? Wait no, wait the error message says the user repeatedly requested this type of task 3 times with no dedicated handler. The user's request was "hello", so the task type is greeting/hello responses? Wait but why was it in Proactive Scanner? Oh maybe the Proactive Scanner is supposed to handle greetings but doesn't, so we need a plugin that intercepts those requests?

Wait no, let's follow the spec. The plugin is a ROUTER plugin (since it's auto-repair, filling capability gap). So PLUGIN_TYPE = "ROUTER". What's the trigger? The user said "hello", so triggers like "hello", "hi", "hey", "greetings"? Wait but wait, the error was in agent 'Proactive Scanner'—wait maybe the PLUGIN_ROUTE_TOKEN should be PROACTIVE_SCANNER? No, wait no, the route token is what the router uses to route to this plugin. Wait no, wait if the request was going to Proactive Scanner but failing, then maybe we need to make a plugin that handles the requests that were going to Proactive Scanner? Wait no, maybe I'm overcomplicating. Wait the user's request was "hello", so the capability gap is handling greeting messages. So let's make a ROUTER plugin that triggers on common greetings, returns a friendly response.

Wait but let's make sure. Let's set the metadata correctly:

PLUGIN_NAME = "Greeting Responder"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles greeting requests like hello, hi, hey to fill capability gap"
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = [] # no external deps needed
PLUGIN_TRIGGERS = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = ["/greet"]

Then the run function. The run function takes prompt and context. We need to check if the prompt matches any of the triggers? Wait no, the router already matches the triggers, right? Wait the PLUGIN_TRIGGERS are the phrases that cause the router to route to this plugin. So when the user says "hello", the router sees the trigger, calls run with the prompt. Then we can return a friendly greeting, maybe personalized? Wait but we can use the context if needed, but for hello, just a friendly response. Wait but also, we should use context["print_fn"] to show output? Wait no, the run function returns a string, which the router will display. Wait but let's make it friendly. Also, make sure no crashes, no external calls.

Wait wait, but the error was in Proactive Scanner. Oh! Wait a minute, maybe the original request was supposed to go to Proactive Scanner, but it doesn't have a handler for greetings? So maybe the PLUGIN_ROUTE_TOKEN should be PROACTIVE_SCANNER? No, wait no, the route token has to be unique. Wait no, the existing plugins are none yet, so any token is fine. Wait but let's make sure. Wait the error says the request failed in agent 'Proactive Scanner'—so maybe the user was trying to use the Proactive Scanner agent, but it can't handle the request. So maybe we need an AGENT plugin? Wait no, the spec says for auto-repair plugins that fill capability gap, PLUGIN_TYPE is ROUTER. Wait let's check the spec again: "PLUGIN_TYPE = "ROUTER" (for auto-repair plugins that fill a capability gap)". Oh right, that's explicitly stated. So it's a ROUTER plugin.

Wait but let's make the run function robust. Let's see: the prompt is the user's input, which is "hello" in this case. So the run function can return a friendly greeting, maybe mention that it's handling the greeting since the Proactive Scanner was unavailable? Wait no, maybe just a natural response. Wait but let's make it work. Also, make sure that if for some reason the trigger is matched, it returns a proper string. No external calls, so no try/except needed for external stuff, but maybe just in case.

Wait also, the file name is autorepair_<token_lowercase>.py, so the token is GREETING, so file name is autorepair_greeting.py, which matches.

Wait let's write the code:

First the metadata, then the run function. Let's see:

Wait the module docstring? The spec says start with module docstring or first import. Let's add a docstring.

Wait:

"""
Electra AI Auto-Repair Plugin: Greeting Handler
Fills capability gap for greeting requests (e.g. hello, hi) that previously failed in the Proactive Scanner agent.
"""
import os

PLUGIN_NAME = "Greeting Responder"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles common greeting requests to resolve CAPABILITY_GAP errors from missing Proactive Scanner handler"
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []
PLUGIN_TRIGGERS = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening", "howdy", "what's up"]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = ["/greet"]

def run(prompt: str, context: dict) -> str:
    # Normalize prompt to lowercase for matching
    normalized_prompt = prompt.strip().lower()
    
    # Get user's name from context if available, else default
    user_name = context.get("user_name", "there")
    
    # Generate appropriate response based on time of day if possible
    from datetime import datetime
    current_hour = datetime.now().hour
    if 5 <= current_hour < 12:
        time_greeting = "Good morning"
    elif 12 <= current_hour < 17:
        time_greeting = "Good afternoon"
    elif 17 <= current_hour < 21:
        time_greeting = "Good evening"
    else:
        time_greeting = "Hello"
    
    # Check for specific greeting types
    if normalized_prompt in ["good morning", "good afternoon", "good evening"]:
        response = f"{prompt.strip().capitalize()}! How can I help you today?"
    elif normalized_prompt in ["hi", "hello", "hey", "howdy"]:
        response = f"{time_greeting}, {user_name}! What can I do for you?"
    elif "what's up" in normalized_prompt:
        response = f"Not much, {user_name}! Just here to help. What's on your mind?"
    else:
        # Fallback for any other matched trigger
        response = f"Hello! I'm here to assist you with any questions or tasks you have."
    
    # Use print_fn if available for progressive output (optional, since we return the string)
    if "print_fn" in context and callable(context["print_fn"]):
        context["print_fn"](response)
    
    return response

Wait wait, but importing datetime inside the function? Or at the top? Either is fine, but maybe at the top. Also, is user_name in the context? Wait the spec's context keys don't mention user_name, so maybe don't rely on that. Oh right, the context keys listed are user_home, plugin_dir, chat_history, etc. No user_name. So remove that part. Let's adjust:

Wait remove the user_name part, since it's not in the context. So:

"""
Electra AI Auto-Repair Plugin: Greeting Handler
Fills capability gap for greeting requests (e.g. hello, hi) that previously failed in the Proactive Scanner agent.
"""
from datetime import datetime

PLUGIN_NAME = "Greeting Responder"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles common greeting requests to resolve CAPABILITY_GAP errors from missing Proactive Scanner handler"
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []
PLUGIN_TRIGGERS = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening", "howdy", "what's up"]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = ["/greet"]

def run(prompt: str, context: dict) -> str:
    normalized_prompt = prompt.strip().lower()
    current_hour = datetime.now().hour
    
    # Determine time-appropriate greeting
    if 5 <= current_hour < 12:
        time_greeting = "Good morning"
    elif 12 <= current_hour < 17:
        time_greeting = "Good afternoon"
    elif 17 <= current_hour < 21:
        time_greeting = "Good evening"
    else:
        time_greeting = "Hello"
    
    # Generate response based on input
    if normalized_prompt in ["good morning", "good afternoon", "good evening"]:
        response = f"{prompt.strip().capitalize()}! How can I assist you today?"
    elif normalized_prompt in ["hi", "hello", "hey", "howdy"]:
        response = f"{time_greeting}! What can I help you with?"
    elif "what's up" in normalized_prompt:
        response = "Not much! I'm here and ready to help with whatever you need. What's on your mind?"
    else:
        response = "Hello! I'm your Electra assistant. How can I help you today?"
    
    # Optional: print via Rich renderer if available
    if "print_fn" in context and callable(context["print_fn"]):
        try:
            context["print_fn"](response)
        except Exception:
            # Silently fail if print_fn is unavailable, don't crash the host
            pass
    
    return response

Wait that's good. Let's check the rules:

- PLUGIN_ROUTE_TOKEN is GREETING, no clash (no existing plugins).
- PLUGIN_ENABLED is True.
- PLUGIN_TYPE is ROUTER, which is correct for auto-repair.
- run returns a non-empty string.
- Uses context["print_fn"] if available, wraps in try/except so it doesn't crash.
- No hardcoded paths, uses os.path if needed but we don't need it here.
- No external imports except datetime which is standard library, so no PLUGIN_REQUIRES needed.
- Wraps the print_fn call in try/except, so no crashes.
- The triggers cover the user's "hello" request, plus other common greetings so it handles similar requests.
- The file name would be autorepair_greeting.py which matches the spec.

Wait but wait, the error was that the request failed in Proactive Scanner. Does this plugin address that? Yes, because it handles the greeting requests that were failing, so future identical requests (hello, hi, etc.) will be caught by this plugin's triggers and handled successfully, instead of going to Proactive Scanner and failing.

Wait but should we mention that it's handling the Proactive Scanner gap? The description does that. That's fine.

Wait is there any issue here? Let's check: no external dependencies, so PLUGIN_REQUIRES is empty, which is fine. The run function doesn't crash, returns a valid string. The triggers include "hello" which is the user's request. Perfect.

Wait another thing: the spec says "Wrap ALL external calls in try/except"—but we have no external calls, only standard library datetime, which is safe. The print_fn call is wrapped in try/except, which is good.

Yes, this should</think>
"""
Electra AI Auto-Repair Plugin: Greeting Handler
Fills capability gap for greeting requests (e.g. hello, hi) that previously failed in the Proactive Scanner agent.
"""
from datetime import datetime

PLUGIN_NAME = "Greeting Responder"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles common greeting requests to resolve CAPABILITY_GAP errors from missing Proactive Scanner handler"
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []
PLUGIN_TRIGGERS = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening", "howdy", "what's up"]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = ["/greet"]

def run(prompt: str, context: dict) -> str:
    normalized_prompt = prompt.strip().lower()
    current_hour = datetime.now().hour

    # Determine time-appropriate base greeting
    if 5 <= current_hour < 12:
        time_greeting = "Good morning"
    elif 12 <= current_hour < 17:
        time_greeting = "Good afternoon"
    elif 17 <= current_hour < 21:
        time_greeting = "Good evening"
    else:
        time_greeting = "Hello"

    # Generate context-aware response
    if normalized_prompt in ["good morning", "good afternoon", "good evening"]:
        response = f"{prompt.strip().capitalize()}! How can I assist you today?"
    elif normalized_prompt in ["hi", "hello", "hey", "howdy"]:
        response = f"{time_greeting}! What can I help you with?"
    elif "what's up" in normalized_prompt:
        response = "Not much! I'm here and ready to help with whatever you need. What's on your mind?"
    else:
        response = "Hello! I'm your Electra assistant. How can I help you today?"

    # Optional: Use Rich renderer for output if available, fail silently if not
    if "print_fn" in context and callable(context["print_fn"]):
        try:
            context["print_fn"](response)
        except Exception:
            pass

    return response