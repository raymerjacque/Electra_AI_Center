# ── Required metadata ───────────────────────────────────────────────────────
PLUGIN_NAME        = "Image Finder"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Scrape the web for images based on user request"
PLUGIN_AUTHOR      = "Electra"
PLUGIN_ENABLED     = True

# ── Router integration ──────────────────────────────────────────────────────
PLUGIN_TRIGGERS    = ["find images of", "search images for", "show me images of"]
PLUGIN_ROUTE_TOKEN = "IMAGE_FINDER"
PLUGIN_COMMANDS    = ["/image"]

# ── Required entry point ────────────────────────────────────────────────────
import re
import requests

def run(prompt: str, context: dict) -> str:
    """
    Called when a trigger phrase matches.
    Returns a response with image URLs or empty to fall through.
    """
    # Check if any trigger is at the start (case‑insensitive)
    trigger = None
    remaining = prompt
    for t in PLUGIN_TRIGGERS:
        if remaining.lower().startswith(t):
            trigger = t
            remaining = remaining[len(t):].strip()
            break
    if not trigger:
        return ""  # not our plugin

    query = remaining
    if not query:
        return "[Image Finder] Please provide a search term after the trigger."

    # Perform a simple image search using Google Images (no API key required)
    search_url = f"https://www.google.com/search?tbm=isch&q={requests.utils.quote(query)}"
    try:
        resp = requests.get(search_url, timeout=10, headers={
            "User-Agent": "Mozilla/5.0 (compatible; ImageFinder/1.0)"
        })
        resp.raise_for_status()
    except Exception as e:
        return f"[Image Finder] Search failed: {e}"

    # Extract image URLs from the HTML response
    # Look for typical image source patterns
    img_urls = re.findall(r'https?://[^"\']+\.(?:jpg|jpeg|png|gif|bmp|webp)', resp.text, re.IGNORECASE)
    img_urls = list(dict.fromkeys(img_urls))  # deduplicate while preserving order
    if not img_urls:
        return "[Image Finder] No images found for query."

    # Return the first few results formatted for the user
    preview = "\n".join([f"• {url}" for url in img_urls[:5]])
    return f"[Image Finder] Here are some images for \"{query}\":\n{preview}"

# ── Optional: called once at load time ─────────────────────────────────────
def setup(config: dict) -> bool:
    # No special config needed; placeholder for future API keys
    return True

# ── Optional: help text ─────────────────────────────────────────────────────
def get_help() -> str:
    return f"Image Finder v{PLUGIN_VERSION}: {PLUGIN_DESCRIPTION}. Triggers: {PLUGIN_TRIGGERS}"

# ── Optional: handle a slash command ────────────────────────────────────────
def handle_command(command: str, args: str) -> bool:
    """
    Handles "/image <query>" if the user prefers a slash command.
    Returns True if handled, False to pass through.
    """
    if command == "/image":
        if not args:
            print("[Image Finder] Usage: /image <search term>")
            return True
        # Re‑use the same logic as run() but with args as the prompt
        response = run(f"find images of {args}", {})
        # The router expects a string return; we just print it for demo
        print(response)
        return True
    return False