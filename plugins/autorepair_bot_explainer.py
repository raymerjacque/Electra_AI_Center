<think>We are given a capability gap: the user repeatedly requested "explain what is a bot" and it failed because there's no dedicated handler.
 We are to write a plugin that handles this type of request.

 Since the request is a general explanation about bots, we can create a ROUTER plugin that triggers on phrases like "explain what is a bot", "what is a bot", etc.

 However, note that the error says it failed in agent 'Proactive Scanner'. This suggests that the request was being routed to an agent that doesn't handle this.

 We are to write a plugin that will handle such requests. We can make it an AGENT plugin so that it becomes a first-class routing target, or a ROUTER plugin that intercepts and handles.

 But note: the specification says that for a capability gap, we are to write a plugin that handles the request. Since the request is a general question, we can handle it with a simple response.

 Let's design:

 Option 1: ROUTER plugin that triggers on phrases like "explain what is a bot", "what is a bot", "define bot", etc.

 Option 2: AGENT plugin that is triggered by the same phrases and returns an explanation.

 Since the error says it failed in agent 'Proactive Scanner', it might be that the router tried to route to an agent that doesn't exist. We can create an AGENT plugin that will be the target for such queries.

 However, note that the user's request is very specific: "explain what is a bot". We don't want to interfere with other agents. So we can create an AGENT plugin that is triggered by a set of phrases and returns a fixed explanation.

 But wait: the specification says that AGENT plugins are first-class routing targets and the router sees them exactly like built-in agents. So we can create an AGENT plugin with a trigger phrase and then the router will route to it.

 However, the error says the request was routed to 'Proactive Scanner' and failed. So maybe the router already has a mapping for some phrases to 'Proactive Scanner'? We don't want to break that.

 Alternatively, we can create a ROUTER plugin that intercepts the request and handles it without routing to an agent. But note: the original behavior of ROUTER plugins is to intercept and then return a response. So we can do:

 PLUGIN_TYPE = "ROUTER"
 PLUGIN_TRIGGERS = ["explain what is a bot", "what is a bot", "define bot", "bot definition"]
 Then in run(), we return the explanation.

 But note: the error says the request was routed to an agent. So maybe the router already has a rule that routes "explain what is a bot" to the Proactive Scanner? We don't know.

 Since we are filling a capability gap, we want to handle the request. We can do:

 Let's create a ROUTER plugin that triggers on the exact phrase and returns the explanation. But note: the user might ask in different ways. We can use a list of triggers.

 However, the specification says that the router will check the triggers in order? We don't know the order. But we can make our plugin have a high priority by having a trigger that matches exactly.

 But wait: the error says the user repeatedly requested this type of task (3 times). So maybe the router is trying to route to an agent that doesn't exist? We are not sure.

 Alternatively, we can create an AGENT plugin that is triggered by the same phrases and then the router will route to our agent. But then we have to make sure that our agent is triggered before the Proactive Scanner? We don't control the order.

 Since we are writing a plugin to fill the gap, and the gap is that there's no handler for this, we can create a ROUTER plugin that handles it and returns the explanation. This way, it won't go to the agent at all.

 Let's do:

 PLUGIN_TYPE = "ROUTER"
 PLUGIN_TRIGGERS = ["explain what is a bot", "what is a bot", "define bot", "bot definition", "what is a bot?"]
 PLUGIN_ROUTE_TOKEN = "BOT_EXPLAINER"

 But note: the PLUGIN_ROUTE_TOKEN is used for the router to identify the plugin? Actually, for ROUTER plugins, the PLUGIN_ROUTE_TOKEN is the token that the router uses to route to this plugin? Wait, the specification says:

 For ROUTER:
   PLUGIN_ROUTE_TOKEN = "GROQ"   # becomes a real routing token? Actually, the example shows that the run function returns a string.

 But note: the example for ROUTER doesn't use the token in the run function. It just returns a string.

 However, the specification says: "PLUGIN_ROUTE_TOKEN: becomes a real routing token" for AGENT. For ROUTER, it's not clear.

 Looking at the specification:

 For ROUTER:
   PLUGIN_TRIGGERS    = ["ask groq", "use groq", "groq:"]
   PLUGIN_ROUTE_TOKEN = "GROQ"

 But then the run function doesn't use the token. So maybe the token is used for the router to know which plugin to call? Actually, the router will check the triggers and if matched, it will call the run function of that plugin.

 So for ROUTER, the PLUGIN_ROUTE_TOKEN is just an identifier? It might be used in the context? We don't know.

 Since we are writing a ROUTER plugin, we can set PLUGIN_ROUTE_TOKEN to something that doesn't clash, like "BOT_EXPLAINER".

 But note: the error says the request was routed to agent 'Proactive Scanner'. So maybe the router has a rule that if the prompt matches a certain pattern, it routes to the Proactive Scanner agent. We don't want to break that.

 Alternatively, we can make our plugin an AGENT and then the router will have a new agent. But then the router might still route to Proactive Scanner for the same prompt? We don't know the routing logic.

 Since we are not sure, and the requirement is to handle the request, let's create a ROUTER plugin that triggers on the exact phrases and returns the explanation. This way, when the user says "explain what is a bot", our plugin will catch it and return the explanation, and the router won't try to route to an agent.

 Steps:

 1. Create a ROUTER plugin.
 2. Set PLUGIN_TRIGGERS to a list of phrases that match the user's request.
 3. In run(), return a string that explains what a bot is.

 However, note: the user might ask in a different way. We can use a simple string matching. But the router might do exact match or substring? We don't know.

 The specification doesn't say how the router matches triggers. We assume it's a simple substring match? Or exact? We'll use exact phrases for safety.

 But the user said: "explain what is a bot". We can also include "what is a bot?" and "what is a bot" and "define bot".

 Let's write:

 PLUGIN_TRIGGERS = [
     "explain what is a bot",
     "what is a bot",
     "what is a bot?",
     "define bot",
     "bot definition"
 ]

 But note: the user might say "can you explain what a bot is?" etc. We can't cover all. We are just filling the gap for the exact request that failed.

 However, the error says the user repeatedly requested this type of task. So maybe the user is asking in the same way each time? We don't know.

 We'll stick to the exact phrase that failed: "explain what is a bot". But to be safe, we can add a few variations.

 But note: the plugin will be triggered by any of these phrases. We want to return the same explanation.

 Let's write the explanation:

 A bot (short for robot) is a software application that runs automated tasks over the internet. Typically, bots perform simple and repetitive tasks at a much higher rate than humans. They can be used for various purposes, such as:

 - Web crawling: Search engines use bots to index web pages.
 - Chatbots: Simulate human conversation to answer questions or perform tasks.
 - Social media bots: Automate posting, liking, or following on social platforms.
 - Malicious bots: Used for spamming, scraping, or attacking websites.

 Bots can be beneficial or harmful, depending on their use. They are often programmed to follow specific rules and can operate without human intervention.

 We'll return this as a string.

 However, note: the run function must return a non-empty string.

 Let's code accordingly.

 But wait: the specification says we must use context["print_fn"] for progressive output? We can, but we are returning a string. We can also use print_fn to print and then return the same? Or just return.

 Since the explanation is short, we can just return the string.

 However, the specification says: "Use context["print_fn"](text) to show progressive output instead of print()". We are not doing progressive output, so we can just return.

 But note: the example in the specification for AGENT uses print_fn to show a message and then returns the result. We can do:

   context["print_fn"]("Fetching explanation...")
   return explanation

 But we don't need to fetch, we have the explanation. So we can just return.

 However, to be consistent with the example, we can print a message and then return.

 Let's do:

   context["print_fn"]("Here is an explanation of what a bot is:")
   return explanation

 But note: the run function returns a string that will be shown to the user. The print_fn is for streaming output during processing. We are not processing, so we can skip.

 Alternatively, we can do:

   context["print_fn"](explanation)
   return explanation

 But that would print twice? Actually, the return value is what the router will output. So if we print and then return, it will be printed twice? We don't know.

 Let's just return the explanation without printing.

 However, the specification says: "Use context["print_fn"](text) to show progressive output". We are not doing progressive, so we don't need to use it.

 So:

   return explanation

 But wait: the example in the specification for ROUTER doesn't use print_fn. It just returns.

 So we are safe.

 Let's code accordingly.

 However, note: the plugin must be placed in the directory and named autorepair_<token_lowercase>.py. Our token is "BOT_EXPLAINER", so the file should be named: autorepair_bot_explainer.py

 But the specification says: "File will be auto-named: autorepair_<token_lowercase>.py". So we set PLUGIN_ROUTE_TOKEN = "BOT_EXPLAINER", then the file will be named autorepair_bot_explainer.py.

 But wait: the user said the plugin is for a capability gap. We are writing a plugin that will be placed in the directory. We are to output the source code.

 We are to output only the raw Python source.

 Let's write the plugin:

 Note: We must include the required metadata.

 We are writing a ROUTER plugin.

 We'll set:

 PLUGIN_NAME = "Bot Explainer"
 PLUGIN_VERSION = "1.0.0"
 PLUGIN_DESCRIPTION = "Explains what a bot is"
 PLUGIN_AUTHOR = "Electra Plugin Forge"
 PLUGIN_ENABLED = True
 PLUGIN_TYPE = "ROUTER"
 PLUGIN_REQUIRES = []   # no external dependencies

 PLUGIN_TRIGGERS = [ ... ]
 PLUGIN_ROUTE_TOKEN = "BOT_EXPLAINER"
 PLUGIN_COMMANDS = []   # we don't need slash commands for this? Actually, the specification says for ROUTER, PLUGIN_COMMANDS is optional? It's in the example but not required.

 We'll set PLUGIN_COMMANDS to an empty list.

 Then define run(prompt, context).

 Let's code accordingly.

 However, note: the context has a key "print_fn". We are not using it, but it's there.

 We'll write:

   def run(prompt: str, context: dict) -> str:
        explanation = """A bot (short for robot) is a software application that runs automated tasks over the internet. Typically, bots perform simple and repetitive tasks at a much higher rate than humans. They can be used for various purposes, such as:

 - Web crawling: Search engines use bots to index web pages.
 - Chatbots: Simulate human conversation to answer questions or perform tasks.
 - Social media bots: Automate posting, liking, or following on social platforms.
 - Malicious bots: Used for spamming, scraping, or attacking websites.

 Bots can be beneficial or harmful, depending on their use. They are often programmed to follow specific rules and can operate without human intervention."""
        return explanation

 But wait: the user might have provided a prompt that is not exactly one of our triggers? The router will only call our run if the prompt matches one of the triggers. So we don't need to check the prompt in run? Actually, the router will only call us if the prompt matches one of the triggers. So we can assume the prompt is about explaining a bot.

 However, to be safe, we can check the prompt and if it's not one of the triggers, we can return an empty string? But the router only calls us when it matches, so we don't need to check.

 But what if the user says "explain what is a bot and how to make one"? Our trigger "explain what is a bot" might not match exactly? We don't know the matching algorithm.

 Since we are writing a plugin for a specific capability gap, and the gap is for the exact request "explain what is a bot", we can just handle that.

 However, the error says the user repeatedly requested this type of task. So maybe the user is asking in the same way. We'll stick to the exact phrase.

 But note: the router might do a substring match? We don't know. We can make our triggers more general by using:

   PLUGIN_TRIGGERS = ["explain what is a bot", "what is a bot", "define bot"]

 But if the user says "what is a bot and how to make one", then "what is a bot" is a substring? We don't know.

 Since we are not sure, we'll use the exact phrases that we think the user used.

 Alternatively, we can use a more flexible approach in the run function? But the router will only call us if the prompt matches one of the triggers. So we have to set the triggers to match the user's input.

 We don't know the exact input. The error says: "User repeatedly requested this type of task (3 times) with no dedicated handler."

 So the user might have said:

   "explain what is a bot"
   "what is a bot"
   "define bot"

 We'll set the triggers to these three.

 Let's code accordingly.

 However, note: the plugin must be robust. We are going to return the same explanation for any of these triggers.

 We are done.

 But wait: the specification says we must wrap external calls in try/except. We don't have external calls.

 We are safe.

 Let's write the code.</think>
