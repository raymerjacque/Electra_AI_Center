"""
Plugin to handle greetings and casual interactions like 'ciao' for MakuluLinux Electra AI.
"""

PLUGIN_NAME = "Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles casual greetings and simple interactions like 'ciao'"
PLUGIN_AUTHOR = "System Repair Bot"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["ciao", "hello", "hi", "hey", "greetings", "salut"]
PLUGIN_ROUTE_TOKEN = "GREETING"

def run(prompt: str, context: dict) -> str:
    try:
        user_home = context.get("user_home", os.path.expanduser("~"))
        username = os.path.basename(user_home)

        responses = [
            f"Ciao {username}! How can I assist you today?",
            f"Hello {username}! What's on your mind?",
            f"Hey {username}! How can I help?",
            "Greetings! How can I assist you right now?",
            f"Salut {username}! What do you need help with?"
        ]

        import random
        return random.choice(responses)
    except Exception as e:
        return f"[Greeting Handler] Error: {str(e)}"