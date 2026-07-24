<think>We are writing a ROUTER plugin that will handle requests to install Steam on MakuluLinux (Ubuntu-based).
 The user's request: "instalame steam" (likely a typo for "instala me steam" or "install steam")
 We note that the error says the user repeatedly requested this type of task (4 times) with no dedicated handler.

 We are to write a plugin that will handle such requests.

 Steps:
 1. We'll create a ROUTER plugin that triggers on phrases like "instalar steam", "install steam", "steam install", etc.
 2. The plugin will run a command to install Steam on Ubuntu (MakuluLinux is Ubuntu-based). We assume the user has sudo privileges.
 3. We must be cautious: we are in a terminal app, and we don't want to run commands without user confirmation? 
    However, the specification says the plugin must return a non-empty string on success. We are to handle the request.

 But note: the user's request is in Spanish? "instalame" -> "instala me" (install for me). We can trigger on "instalame", "instalar", "install", etc.

 However, the error says the user repeatedly requested this type of task. So we want to catch any request about installing Steam.

 Let's design:
   PLUGIN_TRIGGERS: We'll include variations in English and Spanish.

 But note: the user is on MakuluLinux (Ubuntu) so the command to install Steam is:
   sudo apt update && sudo apt install -y steam

 However, we must consider:
   - The user might not have sudo rights? We can try and if it fails, report the error.
   - We are in a plugin that runs in the Electra app. We have access to the context, which includes a `print_fn` for output.

 We are to use `subprocess.run` for system commands.

 We must also consider that the user might be in a non-interactive shell? But the Electra app is a terminal.

 We'll write the plugin to:
   - Check if steam is already installed? Maybe not necessary, but we can try to install anyway.

 However, note: the plugin must not crash the host app. So we wrap in try/except.

 We are to return a string that will be shown to the user.

 Let's plan the run function:

  1. Check if we are on a Debian/Ubuntu system? We are on MakuluLinux which is Ubuntu-based, but let's check for the existence of apt.
  2. Run the installation command with sudo. But note: the user might not have sudo without a password? We cannot assume.
  3. We can run the command and capture the output. Then return the output.

 However, the user might not want to run sudo without being asked? But the request is to install.

 Since the user explicitly asked to install, we proceed.

 But note: the plugin is triggered by the router when the user says something like "instalame steam". We are to handle that.

 We'll write:

   import subprocess
   import sys

   def run(prompt, context):
        # We are going to run the installation command.
        # We'll use the context's print_fn to show progress? But the run function returns a string.

        # We can do:
        #   result = subprocess.run(["sudo", "apt", "update"], capture_output=True, text=True)
        #   then install.

        # However, note: the user might not have sudo configured. We can try without sudo? No, installing packages requires sudo.

        # We'll run:
        #   sudo apt update
        #   sudo apt install -y steam

        # But note: the user might be in a container or without internet? We'll just run and return the output.

        # We'll combine the two commands and return the combined output.

        # However, we must be cautious: if the first command fails, we might not want to run the second? But the user wants steam.

        # Alternatively, we can do:

        #   cmd = "sudo apt update && sudo apt install -y steam"
        #   result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

        # But using shell=True can be a security risk if the prompt is used in the command? We are not using the prompt in the command.

        # We are not using the prompt in the command, so it's safe.

        # However, we are in a plugin that might be run in a context where the user's environment is set. We can use the user's shell.

        # But note: the app might be running in a non-interactive shell. We'll use the system's default shell.

        # Alternatively, we can run without shell:

        #   subprocess.run(["sudo", "apt", "update"])
        #   subprocess.run(["sudo", "apt", "install", "-y", "steam"])

        # But then we have to handle each separately.

        # Let's do:

        try:
            # Update
            update_result = subprocess.run(["sudo", "apt", "update"], capture_output=True, text=True, timeout=300)
            # Install
            install_result = subprocess.run(["sudo", "apt", "install", "-y", "steam"], capture_output=True, text=True, timeout=300)

            output = "Update:\n" + update_result.stdout + update_result.stderr
            output += "\nInstall:\n" + install_result.stdout + install_result.stderr

            if update_result.returncode == 0 and install_result.returncode == 0:
                output += "\nSteam installed successfully."
            else:
                output += "\nSteam installation failed. Check the errors above."

            return output

        except subprocess.TimeoutExpired:
            return "The installation command timed out. Please try again or check your network connection."
        except Exception as e:
            return f"An error occurred: {str(e)}"

 However, note: the user might not have sudo rights. The sudo command might prompt for a password, but in a non-interactive subprocess it will fail.

 We cannot handle password prompts in a non-interactive way. So we assume the user has passwordless sudo for apt? Or we can't do it.

 But the user is on their own system, so they might have sudo rights. However, if they don't, the command will fail and we return the error.

 Alternatively, we can check if the user is in the sudo group? But that's not enough.

 We'll leave it as above and let the user see the error.

 But note: the plugin is for MakuluLinux, which is Ubuntu-based. We assume apt.

 However, what if the user is on a different distribution? The error says MakuluLinux, so we assume Ubuntu.

 But to be safe, we can check for the existence of apt? We can do:

   import shutil
   if not shutil.which("apt"):
        return "This plugin only works on Debian/Ubuntu-based systems."

 Let's add that.

 Also, we should check if steam is already installed? We can do:

   if shutil.which("steam"):
        return "Steam is already installed."

 But note: the user might want to reinstall? We can skip that check.

 However, the user asked to install, so if it's already installed, we can say so.

 Let's do:

   if shutil.which("steam"):
        return "Steam is already installed. Use 'steam' to run it."

 But note: the steam command might be in the path but the package might be broken? We are not checking that.

 We'll keep it simple.

 Revised plan:

  1. Check for apt.
  2. Check if steam is already in the path.
  3. Run update and install.

 However, note: the user might have steam installed but from a different source? We are using apt.

 We'll assume the user wants the apt version.

 Let's code accordingly.

 But note: the plugin must be named appropriately. The specification says the file will be auto-named: autorepair_<token_lowercase>.py

 We are to choose a PLUGIN_ROUTE_TOKEN that does not clash. Since this is for installing Steam, let's use "STEAM_INSTALL".

 However, the error says the user repeatedly requested "instalame steam". We want to catch that.

 We'll set:

   PLUGIN_TRIGGERS = ["instalame steam", "instalar steam", "install steam", "steam install", "steam"]

 But note: the trigger "steam" might be too broad? But the user's request is about installing steam.

 We can also include "quiero steam" (I want steam) and "necesito steam" (I need steam).

 But let's stick to the ones that are about installation.

 However, the user might say "steam" and mean something else? But in the context of the error, they are trying to install.

 We'll use:

   PLUGIN_TRIGGERS = [
        "instalame steam",
        "instalar steam",
        "install steam",
        "steam install",
        "steam setup",
        "steam configuration",
        "steam installieren",  # German? But the user is on MakuluLinux (Spanish/English?) We don't know.
        "install steam on ubuntu",
        "install steam on makulu",
        "como instalar steam",  # how to install steam
        "cómo instalar steam",
        "steam instalar",
        "steam installation"
    ]

 But note: the trigger matching is probably exact? Or substring? The specification doesn't say.

 The original Electra app might do substring matching? We don't know.

 We'll assume it's substring matching (case insensitive?).

 We'll make the triggers in lowercase and hope the matching is case insensitive.

 Alternatively, we can use a function to check? But the specification says PLUGIN_TRIGGERS is a list of strings.

 We'll put common phrases.

 However, the user's request was "instalame steam". So we must catch that.

 Let's set:

   PLUGIN_TRIGGERS = ["instalame steam", "instalar steam", "install steam", "steam install"]

 But to be safe, we can also include "steam" alone? But that might be too broad.

 Since the error says the user repeatedly requested this type of task, we want to catch any request about installing steam.

 We'll include:

   "steam" only if the prompt also has an installation word? But we can't do that in triggers.

 Alternatively, we can make the run function check the prompt for keywords? But the triggers are for routing.

 We are a ROUTER plugin, so we are triggered by the triggers. Then in run, we get the full prompt.

 We can do:

   In run, we check the prompt for installation keywords and if steam is mentioned? But then we are triggered by the triggers.

 We are already triggered by the triggers, so we don't need to check again.

 But what if the user says "I want to play games" and mentions steam? We don't want to trigger then.

 So we must be careful with the triggers.

 Let's stick to the ones that clearly indicate installation.

 We'll use:

   PLUGIN_TRIGGERS = [
        "instalame steam",
        "instalar steam",
        "install steam",
        "steam install",
        "steam setup",
        "steam configuration",
        "como instalar steam",
        "cómo instalar steam",
        "steam instalar",
        "steam installation",
        "install steam on ubuntu",
        "install steam on makulu"
    ]

 We'll also note that the user might use "steam" in a different context? But the error says they are trying to install.

 We'll take the risk.

 Now, the plugin metadata:

   PLUGIN_NAME = "Steam Installer"
   PLUGIN_VERSION = "1.0.0"
   PLUGIN_DESCRIPTION = "Installs Steam on MakuluLinux (Ubuntu-based)"
   PLUGIN_AUTHOR = "Plugin Forge"
   PLUGIN_ENABLED = True
   PLUGIN_TYPE = "ROUTER"
   PLUGIN_REQUIRES = []   # we are using only standard library

 But note: we are using subprocess, which is standard.

 However, we are using shutil.which, which is also standard.

 So no external dependencies.

 Let's code accordingly.

 But note: the context has a `print_fn` and `notify_panel`. We can use `print_fn` to show progress? But we are returning a string.

 We are returning the entire output. We can also use `print_fn` to print during the process? But the run function returns a string that will be printed by the app.

 We can do:

   context["print_fn"]("Updating package list...")
   ... then run update and print the output? But the output might be long.

 Alternatively, we can just return the output and let the app print it.

 We'll return the output.

 However, the user might want to see the progress in real time? But we are capturing the output and returning it at the end.

 We can change to:

   We run the commands and capture the output, then return it.

 But if the installation takes time, the user might think it's stuck.

 We can use `print_fn` to print step by step? But then we also return the output? That would duplicate.

 We can do:

   context["print_fn"]("Starting Steam installation...")
   ... then run the commands and capture output, then at the end return the output.

 But the app will print the returned string anyway.

 We'll just return the output and let the app print it.

 However, the app might print the returned string with Rich Markdown? We don't need formatting.

 We'll return plain text.

 Let's code accordingly.

 But note: the context has `cwd` and `workspace`. We don't need to change directory.

 We'll run in the current directory.

 Now, the code:

   We must import subprocess and shutil.

   We'll write:

   import subprocess
   import shutil
   import sys

   Then the metadata and the run function.

 However, note: the plugin must be a standalone file. We are not allowed to import from ai_terminal.

 We are only using standard library.

 Let's write the plugin.

 But note: the user might not have sudo installed? We are on Ubuntu, so sudo is installed by default.

 We'll assume sudo is there.

 However, we can check for sudo? We can run `which sudo`? But if sudo is not installed, the command will fail.

 We'll let the command fail and return the error.

 We are going to write:

   if not shutil.which("apt"):
        return "Error: apt package manager not found. This plugin only works on Debian/Ubuntu-based systems."

   if shutil.which("steam"):
        return "Steam is already installed. You can run it by typing 'steam' in the terminal."

   Then run the commands.

 But note: the steam command might be from a different installation? We are checking the path.

 We'll assume that if the steam command is in the path, then it's installed.

 However, the user might have installed steam via flatpak? Then the command might be `flatpak run com.valvesoftware.Steam`?

 We are only installing via apt. So if the user has steam via flatpak, we might still install the apt version? That could cause conflicts.

 But the user asked to install steam, and on Ubuntu the standard way is apt.

 We'll proceed.

 Let's code accordingly.

 However, note: the user might not have internet? We'll let the apt command fail.

 We are going to write the plugin.

 But note: the plugin must be named: autorepair_steam_install.py? The specification says the file will be auto-named: autorepair_<token_lowercase>.py

 We are setting PLUGIN_ROUTE_TOKEN = "STEAM_INSTALL", so the file will be named: autorepair_steam_install.py

 But the user is placing the file in ~/.config/ai_plugins. We are writing the content.

 We are to output only the raw Python source.

 Let's write the code.</think>
