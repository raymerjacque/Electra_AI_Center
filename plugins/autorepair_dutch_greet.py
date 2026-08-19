<think>Got it, let's tackle this. First, the user said "bjr" which is Dutch for "good day" right? Wait, but wait, the error says it's a capability gap for repeated requests of this type. Wait no, wait the error is from Proactive Scanner? Wait no, wait the user's request is "bjr" — wait, maybe it's a greeting? Wait no, wait let's check the plugin spec. We need a ROUTER plugin, right? Because it's a capability gap, so we need to handle the "bjr" trigger.

Wait first, PLUGIN_NAME: let's make it "Dutch Greeting Handler"? Wait no, wait "bjr" is a common Dutch abbreviation for "goedemorgen" (good morning) or just a casual greeting. Wait but wait, maybe the user is using MakuluLinux which is based on Ubuntu, but "bjr" is Dutch. Wait but let's make the plugin handle "bjr" as a greeting, right? Because the user sent "bjr" and it failed because there's no handler.

Wait first, the required metadata: PLUGIN_TYPE is ROUTER, right? Because it's a capability gap filler. PLUGIN_TRIGGERS should include "bjr" obviously. PLUGIN_ROUTE_TOKEN should be something unique, like "DUTCH_GREETING" — wait no, make sure it doesn't clash. Let's see, existing ones are none, so that's fine. Wait PLUGIN_TRIGGERS: ["bjr", "goedemorgen", "goedemiddag", "goedenavond"]? Wait no, the user's request was "bjr", so at least include that. Wait but let's make the trigger match "bjr" case-insensitive? Wait no, the triggers are matched as per the router, but let's include "bjr" as the main trigger.

Wait then the run function: when the prompt is "bjr" or related, respond with a friendly Dutch greeting? Wait but wait, maybe also handle if it's a different context? Wait no, the user's request was "bjr" which failed, so the plugin needs to respond to that. Wait but also, make sure it's robust. Let's see: the run function takes prompt and context. Let's check if the prompt (lowercased) is in the triggers, then return a friendly response. Wait but also, maybe add a little more? Like, if it's morning, say goedemorgen, etc? Wait but maybe keep it simple first, but make sure it works.

Wait also, PLUGIN_REQUIRES: do we need any packages? No, right? Because it's just a greeting, no external calls. So PLUGIN_REQUIRES is empty list.

Wait PLUGIN_ENABLED is True, PLUGIN_TYPE is ROUTER. PLUGIN_NAME: "Dutch Greeting Responder"? Wait no, maybe "BJ R Greeting Handler"? Wait no, better "Dutch Casual Greeting Handler". Wait PLUGIN_DESCRIPTION: "Responds to Dutch casual greetings like 'bjr' with appropriate friendly replies." That makes sense.

Wait PLUGIN_TRIGGERS: ["bjr", "goedemorgen", "goedemiddag", "goedenavond", "goedennacht"] — those are common Dutch greetings, so if the user uses any of those, it triggers. PLUGIN_ROUTE_TOKEN: "DUTCH_GREET" — that's unique, no clash.

Wait then the run function: let's take the prompt, lower case it, check if it's one of the triggers. Then, maybe respond with a friendly Dutch greeting, maybe also in English? Wait no, the user said "bjr" so respond in Dutch? Or maybe bilingual? Wait let's see: if the prompt is "bjr", return "Hoi! Goed om je te horen. Hoe kan ik je vandaag helpen?" That's friendly. Wait but also, maybe handle if it's a different greeting? Like if it's "goedemorgen", respond with "Goedemorgen! Fijne dag gewenst." That's good.

Wait but also, make sure to handle any errors? Wait no, the run function is simple, no external calls, so no need for try/except? Wait but the spec says wrap all external calls in try/except, but if there are no external calls, it's okay. Wait but maybe add a try/except just in case? No, it's unnecessary, but maybe not needed.

Wait also, the spec says run must return a non-empty string on success. So that's covered.

Wait let's structure the plugin:

First, the metadata:

PLUGIN_NAME = "Dutch Greeting Responder"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles Dutch casual greetings like 'bjr' with appropriate friendly responses, filling the capability gap for repeated greeting requests."
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []
PLUGIN_TRIGGERS = ["bjr", "goedemorgen", "goedemiddag", "goedenavond", "goedennacht"]
PLUGIN_ROUTE_TOKEN = "DUTCH_GREET"
PLUGIN_COMMANDS = ["/dutchgreet", "/bjr"]

Then the run function:

def run(prompt: str, context: dict) -> str:
    normalized_prompt = prompt.strip().lower()
    # Check if the prompt matches any of our triggers
    if normalized_prompt in [t.lower() for t in PLUGIN_TRIGGERS]:
        # Customize response based on the specific greeting
        if normalized_prompt == "bjr":
            return "Hoi! Fijn om je te horen. Hoe kan ik je vandaag assisteren?"
        elif normalized_prompt == "goedemorgen":
            return "Goedemorgen! Ik wens je een prettige dag toe."
        elif normalized_prompt == "goedemiddag":
            return "Goedemiddag! Hoe kan ik je helpen in de namiddag?"
        elif normalized_prompt == "goedenavond":
            return "Goedenavond! Fijne avond gewenst."
        elif normalized_prompt == "goedennacht":
            return "Goedennacht! Slaap lekker."
    # If for some reason it's triggered but not matching, fallback
    return "Hoi! Ik heb je begroeting ontvangen. Waar kan ik je mee helpen?"

