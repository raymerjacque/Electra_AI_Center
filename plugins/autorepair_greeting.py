<think>We are given a capability gap: the user repeatedly requested "hi" (or similar) and there's no dedicated handler.
 The error says: "User repeatedly requested this type of task (3 times) with no dedicated handler."

 We are to write a plugin that handles this type of request. Since the user is saying "hi", it's a simple greeting.

 However, note that the error says "Proactive Scanner" agent failed. But we are writing a plugin to handle the request.

 Since the user is just saying "hi", we can create a ROUTER plugin that triggers on common greetings.

 But note: the error says the user repeatedly requested this type of task. So we want to handle any greeting.

 Let's design:

 PLUGIN_TYPE = "ROUTER"
 PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"]
 PLUGIN_ROUTE_TOKEN = "GREETING"
 PLUGIN_COMMANDS = ["/greet"]

 We'll write a run function that returns a friendly greeting.

 However, note that the error says the agent 'Proactive Scanner' failed. But we are not writing an agent for that.
 We are writing a plugin to handle the user's greeting. The router will intercept when the user says a greeting.

 But wait: the error says the user repeatedly requested this type of task. So maybe the user is saying "hi" and expecting a response.

 We are to write a plugin that handles this request. Since the user is just greeting, we can respond with a greeting.

 However, note that the plugin must be placed in ~/.config/ai_plugins and named appropriately.

 The specification says: "File will be auto-named: autorepair_<token_lowercase>.py"

 So our token is "GREETING", so the file should be named: autorepair_greeting.py

 But note: the user's request was just "hi". We are to handle that.

 Let's write the plugin accordingly.

 Important: We must use the context to print if needed, but we can just return a string.

 However, note that the run function must return a non-empty string.

 Let's write:

   return "Hello! How can I assist you today?"

 But we can make it more dynamic: maybe use the time of day.

 However, note: we are on MakuluLinux (Ubuntu/Cinnamon). We can use the system time.

 But we must be cautious: the app is a compiled Nuitka binary and we are in a plugin. We can use standard Python.

 Let's get the current hour and adjust greeting.

 However, note: the context has a `print_fn` but we are returning a string. We can also use `print_fn` to show progressive output, but for a simple greeting we can just return.

 But the specification says: "Use context["print_fn"](text) to show progressive output instead of print()"

 We are not doing progressive output, so we can just return.

 However, let's use the time to make it better.

 Steps:

  1. Import datetime (or time) to get current hour.
  2. Determine part of day.
  3. Return appropriate greeting.

 But note: the user might be in a different timezone. We don't have timezone in context. We can use local time.

 Alternatively, we can just return a generic greeting.

 Since the error says the user repeatedly requested, maybe they want a more engaging response.

 Let's do:

   import datetime
   now = datetime.datetime.now()
   hour = now.hour
   if 5 <= hour < 12:
        greeting = "Good morning"
   elif 12 <= hour < 18:
        greeting = "Good afternoon"
   else:
        greeting = "Good evening"

   return f"{greeting}! How can I help you?"

 But note: the user might not be in the same timezone as the system. However, we don't have user's timezone.

 Alternatively, we can just say "Hello" without time.

 Since the error is about a capability gap for "hi", we can just respond with a simple greeting.

 However, let's make it a bit more friendly and include the user's name? We don't have the user's name in context.

 We have: user_home, but not username. We can get the username from os.getlogin() but that might not be safe in all environments.

 Alternatively, we can just say "Hello there!" or "Hi!".

 Let's stick to a simple, safe greeting.

 But note: the plugin must be robust and not crash. So we'll wrap the time part in try/except.

 However, the specification says: "Wrap ALL external calls in try/except"

 But getting the current time is not an external call? It's using the system clock, which is safe.

 But to be safe, we can do:

   try:
        ... time based greeting ...
   except:
        greeting = "Hello"

 Alternatively, we can avoid the time and just use a fixed greeting.

 Since the user said "hi", we can respond with "Hi! How can I assist you today?"

 But the error says the user repeatedly requested. Maybe they want a more proactive response?

 Let's read the error again: "User repeatedly requested this type of task (3 times) with no dedicated handler."

 So the user has said "hi" three times and there was no handler. Now we are providing one.

 We can also log that we are handling it? But we don't have a logger. We can use print_fn to print to the terminal?

 But the run function returns a string that will be shown to the user. So we can just return.

 However, the context has a `print_fn` that we can use to print to the terminal (like streaming). But for a simple response, returning is enough.

 Let's write the plugin accordingly.

 But note: the plugin must be named autorepair_greeting.py and the token is GREETING.

 We are going to write:

   PLUGIN_NAME = "Greeting Handler"
   PLUGIN_VERSION = "1.0.0"
   PLUGIN_DESCRIPTION = "Handles common greetings like hi, hello, etc."
   PLUGIN_AUTHOR = "Plugin Forge"
   PLUGIN_ENABLED = True
   PLUGIN_TYPE = "ROUTER"
   PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"]
   PLUGIN_ROUTE_TOKEN = "GREETING"
   PLUGIN_COMMANDS = ["/greet"]

   Then the run function.

 However, note: the triggers are case-insensitive? The router might do case-insensitive matching? We don't know.

 We can make our triggers lower case and then in run, we can convert the prompt to lower for matching? But the router does the matching.

 Actually, the router will match the triggers against the prompt. We don't know if it's case-sensitive.

 To be safe, we can include both upper and lower? But the specification doesn't say.

 Alternatively, we can assume the router does case-insensitive matching? We don't know.

 Since we are writing a plugin for the Electra app, and the router is part of the app, we have to rely on the app's behavior.

 But note: the error says the user said "hi". So we can assume the router is case-insensitive? Or maybe the user said exactly "hi".

 We'll put the triggers in lower case and hope the router is case-insensitive. If not, we can add more variations.

 Let's keep it simple and use lower case.

 Now, the run function:

   We are going to return a greeting.

   We can also use the context to get the current mode? Maybe we can adjust based on mode? Not necessary.

   We'll just return a string.

   But note: the run function must return a non-empty string.

   We'll do:

        return "Hello! How can I assist you today?"

   But we can make it more dynamic with time.

   Let's do:

        import datetime
        now = datetime.datetime.now()
        hour = now.hour
        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"

        return f"{greeting}! How can I help you?"

   But if there's an exception (unlikely), we fall back to "Hello".

   We'll wrap the time part in try/except.

   However, note: the specification says to wrap ALL external calls. Is getting the current time an external call? It's a system call, but it's built-in and safe.

   But to be safe, we'll do:

        try:
            ... time based ...
        except:
            greeting = "Hello"

   Alternatively, we can avoid the time and just use a fixed greeting to keep it simple.

   Since the user said "hi", we can just say "Hi!".

   But the error says the user repeatedly requested. Maybe they want a more engaging response.

   Let's do:

        try:
            import datetime
            now = datetime.datetime.now()
            hour = now.hour
            if 5 <= hour < 12:
                greeting = "Good morning"
            elif 12 <= hour < 18:
                greeting = "Good afternoon"
            else:
                greeting = "Good evening"
        except:
            greeting = "Hello"

        return f"{greeting}! How can I assist you today?"

   But note: the user might be in a different timezone. We don't have timezone info.

   Alternatively, we can use the context's `cwd`? No.

   We can also use the `user_home` to guess? No.

   So we'll stick to system time.

   However, note: the app might be running in a container or something? But it's the user's system.

   We'll go with that.

   But wait: the plugin must be self-contained and not crash. So we'll catch any exception in the time part.

   Alternatively, we can avoid the time and just use a fixed greeting to be safe.

   Since the user said "hi", we can just say "Hi! How can I help?".

   Let's do:

        return "Hi! How can I help you today?"

   But then we don't need the try/except.

   However, the specification says to wrap external calls. We are not making any external call if we don't use time.

   So let's keep it simple.

   But the error says the user repeatedly requested. Maybe they want a more personalized response?

   We don't have the user's name. So we can't.

   We'll just return a simple greeting.

   However, note: the plugin is for a capability gap. The gap is that there's no handler for "hi". So we are providing one.

   We can also log that we handled it? But we don't have a logger. We can use print_fn to print to the terminal?

   But the run function returns the response that will be shown to the user. So we don't need to print.

   However, if we want to log for debugging, we can use print_fn. But note: the print_fn is for streaming output to the terminal.

   We can do:

        context["print_fn"]("Greeting plugin activated.")

   But that would be printed to the terminal and then the return string would also be printed? We don't want two messages.

   Actually, the return string is the response to the user. The print_fn is for intermediate output.

   So we don't need to use print_fn for this simple response.

   Let's just return.

   But note: the specification says: "Use context["print_fn"](text) to show progressive output instead of print()"

   We are not doing progressive output, so we don't need it.

   So the plugin:

   We'll write:

        PLUGIN_NAME = "Greeting Handler"
        ... etc ...

        def run(prompt: str, context: dict) -> str:
            # We don't use the prompt because the router already matched.
            # But we can use it to customize? For example, if the user said "good morning", we can say "Good morning to you too!"

            # However, the router matched one of the triggers. We don't know which one.

            # We can check the prompt and adjust? But the prompt might be "hi" or "hello".

            # Let's just return a generic greeting.

            return "Hello! How can I assist you today?"

   But wait: the user might have said "good morning". Then we should say "Good morning!"?

   We can do:

        prompt_lower = prompt.lower()
        if "good morning" in prompt_lower:
            return "Good morning! How can I help you today?"
        elif "good afternoon" in prompt_lower:
            return "Good afternoon! How can I help you today?"
        elif "good evening" in prompt_lower:
            return "Good evening! How can I help you today?"
        else:
            return "Hello! How can I assist you today?"

   But note: the triggers are exact? The router might match the entire prompt? We don't know.

   The router might match if the prompt contains the trigger? Or exactly equals?

   We don't know. But the error says the user said "hi". So we can assume the prompt is exactly "hi" or one of the triggers.

   But the user might say "hi there". Then our trigger "hi" would match? We don't know.

   Since we are writing the plugin, we can adjust the triggers to be more flexible? But the router does the matching.

   We are only responsible for the run function when the router matches.

   So in the run function, we can look at the prompt and adjust.

   However, the router might have matched on "hi" but the prompt is "hi there". Then we can still say "Hello".

   Let's do:

        prompt_lower = prompt.lower()
        if "good morning" in prompt_lower:
            return "Good morning! How can I help you today?"
        elif "good afternoon" in prompt_lower:
            return "Good afternoon! How can I help you today?"
        elif "good evening" in prompt_lower:
            return "Good evening! How can I help you today?"
        else:
            return "Hello! How can I assist you today?"

   But note: the user might say "hey" or "greetings". We don't have specific responses for those.

   We can also check for "hey" and "greetings" and respond accordingly? But we don't have to.

   We'll just use the above.

   However, note: the user might say "hi" and we respond with "Hello". That's okay.

   Let's code accordingly.

   But wait: the plugin must be named autorepair_greeting.py and the token is GREETING.

   We are going to write the entire plugin.

   Also, note: the plugin must not require any external packages? We are only using datetime, which is standard.

   So PLUGIN_REQUIRES = [] (or we can omit, default is [])

   Let's write the plugin.

   However, note: the specification says the plugin must be placed in ~/.config/ai_plugins and named autorepair_<token_lowercase>.py

   So we are writing the code for that file.

   We are to output only the raw Python source.

   Let's write:

   """
   Greeting Handler Plugin for Electra AI
   Handles common greetings and responds appropriately.
   """

   Then the metadata and run function.

   But note: the specification says the plugin must have a module docstring? It doesn't require, but we can have one.

   We'll start with the imports and then the metadata.

   However, note: the plugin is loaded by the app, and the app expects the metadata variables at the top.

   We'll put the metadata at the top, then the run function.

   But note: the specification says the run function must be defined.

   Let's code accordingly.

   Also, note: the plugin type is ROUTER, so we have PLUGIN_TRIGGERS and PLUGIN_ROUTE_TOKEN.

   We are done.

   However, note: the error says the agent 'Proactive Scanner' failed. But we are not writing an agent for that.

   We are writing a router plugin that will intercept when the user says a greeting.

   This should solve the capability gap for greetings.

   Let's write the code.</think>