"""
Plugin para instalar Steam en MakuluLinux (Ubuntu-based)
"""

PLUGIN_NAME = "Steam Installer"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Instala Steam en MakuluLinux usando apt"
PLUGIN_AUTHOR = "Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = [
    "instalame steam",
    "instalar steam",
    "install steam",
    "steam install",
    "steam setup",
    "steam configuration",
    "como instalar steam",
    "cómo instalar steam",
    "steam instalar",
    "steam installation",
    "install steam on ubuntu",
    "install steam on makulu"
]
PLUGIN_ROUTE_TOKEN = "STEAM_INSTALL"
PLUGIN_COMMANDS = ["/steam-install"]
PLUGIN_REQUIRES = []

import subprocess
import shutil
import sys
import os

def run(prompt: str, context: dict) -> str:
    """
    Instala Steam en MakuluLinux (Ubuntu-based) usando apt.
    """
    try:
        # Verificar que estamos en un sistema basado en Ubuntu/Debian
        if not shutil.which("apt"):
            return "❌ Error: Este plugin solo funciona en sistemas basados en Ubuntu/Debian (MakuluLinux)."
        
        # Verificar si Steam ya está instalado
        if shutil.which("steam") or os.path.exists("/usr/games/steam") or os.path.exists("/usr/bin/steam"):
            return "✅ Steam ya está instalado en el sistema. Ejecuta 'steam' para iniciarlo."
        
        # Verificar si el usuario tiene privilegios sudo
        sudo_check = subprocess.run(
            ["sudo", "-n", "true"],
            capture_output=True,
            text=True
        )
        if sudo_check.returncode != 0:
            return ("⚠️  Se necesitan privilegios de administrador para instalar Steam.\n"
                   "Por favor, ejecuta manualmente:\n"
                   "  sudo apt update && sudo apt install -y steam")
        
        # Mostrar progreso usando print_fn si está disponible
        print_fn = context.get("print_fn", lambda x: print(x))
        print_fn("🔄 Iniciando instalación de Steam...")
        
        # Actualizar repositorios
        print_fn("📦 Actualizando lista de paquetes...")
        update_result = subprocess.run(
            ["sudo", "apt", "update"],
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if update_result.returncode != 0:
            return f"❌ Error al actualizar paquetes:\n{update_result.stderr}"
        
        # Instalar Steam
        print_fn("🎮 Instalando Steam (esto puede tardar varios minutos)...")
        install_result = subprocess.run(
            ["sudo", "apt", "install", "-y", "steam"],
            capture_output=True,
            text=True,
            timeout=600
        )
        
        output = "📋 Resultado de la instalación:\n\n"
        output += "=== ACTUALIZACIÓN ===\n"
        output += update_result.stdout + update_result.stderr + "\n\n"
        output += "=== INSTALACIÓN ===\n"
        output += install_result.stdout + install_result.stderr + "\n\n"
        
        if install_result.returncode == 0:
            output += "✅ Steam se instaló correctamente.\n"
            output += "🚀 Ejecuta 'steam' en tu terminal para iniciar la aplicación."
        else:
            output += "❌ La instalación falló. Revisa los errores anteriores.\n"
            output += "💡 Intenta manualmente: sudo apt install -y steam"
        
        return output
        
    except subprocess.TimeoutExpired:
        return ("⏱️  La instalación tardó demasiado tiempo.\n"
               "Posibles causas:\n"
               "  • Conexión a internet lenta\n"
               "  • Repositorios ocupados\n"
               "Intenta manualmente: sudo apt update && sudo apt install -y steam")
    except Exception as e:
        return f"❌ Error inesperado durante la instalación: {str(e)}"