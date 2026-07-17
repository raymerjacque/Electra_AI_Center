<think>We are given a specific error: "CAPABILITY_GAP" for the request "hello" in the agent 'Proactive Scanner'.
 The user has requested "hello" and the system has detected a capability gap because this type of task (a simple greeting) has been requested 3 times without a dedicated handler.

 We are to write a plugin that handles this type of request successfully.

 Since the error occurred in the agent 'Proactive Scanner', we note that the plugin we write should be of type ROUTER (as per the specification for auto-repair plugins that fill a capability gap) and should intercept the trigger for "hello".

 However, note that the error message says: "User repeatedly requested this type of task (3 times) with no dedicated handler."

 We are to write a plugin that will handle the request "hello". But note that the user might say "hello" in various ways (like "hi", "hey", etc.). But the error specifically says the request was "hello".

 Let's design a plugin that triggers on common greetings and responds appropriately.

 Steps:
 1. We'll create a ROUTER plugin that triggers on words like "hello", "hi", "hey", etc.
 2. We'll set PLUGIN_ROUTE_TOKEN to something that doesn't clash. Since the error was in 'Proactive Scanner', we can choose a token that is not used. Let's choose "GREETING".
 3. We'll write a run function that returns a friendly greeting.

 However, note the specification says: for auto-repair plugins that fill a capability gap, we set:
   PLUGIN_TYPE = "ROUTER"
   PLUGIN_ENABLED = True

 Also, we must avoid hardcoding paths and use the context.

 But note: the error occurred in the agent 'Proactive Scanner'. We are not replacing that agent, but providing a handler for the request "hello". The router will now route the request to our plugin when the trigger matches.

 Let's write the plugin accordingly.

 Important: The plugin must be placed in ~/.config/ai_plugins and named appropriately. The system will auto-name it as autorepair_<token_lowercase>.py. So if we set PLUGIN_ROUTE_TOKEN = "GREETING", the file should be named autorepair_greeting.py.

 However, note that the user's current plugin list shows only one plugin: autorepair_casual.py. We are adding a new one.

 Let's code accordingly.

 We are to output only the raw Python source.

 We'll write:

   PLUGIN_NAME = "Greeting Handler"
   PLUGIN_VERSION = "1.0.0"
   PLUGIN_DESCRIPTION = "Handles simple greetings like hello, hi, hey"
   PLUGIN_AUTHOR = "Electra AI Community"
   PLUGIN_ENABLED = True
   PLUGIN_TYPE = "ROUTER"
   PLUGIN_TRIGGERS = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
   PLUGIN_ROUTE_TOKEN = "GREETING"
   PLUGIN_COMMANDS = []   # We don't need slash commands for this, but we can leave empty or add if needed.

   Then define run(prompt, context) -> str.

   We'll return a simple greeting. We can also use the context to get the current time and adjust the greeting.

   However, note: the context has a key 'current_mode' and others, but we don't need them for a simple greeting.

   We'll do:

      import datetime
      now = datetime.datetime.now()
      hour = now.hour
      if 5 <= hour < 12:
          time_greeting = "Good morning"
      elif 12 <= hour < 18:
          time_greeting = "Good afternoon"
      else:
          time_greeting = "Good evening"

      return f"{time_greeting}! How can I assist you today?"

   But note: the user might have said "hello" at any time. We can also just say "Hello!" if we don't want to be time-specific.

   However, the error says the request was "hello", so we can just respond with "Hello!".

   But to be more engaging, let's use the time-based greeting.

   Also, note that the plugin must not crash. We'll wrap the datetime in a try-except, but it's unlikely to fail.

   Alternatively, we can avoid the time-based greeting and just say "Hello!".

   Let's keep it simple: "Hello! How can I help you?"

   However, the specification says we must return a non-empty string.

   We'll do:

      return "Hello! How can I assist you today?"

   But note: the user might be in a different timezone. We don't have the timezone in context. So maybe just a generic greeting.

   Alternatively, we can use the context to get the user's home directory and then maybe read a config? But that's overkill.

   Let's stick to a simple greeting.

   However, the error message says the user repeatedly requested "hello". So we are just providing a response for that.

   We'll write:

      def run(prompt: str, context: dict) -> str:
          return "Hello! How can I assist you today?"

   But note: the prompt might be "hello" or "hi", etc. We are triggering on multiple, so we can adjust the response accordingly?

   We can check the prompt and adjust:

      if prompt.lower() in ["good morning", "good afternoon", "good evening"]:
          return f"{prompt.capitalize()}! How can I assist you today?"
      else:
          return "Hello! How can I assist you today?"

   But note: the triggers include "good morning", etc. So if the user says "good morning", we want to respond with "Good morning! ...".

   Let's do:

      prompt_lower = prompt.lower()
      if prompt_lower in ["good morning", "good afternoon", "good evening"]:
          return f"{prompt.capitalize()}! How can I assist you today?"
      else:
          return "Hello! How can I assist you today?"

   However, note that the trigger list includes "good morning", etc. So we are safe.

   But what if the user says "Hello, how are you?"? Our trigger is just "hello", so it will match and we'll respond with "Hello! ...". That's acceptable.

   We are not doing NLP, just a simple trigger.

   Let's code accordingly.

   Also, note that the plugin must be self-contained. We don't need any external packages for this.

   We'll write the plugin as below.

   Important: The plugin must be named autorepair_greeting.py, but the system will auto-name it. We just set PLUGIN_ROUTE_TOKEN to "GREETING".

   Let's output the code.</think>
"""
Greeting Handler Plugin for Electra AI
Handles simple greetings (hello, hi, hey, etc.) that were previously unhandled.
"""

PLUGIN_NAME = "Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles simple greetings like hello, hi, hey"
PLUGIN_AUTHOR = "Electra AI Community"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["hello", "hi", "hey", "greetings", "good morning", "good afternoon", "good evening"]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = []

def run(prompt: str, context: dict) -> str:
    """
    Responds to greeting prompts with appropriate friendly responses.
    Uses time-aware greetings when possible.
    """
    try:
        import datetime
        now = datetime.datetime.now()
        hour = now.hour
        
        # Time-based greeting selection
        if 5 <= hour < 12:
            time_greeting = "Good morning"
        elif 12 <= hour < 18:
            time_greeting = "Good afternoon"
        else:
            time_greeting = "Good evening"
        
        prompt_lower = prompt.lower().strip()
        
        # Match specific greeting types
        if any(word in prompt_lower for word in ["good morning", "good afternoon", "good evening"]):
            # User specified time greeting, use theirs
            for time_word in ["good morning", "good afternoon", "good evening"]:
                if time_word in prompt_lower:
                    return f"{time_word.capitalize()}! How can I assist you today?"
        elif "hello" in prompt_lower or "hi" in prompt_lower or "hey" in prompt_lower:
            return f"Hello! How can I assist you today?"
        elif "greetings" in prompt_lower:
            return f"Greetings! How may I help you?"
        else:
            # Fallback to time-based greeting
            return f"{time_greeting}! How can I assist you today?"
            
    except Exception as e:
        # Fallback response if anything fails
        return "Hello! How can I assist you today?"