"""
Greeting Handler Plugin for Electra AI
Handles common greetings (hi, hello, hey, etc.) with contextual responses.
Fills capability gap for simple conversational acknowledgments.
"""

import datetime
import os

PLUGIN_NAME = "Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Responds to greetings like hi, hello, hey with contextual replies"
PLUGIN_AUTHOR = "Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening", "howdy", "hola"]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = ["/greet"]
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    """
    Responds to greetings with time-appropriate, friendly acknowledgments.
    Uses context to avoid being repetitive and adds slight personality.
    """
    try:
        prompt_lower = prompt.lower().strip()
        current_hour = datetime.datetime.now().hour
        
        # Determine time of day for appropriate greeting
        if 5 <= current_hour < 12:
            time_greeting = "Good morning"
        elif 12 <= current_hour < 17:
            time_greeting = "Good afternoon"
        elif 17 <= current_hour < 22:
            time_greeting = "Good evening"
        else:
            time_greeting = "Hello"
        
        # Check for specific greeting types
        if any(word in prompt_lower for word in ["good morning", "morning"]):
            response = f"{time_greeting}! Ready to help with your tasks today."
        elif any(word in prompt_lower for word in ["good afternoon", "afternoon"]):
            response = f"{time_greeting}! How can I assist you this afternoon?"
        elif any(word in prompt_lower for word in ["good evening", "evening"]):
            response = f"{time_greeting}! Still working late or just checking in?"
        elif "hey" in prompt_lower or "howdy" in prompt_lower:
            response = f"Hey there! What's on your mind?"
        elif "hola" in prompt_lower:
            response = "¡Hola! How can I help you today?"
        else:
            # Default greeting response
            response = f"{time_greeting}! I'm here and ready to help. What would you like to do?"
        
        # Add slight variation based on conversation history length
        history = context.get("chat_history", [])
        if len(history) > 5:
            response += " (I see we've been chatting a bit today!)"
        
        return response
        
    except Exception as e:
        # Fallback response if anything fails
        return "Hello! How can I assist you today?"