PLUGIN_NAME        = "Electra System Info"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Provides detailed information about the Electra AI system"
PLUGIN_AUTHOR      = "MakuluLinux Community"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "ROUTER"
PLUGIN_TRIGGERS    = ["electra info", "electra system", "electra details", "electra version", "electra status"]
PLUGIN_ROUTE_TOKEN = "ELECTRA_INFO"
PLUGIN_COMMANDS    = ["/electra"]

import os
import subprocess
import platform
from datetime import datetime

def run(prompt: str, context: dict) -> str:
    try:
        # Get system information
        system_info = {
            "System": platform.system(),
            "Node Name": platform.node(),
            "Release": platform.release(),
            "Version": platform.version(),
            "Machine": platform.machine(),
            "Processor": platform.processor(),
            "Python Version": platform.python_version(),
            "Electra Version": "2.0.1",  # This would be dynamically fetched in a real implementation
            "Current Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Current Directory": context["cwd"],
            "GUI Active": context["gui_active"],
            "Telegram Active": context["telegram_active"],
            "Current Model": context["model"],
            "Current Mode": context["current_mode"]
        }

        # Get Electra process information
        try:
            electra_process = subprocess.run(
                ["ps", "-C", "electra", "-o", "pid,etime,cmd"],
                capture_output=True,
                text=True,
                check=True
            )
            system_info["Electra Process"] = electra_process.stdout.strip()
        except subprocess.CalledProcessError:
            system_info["Electra Process"] = "Not running or not found"

        # Get memory information
        try:
            mem_info = subprocess.run(
                ["free", "-h"],
                capture_output=True,
                text=True,
                check=True
            )
            system_info["Memory Info"] = mem_info.stdout.strip()
        except subprocess.CalledProcessError:
            system_info["Memory Info"] = "Could not retrieve memory information"

        # Get disk information
        try:
            disk_info = subprocess.run(
                ["df", "-h"],
                capture_output=True,
                text=True,
                check=True
            )
            system_info["Disk Info"] = disk_info.stdout.strip()
        except subprocess.CalledProcessError:
            system_info["Disk Info"] = "Could not retrieve disk information"

        # Format the output
        output = "Electra System Information:\n\n"
        for key, value in system_info.items():
            output += f"{key}: {value}\n"

        return output

    except Exception as e:
        context["print_fn"](f"Error retrieving Electra system information: {str(e)}")
        return "Sorry, I encountered an error while trying to retrieve the Electra system information. Please try again later."