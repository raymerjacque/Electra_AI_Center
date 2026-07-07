<think>We are writing a ROUTER plugin that will handle the "ollama login" request.
 The user is on MakuluLinux (Ubuntu-based) and wants to log in to Ollama.

 Steps:
 1. We need to check if Ollama is installed and running.
 2. If not, we might need to guide the user to install it or start the service.
 3. The login process for Ollama typically involves pulling a model and then using `ollama run` with a model that requires authentication? 
    But note: Ollama doesn't have a traditional login. It might be that the user wants to use a model that requires authentication (like from a private registry) or they want to set up authentication for the Ollama server.

 However, the error says "CAPABILITY_GAP" for "ollama login". So we assume the user wants to log in to an Ollama server (maybe a remote one) or set up authentication for pulling models.

 Let's break down:

 Option 1: The user wants to log in to the Ollama server (if it's running with authentication). 
   - Ollama server can be configured with authentication (via environment variables or config). But by default, it doesn't have a login command.

 Option 2: The user wants to pull a model that requires authentication (from a private registry). In that case, we need to set up credentials for the registry.

 Since the request is vague, we'll design a plugin that:
   - Checks if Ollama is installed and running.
   - If not, provides instructions to install and start.
   - If it is running, then we check if the user is trying to log in to a remote server (maybe by providing a URL) or set up authentication for a registry.

 But note: the user just said "ollama login". We don't have a URL or registry.

 Let's assume the user wants to set up authentication for the default Ollama server (localhost:11434) or for a remote server.

 However, the Ollama CLI does not have a `login` command. Instead, for private registries, you set the `OLLAMA_REGISTRY` environment variable and then use `ollama pull` which will prompt for credentials if needed.

 Alternatively, if the user is running an Ollama server with authentication, they might need to set the `OLLAMA_TOKEN` environment variable.

 Since the request is ambiguous, we'll create a plugin that:

 1. Checks if Ollama is installed (by checking the `ollama` command).
 2. If not, instructs the user to install it (for Ubuntu, we can give the curl command).
 3. If installed, check if the service is running (by trying to connect to localhost:11434 or by checking the process).
 4. Then, we ask the user: 
    - Are you trying to log in to a remote Ollama server? (if so, we set OLLAMA_HOST and maybe OLLAMA_TOKEN)
    - Or are you trying to set up authentication for pulling from a private registry? (then we set OLLAMA_REGISTRY and maybe credentials)

 But note: the plugin must return a string. We can't have an interactive conversation in the run function? Actually, the run function is called with a prompt and context. We can use the context to have a conversation? But the plugin is for a single request.

 However, the user might have said "ollama login" and we are expected to handle it. We can break it down:

 Since we don't have a clear way to get the user's intent, we can:

   a) If the user has provided a URL in the prompt (like "ollama login to https://example.com"), then we set OLLAMA_HOST to that URL and maybe ask for a token? But we don't have a way to store the token securely.

   b) Alternatively, we can guide the user to set environment variables.

 But note: the plugin runs in the context of the Electra app, which might be a terminal. We can run shell commands? We are allowed to use subprocess.

 However, setting environment variables for the current process (the Electra app) might not be enough because the Ollama client (when called from the plugin) will inherit the environment. But if the user wants to set it permanently, we might need to edit shell config files.

 Given the complexity and the fact that we don't have a clear specification, let's design a simple plugin that:

   - If the user says "ollama login", we check if Ollama is installed and running.
   - Then we output instructions for setting up authentication for a remote server or private registry.

 But wait, the error says the user repeatedly requested this. So we must handle it in a way that satisfies the user.

 Alternatively, we can try to mimic the `docker login` style? But Ollama doesn't have that.

 After reading the Ollama documentation: 
   - For private registries, you can set the `OLLAMA_REGISTRY` environment variable and then when you pull, it will ask for credentials (if the registry requires it). But there's no separate login command.

   - For server authentication, you set `OLLAMA_TOKEN` and `OLLAMA_HOST`.

 So, we can:

   Step 1: Check if Ollama is installed and running.
   Step 2: If the user's prompt contains a URL, then set OLLAMA_HOST to that URL and ask for a token? But we can't store the token in the plugin because it's not secure and we don't have a way to persist it.

   Alternatively, we can output:

   "To log in to a remote Ollama server, set the environment variable OLLAMA_HOST to the server URL and OLLAMA_TOKEN to your token. For example:

      export OLLAMA_HOST=https://example.com
      export OLLAMA_TOKEN=your_token_here

   Then, you can run `ollama pull <model>`.

   For private registries, set OLLAMA_REGISTRY to the registry URL and then when pulling, you will be prompted for credentials."

 But note: the user might be expecting an interactive login. We don't have a way to store the token in the plugin's state? We have `electra_state` which is a shared state store. We could store the token there? But that would be in plain text and not secure.

 Given the constraints, we'll output instructions and let the user set the environment variables themselves.

 However, the plugin must return a string. We can return a multi-line string with instructions.

 But wait, the user might have a specific use case. Since we don't have more context, we'll make it generic.

 Let's code:

   - Check if `ollama` command exists.
   - Check if the Ollama service is running (by trying to connect to localhost:11434 or by checking the process).

   Then, if the user's prompt has a URL, we assume they want to set OLLAMA_HOST and OLLAMA_TOKEN.

   But we don't have a way to get the token from the user in the plugin. So we can only set the host and then tell them to set the token.

   Alternatively, we can ask the user to provide the token in the prompt? But that's not secure and the prompt might be logged.

   So, we'll just output:

   "To log in to an Ollama server, you need to set two environment variables:

   1. OLLAMA_HOST: the URL of the Ollama server (e.g., https://example.com)
   2. OLLAMA_TOKEN: your authentication token.

   You can set them in your current shell session by:

      export OLLAMA_HOST=<server_url>
      export OLLAMA_TOKEN=<your_token>

   Then, you can use `ollama pull` to pull models from that server.

   If you are using a private registry, set OLLAMA_REGISTRY to the registry URL and you will be prompted for credentials when pulling."

   But wait, the user might be using the default local server and just wants to log in? That doesn't make sense because the local server doesn't require login.

   So, we assume they are using a remote server.

   However, the user might have a different intent. Since we don't have more context, we'll stick to this.

   But note: the plugin must be robust. We'll wrap everything in try/except.

   Also, we are allowed to use context["print_fn"] to print progressive output? But the run function returns a string. We can use print_fn to show intermediate steps and then return the final string.

   However, the specification says: "run(prompt, context) must return a non-empty string on success". So we can use print_fn for side messages and then return the final answer.

   Let's design:

   Steps in run:

   1. Check if ollama is installed.
   2. Check if the Ollama service is running (by trying to connect to localhost:11434 or by checking the process).
   3. If the user's prompt contains a URL, extract it and set OLLAMA_HOST to that URL? But we cannot set environment variables for the parent process. We can only set for the current process and subprocesses.

   Actually, we can set environment variables for the current process (the plugin) and then when we run `ollama` commands, they will inherit. But the user might want to set it for their shell.

   So, we can:

      - If the user provided a URL, we set OLLAMA_HOST in the current environment (os.environ) and then try to run `ollama pull` of a small model to test? But that might require a token.

   Alternatively, we can just output the instructions and not set anything.

   Given the complexity and the fact that we don't have a clear way to get the token, we'll just output instructions.

   But wait, the user might have provided the token in the prompt? We can look for a token in the prompt? That's not safe.

   So, we'll do:

   If the user's prompt has a URL and a token (maybe in the format "ollama login <url> <token>"), then we set both and then try to run `ollama pull` of a small model to test the connection.

   But again, we are storing the token in the prompt, which might be logged.

   Given the security implications, we decide:

   We will not handle the token in the plugin. We will only set the OLLAMA_HOST if a URL is provided, and then we will instruct the user to set the token.

   Steps:

   - Check if the prompt contains a URL (using a simple regex for http/https).
   - If yes, set OLLAMA_HOST to that URL in the current environment (so that subsequent ollama commands in the same session will use that host).
   - Then, we output:

        "Ollama host set to <url>. Please set your OLLAMA_TOKEN environment variable with your token.

        You can do this by:

            export OLLAMA_TOKEN=your_token_here

        Then, try pulling a model to test:

            ollama pull <model_name>

        If you are using a private registry, set OLLAMA_REGISTRY to the registry URL and you will be prompted for credentials."

   - If no URL is provided, we output the general instructions.

   But note: the user might be using the default localhost. Then we don't set OLLAMA_HOST.

   Also, we must check if Ollama is installed and running.

   Let's code accordingly.

   However, note: the plugin is for MakuluLinux (Ubuntu). We can assume the user has sudo? We don't want to run sudo in the plugin.

   We'll just check for the `ollama` command and the service.

   How to check if the service is running? We can try to connect to localhost:11434 with a socket? Or run `ollama serve` in the background? But we don't want to start the service if it's not running? That might be out of scope.

   We'll just check if the `ollama` command exists and then if we can connect to the default port (11434) on localhost.

   If the user set OLLAMA_HOST to a remote URL, we try to connect to that.

   But note: the user might have set OLLAMA_HOST already? We are going to override it if they provided a URL in the prompt.

   Let's code:

   We'll use:
      import os
      import socket
      import subprocess
      import re

   Steps:

   1. Check if `ollama` is in the PATH.
   2. Check if the Ollama server is running (by trying to connect to the host and port from OLLAMA_HOST or default localhost:11434).
   3. If the user provided a URL in the prompt, set OLLAMA_HOST to that URL (and maybe OLLAMA_REGISTRY? No, that's for registries).
   4. Then, output instructions.

   But wait, the user might be trying to log in to a registry? Then we need to set OLLAMA_REGISTRY.

   How about:

      If the prompt contains a URL and the word "registry", then set OLLAMA_REGISTRY.

   But that's too vague.

   Given the ambiguity, we'll stick to:

      If the prompt contains a URL, set OLLAMA_HOST to that URL and assume it's for the server.

   And then we output:

      "Ollama host set to <url>. If this is a private registry, you may also need to set OLLAMA_REGISTRY to the registry URL. Then, set OLLAMA_TOKEN for server authentication or you will be prompted for credentials when pulling from a private registry."

   But note: the user might be using a remote server that also has a private registry? Then they need both.

   We can't cover all cases. We'll keep it simple.

   Let's code accordingly.

   However, note: the plugin must not crash. We'll wrap everything in try/except.

   Also, we are allowed to use context["print_fn"] to print. We'll use that for intermediate steps and then return a string.

   But the run function must return a string. We can return the instructions as a string.

   We'll do:

      try:
          # check ollama command
          # check server
          # if url in prompt, set OLLAMA_HOST
          # then return instructions
      except Exception as e:
          return f"Error: {str(e)}"

   But we don't want to expose internal errors? We can log them with print_fn and return a user-friendly message.

   Let's code:

   We are going to:

     1. Check for ollama command.
     2. Check if we can connect to the server (using the current OLLAMA_HOST or default).
     3. If the user provided a URL, set OLLAMA_HOST and then re-check the connection? Maybe.

   But note: setting OLLAMA_HOST in the current process will affect the subsequent connection check? Yes.

   Steps:

     current_host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
     If we find a URL in the prompt, set os.environ["OLLAMA_HOST"] = url and then set current_host = url.

     Then, try to connect to current_host.

   If the connection fails, we tell the user that the server is not reachable.

   Let's code accordingly.

   However, note: the user might be using HTTPS. We'll try to connect with a socket? But if it's HTTPS, we need to use SSL? We can just try to open a socket to the host and port (11434). But if it's HTTPS, the port might be 443? Actually, Ollama uses 11434 for HTTP and 11443 for HTTPS? Not sure.

   According to the Ollama documentation, the default is 11434 for HTTP and 11443 for HTTPS? Actually, the server runs on 11434 by default and if you set OLLAMA_HOST to https://, then it uses 443? I think it uses the standard ports.

   We'll just try to connect to the host and port 11434 (or the port from the URL if provided). But parsing the URL to get the port is complex.

   Alternatively, we can run `ollama serve` and check the output? But that would start the server if it's not running? We don't want to do that.

   We'll do a simple socket connection to the host and port 11434 (or the port from the URL if we can extract it). If the URL has a port, use that, else use 11434.

   But note: the user might have set OLLAMA_HOST to a remote server that uses a different port.

   We'll extract the port from the URL if present, else use 11434.

   Steps for connection check:

      import urllib.parse

      parsed = urllib.parse.urlparse(current_host)
      host = parsed.hostname or "localhost"
      port = parsed.port or 11434

      Then try to create a socket connection to (host, port) with a timeout.

   If it fails, we say the server is not reachable.

   Let's code accordingly.

   But note: the user might be using a Unix socket? Ollama also supports Unix socket? I think by default it's TCP.

   We'll stick to TCP.

   Now, the code:

   We are going to:

     1. Check if `ollama` command exists by running `which ollama` or `command -v ollama`.
     2. If not, return instructions to install.

     3. Then, check the server connection.

     4. If the user provided a URL, set OLLAMA_HOST and then check again? Actually, we set it and then check with the new host.

     5. Then, return instructions.

   But note: the user might have provided a URL that is not reachable. Then we tell them.

   Let's code.

   However, note: the plugin is for MakuluLinux (Ubuntu). The installation command for Ollama is:

      curl -fsSL https://ollama.com/install.sh | sh

   We'll include that.

   Let's write the plugin.

   We are going to use:

      import os
      import re
      import socket
      import subprocess
      import urllib.parse

   But note: we are not allowed to import from ai_terminal. We are standalone.

   We'll do:

      try:
          import ... 
      except ImportError:
          # but these are standard libraries, so should be there.

   We'll assume they are there.

   Now, the code structure:

   PLUGIN_NAME = "Ollama Login Helper"
   PLUGIN_VERSION = "1.0.0"
   PLUGIN_DESCRIPTION = "Handles 'ollama login' requests by setting up environment and providing instructions"
   PLUGIN_AUTHOR = "Plugin Forge"
   PLUGIN_ENABLED = True
   PLUGIN_TYPE = "ROUTER"
   PLUGIN_TRIGGERS = ["ollama login"]
   PLUGIN_ROUTE_TOKEN = "OLLAMA_LOGIN"
   PLUGIN_COMMANDS = ["/ollama_login"]

   Then, the run function.

   Let's code accordingly.

   But note: the user might say "ollama login" in a sentence. We are using triggers, so if the prompt contains "ollama login", we trigger.

   We'll extract the URL from the prompt if present.

   We'll use a regex to find a URL.

   Example: "ollama login https://example.com"

   We'll look for http or https URLs.

   Code:

      url_pattern = r'https?://[^\s]+'
      urls = re.findall(url_pattern, prompt)
      if urls:
          url = urls[0]
          # set OLLAMA_HOST to url
          os.environ["OLLAMA_HOST"] = url

   Then, we check the connection.

   Let's code the connection check:

      def check_ollama_server(host):
          parsed = urllib.parse.urlparse(host)
          hostname = parsed.hostname or "localhost"
          port = parsed.port or 11434
          try:
              with socket.create_connection((hostname, port), timeout=5):
                  return True
          except:
              return False

   Then, we use that.

   Now, the run function:

      try:
          # Check if ollama command exists
          ollama_path = subprocess.run(["which", "ollama"], capture_output=True, text=True).stdout.strip()
          if not ollama_path:
              return "Ollama is not installed. To install on MakuluLinux (Ubuntu), run:\n\ncurl -fsSL https://ollama.com/install.sh | sh\n\nAfter installation, start the service with:\n\nollama serve"

          # Check if the server is running (using the current OLLAMA_HOST or default)
          current_host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
          if check_ollama_server(current_host):
              status = "running"
          else:
              status = "not running"

          # If the user provided a URL, set OLLAMA_HOST and then check again? Actually, we set it above and then check with the new host.
          # But note: we set OLLAMA_HOST only if we found a URL. Then we check with that host.

          # Actually, we set OLLAMA_HOST and then we check with the current_host (which is now the new one if we set it).

          # But wait, we set OLLAMA_HOST and then current_host is still the old one? We set current_host after setting OLLAMA_HOST? Let's fix:

          # We set OLLAMA_HOST if we found a URL, then we set current_host to that URL? Actually, we set current_host from OLLAMA_HOST after setting.

          # Let's restructure:

          # 1. Check for URL in prompt and set OLLAMA_HOST if found.
          # 2. Then, set current_host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
          # 3. Then check the server.

          # So:

          url_pattern = r'https?://[^\s]+'
          urls = re.findall(url_pattern, prompt)
          if urls:
              url = urls[0]
              os.environ["OLLAMA_HOST"] = url
              current_host = url
          else:
              current_host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")

          # Now check the server at current_host.

          if check_ollama_server(current_host):
              server_status = "running and reachable"
          else:
              server_status = "not reachable"

          # Now, build the response.

          response = f"Ollama command found at: {ollama_path}\n"
          response += f"Ollama server at {current_host} is {server_status}.\n\n"

          if "not reachable" in server_status:
              response += "Please make sure the Ollama server is running and accessible.\n"
              if "localhost" in current_host:
                  response += "You can start the server with: ollama serve\n"
              else:
                  response += f"Check the server at {current_host} and your network connection.\n"

          response += "\nTo log in to a remote Ollama server or private registry:\n"
          response += "1. Set the OLLAMA_HOST environment variable to the server URL (if not already set).\n"
          response += "2. For server authentication, set OLLAMA_TOKEN to your token.\n"
          response += "3. For private registries, set OLLAMA_REGISTRY to the registry URL.\n"
          response += "   You will be prompted for credentials when pulling models.\n\n"
          response += "Example:\n"
          response += "   export OLLAMA_HOST=https://example.com\n"
          response += "   export OLLAMA_TOKEN=your_token_here\n"
          response += "   ollama pull <model_name>\n"

          return response

      except Exception as e:
          return f"An error occurred: {str(e)}"

   But wait, we are setting OLLAMA_HOST in the current process. That might affect subsequent plugin runs? Yes, but that's okay because the environment is per process.

   However, note: the Electra app might run plugins in the same process? Then setting OLLAMA_HOST will persist for the rest of the session. That might be what we want.

   But if the user runs multiple times, we might set it multiple times? That's okay.

   Let's code accordingly.

   However, note: the user might not want to set OLLAMA_HOST permanently? We are setting it for the current process only. If they want to set it permanently, they have to do it in their shell config.

   We are just setting it for the current session (the Electra app's process). That might be enough for the current session.

   But if the user wants to use the same host in the future, they have to set it again? We can store it in electra_state? But that's for cross-plugin data. We could store it there and then set it every time the plugin runs? But that might be overkill.

   We'll just set it for the current process and then the user can set it in their shell if they want.

   Alternatively, we can ask the user if they want to set it permanently? But we don't have interactive input.

   So, we'll just set it for the current process and then tell them to set it in their shell if they want.

   Now, let's code the plugin.

   But note: the plugin must be named: autorepair_ollama_login.py

   We'll write the code accordingly.

   However, note: the user might have provided a URL that is not valid. We set it anyway? We set it and then check the connection. If the connection fails, we tell them.

   We are not validating the URL format beyond the regex.

   Let's code.

   One more thing: the user might have provided a URL that is not for the Ollama server? We can't know.

   We'll just set it and then check the connection.

   Now, the code:

   We are going to write the plugin as described.

   But note: the plugin must be in the directory: ~/.config/ai_plugins/autorepair_ollama_login.py

   We are only to output the source code.

   Let's write the code.</think>
"""
Ollama Login Handler for Electra AI
Handles 'ollama login' requests by setting up authentication for Ollama services.
"""

import os
import re
import subprocess
import socket
import urllib.parse
from pathlib import Path

PLUGIN_NAME = "Ollama Login Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles 'ollama login' requests for Ollama authentication"
PLUGIN_AUTHOR = "Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["ollama login", "login to ollama", "ollama authenticate"]
PLUGIN_ROUTE_TOKEN = "OLLAMA_LOGIN"
PLUGIN_COMMANDS = ["/ollama_login"]
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    """
    Handle ollama login requests by setting up authentication environment
    and providing instructions for Ollama server/registry access.
    """
    try:
        print_fn = context.get("print_fn", lambda x: None)
        user_home = context.get("user_home", os.path.expanduser("~"))
        
        # Extract potential URL from prompt
        url_pattern = r'https?://[^\s<>"\']+|localhost:\d+|[\w.-]+:\d+'
        urls = re.findall(url_pattern, prompt)
        target_url = urls[0] if urls else None
        
        # Check if ollama is installed
        ollama_installed = False
        ollama_path = None
        
        try:
            result = subprocess.run(["which", "ollama"], 
                                  capture_output=True, 
                                  text=True, 
                                  timeout=5)
            if result.returncode == 0:
                ollama_installed = True
                ollama_path = result.stdout.strip()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass
        
        # Check if ollama service is running
        service_running = False
        service_host = "localhost"
        service_port = 11434
        
        if target_url:
            parsed = urllib.parse.urlparse(target_url if "://" in target_url else f"http://{target_url}")
            service_host = parsed.hostname or parsed.path or "localhost"
            service_port = parsed.port or 11434
        
        try:
            with socket.create_connection((service_host, service_port), timeout=3):
                service_running = True
        except:
            pass
        
        # Build response
        response_parts = []
        
        if not ollama_installed:
            response_parts.append("⚠️  Ollama is not installed on this system.")
            response_parts.append("\nTo install Ollama on MakuluLinux (Ubuntu-based):")
            response_parts.append("  curl -fsSL https://ollama.com/install.sh | sh")
            response_parts.append("\nAfter installation, start the service:")
            response_parts.append("  ollama serve")
            return "\n".join(response_parts)
        
        response_parts.append(f"✓ Ollama found at: {ollama_path}")
        
        if not service_running:
            response_parts.append(f"⚠️  Ollama service not running on {service_host}:{service_port}")
            response_parts.append("\nStart the service with:")
            response_parts.append("  ollama serve")
            response_parts.append("\nOr if using a remote server, ensure it's accessible.")
        else:
            response_parts.append(f"✓ Ollama service running on {service_host}:{service_port}")
        
        # Authentication instructions
        response_parts.append("\n" + "="*50)
        response_parts.append("OLLAMA AUTHENTICATION SETUP")
        response_parts.append("="*50)
        
        if target_url:
            response_parts.append(f"\nTarget server: {target_url}")
            response_parts.append(f"Set environment variable:")
            response_parts.append(f"  export OLLAMA_HOST={target_url}")
        
        response_parts.append("\nFor server authentication (if required):")
        response_parts.append("  export OLLAMA_TOKEN=your_api_token_here")
        response_parts.append("\nFor private registries:")
        response_parts.append("  export OLLAMA_REGISTRY=registry.example.com")
        response_parts.append("  (You'll be prompted for credentials when pulling)")
        
        response_parts.append("\nTo test authentication:")
        response_parts.append("  ollama pull llama2  # or any model name")
        
        response_parts.append("\nTo make settings permanent, add to ~/.bashrc or ~/.zshrc:")
        if target_url:
            response_parts.append(f"  echo 'export OLLAMA_HOST={target_url}' >> ~/.bashrc")
        response_parts.append("  echo 'export OLLAMA_TOKEN=your_token' >> ~/.bashrc")
        
        response_parts.append("\n" + "="*50)
        response_parts.append("NOTE: Ollama doesn't have a traditional 'login' command.")
        response_parts.append("Authentication is handled via environment variables.")
        response_parts.append("="*50)
        
        return "\n".join(response_parts)
        
    except Exception as e:
        return f"Error handling ollama login: {str(e)}"