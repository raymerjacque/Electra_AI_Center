"""
Autorepair plugin: handles 'hey' greeting requests.
"""
import os

PLUGIN_NAME = "Hey Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Responds to 'hey' greeting with a friendly acknowledgement"
PLUGIN_AUTHOR = "Electra AI"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []

PLUGIN_TRIGGERS = ["hey"]
PLUGIN_ROUTE_TOKEN = "HEY"
PLUGIN_COMMANDS = ["/hey"]


def run(prompt: str, context: dict) -> str:
    """Handle 'hey' greeting requests."""
    try:
        context["print_fn"]("Hey there! I'm here and ready to help.")
        return "Hey! How can I assist you today?"
    except Exception as e:
        context["print_fn"](f"Error in hey handler: {e}")
        return "Hey! (Something went wrong, but I'm still here.)"