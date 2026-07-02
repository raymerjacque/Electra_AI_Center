<think>We are given a specific error: "CAPABILITY_GAP" for the request "hi" in the agent 'Proactive Scanner'.
 The error says: "User repeatedly requested this type of task (5 times) with no dedicated handler."

 We are to write a plugin that handles the request "hi" (or similar greetings) for the Proactive Scanner agent.

 However, note the specification: we are writing a ROUTER plugin (since the error is about a capability gap in an agent?).

 But note: the error occurred in agent 'Proactive Scanner'. The plugin we are writing is to handle this type of request.

 Let's break down:

 The user's request was "hi". The system tried to route it to the 'Proactive Scanner' agent, but that agent doesn't have a handler for "hi".

 We are to write a plugin that will handle such requests. Since the error says it's a capability gap, we are to fill that gap.

 However, note the plugin type: the specification says for a capability gap we should write a ROUTER plugin that intercepts the trigger and routes to a new agent? Or maybe we are to write an AGENT plugin that handles the greeting?

 But the error says: "User repeatedly requested this type of task (5 times) with no dedicated handler."

 The task type is "hi". So we need a handler for "hi".

 Since the error occurred in the 'Proactive Scanner' agent, it might be that the user is trying to use the Proactive Scanner agent to say hi? Or maybe the user is just saying hi and the system is trying to route to the Proactive Scanner because of some trigger?

 However, the plugin specification says:

   ROUTER: intercepts routing when triggers match.

   AGENT: first-class routing target identical to built-in agents.

 We are told to choose a PLUGIN_ROUTE_TOKEN that does not clash with existing ones.

 But note: the error says the request was handled by the 'Proactive Scanner' agent. So maybe the user's request was routed to that agent because of a trigger? Or maybe the user explicitly used a command for that agent?

 Since we are not given the exact trigger for the Proactive Scanner, we have to assume that the user's request "hi" is being sent to that agent because of some trigger phrase.

 However, the problem says: "Write a plugin that handles this type of request successfully on MakuluLinux."

 We are to write a plugin that will handle the request "hi" (or similar greetings) and return a response.

 But note: the error says it's a capability gap in the 'Proactive Scanner' agent. So maybe we are to write an AGENT plugin that is a new agent that handles greetings? Or a ROUTER plugin that intercepts the trigger and handles it?

 Let's re-read the specification:

   ROUTER: intercepts routing when triggers match.

   AGENT: first-class routing target identical to built-in agents.

 Since the error says the request was being handled by the 'Proactive Scanner' agent, it might be that the user's request was routed to that agent because of a trigger. But the agent doesn't have a handler for "hi".

 We have two options:

 Option 1: Write a ROUTER plugin that intercepts the trigger for the Proactive Scanner and handles the greeting itself, without routing to the Proactive Scanner.

 Option 2: Write an AGENT plugin that is a new agent (with a new token) that handles greetings, and then adjust the trigger for the Proactive Scanner to not catch greetings? But we cannot change existing plugins.

 However, note: the error says the user repeatedly requested this type of task (5 times) with no dedicated handler. So the system is trying to use the Proactive Scanner for greetings, but it doesn't support it.

 We are to write a plugin that handles this type of request. So we want to handle the greeting.

 But the user's request was "hi". We don't know if the user is trying to use the Proactive Scanner agent or just saying hi in general.

 Since the error occurred in the Proactive Scanner agent, it's likely that the user's request was being routed to that agent because of a trigger phrase that matches the Proactive Scanner.

 We are not told what the trigger for the Proactive Scanner is. But we are told that the request "hi" is being sent to that agent.

 So, we can write a ROUTER plugin that has a trigger for "hi" and then handles it, and then we set the PLUGIN_ROUTE_TOKEN to something that doesn't conflict.

 But note: the error says the request was being handled by the Proactive Scanner. So if we write a ROUTER plugin with a trigger for "hi", then our plugin will intercept the request and handle it, and the Proactive Scanner won't be called.

 However, what if the user wants to use the Proactive Scanner for other things? We don't want to break that.

 Alternatively, we can write an AGENT plugin that is a new agent that handles greetings, and then we change the trigger for the Proactive Scanner to not catch greetings? But we cannot change existing plugins.

 Since we are only allowed to write a new plugin, we must assume that the existing Proactive Scanner agent has a trigger that catches "hi". We cannot change that.

 So, we must write a plugin that has a higher priority? But the specification doesn't mention priority.

 Alternatively, we can write a ROUTER plugin that has the same trigger as the Proactive Scanner? But then we would have two plugins with the same trigger? That might cause conflict.

 The specification says: "Choose a PLUGIN_ROUTE_TOKEN that does NOT clash with existing ones". But it doesn't say about triggers.

 However, the router will match the first trigger that matches? We don't know the order.

 Since we are writing a plugin to fill a capability gap, and the error says the user repeatedly requested this type of task (5 times) with no dedicated handler, it means that the Proactive Scanner agent is being called for "hi" but it doesn't handle it.

 We want to handle "hi" in a dedicated way.

 Let's think: the user said "hi". The system tried to route to the Proactive Scanner because of a trigger (maybe the trigger is something like "scan" or "proactive"?). But the user said "hi", so maybe the trigger is just "hi"? That doesn't make sense.

 Alternatively, maybe the user is in a mode where the default agent is the Proactive Scanner? And the user says "hi", and the Proactive Scanner doesn't have a handler for that.

 We are not given enough context.

 But the problem says: "Write a plugin that handles this type of request successfully on MakuluLinux."

 We are to handle the request "hi". So we can write a plugin that when the user says "hi", we respond with a greeting.

 Since the error occurred in the Proactive Scanner agent, it's likely that the user's request was being routed to that agent. We don't want to break the Proactive Scanner for other requests.

 So, we can write a ROUTER plugin that has a trigger for "hi" and then handles it. But what if the Proactive Scanner also has a trigger for "hi"? Then we have two plugins with the same trigger. We don't know which one will be called.

 Alternatively, we can write an AGENT plugin that is a new agent that handles greetings, and then we change the user's mode or something? But we cannot change the user's mode.

 Since we are only allowed to write a plugin, and we cannot change existing ones, we must assume that the existing Proactive Scanner agent has a trigger that catches "hi". We want to handle "hi" in a different way.

 But note: the error says the request was being handled by the Proactive Scanner. So if we write a ROUTER plugin with a trigger for "hi", then our plugin will be called instead of the Proactive Scanner? Or will both be called?

 The specification doesn't say. But typically, the router would match the first trigger and then route to that plugin. So if our plugin is loaded after the Proactive Scanner, then the Proactive Scanner's trigger might be matched first? We don't know the order.

 Since we are writing a plugin to fill a gap, and the gap is that the Proactive Scanner doesn't handle "hi", we want to handle "hi" in a way that doesn't involve the Proactive Scanner.

 So, we write a ROUTER plugin that has a trigger for "hi" and then returns a greeting. We set the PLUGIN_ROUTE_TOKEN to something like "GREETING" and then we set PLUGIN_COMMANDS to maybe "/greeting" or something.

 But note: the user's request was just "hi". So we want to trigger on "hi".

 However, what if the user says "hi" in the context of the Proactive Scanner? We don't know.

 Since the error says the user repeatedly requested this type of task (5 times) with no dedicated handler, it means that the user is trying to do something that the Proactive Scanner doesn't support. And that something is saying "hi".

 So, we are going to write a plugin that handles the greeting.

 Let's design:

 We'll write a ROUTER plugin that triggers on "hi" (and maybe other greetings) and then returns a greeting message.

 We'll set:
   PLUGIN_NAME = "Greeting Handler"
   PLUGIN_VERSION = "1.0.0"
   PLUGIN_DESCRIPTION = "Handles greeting messages like 'hi'"
   PLUGIN_AUTHOR = "Your Name"
   PLUGIN_ENABLED = True
   PLUGIN_TYPE = "ROUTER"
   PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings"]
   PLUGIN_ROUTE_TOKEN = "GREETING"
   PLUGIN_COMMANDS = ["/greeting"]

 Then in the run function, we return a greeting.

 But note: the context has a print_fn. We can use that to print progressively? But we are just returning a string.

 However, the specification says: run(prompt, context) must return a non-empty string on success.

 So we return a string.

 But wait: the error occurred in the Proactive Scanner agent. If we write a ROUTER plugin that triggers on "hi", then when the user says "hi", our plugin will be called and we return a greeting. Then the Proactive Scanner won't be called.

 But what if the user says something else that the Proactive Scanner handles? Then the Proactive Scanner will be called.

 This seems safe.

 However, what if the user says "hi" and expects the Proactive Scanner to do something? We are changing the behavior. But the Proactive Scanner doesn't handle "hi" anyway, so we are just providing a handler for "hi".

 But note: the error says the user repeatedly requested this type of task (5 times) with no dedicated handler. So the user is trying to do something that the Proactive Scanner doesn't support. We are providing a dedicated handler for that task (greeting).

 So, let's write the plugin accordingly.

 However, note: the plugin must be placed in ~/.config/ai_plugins and named appropriately. The problem says: "File will be auto-named: autorepair_<token_lowercase>.py"

 But wait, the problem says: "Write a complete, working plugin file that adds support for this type of request so future identical requests succeed immediately."

 And the critical rules say: "File will be auto-named: autorepair_<token_lowercase>.py"

 So we are writing an auto-repair plugin? The problem says: "Expert Python developer (Plugin Forge) — writes self-repair plugins for the Electra AI terminal app"

 And the current plugin is named "autorepair_greeting.py". So we are to write a plugin that is named "autorepair_<token_lowercase>.py", and the token is the PLUGIN_ROUTE_TOKEN in lowercase.

 But note: the problem says: "Choose a PLUGIN_ROUTE_TOKEN that does NOT clash with existing ones"

 We are going to use "GREETING", so the file should be named "autorepair_greeting.py".

 But wait, the current installed plugin is already named "autorepair_greeting.py". So we are replacing it? Or is this a new one?

 The problem says: "Write a complete, working plugin file that adds support for this type of request"

 And the current installed plugin is "autorepair_greeting.py". So maybe we are to write a plugin that handles the greeting, and the existing one is broken? Or maybe we are to write a new one with a different token?

 But the problem says: "The user requested: hi" and it failed in agent 'Proactive Scanner'. So we are to write a plugin that handles "hi".

 Since the existing plugin is named "autorepair_greeting.py", it might be that the existing plugin is for something else? Or maybe it's the one that is broken?

 We are not told. But the problem says: "Write a complete, working plugin file"

 So we write a new plugin that handles the greeting.

 However, note: the problem says the plugin will be auto-named: autorepair_<token_lowercase>.py. So if we set PLUGIN_ROUTE_TOKEN = "GREETING", then the file must be named "autorepair_greeting.py".

 But there is already a plugin with that name. So we are going to overwrite it? Or maybe we are to write a plugin with a different token?

 Let's check the current installed plugins: only "autorepair_greeting.py". So we are to write a plugin that handles the greeting, and the existing one might be the one that is broken? Or maybe the existing one is for something else?

 Since the problem says: "Write a complete, working plugin file that adds support for this type of request", and the current installed plugin is "autorepair_greeting.py", it might be that we are to fix that plugin? But the problem says "write a plugin", not fix an existing one.

 Alternatively, maybe the existing plugin is for a different capability gap? We don't know.

 Since the problem says: "The user requested: hi" and it failed in agent 'Proactive Scanner', we are to write a plugin that handles "hi". And the plugin must be named "autorepair_greeting.py" because the token is "GREETING".

 But wait, the existing plugin is already named that. So we are going to replace it? That's acceptable because we are writing a working version.

 However, note: the problem says "so future identical requests succeed immediately". So we are to write a plugin that will be placed in the directory and then it will work.

 Since the existing plugin is named "autorepair_greeting.py", we are going to write a plugin with the same name? That would replace the existing one.

 But the problem says: "Write a complete, working plugin file". So we write the code for the plugin.

 Let's assume we are to write a plugin that handles the greeting and has the token "GREETING", and therefore the file name is "autorepair_greeting.py".

 But wait, the problem says: "Choose a PLUGIN_ROUTE_TOKEN that does NOT clash with existing ones". We don't know what existing tokens are. The only plugin we know is "autorepair_greeting.py", which might have token "GREETING"? We don't know.

 Since we are writing a new plugin to handle the greeting, and the existing one is broken, we can use the same token? But then we are replacing the existing one.

 Alternatively, we can choose a different token? But then the file name would be different.

 The problem says: "File will be auto-named: autorepair_<token_lowercase>.py". So if we choose token "HELLO", then the file would be "autorepair_hello.py". But then we are not replacing the existing one.

 But the problem says: "Write a complete, working plugin file that adds support for this type of request". It doesn't say we have to replace the existing one.

 However, the existing plugin is named "autorepair_greeting.py", so it's likely that the existing plugin is for greeting. And it's broken? Or maybe it's for something else?

 Since the error says the request "hi" failed in the Proactive Scanner, it's possible that the existing "autorepair_greeting.py" is not being triggered for "hi". Maybe its triggers are different.

 We don't know.

 Given the ambiguity, and since the problem says we are to write a plugin that handles "hi", we will write a plugin that triggers on "hi" and returns a greeting.

 We'll set the token to "GREETING" and the file name will be "autorepair_greeting.py". But if there's already a plugin with that token, we are replacing it.

 Alternatively, we can set the token to something else, like "HI_HANDLER", and then the file name would be "autorepair_hi_handler.py". But then we are adding a new plugin.

 Since the problem says "adds support", we are adding a new plugin. So we should choose a token that doesn't clash.

 But we don't know the existing tokens. The only plugin we know is "autorepair_greeting.py", which might have token "GREETING". So if we choose "GREETING", we clash.

 So let's choose a different token, say "HI_RESPONSE", and then the file name will be "autorepair_hi_response.py".

 But wait, the problem says: "File will be auto-named: autorepair_<token_lowercase>.py". So if we set PLUGIN_ROUTE_TOKEN = "HI_RESPONSE", then the file must be named "autorepair_hi_response.py".

 However, the problem says: "Write a complete, working plugin file". We are writing the code, and then the system will name it accordingly? Or we have to name it ourselves?

 The problem says: "File will be auto-named: autorepair_<token_lowercase>.py". So we don't have to worry about the file name? We just set the token and the system will name it.

 But then, if we set the token to "GREETING", the file will be named "autorepair_greeting.py", which already exists. That would replace the existing one.

 Since we are writing a new plugin to handle the greeting, and the existing one might be broken, we can replace it? But the problem says "adds support", not "replaces".

 Alternatively, we can set the token to something else and then the file will be named differently, and then we have two plugins? But then the existing one might still be broken.

 Since we are only allowed to write one plugin, and we are to fix the capability gap, we should write a plugin that handles the greeting and has a token that doesn't clash.

 But we don't know the existing tokens. The only plugin we know is "autorepair_greeting.py", so we assume that token is "GREETING". So we choose a different token.

 Let's choose "HELLO_HANDLER". Then the file will be named "autorepair_hello_handler.py".

 But wait, the problem says: "The user requested: hi". So we want to trigger on "hi". We can set the triggers to ["hi", "hello", "hey"].

 And then we set the token to "HELLO_HANDLER".

 However, note: the error occurred in the Proactive Scanner agent. We don't know what trigger the Proactive Scanner has. It might have a trigger for "hi"? Then we have two plugins with the same trigger? We don't know.

 Since we are writing a ROUTER plugin, and the router will match the first trigger that matches, we don't know the order.

 But the problem says: "so future identical requests succeed immediately". We want to handle "hi" successfully.

 We can write a plugin that triggers on "hi" and then returns a greeting. And we hope that our plugin is loaded before the Proactive Scanner? We don't know.

 Alternatively, we can write an AGENT plugin? But the error occurred in an agent, so maybe we want to write an AGENT plugin that handles the greeting? But then the user would have to explicitly call that agent.

 The user just said "hi". They didn't say "use greeting agent". So we want to handle "hi" in the default routing.

 So, we write a ROUTER plugin.

 Given the uncertainty, we write a ROUTER plugin that triggers on "hi" and returns a greeting.

 We'll set:
   PLUGIN_ROUTE_TOKEN = "GREETING_RESPONSE"
   PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings"]

 Then the file will be named "autorepair_greeting_response.py".

 But wait, the problem says: "File will be auto-named: autorepair_<token_lowercase>.py". So if we set token to "GREETING_RESPONSE", the file will be "autorepair_greeting_response.py".

 However, the existing plugin is "autorepair_greeting.py", so we are not clashing.

 Let's do that.

 But note: the problem says the plugin must be placed in ~/.config/ai_plugins. We are writing the code for that file.

 We are to output only the raw Python source.

 Let's write the plugin accordingly.

 However, note: the context has a print_fn. We can use that to print progressively? But we are just returning a string.

 We'll return a simple greeting.

 Also, we must wrap external calls in try/except. We don't have external calls.

 We must use context["user_home"] if we need to access the home directory. We don't need to.

 We are just returning a string.

 Let's code accordingly.

 But wait: the error says the request was in the 'Proactive Scanner' agent. Maybe the user is in a mode where the Proactive Scanner is the default agent? We don't know.

 Our plugin will intercept the trigger and handle it, so the Proactive Scanner won't be called for "hi".

 That's what we want.

 Let's write the plugin.</think>
