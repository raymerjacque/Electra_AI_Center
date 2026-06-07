<think>We are given that the user requested "hello" and it failed in agent 'Proactive Scanner' with a CAPABILITY_GAP error.
 The error message says: "User repeatedly requested this type of task (4 times) with no dedicated handler."

 We are to write a plugin that handles this type of request successfully.

 Since the error is about a capability gap for the request "hello", we can assume that the user is expecting a simple greeting response.

 However, note that the error occurred in the 'Proactive Scanner' agent. This suggests that the request was being handled by that agent and it failed.

 But the specification says we are to write a plugin that handles this type of request. We have two options:

 Option 1: Write a ROUTER plugin that intercepts the trigger "hello" and returns a greeting.

 Option 2: Write an AGENT plugin that becomes a routing target for "hello".

 Since the error says "with no dedicated handler", it might be that the current routing does not have a handler for "hello".

 Let's look at the existing plugins: only one is installed: autorepair_content_summarizer.py

 We don't know what that does, but we are to write a new plugin.

 Considering the simplicity of the request, a ROUTER plugin that triggers on "hello" and returns a greeting would be sufficient.

 However, note that the error occurred in the 'Proactive Scanner' agent. It's possible that the request was being routed to that agent because of some trigger.

 But the user's request was just "hello". We don't know what triggers the Proactive Scanner agent.

 Since we are to fill the capability gap, we can create a plugin that handles the word "hello" in any context.

 But note: the plugin specification says for ROUTER:

   PLUGIN_TRIGGERS    = ["ask groq", "use groq", "groq:"]

 So we can set our triggers to include "hello".

 However, we must be cautious: if the user says "hello" in the middle of a conversation, we don't want to intercept every message.

 But the error says the user repeatedly requested this type of task (4 times). So it's likely that the user is trying to get a greeting.

 Let's design a ROUTER plugin that triggers on "hello" and returns a greeting.

 But note: the plugin must not break existing functionality. We are only to handle the case when the user says "hello".

 However, the error message says the request failed in the 'Proactive Scanner' agent. So maybe the request was being routed to that agent because of some trigger.

 We don't have the full context of the routing table. But we are told to write a plugin that handles this type of request.

 Since the user's request is "hello", we can create a plugin that triggers on "hello" and returns a simple greeting.

 Steps:

 1. Choose a PLUGIN_ROUTE_TOKEN that doesn't clash. Let's use "HELLO_HANDLER".

 2. Set PLUGIN_TRIGGERS to include "hello". But note: the user might say "hello" in different cases. We can make it case-insensitive by including multiple cases or by handling in the run function.

    However, the specification says the triggers are exact string matches? Actually, the example shows exact strings.

    But the router might do case-insensitive matching? We don't know. To be safe, we can include common variations.

    Alternatively, we can handle case insensitivity in the run function by checking the prompt.

    But note: the run function is only called when one of the triggers matches. So if we set the trigger to "hello", then only when the prompt exactly matches "hello" (or one of the triggers) will it be called.

    However, the user might say "Hello" or "HELLO". So we should include:

        PLUGIN_TRIGGERS = ["hello", "Hello", "HELLO"]

    But that's not exhaustive. Alternatively, we can set the trigger to a single string and then in the run function, we can check the prompt in a case-insensitive way.

    But the specification says: PLUGIN_TRIGGERS are the triggers that cause the router to route to this plugin.

    We don't know how the router matches. It might be exact or substring? The example shows exact phrases.

    Since we are not sure, let's assume the router does exact string matching (case-sensitive). Then we must list all case variations we want.

    Alternatively, we can set the trigger to a single string and then in the run function, we can check if the prompt (stripped and lowercased) is "hello". But then the router would only call us if the prompt exactly matches one of the triggers.

    So we have two options:

    Option A: Set PLUGIN_TRIGGERS to multiple case variations of "hello".

    Option B: Set PLUGIN_TRIGGERS to a single string, say "hello", and then in the run function, we check the prompt in a case-insensitive way and return the greeting only if it's a greeting.

    But note: the run function is only called when the trigger matches. So if we set the trigger to "hello", then only when the prompt is exactly "hello" (case-sensitive) will we be called.

    We want to handle "Hello", "HELLO", etc. So we must set the triggers to include these.

    Let's set:

        PLUGIN_TRIGGERS = ["hello", "Hello", "HELLO"]

    But what about "hello!" or "hello."? The user might have punctuation.

    The error message says the user repeatedly requested this type of task. It might be that the user is just saying "hello" without punctuation.

    However, to be safe, we can also include:

        PLUGIN_TRIGGERS = ["hello", "Hello", "HELLO", "hello!", "Hello!", "HELLO!", "hello.", "Hello.", "HELLO."]

    But that's getting messy.

    Alternatively, we can set the trigger to a single word and then in the run function, we can check if the prompt (stripped of punctuation and case) is "hello".

    But again, the router will only call us if the prompt exactly matches one of the triggers.

    So we must list all the variations we want to trigger on.

    Since we don't know the exact user input, let's assume the user is just saying "hello" in various cases and with common punctuation.

    We can do:

        PLUGIN_TRIGGERS = ["hello", "Hello", "HELLO", "hello!", "Hello!", "HELLO!", "hello.", "Hello.", "HELLO."]

    But what about "hello?" or "hello,"? We can't list every punctuation.

    Alternatively, we can set the trigger to a single string and then in the run function, we can check the prompt in a case-insensitive way and ignore punctuation.

    But then the router would only call us for the exact string we set in the trigger.

    So we must set the trigger to a string that matches the user's input exactly.

    Since we don't know the exact input, we have to make an educated guess.

    Given the error message, it's likely the user is just saying "hello" (without punctuation) in different cases.

    Let's stick to:

        PLUGIN_TRIGGERS = ["hello", "Hello", "HELLO"]

    And if the user says "hello!" then it won't trigger. But maybe the user is just saying "hello".

    Alternatively, we can set the trigger to a single string and then in the run function, we can check the prompt in a case-insensitive way and return the greeting for any prompt that starts with "hello" or is exactly "hello" (ignoring case and punctuation).

    But again, the router will only call us if the prompt exactly matches one of the triggers.

    So we must set the triggers to cover the user's input.

    Since we don't have the exact input, we can only guess.

    Let's assume the user is saying "hello" in a simple way.

    We'll set:

        PLUGIN_TRIGGERS = ["hello"]

    And then in the run function, we'll check:

        if prompt.strip().lower().rstrip('!.?,;:') == "hello":

    But wait, the run function is only called when the prompt exactly matches "hello" (case-sensitive). So if the user says "Hello", it won't be called.

    Therefore, we must set the triggers to include "Hello" and "HELLO".

    Let's set:

        PLUGIN_TRIGGERS = ["hello", "Hello", "HELLO"]

    And then in the run function, we don't need to check the prompt again because we know it's one of these.

    But what if the user says "hello world"? Then it won't trigger because the trigger is exact.

    The error says the user repeatedly requested this type of task. It might be that the user is just saying "hello" and nothing else.

    So we'll go with the three variations.

 3. We'll write a simple run function that returns a greeting.

 4. We must also consider that the plugin might be called in a context where the user is in the middle of a conversation. But the request is just "hello", so we assume it's a new conversation.

 5. We'll use context["print_fn"] to print a greeting and then return a string.

 6. We must not crash the host app, so we'll wrap any external calls in try/except. But we don't have external calls.

 7. We'll set PLUGIN_ENABLED = True.

 8. We'll set PLUGIN_TYPE = "ROUTER".

 9. We'll set PLUGIN_COMMANDS to an empty list because we don't need a slash command for this.

 10. We'll set PLUGIN_DESCRIPTION to something like "Handles simple greetings".

 11. We'll set PLUGIN_AUTHOR to "Electra Plugin Forge" or leave it out? The spec says optional.

 12. We'll set PLUGIN_REQUIRES to an empty list because we don't need any external packages.

 However, note: the error occurred in the 'Proactive Scanner' agent. We don't know what that agent does. But we are just providing a simple greeting.

 Let's write the plugin.

 But wait: the user might be in a different mode (CHAT, CODER, etc.). We don't care, we just return a greeting.

 However, note that the context has a current_mode. We can use that to customize the greeting? Not necessary.

 Let's write:

     PLUGIN_NAME = "Hello Handler"
     PLUGIN_VERSION = "1.0.0"
     PLUGIN_DESCRIPTION = "Handles simple greetings like 'hello'"
     PLUGIN_AUTHOR = "Electra Plugin Forge"
     PLUGIN_ENABLED = True
     PLUGIN_TYPE = "ROUTER"
     PLUGIN_TRIGGERS = ["hello", "Hello", "HELLO"]
     PLUGIN_ROUTE_TOKEN = "HELLO_HANDLER"
     PLUGIN_COMMANDS = []

     def run(prompt: str, context: dict) -> str:
         # We know the prompt is one of the triggers, so we can just return a greeting.
         # But let's be safe and check the prompt in a case-insensitive way and ignore punctuation?
         # Actually, we don't need to because the router only calls us when the prompt exactly matches one of the triggers.

         # However, what if the user says "hello" with extra spaces? The router might not match.

         # We don't know how the router trims. Let's assume the router does exact string matching.

         # So we can just return a greeting.

         greeting = "Hello! How can I assist you today?"

         # Use the print_fn to show the greeting in a streaming way? Not necessary, but we can.
         context["print_fn"](greeting)

         return greeting

 But wait, the run function must return a string. We are returning the same string we printed.

 However, note: the context["print_fn"] is for streaming output. We are printing the entire greeting at once.

 Alternatively, we can just return the string and let the app handle the printing? The specification says we can use print_fn to show progressive output.

 Since we are returning a string, the app will print it anyway. But using print_fn might be more consistent with the streaming feel.

 Let's use print_fn and then return the same string.

 But note: the app might print the return value again? We don't know. The specification doesn't say.

 To be safe, we can just return the string and not use print_fn. But the specification says we can use print_fn for progressive output.

 Since we are returning a simple string, we can just return it.

 However, the example in the specification for AGENT uses print_fn and then returns the result.

 Let's do:

     context["print_fn"](greeting)
     return greeting

 But then the greeting might be printed twice? We don't know.

 Since we are writing a ROUTER plugin, the app might print the return value. So we might get:

     Hello! How can I assist you today?
     Hello! How can I assist you today?

 To avoid that, we can just return the string and not use print_fn.

 But the specification says we can use print_fn to show progressive output. It doesn't say we must.

 Let's just return the string.

 However, the example in the specification for ROUTER does not use print_fn. It just returns a string.

 So we'll do:

     return "Hello! How can I assist you today?"

 But wait, the user might be in a different mode. We can customize:

     if context["current_mode"] == "CODER":
         return "Hello, coder! How can I help with your code?"
     else:
         return "Hello! How can I assist you today?"

 But the request is just "hello", so we don't know the mode. We can check the mode and adjust.

 However, the error says the request failed in the 'Proactive Scanner' agent. We don't know what mode that is.

 Let's keep it simple.

 We'll write:

     def run(prompt: str, context: dict) -> str:
         return "Hello! How can I assist you today?"

 But note: the user might be expecting a different response. Since we are filling a capability gap, we are just providing a basic response.

 However, the error says the user repeatedly requested this type of task. So maybe the user is expecting a specific response from the Proactive Scanner?

 We don't know what the Proactive Scanner does. But we are not the Proactive Scanner. We are a new plugin that handles "hello".

 So we are just providing a generic greeting.

 Let's write the plugin accordingly.

 But wait: the plugin must be named autorepair_<token_lowercase>.py. The token is "HELLO_HANDLER", so the file should be named autorepair_hello_handler.py.

 However, the user is asking us to write the plugin code. We are to output the raw Python source.

 We are not creating the file, just the content.

 So we output:

     # autorepair_hello_handler.py

 But the specification says: "File will be auto-named: autorepair_<token_lowercase>.py"

 So we don't need to worry about the filename, just the content.

 Let's write the code.

 However, note: the plugin must be placed in ~/.config/ai_plugins. We are just writing the code.

 We'll write:

     PLUGIN_NAME = "Hello Handler"
     PLUGIN_VERSION = "1.0.0"
     PLUGIN_DESCRIPTION = "Handles simple greetings like 'hello'"
     PLUGIN_AUTHOR = "Electra Plugin Forge"
     PLUGIN_ENABLED = True
     PLUGIN_TYPE = "ROUTER"
     PLUGIN_TRIGGERS = ["hello", "Hello", "HELLO"]
     PLUGIN_ROUTE_TOKEN = "HELLO_HANDLER"
     PLUGIN_COMMANDS = []

     def run(prompt: str, context: dict) -> str:
         return "Hello! How can I assist you today?"

 But wait, what if the user says "hello" in a different language? We are only handling English.

 The error message is in English, so we assume the user is speaking English.

 However, the user might be on a MakuluLinux system which is Ubuntu-based and might have multiple languages.

 But the request was in English.

 We'll stick to English.

 Let's write the code accordingly.

 However, note: the plugin must not crash. We are not doing any external calls, so it's safe.

 But what if the context doesn't have the keys we expect? The specification says the context dict has certain keys.

 We are only using the prompt and returning a string. We don't use any context keys.

 So it's safe.

 Let's output the code.

 But wait: the specification says we must wrap external calls in try/except. We don't have any.

 We are good.

 However, note: the plugin might be loaded in an environment where the context is missing some keys? The specification says the context dict has the listed keys.

 We are not using any of them, so it's safe.

 Let's write the code.

 But note: the plugin must be a complete Python file. We don't need any imports because we are not using any external modules.

 However, we are using type hints (str, dict). That's okay because the host app is using Python 3.6+? We don't know.

 But the specification shows type hints in the example.

 We'll keep the type hints.

 Final code:</think>
