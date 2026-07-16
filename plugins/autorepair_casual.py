import os
import random
import datetime

PLUGIN_NAME = "Casual Chat Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles casual greetings and status checks like 'whats up'"
PLUGIN_AUTHOR = "Electra Auto-Repair"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []
PLUGIN_TRIGGERS = ["whats up", "what's up", "sup", "wassup", "how goes it", "what is happening"]
PLUGIN_ROUTE_TOKEN = "CASUAL"
PLUGIN_COMMANDS = ["/status", "/greet"]

def run(prompt: str, context: dict) -> str:
    try:
        # Normalize prompt for checking
        p_clean = prompt.strip().lower()
        
        # Gather system context for a dynamic response
        hostname = os.uname().nodename
        uptime = datetime.datetime.now().strftime("%H:%M")
        
        responses = [
            f"Not much! Just running on {hostname}. Time is {uptime}. How can I help?",
            f"All systems operational on {hostname}. I'm ready for your next command.",
            f"Chilling in the Cinnamon desktop environment. What do you need?",
            f"Electra is online and listening. The terminal is yours.",
            f"Just waiting for input. Uptime is looking good!"
        ]
        
        # Select a random response
        reply = random.choice(responses)
        
        # Use the print function for immediate feedback if available
        print_fn = context.get("print_fn")
        if print_fn_fn:
            print_fn_fn(f"**Electra:** {reply}")
        
        return reply

    except Exception as e:
        return f"[Casual Chat] Error: {str(e)}"