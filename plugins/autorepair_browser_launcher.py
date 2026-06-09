<think>We are given a capability gap: the user repeatedly asked for the terminal command to launch "brow6el" (likely a typo for "browser").
 We are to write a plugin that handles this type of request.

 Since the user is asking for a terminal command to launch a browser, we can create a ROUTER plugin that triggers on phrases like "terminal command to launch browser", "how to open browser in terminal", etc.

 However, note that the user's request was: "whats the terminal command to lauch brow6el"
 We can assume they meant "browser". But note the typo: "brow6el". We should handle common typos.

 We are on MakuluLinux (Ubuntu-based, Cinnamon desktop). The default browser might be Firefox, but we can also check for common browsers.

 Approach:
 1. We'll create a ROUTER plugin that triggers on phrases that ask for the terminal command to launch a browser.
 2. We'll try to determine the default browser or common browsers and provide the command accordingly.

 Steps in the plugin:
 - We can check for the existence of common browser commands (like firefox, chromium-browser, google-chrome, etc.) in the system.
 - Alternatively, we can check the default browser by looking at xdg-settings or the update-alternatives system.

 However, note that the plugin must be self-contained and not rely on external packages that might not be installed.

 We can use `subprocess` to run system commands to check for the default browser.

 But note: the plugin must not crash the host app. So we must handle errors gracefully.

 Let's design:

 PLUGIN_TRIGGERS: We'll use a list of phrases that might indicate the user wants to know the terminal command for the browser.

 We'll also consider the typo: "brow6el" -> we can include that in triggers? But note the user might have meant "browser".

 Alternatively, we can have a more general trigger: any request that includes "terminal command" and "browser" (with possible typos).

 However, the error says the user repeatedly requested this type of task. So we want to catch similar requests.

 Let's define triggers that are case-insensitive and allow for some variation.

 We can use:
   PLUGIN_TRIGGERS = [
        "terminal command to launch browser",
        "how to open browser in terminal",
        "what is the command to start browser",
        "browser terminal command",
        "launch browser from terminal",
        "brow6el terminal command",   # the exact typo from the user
        "browser command line"
    ]

 But note: the user might ask in a different way. We can also use a more flexible approach by checking for keywords in the prompt.

 However, the plugin system uses exact string matching? The specification says "trigger phrases match". It doesn't specify if it's exact or substring.

 Looking at the example: PLUGIN_TRIGGERS = ["ask groq", "use groq", "groq:"]

 It seems like it's looking for the exact trigger phrase in the prompt? Or maybe it's a list of prefixes? The example uses "groq:" which is a prefix.

 The specification doesn't clarify. But note: the example for AGENT uses triggers that are full phrases.

 Since we are writing a ROUTER plugin, we want to intercept when the user asks about the browser terminal command.

 We can set the trigger to be a list of strings that, if any of them is a substring of the prompt (case-insensitive?), then we route to this plugin.

 However, the specification says "trigger phrases match". It might be that the router checks if any of the trigger strings is a substring of the prompt (case-insensitive?).

 Let's assume it's case-insensitive substring matching.

 We'll define:

   PLUGIN_TRIGGERS = [
        "terminal command to launch browser",
        "how to open browser in terminal",
        "what is the command to start browser",
        "browser terminal command",
        "launch browser from terminal",
        "brow6el terminal command",
        "browser command line"
    ]

 But note: the user might say "browser" in a different way. We can also include "web browser".

 However, to avoid false positives, we want to be specific to the intent of getting the terminal command.

 Alternatively, we can use a more general trigger and then in the run function check the prompt more carefully.

 But the plugin system might not allow that because the trigger is what routes to the plugin.

 Since we are the plugin for this capability gap, we want to catch all similar requests.

 Let's think: the user asked "whats the terminal command to lauch brow6el". We can break it down:

   - "terminal command"
   - "lauch" (typo for launch)
   - "brow6el" (typo for browser)

 So we can have triggers that include "terminal command" and "browser" (with possible typos) but that might be too broad.

 Alternatively, we can have a single trigger: "terminal command" and then in the run function check if the prompt also contains something like "browser", "brow6el", "web", etc.

 But the specification says the router uses PLUGIN_TRIGGERS to match. So we must put in PLUGIN_TRIGGERS the strings that we want to match.

 Since we don't know the exact matching algorithm, let's be safe and include a variety of phrases that we think the user might use.

 We'll also include the exact phrase from the user: "whats the terminal command to lauch brow6el"

 But note: the user might use different wording. We can also include:

   "terminal command for browser"
   "command to open browser in terminal"

 However, we don't want to catch every mention of browser and terminal command. We want to catch when the user is asking for the command.

 Let's look at the error: the user repeatedly requested this type of task. So we want to catch the intent.

 We can define:

   PLUGIN_TRIGGERS = [
        "terminal command to launch browser",
        "terminal command to launch brow6el",
        "how to open browser in terminal",
        "what is the command to start browser",
        "browser terminal command",
        "launch browser from terminal",
        "browser command line",
        "terminal command for browser",
        "command to open browser in terminal"
    ]

 But note: the user might use "start" instead of "launch", or "run" instead of "launch".

 We can also include:

        "terminal command to start browser",
        "terminal command to run browser"

 However, we must be cautious not to make the triggers too broad.

 Alternatively, we can use a single trigger: "terminal command" and then in the run function, check if the prompt also contains a word that is like "browser" (with typo) or "web".

 But the specification doesn't say we can do that. The router will route based on the trigger. So if we set the trigger to "terminal command", then every time the user says "terminal command" we will route to this plugin, even if they are asking about something else.

 So we must make the trigger specific enough.

 Given the user's exact request, we can include:

   "terminal command to lauch brow6el"

 But note: the user might correct the typo in the future. So we should also include the correct spelling.

 Let's include:

   "terminal command to launch browser",
   "terminal command to launch brow6el"

 And also:

   "whats the terminal command to lauch brow6el"

 But note: the user might use "what's" or "what is". We can't cover every variation.

 Alternatively, we can use a more flexible approach by having a trigger that is a substring that is likely to appear in such requests.

 Since the user's request is very specific, we can also check in the run function for the intent and if it doesn't match, we can return a message that we don't understand and then the router might try other plugins.

 But the specification says the run function must return a non-empty string on success. We are expected to handle the request.

 Let's design the run function:

   We are going to check the prompt for keywords: "terminal command", and then a word that is like "browser" (with possible typos).

   We can use a simple method: if "terminal command" in prompt.lower() and any(word in prompt.lower() for word in ["browser", "brow6el", "web", "firefox", "chromium", "chrome"]):
        then we provide the answer.

   But note: the trigger already matched one of our trigger phrases, so we are already in the plugin. So we can assume the user is asking about the browser.

   However, to be safe, we can still check.

   Steps:

   1. Check if the prompt contains "terminal command" and a browser-related word. If not, we can return a generic message or even let the router try other plugins? But we are already in the plugin.

   2. We try to determine the default browser.

   How to determine the default browser on Ubuntu/MakuluLinux?

   We can check:

      xdg-settings get default-web-browser

   But xdg-settings might not be installed? It's part of xdg-utils, which is usually installed.

   Alternatively, we can check the update-alternatives for x-www-browser:

      update-alternatives --get-selections | grep x-www-browser

   But note: the user might not have set the default browser via update-alternatives.

   Another way: check the desktop environment's default. For Cinnamon, we can check:

      gsettings get org.cinnamon.default-applications.browser exec

   But gsettings might not be available in a terminal? It is, but we are in a plugin that runs in the terminal app.

   However, we are in a Python plugin and we can run these commands.

   But note: the plugin must not crash. So we try one method and if it fails, try another.

   We can try:

      Method 1: xdg-settings
      Method 2: update-alternatives
      Method 3: gsettings (for Cinnamon)
      Method 4: check for common browser commands in the PATH and pick the first one that exists.

   We'll write a function to get the default browser command.

   However, note: the user might have multiple browsers and want to know the command for a specific one? The request is general.

   We can return:

      "The default browser is <browser_name>. You can launch it from the terminal with: <command>"

   Or if we can't determine, we can list common browsers and their commands.

   Let's code:

   We'll try:

     1. xdg-settings get default-web-browser -> returns a desktop file name, e.g., firefox.desktop. Then we can map to the command? Not straightforward.

     2. update-alternatives: we can get the alternative for x-www-browser and then get the path.

     3. gsettings: for Cinnamon, we can get the exec string.

   Alternatively, we can check the desktop file in ~/.local/share/applications/mimeapps.list for the default browser.

   But this is getting complex.

   Since we are on MakuluLinux (Ubuntu-based) and the user is using Cinnamon, let's try:

      gsettings get org.cinnamon.default-applications.browser exec

   If that fails, try:

      xdg-settings get default-web-browser

   Then, if we get a desktop file, we can try to find the corresponding command by looking in /usr/share/applications and ~/.local/share/applications.

   But note: the desktop file might have an Exec key that we can parse.

   However, this is a lot of work and might be error-prone.

   Alternatively, we can just list the common browsers and their commands, and let the user choose.

   Given the simplicity of the request, maybe we can just say:

      "Common terminal commands for browsers on Ubuntu/MakuluLinux:

        Firefox: firefox
        Chromium: chromium-browser
        Google Chrome: google-chrome

      You can also set your default browser and then use xdg-open <url> to open a URL in the default browser."

   But the user asked for the command to launch the browser (presumably without a URL). So we can give the command to launch the browser.

   However, the user might want to know the command for the default browser.

   Let's try to get the default browser command by checking the update-alternatives for x-www-browser:

      update-alternatives --get-selections | grep x-www-browser

   This will show the current alternative for x-www-browser. Then we can get the path of that alternative.

   Example output:

      x-www-browser auto /usr/bin/firefox

   Then the command is the path without the arguments? Actually, the alternative is a symlink. We can read the symlink.

   But note: the alternative might be set to a script that launches the browser.

   Alternatively, we can just use the command that is set as the alternative.

   Steps:

     1. Run: update-alternatives --get-selections
     2. Parse the line for x-www-browser
     3. The third column is the path.

   But if the user doesn't have update-alternatives set for x-www-browser, we can try the other methods.

   Let's write a function that tries:

     a) update-alternatives for x-www-browser
     b) gsettings for Cinnamon
     c) xdg-settings for default-web-browser and then map to a command by looking at the desktop file.

   We'll do:

     try:
         # method a
         output = subprocess.check_output(["update-alternatives", "--get-selections"], text=True)
         for line in output.splitlines():
             if line.startswith("x-www-browser"):
                 parts = line.split()
                 if len(parts) >= 3:
                     command = parts[2]
                     # Check if the command exists and is executable?
                     if os.path.isfile(command) and os.access(command, os.X_OK):
                         return command
                     else:
                         # It might be a symlink, so we can try to resolve?
                         # But let's just return the command string and hope it's in PATH.
                         return command
     except:
         pass

     try:
         # method b: gsettings
         output = subprocess.check_output(["gsettings", "get", "org.cinnamon.default-applications.browser", "exec"], text=True)
         # The output might be something like: '/usr/bin/firefox %s'
         # We want the command without the arguments.
         command = output.strip().split()[0].strip("'")
         return command
     except:
         pass

     try:
         # method c: xdg-settings
         desktop_file = subprocess.check_output(["xdg-settings", "get", "default-web-browser"], text=True).strip()
         # desktop_file is something like "firefox.desktop"
         # Now we need to find the desktop file and parse the Exec key.
         # Look in /usr/share/applications and ~/.local/share/applications
         paths = ["/usr/share/applications", os.path.expanduser("~/.local/share/applications")]
         for path in paths:
             desktop_path = os.path.join(path, desktop_file)
             if os.path.isfile(desktop_path):
                 with open(desktop_path, 'r') as f:
                     for line in f:
                         if line.startswith("Exec="):
                             exec_line = line.strip().split('=')[1]
                             # The Exec line may have arguments like %u, %s, etc. We want the command.
                             command = exec_line.split()[0]
                             return command
     except:
         pass

     # If all else fails, return a list of common browsers and their commands.

   But note: the user might not have any of these. So we can return a message with common commands.

   However, the plugin must return a string. We can return:

      "I couldn't determine your default browser. Here are common browser commands on Ubuntu/MakuluLinux:

        Firefox: firefox
        Chromium: chromium-browser
        Google Chrome: google-chrome

      You can also use 'xdg-open <url>' to open a URL in your default browser."

   But the user asked for the command to launch the browser (without a URL). So we are giving the command to launch the browser.

   However, note that some browsers might require a URL? Actually, you can run `firefox` without a URL and it will open the homepage.

   So we are safe.

   Let's code accordingly.

   We'll write a helper function to get the default browser command.

   But note: the plugin must be self-contained and not rely on external packages. We are using only standard library.

   We'll use subprocess, os, and maybe re? We don't need re.

   Steps in run:

     if the prompt matches our intent (we already matched the trigger, but we can double-check):

        command = get_default_browser_command()

        if command:
            return f"The default browser command is: {command}"
        else:
            return "I couldn't determine your default browser. Common commands are: firefox, chromium-browser, google-chrome. You can also use 'xdg-open <url>' to open a URL in your default browser."

   But note: the user might have a browser that is not in the common list. We are only giving common ones.

   Alternatively, we can list the browsers that are installed? We can check the PATH for common browser commands.

   We can do:

        common_browsers = ["firefox", "chromium-browser", "google-chrome", "epiphany", "midori", "konqueror"]
        installed = [b for b in common_browsers if shutil.which(b)]
        if installed:
            return f"Installed browsers: {', '.join(installed)}. You can launch any of them by typing its name in the terminal."
        else:
            return "I couldn't find any common browser in your PATH. You might need to install a browser first."

   But note: the user might have a browser that is not in the common list. We can also check for any executable that has "browser" in the name? That might be too broad.

   Given the complexity, let's stick to:

        Try to get the default browser command by the methods above.

        If we get a command, return that.

        Else, check for common browsers in the PATH and list them.

        Else, return a message that we couldn't find any.

   We'll write:

        def get_default_browser_command():
            # try the three methods
            # if any returns a non-empty string, return it.
            # else, return None

        Then in run:

            command = get_default_browser_command()
            if command:
                return f"The default browser command is: {command}"
            else:
                # Check for common browsers in PATH
                common_browsers = ["firefox", "chromium-browser", "google-chrome", "epiphany", "midori", "konqueror"]
                installed = [b for b in common_browsers if shutil.which(b)]
                if installed:
                    return f"I couldn't determine your default browser, but these browsers are installed: {', '.join(installed)}. You can launch any by typing its name."
                else:
                    return "I couldn't find any common browser in your PATH. You might need to install a browser first."

   But note: the user might have a browser that is not in the common list and not the default. We are only checking the common ones.

   Alternatively, we can list all executables in the PATH that have "browser" in the name? That might be too many.

   Let's keep it simple.

   We are writing a plugin for a specific capability gap. The user asked for the terminal command to launch the browser.

   We are providing:

     1. The default browser command if we can determine it.
     2. Otherwise, a list of common browsers that are installed.

   This should cover most cases.

   Now, let's code the plugin.

   We must include the required metadata.

   We are writing a ROUTER plugin.

   We'll set:

      PLUGIN_NAME = "Browser Launcher Helper"
      PLUGIN_VERSION = "1.0.0"
      PLUGIN_DESCRIPTION = "Provides terminal command to launch the default web browser"
      PLUGIN_AUTHOR = "Electra Plugin Forge"
      PLUGIN_ENABLED = True
      PLUGIN_TYPE = "ROUTER"
      PLUGIN_TRIGGERS = [ ... list of triggers ... ]
      PLUGIN_ROUTE_TOKEN = "BROWSER_LAUNCHER"
      PLUGIN_COMMANDS = ["/browser"]

   We'll also declare any dependencies? We are using only standard library, so PLUGIN_REQUIRES = [].

   Let's code.

   Note: We must use context["print_fn"] for progressive output? The run function returns a string. We can use print_fn to show progress, but we are doing a quick check.

   We can do:

        context["print_fn"]("Checking for default browser...")

   But note: the run function must return a string. We can use print_fn to show intermediate steps and then return the final string.

   However, the user might not want to see the intermediate steps. We can just return the final string.

   Let's not use print_fn unless we are doing a long operation. This is quick.

   We'll just return the string.

   But note: the specification says we can use print_fn to show progressive output. We don't need to.

   We'll write the helper function and then return the result.

   Let's code.

   Important: We must handle exceptions in the helper function and in the run function.

   We'll wrap the entire run function in a try/except and return an error message if something goes wrong.

   But note: the plugin must not crash the host app. So we must catch all exceptions.

   We'll do:

        try:
            ... our code ...
        except Exception as e:
            return f"Error in Browser Launcher plugin: {str(e)}"

   However, we are already catching exceptions in the helper function? We'll catch in the helper and return None, and then in run we handle the None.

   Let's code accordingly.

   We are going to write:

        import subprocess
        import os
        import shutil

        def get_default_browser_command():
            # method a: update-alternatives
            try:
                output = subprocess.check_output(["update-alternatives", "--get-selections"], text=True, stderr=subprocess.DEVNULL)
                for line in output.splitlines():
                    if line.startswith("x-www-browser"):
                        parts = line.split()
                        if len(parts) >= 3:
                            command = parts[2]
                            # Check if the command is in the PATH? We can use shutil.which
                            if shutil.which(command):
                                return command
                            else:
                                # Maybe it's a full path? We can return it anyway and let the user try.
                                return command
            except:
                pass

            # method b: gsettings for Cinnamon
            try:
                output = subprocess.check_output(["gsettings", "get", "org.cinnamon.default-applications.browser", "exec"], text=True, stderr=subprocess.DEVNULL)
                # Example output: '/usr/bin/firefox %s'
                command = output.strip().split()[0].strip("'\"")
                if shutil.which(command):
                    return command
                else:
                    return command  # even if not in PATH, it might be a full path
            except:
                pass

            # method c: xdg-settings and desktop file
            try:
                desktop_file = subprocess.check_output(["xdg-settings", "get", "default-web-browser"], text=True, stderr=subprocess.DEVNULL).strip()
                if desktop_file.endswith('.desktop'):
                    paths = ["/usr/share/applications", os.path.expanduser("~/.local/share/applications")]
                    for path in paths:
                        desktop_path = os.path.join(path, desktop_file)
                        if os.path.isfile(desktop_path):
                            with open(desktop_path, 'r') as f:
                                for line in f:
                                    if line.startswith("Exec="):
                                        exec_line = line.strip().split('=', 1)[1]
                                        command = exec_line.split()[0]
                                        # Remove any arguments like %u, %s, etc.
                                        # We just want the command.
                                        if shutil.which(command):
                                            return command
                                        else:
                                            return command
            except:
                pass

            return None

        Then in run:

            try:
                # Check if the prompt is about browser terminal command? We already matched the trigger, but let's be safe.
                prompt_lower = prompt.lower()
                if "terminal command" in prompt_lower and any(word in prompt_lower for word in ["browser", "brow6el", "web", "firefox", "chromium", "chrome"]):
                    command = get_default_browser_command()
                    if command:
                        return f"The default browser command is: {command}"
                    else:
                        common_browsers = ["firefox", "chromium-browser", "google-chrome", "epiphany", "midori", "konqueror"]
                        installed = [b for b in common_browsers if shutil.which(b)]
                        if installed:
                            return f"I couldn't determine your default browser, but these browsers are installed: {', '.join(installed)}. You can launch any by typing its name."
                        else:
                            return "I couldn't find any common browser in your PATH. You might need to install a browser first."
                else:
                    # The trigger matched but the prompt doesn't seem to be about browser? Then we return None? But we must return a string.
                    # We can return a message that we don't understand, but then the router might try other plugins? 
                    # Since we are a ROUTER plugin and we matched the trigger, we are expected to handle it.
                    # So we should handle it. But if the prompt is not about browser, maybe we should not have matched?
                    # We can adjust the triggers to be more specific. But for now, we'll return a generic message.
                    return "I can help with terminal commands for launching a browser. Please ask about the browser terminal command."
            except Exception as e:
                return f"Error in Browser Launcher plugin: {str(e)}"

   However, note: the trigger already matched, so we are in the plugin. We must return a string.

   We can also adjust the triggers to be more specific so that we don't get false positives.

   But the user's request was very specific, so we are safe.

   Let's write the plugin accordingly.

   We'll also note that the user might be on a different desktop environment. We are trying Cinnamon first because MakuluLinux uses Cinnamon.

   But if the user is on a different DE, gsettings might not work. We are catching exceptions.

   Let's code the plugin.

   We must also note: the plugin file will be named: autorepair_browser_launcher.py

   We are using PLUGIN_ROUTE_TOKEN = "BROWSER_LAUNCHER", so the file will be: autorepair_browser_launcher.py

   Let's write the code.</think>