"""
Hello Handler Plugin
Fills capability gap for simple greeting requests that previously failed in Proactive Scanner.
"""

PLUGIN_NAME = "Hello Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles simple greeting requests like 'hello'"
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["hello", "Hello", "HELLO", "hi", "Hi", "HI", "hey", "Hey", "HEY"]
PLUGIN_ROUTE_TOKEN = "HELLO_HANDLER"
PLUGIN_COMMANDS = []
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    """
    Handles simple greeting requests with a friendly response.
    """
    try:
        # Get user's name from context if available (from previous interactions)
        user_name = ""
        chat_history = context.get("chat_history", [])
        if chat_history:
            # Look for user's name in recent history (simple heuristic)
            for msg in reversed(chat_history[-5:]):  # Check last 5 messages
                if "my name is" in msg.get("content", "").lower():
                    parts = msg["content"].lower().split("my name is")
                    if len(parts) > 1:
                        user_name = parts[1].strip().title()
                        break
        
        # Generate appropriate greeting
        if user_name:
            greeting = f"Hello, {user_name}! How can I assist you today?"
        else:
            greeting = "Hello! How can I assist you today?"
        
        # Use print_fn for immediate feedback
        context["print_fn"](greeting)
        return greeting
        
    except Exception as e:
        error_msg = f"Hello handler encountered an error: {str(e)}"
        context["print_fn"](error_msg)
        return "Hello! (There was a minor issue, but I'm here to help.)"