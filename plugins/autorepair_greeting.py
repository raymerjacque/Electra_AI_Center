<think>We are given a request: "Boa noite!" which is Portuguese for "Good evening!"
 The error indicates that the user has repeatedly requested this type of task (4 times) and there's no dedicated handler.
 We are to write a plugin that handles this type of request.

 Since the request is a greeting, we can create a simple ROUTER plugin that triggers on common greetings in Portuguese (and maybe other languages?).
 However, note that the error says "this type of task", and the example is a greeting. We are to handle the specific request "Boa noite!".

 But note: the user might also say "Boa tarde" (good afternoon) or "Bom dia" (good morning). We can make a plugin that handles all these.

 However, the error says the user repeatedly requested "this type of task", meaning the same type of request (greeting) but maybe with variations.

 Let's design a plugin that:
   - Triggers on common greetings in Portuguese (and maybe English too, to be safe) and responds appropriately.

 But note: the plugin must be specific to the request type. Since the error says the user requested "Boa noite!" 4 times, we can assume that the user wants a response to that.

 However, the plugin should be general enough to handle similar greetings.

 Steps:
 1. We'll create a ROUTER plugin with triggers for:
      "Boa noite", "Boa tarde", "Bom dia", "Olá", "Oi", "Hello", "Hi", etc.

 2. We'll check the prompt (case-insensitive) and respond with an appropriate greeting.

 3. We must follow the plugin specification.

 4. We are to write the plugin in the format that will be saved as: autorepair_<token_lowercase>.py

 5. We must choose a PLUGIN_ROUTE_TOKEN that doesn't clash. Since this is for greetings, let's use "GREETING".

 6. We'll set PLUGIN_TYPE = "ROUTER"

 7. We'll set PLUGIN_TRIGGERS to a list of trigger phrases.

 8. We'll set PLUGIN_COMMANDS to an empty list or maybe a command like "/greeting" but note: the specification says for ROUTER, PLUGIN_COMMANDS is optional and is a list of slash commands that can be used to invoke the plugin. Since we are using triggers, we might not need a command. But let's include one for completeness: "/greeting"

 9. The run function will:
      - Check the prompt (lowercase) against our triggers (also in lowercase) and respond accordingly.

 10. We must use the context to print if needed, but since we are just returning a string, we can return the greeting.

 11. We must handle the case when the prompt is exactly one of our triggers, but also allow for some variation (like with exclamation mark).

 12. We'll write the plugin to be robust and not crash.

 Let's code accordingly.

 However, note: the error says the user requested "Boa noite!" (with exclamation). We should handle that.

 We'll create a mapping of trigger patterns (without exclamation, case-insensitive) to responses.

 But note: the triggers in PLUGIN_TRIGGERS are exact strings? The specification says "trigger phrases". We can use a list of strings and then check if the prompt (stripped of punctuation and lowercased) starts with any of them? Or we can do a simple substring match? 

 Since the user might say "Boa noite!" or "Boa noite", we can remove non-alphanumeric characters and then compare.

 Alternatively, we can use a simple approach: convert both to lowercase and remove non-alphanumeric (except spaces) and then check if the prompt starts with the trigger (also processed similarly).

 However, note that the triggers are provided as a list of strings. We can do:

   prompt_clean = re.sub(r'[^a-z0-9\s]', '', prompt.lower()).strip()
   for trigger in PLUGIN_TRIGGERS:
        trigger_clean = re.sub(r'[^a-z0-9\s]', '', trigger.lower()).strip()
        if prompt_clean.startswith(trigger_clean):
            return response

 But note: the trigger might be "Boa noite" and the prompt "Boa noite!" -> after cleaning: "boa noite" and "boa noite" -> match.

 However, what if the user says "Boa noite, como vai?" -> then it starts with "Boa noite", so we match.

 But what if the user says "Olá, boa noite!"? Then we might want to match on "Boa noite" but the prompt starts with "Olá". So we might need to check if the trigger is anywhere in the prompt? 

 The specification says "trigger phrases", so we are looking for the trigger to be present. But note: the original error was for "Boa noite!" so we want to catch that.

 Let's decide: we'll check if the cleaned prompt contains the cleaned trigger as a word? Or we can split the prompt into words and see if the trigger (as a sequence of words) is present.

 However, to keep it simple and because the triggers are short, we can do:

   if trigger_clean in prompt_clean.split():   # but note: "Boa noite" is two words.

 Alternatively, we can do:

   if prompt_clean.startswith(trigger_clean) or f" {trigger_clean}" in prompt_clean:

 But that might be overkill.

 Since the user's request is exactly "Boa noite!" (or with variation) and we are only asked to handle that type, let's assume the trigger is at the beginning.

 However, the user might say "Eu digo: Boa noite!" and we still want to catch it? Probably not, because then it's not a direct greeting.

 Given the context of the error (the user repeatedly requested this type of task) and the example is a direct greeting, we assume the user is directly greeting.

 So we'll check if the prompt starts with the trigger (after cleaning).

 But note: the trigger list might have multiple triggers. We'll loop and if any trigger matches at the beginning, we respond.

 However, what if the user says "Boa noite e boa tarde"? Then both triggers are present? We'll respond to the first one that matches.

 Let's code accordingly.

 But note: the plugin must be named: autorepair_greeting.py

 We'll set:
   PLUGIN_NAME = "Greeting Handler"
   PLUGIN_VERSION = "1.0.0"
   PLUGIN_DESCRIPTION = "Handles common greetings in multiple languages"
   PLUGIN_AUTHOR = "AutoRepair"
   PLUGIN_ENABLED = True
   PLUGIN_TYPE = "ROUTER"
   PLUGIN_TRIGGERS = ["Boa noite", "Boa tarde", "Bom dia", "Olá", "Oi", "Hello", "Hi", "Good morning", "Good afternoon", "Good evening"]
   PLUGIN_ROUTE_TOKEN = "GREETING"
   PLUGIN_COMMANDS = ["/greeting"]

 We'll map the trigger to a response. But note: the response should be in the same language? We can try to detect the language by the trigger.

 Alternatively, we can have a fixed response for each trigger.

 Let's create a dictionary:

   responses = {
        "Boa noite": "Boa noite! Como posso ajudar?",
        "Boa tarde": "Boa tarde! Como posso ajudar?",
        "Bom dia": "Bom dia! Como posso ajudar?",
        "Olá": "Olá! Como posso ajudar?",
        "Oi": "Oi! Como posso ajudar?",
        "Hello": "Hello! How can I help?",
        "Hi": "Hi! How can I help?",
        "Good morning": "Good morning! How can I help?",
        "Good afternoon": "Good afternoon! How can I help?",
        "Good evening": "Good evening! How can I help?"
   }

 But note: the trigger we match might be with or without exclamation, and we are cleaning the prompt. We are matching the trigger_clean (without punctuation) to the start of prompt_clean.

 However, the trigger in the list is without exclamation. So if the user says "Boa noite!" we clean to "boa noite" and the trigger "Boa noite" becomes "boa noite", so it matches.

 But what if the user says "Boa noite, tudo bem?" -> cleaned: "boa noite tudo bem" -> starts with "boa noite", so we match.

 We'll then return the response for that trigger.

 However, note: the trigger might be in the middle? We are only checking startswith. So if the user says "Eu quero dizer Boa noite", then it doesn't start with "Boa noite". We might miss that.

 But the error was for a direct greeting, so we assume the user starts with the greeting.

 Alternatively, we can check if the trigger is at the beginning of the prompt (after cleaning) OR if the prompt is exactly the trigger (with or without punctuation). But the startswith should cover the exact and the beginning.

 Let's stick with startswith.

 Implementation:

   prompt_clean = re.sub(r'[^a-z0-9\s]', '', prompt.lower()).strip()
   for trigger in PLUGIN_TRIGGERS:
        trigger_clean = re.sub(r'[^a-z0-9\s]', '', trigger.lower()).strip()
        if prompt_clean.startswith(trigger_clean):
            return responses.get(trigger, "Olá! Como posso ajudar?")

 But note: the trigger in the list is the original (with capital letters). We are using the original trigger to look up in the responses dictionary.

 However, we are cleaning the trigger to match. But the responses dictionary uses the original trigger as key.

 So we must use the original trigger (from the list) to get the response.

 We are looping over the original triggers, so we have the original trigger string.

 But note: what if the user says "boa noite" (lowercase) and our trigger is "Boa noite"? Then we clean both to "boa noite" and match, and then we use the original trigger "Boa noite" to get the response.

 That works.

 However, what if the user says "BOA NOITE"? Then cleaned to "boa noite", and we match with "Boa noite" (cleaned to "boa noite") and then use the original "Boa noite" to get the response.

 So it's case-insensitive and punctuation-insensitive.

 But note: the trigger list has "Boa noite" and "Boa tarde", etc. We are matching the start of the cleaned prompt.

 What if the user says "Boa noite e boa tarde"? Then we match the first trigger "Boa noite" and return that response.

 That seems acceptable.

 However, we must be cautious: the trigger list order matters. We should put longer triggers first? Actually, "Boa noite" and "Boa tarde" are both 2 words and same length. But if we had "Bom dia" and "Bom dia, tudo bem?" we are only matching the start, so it's okay.

 But what if we have "Bom dia" and "Bom dia, como vai?"? We are matching the start, so it's okay.

 Let's code accordingly.

 However, note: the user might say "Boa noite!" and we have trigger "Boa noite". We match and return the response for "Boa noite".

 But what if the user says "Boa noite, como vai?"? We match and return the same.

 We are not capturing the rest of the prompt. We are just returning a fixed response.

 That's acceptable for a greeting.

 But note: the plugin must return a non-empty string.

 We'll return the response in the same language as the trigger.

 However, what if the trigger is not in our responses dictionary? Then we return a default.

 We'll set a default response: "Olá! Como posso ajudar?" (Portuguese) or maybe we can detect the language? But for simplicity, we'll use the default in Portuguese because the example was in Portuguese.

 But note: the user might be using English. We have English triggers and responses. So if the trigger is in English, we return English.

 But what if the trigger is not in our list? Then we return the default (Portuguese). That might be odd if the user is speaking English.

 Alternatively, we can have a default per language? But we don't have language detection.

 Since the plugin is triggered by the trigger, and the trigger is in a specific language, we can assume the user wants that language.

 But if the trigger is not in our list, we don't trigger. So we only trigger on the triggers we have.

 So the only way we get to the default is if the trigger is in the list but not in the responses dictionary? That shouldn't happen because we have all triggers in the dictionary.

 So we can remove the default and just use:

   return responses[trigger]

 But to be safe, we'll use .get with a default.

 Let's code accordingly.

 However, note: the trigger list and the responses dictionary must have the same set of keys (the original trigger strings). We'll make sure.

 But what if we have a trigger "Boa noite" and the user says "Boa noite!"? We match and use the response for "Boa noite".

 That's fine.

 Let's write the plugin.

 We must also consider: the plugin must not crash. We'll wrap the matching in a try-except? Actually, the code is simple and we are using only standard library (re). But we'll import re.

 We are not using any external packages, so no need for PLUGIN_REQUIRES.

 Let's code.</think>