Wait that's good. Wait but wait, the user's request was "bjr" which is exactly the trigger, so this will handle it. Also, the PLUGIN_ROUTE_TOKEN is unique, no clash. PLUGIN_TYPE is ROUTER as required for auto-repair plugins. PLUGIN_ENABLED is True. No external dependencies, so PLUGIN_REQUIRES is empty. That's perfect.

Wait but wait, should we add a docstring? The spec says start with module docstring or first import. Oh right, the output should start with the module docstring or first import. So let's add a module docstring at the top:

"""
Electra AI Plugin: Dutch Greeting Responder
Handles casual Dutch greetings like 'bjr' to fill the capability gap for repeated greeting requests.
"""

Then the imports? Wait do we need any imports? No, right? Because we're not using any external modules. So no imports needed. Wait but maybe import os? No, we don't use it. So the code starts with the docstring, then the metadata, then the run function.

Wait let's check all the rules:

- PLUGIN_ROUTE_TOKEN is unique: DUTCH_GREET, no clash, correct.
- File will be named autorepair_dutch_greet.py, which matches the token lowercase, correct.
- PLUGIN_ENABLED is True, correct.
- PLUGIN_TYPE is ROUTER, correct for auto-repair.
- run returns non-empty string, correct.
- No hardcoded paths, correct.
- No external calls, so no try/except needed, but if there were, we'd wrap them, but here it's fine.
- No imports from ai_terminal, correct.
- All context keys are available but we don't need them here, which is fine.

Wait that's all. Let's put it all together. Wait let's make sure there's no markdown, just raw Python. Let's write it out:

Wait let's check:

"""
Electra AI Plugin: Dutch Greeting Responder
Fills capability gap for handling Dutch casual greetings like 'bjr' on MakuluLinux.
"""

PLUGIN_NAME = "Dutch Greeting Responder"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Responds to Dutch casual greetings (bjr, goedemorgen, etc.) with appropriate friendly replies, resolving repeated failed request errors."
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []
PLUGIN_TRIGGERS = ["bjr", "goedemorgen", "goedemiddag", "goedenavond", "goedennacht"]
PLUGIN_ROUTE_TOKEN = "DUTCH_GREET"
PLUGIN_COMMANDS = ["/dutchgreet", "/bjr"]


def run(prompt: str, context: dict) -> str:
    normalized_prompt = prompt.strip().lower()
    trigger_list = [t.lower() for t in PLUGIN_TRIGGERS]
    
    if normalized_prompt in trigger_list:
        if normalized_prompt == "bjr":
            return "Hoi! Fijn om je te horen. Hoe kan ik je vandaag assisteren?"
        elif normalized_prompt == "goedemorgen":
            return "Goedemorgen! Ik wens je een prettige dag toe."
        elif normalized_prompt == "goedemiddag":
            return "Goedemiddag! Waar kan ik je mee helpen in de namiddag?"
        elif normalized_prompt == "goedenavond":
            return "Goedenavond! Fijne avond gewenst."
        elif normalized_prompt == "goedennacht":
            return "Goedennacht! Slaap lekker en tot morgen."
    
    # Fallback response for any matched trigger not explicitly handled
    return "Hoi! Ik heb je begroeting ontvangen. Waar kan ik je mee helpen?"

Wait that's perfect. Let's check: the user sent "bjr", which is in the triggers, so it will return the friendly Dutch greeting. That handles the request. The plugin is a ROUTER type, correct. All metadata is present. No external dependencies. No hardcoded paths. Returns a non-empty string. That's exactly what's needed.

Wait wait, but is "bjr" really a Dutch greeting? Yes, it's a common abbreviation for "goedemorgen" (good morning) but also used as a casual greeting any time of day, which is why the first response is a general friendly greeting. That's correct.

Also, the PLUGIN_COMMANDS are optional, but adding them is fine, they are slash commands that trigger the plugin. That's allowed.

Yes, this should work. Let's make sure there's no extra stuff, just raw Python. No markdown, no explanations. Yep.
</think>

"""
Electra AI Plugin: Dutch Greeting Responder
Fills capability gap for handling Dutch casual greetings like 'bjr' on MakuluLinux.
"""

PLUGIN_NAME = "Dutch Greeting Responder"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Responds to Dutch casual greetings (bjr, goedemorgen, etc.) with appropriate friendly replies, resolving repeated failed request errors."
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []
PLUGIN_TRIGGERS = ["bjr", "goedemorgen", "goedemiddag", "goedenavond", "goedennacht"]
PLUGIN_ROUTE_TOKEN = "DUTCH_GREET"
PLUGIN_COMMANDS = ["/dutchgreet", "/bjr"]


def run(prompt: str, context: dict) -> str:
    normalized_prompt = prompt.strip().lower()
    trigger_list = [t.lower() for t in PLUGIN_TRIGGERS]
    
    if normalized_prompt in trigger_list:
        if normalized_prompt == "bjr":
            return "Hoi! Fijn om je te horen. Hoe kan ik je vandaag assisteren?"
        elif normalized_prompt == "goedemorgen":
            return "Goedemorgen! Ik wens je een prettige dag toe."
        elif normalized_prompt == "goedemiddag":
            return "Goedemiddag! Waar kan ik je mee helpen in de namiddag?"
        elif normalized_prompt == "goedenavond":
            return "Goedenavond! Fijne avond gewenst."
        elif normalized_prompt == "goedennacht":
            return "Goedennacht! Slaap lekker en tot morgen."
    
    # Fallback response for any matched trigger not explicitly handled
    return "Hoi! Ik heb je begroeting ontvangen. Waar kan ik je mee helpen?"