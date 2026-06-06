"""
Electra AI Plugin: Hello Responder
Handles basic greetings and provides a friendly welcome message.
"""

import os
import datetime

PLUGIN_NAME        = "Hello Responder"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Handles basic greetings and welcomes the user warmly."
PLUGIN_AUTHOR      = "Electra Plugin Forge"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "ROUTER"

PLUGIN_TRIGGERS    = [
    "hello", "hi", "hey", "greetings", "howdy", 
    "good morning", "good afternoon", "good evening", 
    "sup", "what's up", "yo"
]
PLUGIN_ROUTE_TOKEN = "HELLO_RESPONDER"
PLUGIN_COMMANDS    = ["/hello", "/hi"]

def run(prompt: str, context: dict) -> str:
    try:
        print_fn = context.get("print_fn", print)
        user_home = context.get("user_home", os.path.expanduser("~"))
        username = os.path.basename(user_home) if user_home else "User"
        
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            time_greeting = "Good morning"
        elif 12 <= hour < 18:
            time_greeting = "Good afternoon"
        elif 18 <= hour < 22:
            time_greeting = "Good evening"
        else:
            time_greeting = "Hello"
            
        response = f"{time_greeting}, {username}! I'm Electra AI, ready to assist you on MakuluLinux. What can I help you with today?"
        print_fn(response)
        return response
        
    except Exception:
        fallback = "Hello! I'm Electra AI. How can I assist you today?"
        try:
            context.get("print_fn", print)(fallback)
        except Exception:
            pass
        return fallback