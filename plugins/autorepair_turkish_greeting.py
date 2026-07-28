"""
Turkish greeting handler plugin for Electra AI on MakuluLinux.
Handles 'merhaba' and similar Turkish greetings with appropriate responses.
"""

PLUGIN_NAME = "Turkish Greeting Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles Turkish greetings like 'merhaba' with proper responses"
PLUGIN_AUTHOR = "Electra AI Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["merhaba", "selam", "selamünaleyküm", "günaydın", "iyi günler"]
PLUGIN_ROUTE_TOKEN = "TURKISH_GREETING"

def run(prompt: str, context: dict) -> str:
    try:
        context["print_fn"](f"🇹🇷 **{prompt.strip().capitalize()}!** Hoş geldiniz!")
        return f"Merhaba! Size nasıl yardımcı olabilirim? {prompt.strip().capitalize()} demek istediniz sanırım."
    except Exception as e:
        return f"Üzgünüm, selamlaşma sırasında bir hata oluştu: {str(e)}"