"""
Electra AI Plugin - Browser Launcher Helper
Provides terminal commands to launch web browsers on MakuluLinux (Ubuntu/Cinnamon)
"""

import subprocess
import os
import shutil

PLUGIN_NAME = "Browser Launcher Helper"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Provides terminal commands to launch web browsers on MakuluLinux"
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = [
    "terminal command to launch browser",
    "how to open browser in terminal",
    "what is the command to start browser",
    "browser terminal command",
    "launch browser from terminal",
    "brow6el terminal command",
    "browser command line",
    "terminal command for browser",
    "command to open browser in terminal",
    "start browser from command line"
]
PLUGIN_ROUTE_TOKEN = "BROWSER_LAUNCHER"
PLUGIN_COMMANDS = ["/browser"]
PLUGIN_REQUIRES = []

def get_installed_browsers():
    """Check which browsers are installed on the system"""
    common_browsers = {
        "firefox": "Firefox",
        "chromium-browser": "Chromium",
        "google-chrome": "Google Chrome",
        "chromium": "Chromium (snap)",
        "microsoft-edge": "Microsoft Edge",
        "brave-browser": "Brave",
        "vivaldi": "Vivaldi",
        "epiphany": "Epiphany (GNOME Web)",
        "midori": "Midori",
        "falkon": "Falkon",
        "konqueror": "Konqueror"
    }
    
    installed = {}
    for cmd, name in common_browsers.items():
        if shutil.which(cmd):
            installed[cmd] = name
    
    return installed

