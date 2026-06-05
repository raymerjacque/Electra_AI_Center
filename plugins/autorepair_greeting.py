<think>We are given that the user requested "hi" and it failed in agent 'Proactive Scanner' with a CAPABILITY_GAP error because the user repeatedly requested this type of task (3 times) with no dedicated handler.

We are to write a plugin that handles this type of request successfully on MakuluLinux.

Looking at the specification, we are to write a ROUTER plugin (since it's for auto-repair and filling a capability gap). The plugin should intercept when the user says "hi" and respond appropriately.

However, note that the error says it failed in agent 'Proactive Scanner'. This suggests that the user's "hi" was being routed to the Proactive Scanner agent, which doesn't handle such a simple greeting.

We want to create a plugin that will intercept the "hi" request and handle it with a friendly greeting.

But note: the specification says that for ROUTER plugins, we define PLUGIN_TRIGGERS and PLUGIN_ROUTE_TOKEN. We want to catch the user saying "hi", so we can set:

PLUGIN_TRIGGERS = ["hi", "hello", "hey"]   # maybe more variations?

But note: the error says the user repeatedly requested "this type of task" (3 times). The task is just saying "hi". So we want to handle any greeting.

However, we must be cautious not to override other agents. The router will check the triggers in the order of plugin loading? The specification doesn't specify order, but we can assume that if multiple plugins have matching triggers, the first one (by some order) will be used.

But note: the error occurred in the Proactive Scanner agent. That means the router was trying to route to that agent for the "hi" request. We want to intercept before it gets to the Proactive Scanner.

We can set our plugin to have a high priority? The specification doesn't mention priority. However, note that the plugin system loads plugins at startup and integrates them into the router. The order of loading might be alphabetical by filename? We don't know.

But the specification says: "Plugins are loaded at startup and integrated into the router automatically."

We are writing an auto-repair plugin. The file will be named: autorepair_<token_lowercase>.py

We are to choose a PLUGIN_ROUTE_TOKEN that does not clash with existing ones. The existing plugins are:
  autorepair_proscan.py -> token likely "PROSCAN"
  autorepair_bot_explainer.py -> token likely "BOT_EXPLAINER"
  chuck_norris_jokes.py -> token likely "CHUCK_NORRIS_JOKES"

We want a token for our greeting handler. Let's choose "GREETING" or "HELLO". But note: the token must be unique. We can check the existing ones: PROSCAN, BOT_EXPLAINER, CHUCK_NORRIS_JOKES. So "GREETING" is safe.

But note: the PLUGIN_ROUTE_TOKEN is used in the router to identify the plugin. We are going to set:

PLUGIN_ROUTE_TOKEN = "GREETING"

And then in the run function, we return a greeting.

However, note that the user might say "hi" in the middle of a conversation. We don't want to always respond with a greeting if the user is in the middle of a task. But the error says the user repeatedly requested "hi" and it was being sent to the Proactive Scanner. So we assume that the user is trying to just say hello and get a response.

But what if the user says "hi" as part of a longer prompt? We are only intercepting when the trigger matches. The trigger matching is likely done on the entire prompt? Or maybe the router checks if the prompt starts with a trigger? The specification doesn't say.

Looking at the example for ROUTER:

PLUGIN_TRIGGERS = ["ask groq", "use groq", "groq:"]

This suggests that the trigger is a phrase that might appear at the beginning? Or maybe the router does a substring match? We don't know.

But note: the error says the user requested "hi". So the entire prompt was "hi". So we can set our trigger to exactly "hi", but also include "hello", "hey", etc.

But to be safe, we might want to match only when the entire prompt is a greeting? Or maybe we want to match when the prompt starts with a greeting? The specification doesn't say.

Given the context of the error, the user is just saying "hi" and expecting a greeting. So we can set:

PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings", "good morning", "good afternoon", "good evening"]

But note: if the user says "hi, how are you?" then we might want to handle that too? But the error was for just "hi". However, the user might have said "hi" multiple times and then the system tried to route to Proactive Scanner. So we want to catch any prompt that is just a greeting.

But what if the user says "hi" in the middle of a conversation? We don't want to break the flow. However, the error indicates that the user is trying to get a response to a greeting and the current agent (Proactive Scanner) doesn't handle it.

We can design our plugin to only respond when the prompt is exactly a greeting? Or maybe when the prompt starts with a greeting and then has more? We don't know the exact behavior of the router.

Given the lack of specification, let's assume the router does a simple substring match? Or maybe it checks if the prompt starts with one of the triggers? The example triggers are phrases that might be at the beginning.

But note: the example for AGENT plugin has triggers: ["check weather", "forecast", "temperature outside"] which are also likely at the beginning.

So let's assume the router checks if the prompt starts with any of the trigger strings (case insensitive?).

We want to catch when the user says just a greeting. So we can set:

PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings"]

But note: if the user says "hi there", then our trigger "hi" would match because it starts with "hi". That might be acceptable because we want to respond to a greeting.

But what if the user says "history"? That starts with "hi" too. So we might get false positives.

To avoid that, we can require that the prompt is exactly one of the greetings? But then we would miss "hi there".

Alternatively, we can use a more sophisticated matching in the run function? But the trigger matching is done by the router before calling our run function. So we can only control the triggers.

Given the ambiguity, let's stick to exact matches for the entire prompt? But the specification doesn't say if the trigger matching is exact or substring.

Looking at the example: "ask groq" is a trigger. If the user says "ask groq about the weather", then it would match because it starts with "ask groq". So it's likely a prefix match.

So if we set trigger "hi", then "hi there" would match. But "history" would also match because it starts with "hi". That's a problem.

We can set multiple triggers that are more specific? But we want to catch "hi", "hello", etc.

Alternatively, we can set the trigger to be the entire prompt? But then we would have to list every possible greeting? That's not feasible.

Maybe the router does a word-boundary match? We don't know.

Given the constraints, let's assume the router does a case-insensitive prefix match. Then we have to choose triggers that are unlikely to be prefixes of other words.

But "hi" is a prefix of many words. So maybe we should use a different approach.

Wait, the error says the user repeatedly requested "this type of task" (3 times). The task is just saying "hi". So maybe the user is just typing "hi" and nothing else. So we can set the trigger to be exactly "hi" (with no extra words). But the router might not support exact matching.

Alternatively, we can set the trigger to be "hi" and then in our run function, check if the prompt is exactly "hi" (or one of the greetings) and if not, we can return nothing? But then the router would have already routed to us because the trigger matched, and we would have to handle it.

But note: the run function must return a string. If we don't want to handle a particular prompt that matched our trigger, we can return an empty string? But the specification says: "run(prompt, context) must return a non-empty string on success". So we must return a non-empty string.

So if we get a prompt that starts with "hi" but is not a greeting (like "history"), we would have to return something. That would be wrong.

Therefore, we need to choose triggers that are unlikely to be prefixes of other words. For example, we can use:

PLUGIN_TRIGGERS = ["hi there", "hello there", "hey there"]

But then if the user says just "hi", it wouldn't match.

Alternatively, we can use:

PLUGIN_TRIGGERS = ["hi", "hello", "hey"]

and then in the run function, we check the prompt and if it's exactly one of these (or maybe with a space and then something) we respond with a greeting, otherwise we return a message that we only handle greetings? But then we would be handling non-greetings and returning an error message, which might be confusing.

Given the context, the user is just saying "hi" and expecting a greeting. So let's assume that the user's prompt is exactly "hi" (or one of the greetings). We'll set the triggers to the exact greetings we want to handle.

But note: the router might be doing a prefix match. So if we set trigger "hi", then "hi" and "hi there" and "history" would all match. We cannot control that.

Maybe the router does a whole word match? We don't know.

Given the lack of information, let's design the plugin to handle the exact string "hi" (case insensitive) and also "hello", "hey", etc. But we'll set the triggers to these exact strings? But then if the user says "hi there", it wouldn't match because the trigger is "hi" and the prompt is "hi there" (which starts with "hi")? Wait, if the router does prefix matching, then "hi" would match "hi there". So we would get "hi there" in our run function.

So in our run function, we can check:

if prompt.strip().lower() in ["hi", "hello", "hey", "greetings"]:
    return a greeting

But what about "hi there"? That would be caught by the trigger "hi" (if prefix matching) and then we would check if the prompt is exactly "hi"? No, it's "hi there". So we would not return a greeting? Then we would have to return something else? But we must return a non-empty string.

Alternatively, we can change our triggers to be the exact phrases we want to handle, but then we would miss variations.

Given the ambiguity, let's assume the router does a case-insensitive exact match? But the example "ask groq" suggests that it's not exact because the user might say "ask groq about the weather".

Wait, the example for AGENT plugin: triggers are ["check weather", "forecast", "temperature outside"]. These are also likely to be at the beginning of the prompt.

So I think the router does a prefix match (case insensitive). Therefore, if we set trigger "hi", then any prompt starting with "hi" will be routed to us.

So we must be prepared to handle any prompt that starts with "hi". That's too broad.

Alternatively, we can set the trigger to be "hi " (with a space) so that it only matches when "hi" is followed by a space? But then "hi" alone wouldn't match.

We can set multiple triggers:

PLUGIN_TRIGGERS = ["hi", "hi ", "hello", "hello ", "hey", "hey "]

But that's messy.

Given the problem, the user is just saying "hi". So maybe we can set the trigger to be exactly "hi" and hope that the router does exact matching? But the example suggests otherwise.

Wait, the error says the user requested "hi". So the prompt was exactly "hi". So if we set trigger "hi", then it will match exactly "hi" (if exact) or any prompt starting with "hi" (if prefix). But if the user says "hi there", then we would also match and we would have to handle it.

But the user's repeated request was for "hi", so we are only concerned with the exact "hi" for now.

However, to be safe, let's design the plugin to handle any prompt that is just a greeting (one word) and also two-word greetings like "hi there"? But then we might handle too much.

Given the time, let's write a plugin that handles the exact string "hi" (case insensitive) and also "hello", "hey", etc. But we'll set the triggers to these exact strings? But then if the router does prefix matching, we will get more.

Alternatively, we can set the trigger to be a regex? The specification doesn't say.

Given the constraints, I think we have to assume the router does a simple substring or prefix match. So we set the trigger to be the exact greeting words and then in the run function, we check if the prompt is exactly that word (or maybe with extra spaces) and if not, we return a message that we only handle greetings? But then we would be returning an error for "hi there", which might be acceptable.

But note: the user might say "hi" and then we respond with a greeting. That's what we want.

Let's design:

We'll set:
PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings"]

And in run:

prompt_lower = prompt.strip().lower()
if prompt_lower in ["hi", "hello", "hey", "greetings"]:
    return a friendly greeting

else:
    # This means the prompt started with one of these but had more words? 
    # We can either ignore or return a message that we only handle simple greetings.
    # But we must return a non-empty string.
    return "I only respond to simple greetings like 'hi', 'hello', etc. Please just say a greeting."

But wait, if the router does prefix matching, then "history" would trigger because it starts with "hi". Then we would check if "history" is in the list? It's not, so we would return the error message. That's acceptable.

But what if the user says "hi there"? Then we would get "hi there" and it's not in the list, so we would return the error message. But the user might expect a greeting for "hi there". So we can adjust:

We can check if the prompt starts with one of the greetings and then has more words? We can split the prompt and check the first word.

But note: the trigger already matched, so we know the prompt starts with one of the triggers. So we can do:

first_word = prompt_lower.split()[0]
if first_word in ["hi", "hello", "hey", "greetings"]:
    # Then we have a greeting, but maybe with more words.
    # We can respond with a greeting and then maybe ask how we can help?
    return f"{first_word.capitalize()}! How can I help you?"

But then for "hi there", we would respond with "Hi! How can I help you?" which is acceptable.

But for "history", the first word is "history", which is not in the list, so we would return the error message.

So let's do:

first_word = prompt_lower.split()[0]
if first_word in ["hi", "hello", "hey", "greetings"]:
    return f"{first_word.capitalize()}! How can I help you?"
else:
    return "I only respond to simple greetings. Please start your message with a greeting like 'hi', 'hello', etc."

But wait, what if the user says "greetings, how are you?"? Then first_word is "greetings", so we respond with "Greetings! How can I help you?" which is fine.

But note: the trigger is "greetings", so it would match. And then we respond.

But what if the user says "hi" and then a long sentence? We are only looking at the first word. That's acceptable.

But what about case? We are using lower case for the list and then capitalizing the first word for the response.

Now, we must also consider that the user might have said "Hi" (capital H). Our trigger matching is case insensitive? We don't know. But we are using lower case in the list and converting the prompt to lower for the first word. So it should be case insensitive.

But note: the trigger list we provide: are they case sensitive? The specification doesn't say. We'll assume the router does case-insensitive matching.

So we set:

PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings"]

And then in run, we do the above.

But wait, what about "good morning"? That's a greeting too. We can add it to the triggers and to the list.

But then the trigger "good morning" would match only if the prompt starts with "good morning". And then in run, we would split and the first word would be "good", which is not in our list. So we would have to adjust.

Alternatively, we can change the condition to check if the entire prompt (stripped) is in a list of greetings? But then we would miss "hi there".

Given the complexity, let's stick to one-word greetings for now. We can extend the list of one-word greetings.

But note: the user might say "hey" or "yo". We can add more.

But the error was for "hi". So let's at least handle "hi", "hello", "hey".

We'll do:

greetings = ["hi", "hello", "hey", "greetings", "yo", "howdy"]

But then for "good morning", we would need to set the trigger to "good morning" and then in run, we would have to check for two-word greetings.

Alternatively, we can change the condition to:

if any(prompt_lower.startswith(g) for g in greetings):
    # But then we would match "history" for "hi" again.

So we need to check the first word exactly.

We can do:

first_word = prompt_lower.split()[0]
if first_word in greetings:
    ...

But then for "good morning", the first word is "good", which is not in the list. So we would have to add "good" to the list? But then "good" alone would be a greeting? Not really.

So maybe we should have a list of multi-word greetings and check the beginning of the prompt.

Given the time, let's keep it simple and only handle one-word greetings. We can extend the list of one-word greetings.

But note: the user might say "hi" and then a comma and then more. We are splitting by space, so "hi," would become "hi," which is not in the list. So we should strip punctuation? We can use:

import string
first_word = prompt_lower.split()[0].strip(string.punctuation)

But then we are removing punctuation from the first word.

Alternatively, we can use a regex to extract the first word? But we don't want to import re if we don't have to.

We can do:

first_word = prompt_lower.split()[0]
first_word = first_word.strip(string.punctuation)

But note: the prompt might have leading spaces? We are stripping the entire prompt and then splitting, so the first element of split is the first word without leading spaces.

But if the user says "hi, there", then split gives ["hi,", "there"] and then we strip the comma from "hi," to get "hi". That works.

So let's do:

import string

first_word = prompt_lower.split()[0].strip(string.punctuation)

Then check if first_word in greetings.

But note: what if the user says "hello!"? Then first_word becomes "hello" after stripping.

So that's good.

Now, we must also consider that the user might say "hi" in a non-English language? But the error is in English, so we assume English.

Now, let's write the plugin.

We are to write a ROUTER plugin.

We'll set:

PLUGIN_NAME = "Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles simple greetings like 'hi', 'hello', etc."
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings", "yo", "howdy"]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = []   # We don't need slash commands for this.

But note: the specification says PLUGIN_COMMANDS is for slash commands only. We don't need any.

Now, the run function:

We'll use the context's print_fn to show progressive output? But we are just returning a string. We can use print_fn to print the greeting and then return it? Or just return.

The specification says: use context["print_fn"](text) to show progressive output. But we are returning a string, so we can just return.

But if we want to stream, we can use print_fn and then return the same string? But the run function must return a string.

We can do:

context["print_fn"]("Hello! How can I help you?")
return "Hello! How can I help you?"

But that would print twice? Actually, the app might print the return value. We don't know.

Given the example in the specification for AGENT:

context["print_fn"](f"Fetching weather for: {prompt}")
return weather_result

So they use print_fn for progress and then return the result.

We can do:

greeting = f"{first_word.capitalize()}! How can I help you?"
context["print_fn"](greeting)
return greeting

But if the first_word is "yo", then we capitalize to "Yo", which is fine.

But note: if the prompt is "hi there", then first_word is "hi", so we respond with "Hi! How can I help you?" which is fine.

But what if the prompt is "HELLO"? Then first_word becomes "hello", and we capitalize to "Hello".

Now, what about the case when the prompt is not a greeting? We already said we would return an error message. But note: the trigger matched, so we are in this plugin. We must return a non-empty string.

But if the prompt is "history", then first_word is "history", which is not in our list. So we return the error message.

But wait, the trigger is "hi", so "history" starts with "hi", so it matches. Then we check first_word and it's not in the list, so we return the error.

That's acceptable.

But what if the user says "high"? That starts with "hi", so it would match. Then first_word is "high", not in the list, so error. That's acceptable.

Now, we must also consider that the user might have said "hi" in a different case. We are converting to lower, so it's fine.

Now, let's code accordingly.

But note: the plugin must be placed in ~/.config/ai_plugins and named autorepair_greeting.py (since PLUGIN_ROUTE_TOKEN is "GREETING", so lowercase: greeting).

But the specification says: "File will be auto-named: autorepair_<token_lowercase>.py"

So we are writing the code for that file.

We must also handle any exceptions. We'll wrap the run function in a try/except.

But note: the run function is called by the host app. We must not crash.

We'll do:

def run(prompt: str, context: dict) -> str:
    try:
        # ... our code
    except Exception as e:
        return f"Error in Greeting Handler: {str(e)}"

But we should also log the error? We don't have a logger. We can use print_fn to print the error? But the host app might capture the return string.

We can do:

def run(prompt: str, context: dict) -> str:
    try:
        # ... 
    except Exception as e:
        error_msg = f"Greeting Handler error: {str(e)}"
        context["print_fn"](error_msg)
        return error_msg

But note: the context might not have print_fn? The specification says it does.

Now, let's write the code.

We are going to import string for punctuation.

But note: the plugin must be self-contained. We are allowed to import standard libraries.

We'll do:

import string

Then in run:

prompt_lower = prompt.strip().lower()
if not prompt_lower:
    return "Hello! How can I help you?"   # empty prompt? just greet.

first_word = prompt_lower.split()[0].strip(string.punctuation)
greetings = ["hi", "hello", "hey", "greetings", "yo", "howdy"]

if first_word in greetings:
    response = f"{first_word.capitalize()}! How can I help you?"
    context["print_fn"](response)
    return response
else:
    return "I only respond to simple greetings. Please start your message with a greeting like 'hi', 'hello', etc."

But wait, what if the prompt is "hi, how are you?"? Then first_word is "hi", so we respond with "Hi! How can I help you?" and ignore the rest. That's acceptable because the user just said hi and then asked how we are. We are not answering the how are you part, but we are asking how we can help. That's a reasonable response.

But what if the user says "hello, i need help"? Then we respond with "Hello! How can I help you?" which is fine.

Now, what about the case when the user says "hi" and then a newline? We are stripping the prompt, so it's fine.

But note: the prompt might have multiple lines? We are only taking the first line? We are stripping and then splitting by space, so we only get the first word of the first line? Actually, split() splits by any whitespace, including newlines. So if the prompt is "hi\nthere", then split() gives ["hi", "there"], so first_word is "hi". That's acceptable.

But if the prompt is "hi\n\n", then split() gives ["hi"], so first_word is "hi".

So it's okay.

Now, we must also consider that the user might have said "hi" in a non-English language? We are only handling English.

But the error was in English, so we assume English.

Now, let's write the complete plugin.

We must also declare the metadata.

We'll set:

PLUGIN_NAME = "Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles simple greetings like 'hi', 'hello', etc."
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings", "yo", "howdy"]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = []   # no slash commands

We don't have any external dependencies, so PLUGIN_REQUIRES = [].

Now, the run function as above.

But note: the specification says the run function must return a non-empty string on success. We are returning a string in all branches.

Now, let's write the code.

But wait: the plugin must be named autorepair_greeting.py. We are writing the code for that file.

We are to output only the raw Python source.

So:

import string

PLUGIN_NAME = "Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles simple greetings like 'hi', 'hello', etc."
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings", "yo", "howdy"]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = []
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    try:
        prompt_lower = prompt.strip().lower()
        if not prompt_lower:
            response = "Hello! How can I help you?"
            context["print_fn"](response)
            return response

        first_word = prompt_lower.split()[0].strip(string.punctuation)
        greetings = ["hi", "hello", "hey", "greetings", "yo", "howdy"]

        if first_word in greetings:
            response = f"{first_word.capitalize()}! How can I help you?"
            context["print_fn"](response)
            return response
        else:
            return "I only respond to simple greetings. Please start your message with a greeting like 'hi', 'hello', etc."
    except Exception as e:
        error_msg = f"Greeting Handler error: {str(e)}"
        context["print_fn"](error_msg)
        return error_msg
But note: the specification says to use context["print_fn"] for progressive output. We are using it for the greeting and for the error.

But what if the context doesn't have print_fn? The specification says it does.

Now, we must also consider that the user might have said "hi" in a different way, like "HI" or "Hi". We are converting to lower, so it's fine.

But what about "howdy"? We have it in the list.

Now, let's test with some examples:

- "hi" -> first_word "hi" -> "Hi! How can I help you?"
- "hello" -> "Hello! How can I help you?"
- "hey" -> "Hey! How can I help you?"
- "greetings" -> "Greetings! How can I help you?"
- "yo" -> "Yo! How can I help you?"
- "howdy" -> "Howdy! How can I help you?"
- "hi there" -> first_word "hi" -> "Hi! How can I help you?"
- "hello, how are you?" -> first_word "hello" -> "Hello! How can I help you?"
- "history" -> first_word "history" -> error message.
- "high" -> first_word "high" -> error message.

But note: "howdy" is a greeting, but if the user says "howdy partner", then first_word is "howdy", so we respond with "Howdy! How can I help you?" which is fine.

But what about "good morning"? We don't have "good" in the list, so it would return the error. We can add "good" to the list? But then "good" alone would be a greeting? Not really. We can add multi-word greetings by having the trigger be "good morning" and then in run, check if the prompt starts with "good morning"? But then we would have to list all multi-word greetings.

Given the time, let's keep it simple and only one-word greetings. We can extend the list to include "goodmorning" (without space) but that's not common.

Alternatively, we can change the condition to:

if any(prompt_lower.startswith(g) for g in greetings):

But then we would match "history" for "hi". So we are back to the same problem.

So we stick to first word matching.

But note: the trigger is a prefix match. So if we set trigger "good morning", then the prompt must start with "good morning". Then in run, we can check if the prompt starts with "good morning" and then respond accordingly.

But we don't have "good morning" in our triggers. So we are not handling it.

Given the scope, we are only handling the simple one-word greetings that the user might use.

But the error was for "hi", so we are handling that.

Now, we must also consider that the user might have said "hi" in a different language? We are not handling that.

But the error was in English, so we assume English.

Now, let's write the code as above.

But note: the specification says the plugin must be placed in ~/.config/ai_plugins and named autorepair_greeting.py.

We are writing the code for that file.

We are done.

But wait: the specification says to choose a PLUGIN_ROUTE_TOKEN that does not clash with existing ones. We chose "GREETING". The existing ones are: PROSCAN, BOT_EXPLAINER, CHUCK_NORRIS_JOKES. So it's safe.

Now, output the code.</think>
import string

PLUGIN_NAME = "Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles simple greetings like 'hi', 'hello', etc."
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["hi", "hello", "hey", "greetings", "yo", "howdy"]
PLUGIN_ROUTE_TOKEN = "GREETING"
PLUGIN_COMMANDS = []
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    try:
        prompt_lower = prompt.strip().lower()
        if not prompt_lower:
            response = "Hello! How can I help you?"
            context["print_fn"](response)
            return response

        first_word = prompt_lower.split()[0].strip(string.punctuation)
        greetings = ["hi", "hello", "hey", "greetings", "yo", "howdy"]

        if first_word in greetings:
            response = f"{first_word.capitalize()}! How can I help you?"
            context["print_fn"](response)
            return response
        else:
            return "I only respond to simple greetings. Please start your message with a greeting like 'hi', 'hello', etc."
    except Exception as e:
        error_msg = f"Greeting Handler error: {str(e)}"
        context["print_fn"](error_msg)
        return error_msg