"""
Plugin to handle requests for explaining what a bot is.
Fills capability gap for basic definition queries about bots.
"""

PLUGIN_NAME        = "Bot Definition Plugin"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Provides clear explanation of what a bot is"
PLUGIN_AUTHOR      = "Electra Plugin Forge"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "ROUTER"
PLUGIN_REQUIRES    = []

# Trigger phrases that should route to this plugin
PLUGIN_TRIGGERS    = [
    "explain what is a bot",
    "what is a bot",
    "define bot",
    "bot definition",
    "what are bots",
    "explain bots",
    "bot meaning"
]

PLUGIN_ROUTE_TOKEN = "BOT_DEFINITION"
PLUGIN_COMMANDS    = []

def run(prompt: str, context: dict) -> str:
    """
    Returns a comprehensive explanation of what a bot is.
    Handles various phrasings of the same core question.
    """
    try:
        # Use print_fn for any diagnostic output if needed
        context["print_fn"]("Providing bot definition...")
        
        explanation = """A bot (short for "robot") is a software application that runs automated tasks over the internet. Bots typically perform simple, repetitive tasks at a much higher rate than humans could.

Key characteristics of bots:
• Automation: They operate without human intervention once started
• Scripted behavior: Follow predefined rules or algorithms
• Networked: Usually connect to internet services or APIs
• Task-specific: Designed for particular functions

Common types of bots:
1. Chatbots - Simulate human conversation (like me!)
2. Web crawlers - Index websites for search engines
3. Social media bots - Automate posting/liking/following
4. Monitoring bots - Track system status or prices
5. Malicious bots - Spam, scrape data, or launch attacks

Bots can be beneficial (customer service, search indexing) or harmful (spam, DDoS attacks) depending on their design and purpose. They're fundamental to modern internet infrastructure and automation."""
        
        return explanation.strip()
        
    except Exception as e:
        # Never crash the host app - return error message
        error_msg = f"Error generating bot definition: {str(e)}"
        context["print_fn"](f"[Bot Definition Plugin] {error_msg}")
        return "I encountered an error while explaining what a bot is. Please try again."