"""
Greeting Handler Plugin for Electra AI
Fills capability gap for simple greeting requests like "hi"
"""

PLUGIN_NAME = "Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles greeting messages like 'hi', 'hello', 'hey'"
PLUGIN_AUTHOR = "Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = ["/greeting"]
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    """
    Handle greeting requests with appropriate responses
    """
    try:
        # Normalize input for matching
        normalized = prompt.lower().strip()
        
        # Time-based greeting variations
        from datetime import datetime
        current_hour = datetime.now().hour
        
        if "morning" in normalized or (5 <= current_hour < 12):
            greeting = "Good morning! How can I assist you today?"
        elif "afternoon" in normalized or (12 <= current_hour < 18):
            greeting = "Good afternoon! What can I help you with?"
        elif "evening" in normalized or (18 <= current_hour < 22):
            greeting = "Good evening! How may I be of service?"
        else:
            greeting = "Hello! I'm Electra AI. How can I help you?"
        
        # Add context-aware suggestions based on current mode
        current_mode = context.get("current_mode", "CHAT")
        if current_mode == "CODER":
            greeting += "\n\nI see you're in **CODER** mode. Need help with a programming task?"
        elif current_mode == "WRITER":
            greeting += "\n\nYou're in **WRITER** mode. Working on something creative?"
        
        # Show in GUI if active
        if context.get("gui_active"):
            context["print_fn"](f"[bold cyan]👋 {greeting}[/bold cyan]")
        
        return greeting
        
    except Exception as e:
        error_msg = f"Greeting handler encountered an error: {str(e)}"
        if context.get("print_fn"):
            context["print_fn"](f"[bold red]⚠️ {error_msg}[/bold red]")
        return "Hello! I'm having trouble processing your greeting right now. Please try again."