"""
Greeting Handler Plugin for Electra AI
Handles common greetings including Portuguese 'Boa noite!' and equivalents
"""

import re

PLUGIN_NAME = "Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles common greetings in multiple languages including Portuguese"
PLUGIN_AUTHOR = "AutoRepair"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = [
    "Boa noite", "Boa tarde", "Bom dia", 
    "Olá", "Oi", "Hello", "Hi", "Hey",
    "Good morning", "Good afternoon", "Good evening",
    "Boa noite!", "Boa tarde!", "Bom dia!",
    "Olá!", "Oi!", "Hello!", "Hi!", "Hey!"
]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = ["/greeting"]

# Language-specific greeting responses
GREETING_RESPONSES = {
    "Boa noite": "Boa noite! Como posso ajudar?",
    "Boa tarde": "Boa tarde! Como posso ajudar?",
    "Bom dia": "Bom dia! Como posso ajudar?",
    "Olá": "Olá! Como posso ajudar?",
    "Oi": "Oi! Como posso ajudar?",
    "Hello": "Hello! How can I help?",
    "Hi": "Hi! How can I help?",
    "Hey": "Hey! How can I help?",
    "Good morning": "Good morning! How can I help?",
    "Good afternoon": "Good afternoon! How can I help?",
    "Good evening": "Good evening! How can I help?"
}

def run(prompt: str, context: dict) -> str:
    """
    Handle greeting requests by matching trigger phrases and returning
    appropriate localized responses.
    """
    try:
        # Normalize prompt for matching (lowercase, strip punctuation)
        prompt_clean = re.sub(r'[^\w\s]', '', prompt.lower()).strip()
        
        # Check each trigger
        for trigger in PLUGIN_TRIGGERS:
            trigger_clean = re.sub(r'[^\w\s]', '', trigger.lower()).strip()
            
            # Check if prompt starts with trigger (handles "Boa noite!" and "Boa noite, tudo bem?")
            if prompt_clean.startswith(trigger_clean):
                # Return response for the base trigger (without punctuation)
                base_trigger = re.sub(r'[^\w\s]', '', trigger).strip()
                return GREETING_RESPONSES.get(base_trigger, 
                    GREETING_RESPONSES.get("Olá", "Olá! Como posso ajudar?"))
        
        # If we get here, no trigger matched (shouldn't happen due to router)
        return "Olá! Como posso ajudar?"
        
    except Exception as e:
        # Fallback response if something unexpected happens
        return f"Olá! Como posso ajudar? (Error: {str(e)})"