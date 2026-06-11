<think>We are given that the user requested "hello" and it failed in the agent 'Proactive Scanner' with a CAPABILITY_GAP error because there's no dedicated handler for this type of task (repeated 3 times).

 We are to write a plugin that handles this type of request. Since the error says it's a capability gap for a repeated request of "hello", and the existing plugin list includes several autorepair_* plugins, it's likely that the system expects a plugin that handles a simple greeting.

 However, note that the error occurred in the 'Proactive Scanner' agent. But the user's request was just "hello". It seems that the Proactive Scanner agent is being triggered for some reason and then fails because it doesn't have a handler for "hello".

 But the specification says we are to write a plugin that handles this type of request. Since the request is "hello", we can write a simple ROUTER plugin that triggers on "hello" and returns a greeting.

 However, note that the error says the user repeatedly requested this type of task (3 times). So maybe the system is trying to route to an agent that doesn't handle "hello". We are to fill the gap.

 Let's design a plugin that:
   - Is a ROUTER plugin (since we are intercepting the routing for a trigger)
   - Has a trigger for "hello" (and maybe variations)
   - Returns a friendly greeting.

 But note: the error occurred in the 'Proactive Scanner' agent. It's possible that the router is sending the "hello" request to the Proactive Scanner because of some trigger? We don't know the existing triggers.

 However, the specification says we must choose a PLUGIN_ROUTE_TOKEN that does not clash with existing ones. We don't have a list of existing tokens, but we can look at the installed plugins:

   chuck_norris_jokes.py, autorepair_bot_explainer.py, autorepair_proscan.py, autorepair_content_summarizer.py, autorepair_hello_handler.py, autorepair_system_update.py, autorepair_proactive_scan_confirm.py, autorepair_browser_launcher.py, autorepair_greeting.py, autorepair_quickupdate.py

 We see there's already an autorepair_hello_handler.py and autorepair_greeting.py. So maybe the gap is that these are not being triggered for "hello"? Or maybe the user is saying "hello" and the router is not matching any trigger and then falling back to the Proactive Scanner?

 Since the error says the user repeatedly requested this type of task (3 times) and it failed in the Proactive Scanner, it's likely that the router is sending the request to the Proactive Scanner because no other plugin matched.

 We are to write a plugin that will match "hello" and handle it. We must choose a token that doesn't clash. Let's choose "HELLO_HANDLER" as the token.

 But note: there's already an autorepair_hello_handler.py. We don't know what that does. We are to write a new plugin that will be named autorepair_hello_handler.py? Wait, the specification says:

   "File will be auto-named: autorepair_<token_lowercase>.py"

 So if we set PLUGIN_ROUTE_TOKEN = "HELLO_HANDLER", then the file will be named autorepair_hello_handler.py. But that already exists! So we cannot use that token.

 We must choose a token that is not already used. Let's look at the existing tokens from the installed plugins? We don't have that information. But we can infer from the file names:

   chuck_norris_jokes -> token might be CHUCK_NORRIS_JOKES?
   autorepair_bot_explainer -> BOT_EXPLAINER?
   autorepair_proscan -> PROSCAN?
   autorepair_content_summarizer -> CONTENT_SUMMARIZER?
   autorepair_hello_handler -> HELLO_HANDLER?
   autorepair_system_update -> SYSTEM_UPDATE?
   autorepair_proactive_scan_confirm -> PROACTIVE_SCAN_CONFIRM?
   autorepair_browser_launcher -> BROWSER_LAUNCHER?
   autorepair_greeting -> GREETING?
   autorepair_quickupdate -> QUICKUPDATE?

 We want to handle "hello". We see there's already a HELLO_HANDLER and GREETING. So maybe the existing ones are not working? Or maybe they are for different contexts?

 Since the error says the request is being sent to the Proactive Scanner, it's possible that the existing hello handlers are not being triggered because the trigger phrases don't match exactly? Or maybe the user is saying "hello" in a context that the existing plugins don't handle?

 We are to write a plugin that will handle "hello". We must choose a token that is not already used. Let's choose a token that is not in the above list. How about "SIMPLE_GREETING"?

 But note: the specification says we must not clash. We don't have a list of all tokens, but we can try to avoid the ones we see.

 Alternatively, we can look at the error: it says the agent 'Proactive Scanner' failed. The Proactive Scanner might be an AGENT plugin? We don't know.

 Since we are writing a ROUTER plugin, we want to intercept the request before it gets to the Proactive Scanner.

 Let's design:

   PLUGIN_NAME = "Simple Greeting Handler"
   PLUGIN_VERSION = "1.0.0"
   PLUGIN_DESCRIPTION = "Handles simple greetings like 'hello'"
   PLUGIN_AUTHOR = "Electra Plugin Forge"
   PLUGIN_ENABLED = True
   PLUGIN_TYPE = "ROUTER"
   PLUGIN_TRIGGERS = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
   PLUGIN_ROUTE_TOKEN = "SIMPLE_GREETING"
   PLUGIN_COMMANDS = ["/greet"]

   Then in run(prompt, context):
        return a friendly greeting.

 But note: the user might say "hello" in any context. We don't want to interfere with other plugins that might handle "hello" in a specific context? However, the error says the Proactive Scanner is being used and failing, so we want to catch it early.

 However, the router will try to match the triggers in the order of plugin loading? We don't know. But we can make our trigger very specific to just greetings.

 But wait: the existing plugins might have triggers that also match "hello". We don't know. We are just told to handle this type of request.

 Since the error says the user repeatedly requested this type of task (3 times) and it failed, we assume that the current routing does not have a plugin that matches "hello" and then it goes to the Proactive Scanner which doesn't handle it.

 So we write a plugin that matches "hello" and returns a greeting.

 However, note that the user might say "hello" as part of a longer prompt? The trigger matching might be exact or substring? The specification doesn't say. But typically, the router might do a substring match? We don't know.

 Let's assume the router does a case-insensitive substring match? We can make our triggers list include common greetings.

 But to be safe, we can also check the prompt in our run function and only respond if the prompt is exactly one of the greetings? Or we can let the router do the matching and then we just respond.

 Since we are a ROUTER plugin, the router will call our run function only if the prompt matches one of our triggers (in any position?).

 We don't know the exact matching algorithm. But we can write:

   def run(prompt, context):
        # We can also check if the prompt is exactly a greeting? But the trigger already matched.
        # So we just return a greeting.

        greetings = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
        # But note: the prompt might be "hello, how are you?" and our trigger "hello" would match.

        # We can respond with a generic greeting and then ask how we can help.

        return "Hello! How can I assist you today?"

 But wait, the error says the user repeatedly requested this type of task. Maybe the user is just saying "hello" and expecting a response? So we can just say hello back.

 However, note that the Proactive Scanner agent might be an agent that does something else. We don't want to interfere with other uses of "hello" if they are intended for other agents? But the error says the Proactive Scanner is being used and failing, so we want to prevent that.

 Since we are a ROUTER plugin, we are intercepting the routing. We are going to handle the request and return a string, so the router will not send it to the Proactive Scanner.

 But what if the user says "hello" and then something else? Our trigger will match and we will respond with a greeting, but the user might have intended to ask the Proactive Scanner something? We don't know.

 However, the error says the user repeatedly requested this type of task (3 times) and it failed. So maybe the user is just saying "hello" and nothing else? We can assume that if the prompt is just a greeting, we respond. But if it's a greeting plus more, maybe we should let it go to the Proactive Scanner? But then the Proactive Scanner might fail again.

 Since we don't have more context, we'll handle any prompt that contains a greeting word? That might be too broad.

 Alternatively, we can make our triggers only match if the prompt is exactly one of the greetings? But the specification doesn't say if the router does exact or substring.

 Let's look at the existing plugins? We don't have their code.

 Since we are writing a plugin to fill a gap, and the gap is that the Proactive Scanner is being called for "hello", we want to catch the "hello" requests and handle them.

 We'll do:

   PLUGIN_TRIGGERS = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]

   And in run, we return a greeting.

 But note: the user might say "hello" in a different language? We are on MakuluLinux, but the user might be using English? We don't know.

 We'll stick to English for now.

 However, the error says the user repeatedly requested this type of task. It might be that the user is testing the system by saying "hello" multiple times? We don't know.

 Let's write the plugin accordingly.

 But wait: the specification says we must use context["print_fn"] for progressive output. We are just returning a string, so we don't need to use print_fn? We can if we want to stream.

 Since the greeting is short, we can just return.

 However, to be consistent with the specification, we can use print_fn to print the greeting and then return it? But the run function must return a string.

 We can do:

   context["print_fn"]("Hello! How can I assist you today?")
   return "Hello! How can I assist you today?"

 But that would print twice? Actually, the app might capture the return value and print it, and also we print it. So we might get duplicate.

 Alternatively, we can just return and let the app print the return value.

 Since the specification says we can use print_fn for streaming, but we don't need to stream a short greeting, we can just return.

 Let's just return.

 But note: the context has a notify_panel? We don't know what that is. We are not using it.

 We are also given a list of context keys. We don't need most of them for this.

 We must also handle exceptions. We'll wrap the run function in a try/except? Actually, the specification says to wrap ALL external calls. We don't have external calls, but we can still wrap the entire run function to be safe.

 However, the specification says: "Wrap ALL external calls in try/except". We don't have external calls, so we don't need to? But to be safe, we can.

 But note: the run function might be called in a context where an exception would crash the host? We don't want that.

 Let's do:

   def run(prompt, context):
        try:
            # ... our code
        except Exception as e:
            return f"Error in Simple Greeting Handler: {str(e)}"

 But the specification says the plugin must never crash the host. So we catch all.

 However, we are not doing anything that can fail. But still.

 Let's write the plugin accordingly.

 Also, we must declare any dependencies? We don't have any.

 So:

   PLUGIN_REQUIRES = []

 Now, the file name: we set PLUGIN_ROUTE_TOKEN = "SIMPLE_GREETING", so the file will be named autorepair_simple_greeting.py.

 But wait: the existing plugins are named autorepair_*.py. We are following that pattern.

 However, note that the existing plugins have names like autorepair_hello_handler.py. We are choosing a different token to avoid clash.

 Let's code accordingly.

 But note: the error says the agent 'Proactive Scanner' failed. We don't know what that agent is. It might be an AGENT plugin? We are writing a ROUTER plugin to intercept before it gets to that agent.

 We are done.

 However, let's think: what if the user says "hello" and then something else? Our trigger will match and we will respond with a greeting, but the user might have intended to ask the Proactive Scanner to do something? But the Proactive Scanner doesn't handle "hello", so it would fail anyway.

 We are improving the situation by at least responding to "hello".

 But what if the user says "hello, can you scan my system?"? Our trigger will match on "hello" and we will respond with a greeting, and then the rest of the prompt is ignored? That might not be what the user wants.

 However, the router might be matching the entire prompt? We don't know. The specification doesn't say.

 Since we are a ROUTER plugin, the router will call our run function with the entire prompt. We are not parsing the prompt. We are just returning a greeting.

 So if the user says "hello, scan my system", we will respond with "Hello! How can I assist you today?" and then the user will have to say again "scan my system". That might be acceptable.

 Alternatively, we could check if the prompt is exactly a greeting? But the trigger matching might have already done that? We don't know.

 Given the ambiguity, we'll stick to the simple approach.

 Let's write the plugin.

 Important: We must not import from ai_terminal. We are standalone.

 We'll use only standard library.

 Code:</think>