def get_default_browser():
    """Try to determine the system's default browser"""
    try:
        # Method 1: Check xdg-settings (most reliable)
        result = subprocess.run(
            ["xdg-settings", "get", "default-web-browser"],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0 and result.stdout.strip():
            desktop_file = result.stdout.strip()
            # Extract browser name from desktop file (e.g., firefox.desktop -> firefox)
            browser_name = desktop_file.replace('.desktop', '').replace('-desktop', '')
            return browser_name
    except:
        pass
    
    try:
        # Method 2: Check update-alternatives for x-www-browser
        result = subprocess.run(
            ["update-alternatives", "--get-selections"],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0:
            for line in result.stdout.splitlines():
                if "x-www-browser" in line:
                    parts = line.split()
                    if len(parts) >= 3:
                        return parts[2]  # The command path
    except:
        pass
    
    try:
        # Method 3: Check Cinnamon-specific settings (MakuluLinux uses Cinnamon)
        result = subprocess.run(
            ["gsettings", "get", "org.cinnamon.default-applications.browser", "exec"],
            capture_output=True,
            text=True,
            timeout=2
        )
        if result.returncode == 0 and result.stdout.strip():
            # Output looks like: '/usr/bin/firefox %s'
            exec_cmd = result.stdout.strip().strip("'\"")
            # Extract just the command part
            return exec_cmd.split()[0].replace('/usr/bin/', '')
    except:
        pass
    
    return None

def run(prompt: str, context: dict) -> str:
    """
    Handle browser terminal command requests
    """
    try:
        prompt_lower = prompt.lower()
        
        # Verify this is actually about browser commands
        browser_keywords = ["browser", "brow6el", "web browser", "internet", "firefox", "chrome", "chromium"]
        terminal_keywords = ["terminal", "command", "launch", "start", "open", "run"]
        
        has_browser = any(keyword in prompt_lower for keyword in browser_keywords)
        has_terminal = any(keyword in prompt_lower for keyword in terminal_keywords)
        
        if not (has_browser and has_terminal):
            return "I can help with terminal commands for launching web browsers. Please ask about browser terminal commands specifically."
        
        installed_browsers = get_installed_browsers()
        default_browser = get_default_browser()
        
        if not installed_browsers:
            return "No common web browsers were found installed on your system. You may need to install one first using: sudo apt install firefox (or chromium-browser, google-chrome, etc.)"
        
        response_lines = []
        
        if default_browser and default_browser in installed_browsers:
            response_lines.append(f"Your default browser is {installed_browsers[default_browser]}.")
            response_lines.append(f"Terminal command: {default_browser}")
            response_lines.append("")
        
        response_lines.append("All installed browsers and their terminal commands:")
        for cmd, name in installed_browsers.items():
            response_lines.append(f"  {name:25} → {cmd}")
        
        response_lines.append("")
        response_lines.append("Tips:")
        response_lines.append("  • Add '&' at the end to run in background: firefox &")
        response_lines.append("  • Open specific URL: firefox https://example.com")
        response_lines.append("  • Use xdg-open for default browser: xdg-open https://example.com")
        
        return "\n".join(response_lines)
        
    except Exception as e:
        return f"Error retrieving browser information: {str(e)}\n\nCommon commands you can try directly:\n  firefox\n  chromium-browser\n  google-chrome"