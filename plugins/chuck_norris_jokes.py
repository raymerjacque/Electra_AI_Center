PLUGIN_NAME = 'Chuck Norris Jokes'
PLUGIN_VERSION = '1.0.0'
PLUGIN_DESCRIPTION = 'Fetch random Chuck Norris jokes from the API.'
PLUGIN_AUTHOR = 'Electra Plugin'
PLUGIN_ENABLED = True

PLUGIN_TRIGGERS = ['chuck norris', 'chuck norris joke', 'cnj']
PLUGIN_ROUTE_TOKEN = 'CHUCK_NORRIS_JOKE'
PLUGIN_COMMANDS = ['/cnj']

import requests

def setup(config: dict) -> bool:
    return True

def run(prompt: str, context: dict) -> str:
    # Check if any trigger is present in the prompt
    for trigger in PLUGIN_TRIGGERS:
        if trigger.lower() in prompt.lower():
            # Fetch a random joke
            try:
                resp = requests.get('https://api.chucknorris.io/jokes/random', timeout=10)
                resp.raise_for_status()
                joke = resp.json().get('value', {}).get('text', 'No joke found.')
                return joke
            except Exception as e:
                return '[Chuck Norris Jokes] Error fetching joke: ' + str(e)
    # If no trigger matched, fall through (return empty string)
    return ''

def handle_command(command: str, args: str) -> bool:
    if command == '/cnj':
        if not args:
            print('[Chuck Norris] Usage: /cnj (will fetch a joke automatically)')
            return True
        # Fetch and print a joke
        try:
            resp = requests.get('https://api.chucknorris.io/jokes/random', timeout=10)
            resp.raise_for_status()
            joke = resp.json().get('value', {}).get('text', 'No joke found.')
            print(f'[Chuck Norris] {joke}')
        except Exception as e:
            print(f'[Chuck Norris] Error: {e}')
        return True
    return False

def get_help() -> str:
    return f'{PLUGIN_NAME} v{PLUGIN_VERSION}: {PLUGIN_DESCRIPTION}'