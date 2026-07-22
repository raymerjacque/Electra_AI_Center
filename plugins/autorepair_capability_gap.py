PLUGIN_NAME        = "Capability Gap Handler"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Handles capability gaps with a simple response."
PLUGIN_AUTHOR      = "AI Assistant"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "AGENT"
PLUGIN_ROUTE_TOKEN = "CAPABILITY_GAP"
PLUGIN_COMMANDS    = ["/capability_gap"]
PLUGIN_REQUIRES    = []  # No external dependencies needed

def run(prompt: str, context: dict) -> str:
    """
    Handles requests indicating a capability gap.  Provides a simple,
    consistent response to avoid repeated errors.
    """
    return "[Capability Gap Handler] I understand. I am currently unable to fulfill that request.  I will continue to learn and improve."