PLUGIN_NAME        = "OS Health Check"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Checks MakuluLinux system health, load, and disk usage"
PLUGIN_AUTHOR      = "Plugin Forge"
PLUGIN_ENABLED     = True
PLUGIN_TYPE        = "ROUTER"
PLUGIN_TRIGGERS    = ["check os health", "system health check", "diagnose system", "check health"]
PLUGIN_ROUTE_TOKEN = "OSHEALTH"
PLUGIN_COMMANDS    = ["/health"]
PLUGIN_REQUIRES    = ["psutil"]

import os
import shutil
import subprocess
import platform
import psutil

def run(prompt: str, context: dict) -> str:
    """
    Checks system health using psutil and standard shell commands.
    Ensures safe output formatting by converting all data to strings.
    """
    print_fn = context.get("print_fn", print)
    
    try:
        # System Info
        uname = platform.uname()
        os_info = f"OS: {uname.system} {uname.release} ({uname.version})"
        
        # CPU
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # Memory
        mem = psutil.virtual_memory()
        mem_info = f"Memory: {mem.percent}% used ({mem.used // (1024**2)}MB / {mem.total // (1024**2)}MB)"
        
        # Disk
        disk = shutil.disk_usage("/")
        disk_info = f"Disk (/): {disk.used // (1024**3)}GB / {disk.total // (1024**3)}GB used"
        
        # Load Averages (Linux specific)
        load1, load5, load15 = psutil.getloadavg()
        load_info = f"Load Average: {load1}, {load5}, {load15}"
        
        # Check systemd status for common critical services
        try:
            cmd = ["systemctl", "is-system-running"]
            status = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode().strip()
            service_info = f"Systemd Status: {status}"
        except Exception:
            service_info = "Systemd Status: Could not retrieve"

        # Construct safe string output
        report = [
            "### 🩺 System Health Report",
            os_info,
            f"CPU Usage: {cpu_usage}%",
            mem_info,
            disk_info,
            load_info,
            service_info
        ]
        
        return "\n".join(report)

    except Exception as e:
        error_msg = f"Error during health check: {str(e)}"
        print_fn(error_msg)
        return error_msg