"""
Simple Greeting Handler - Handles basic greetings like 'hello' to prevent
capability gap errors when users simply say hello.
"""

PLUGIN_NAME = "Simple Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles basic greetings (hello, hi, hey) with friendly responses"
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
PLUGIN_ROUTE_TOKEN = "SIMPLE_GREETING"
PLUGIN_COMMANDS = ["/greet"]
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    """
    Handles simple greeting requests with appropriate responses.
    Uses context for logging if needed, but no external dependencies.
    """
    try:
        prompt_lower = prompt.lower().strip()
        
        # Time-based greetings
        if "good morning" in prompt_lower:
            return "Good morning! How can I help you today?"
        elif "good afternoon" in prompt_lower:
            return "Good afternoon! What can I do for you?"
        elif "good evening" in prompt_lower:
            return "Good evening! How may I assist you?"
        
        # Standard greetings
        greetings = {
            "hello": "Hello! How can I assist you today?",
            "hi": "Hi there! What can I help you with?",
            "hey": "Hey! How can I help?",
            "greetings": "Greetings! How may I be of service?"
        }
        
        # Check for exact or partial matches
        for key, response in greetings.items():
            if key in prompt_lower:
                return response
        
        # Fallback for any greeting-like input
        return "Hello! I'm here to help. What would you like to do?"
        
    except Exception as e:
        return f"Greeting error: {str(e)}"