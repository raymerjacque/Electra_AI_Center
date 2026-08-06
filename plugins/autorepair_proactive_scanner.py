<think>Got it, let's tackle this. First, the user needs a plugin for the Proactive Scanner agent that was failing with CAPABILITY_GAP because it's been requested 10 times with no handler. 

First, the plugin type is ROUTER, right? Wait, no, wait the existing plugins are autorepair ones, so the token should be PROACTIVE_SCANNER? Wait no, wait the route token needs to not clash. Wait existing plugins are autorepair_proactive_scanner, so the token is PROACTIVE_SCANNER? Wait no, let's check the existing installed plugins: autorepair_proactive_scanner.py, so the token for that is PROACTIVE_SCANNER? Wait no, the failed agent is 'Proactive Scanner', so the trigger should match that. Wait PLUGIN_TRIGGERS should include things like "proactive scanner", "run proactive scan", "scan system proactively", right? Because the user was requesting that type of task 10 times.

Wait first, the required metadata: PLUGIN_NAME is "Proactive Scanner Handler", PLUGIN_VERSION "1.0.0", PLUGIN_DESCRIPTION "Handles proactive system scan requests for MakuluLinux, filling the previous capability gap", PLUGIN_AUTHOR "Electra Plugin Community", PLUGIN_ENABLED True, PLUGIN_TYPE "ROUTER" because it's an auto-repair plugin filling a capability gap. Then PLUGIN_TRIGGERS should be the phrases users would use to request a proactive scan: ["proactive scanner", "run proactive scan", "start proactive scan", "proactive system scan", "scan my system proactively"]. Then PLUGIN_ROUTE_TOKEN is "PROACTIVE_SCANNER" wait but wait the existing plugin is autorepair_proactive_scanner, so that's okay? Wait no, wait the existing plugin is already there? Wait no, the error says the agent 'Proactive Scanner' failed with CAPABILITY_GAP, so the existing autorepair_proactive_scanner probably doesn't have the handler? Wait no, wait the user's installed plugins are autorepair_proactive_scanner, autorepair_ollama_login, autorepair_greeting. Oh right, so the proactive scanner plugin exists but maybe it's missing the run function? No, wait no, the error is that the user requested this type of task 10 times with no dedicated handler. So we need to write the plugin that handles that.

Wait first, PLUGIN_REQUIRES: what do we need? For a proactive scan on MakuluLinux, we might need psutil for system info, but wait, maybe we can use standard libraries first? Wait no, if we use psutil, we need to declare it. But wait, maybe make it graceful: if psutil is not installed, fall back to standard commands like df, free, ps, etc. Oh right, because we don't want to crash if the dependency is missing.

Wait the run function: when the user requests a proactive scan, we need to gather system info relevant to MakuluLinux (which is Ubuntu-based, Cinnamon desktop). So things like disk usage, memory usage, running processes, CPU load, maybe check for common issues like low disk space, high memory usage, etc. Then return a formatted report.

Also, use context["print_fn"] to show progressive output, right? Because the spec says to use that instead of print. Also, wrap all external calls in try/except so it doesn't crash the host app.

Wait let's outline the steps:

1. Import necessary modules: os, subprocess, json, maybe datetime, and try to import psutil, but handle ImportError gracefully.

2. Define all the required metadata first. PLUGIN_NAME is "Proactive Scanner Handler", PLUGIN_VERSION "1.0.0", PLUGIN_DESCRIPTION "Handles proactive system scan requests for MakuluLinux, resolving previous CAPABILITY_GAP errors", PLUGIN_AUTHOR "Electra Plugin Forge", PLUGIN_ENABLED True, PLUGIN_TYPE "ROUTER", PLUGIN_TRIGGERS are the phrases users use to request this: ["proactive scanner", "run proactive scan", "start proactive scan", "proactive system scan", "scan my system proactively", "proactive scan"], PLUGIN_ROUTE_TOKEN "PROACTIVE_SCANNER", PLUGIN_COMMANDS ["/proactive-scan"], PLUGIN_REQUIRES ["psutil>=5.9.0"] but wait, if we make it work without psutil, then even if it's not installed, it still works. Oh right, so the PLUGIN_REQUIRES can have psutil as optional? No, wait the spec says PLUGIN_REQUIRES is the dependencies, but we can handle missing ones gracefully.

Wait then, the run function: takes prompt and context. First, get the print_fn from context, use that to output progress. Then, start the scan.

First, get system info: hostname, OS info (since it's MakuluLinux, we can get /etc/os-release), uptime, CPU info, memory info, disk usage, running processes, maybe check for common issues like disk space < 10%, memory usage > 90%, etc.

Wait also, use subprocess for commands that are standard on Ubuntu/Makulu: like lsb_release -a for OS info, uptime, df -h, free -h, ps aux --sort=-%mem | head -10, etc. That way, even if psutil is not installed, it works.

Wait let's structure the run function:

- First, print a start message using context["print_fn"]: "Starting proactive system scan for MakuluLinux..."

- Then gather OS info: try to get from /etc/os-release, or lsb_release. Catch errors.

- Gather uptime: from uptime command, or /proc/uptime.

- Gather CPU info: from /proc/cpuinfo, or top command.

- Gather memory info: from free -h, parse the output.

- Gather disk usage: from df -h, parse, check for low space.

- Gather top processes by memory and CPU.

- Check for common issues: low disk, high memory, high load, etc.

- Then compile all into a formatted report, return that.

Also, make sure all subprocess calls are wrapped in try/except, so if any command fails, it just notes that the info couldn't be retrieved, doesn't crash.

Wait also, the context has cwd, user_home, etc. Maybe we can also check the current workspace (cwd) disk usage specifically? That's useful.

Wait let's write the code step by step.

First, the module docstring? Wait the spec says start directly with import or module docstring. Let's start with the metadata first? Wait no, the imports come first? Wait no, the metadata is top-level variables. Let's see:

Wait first, the required metadata:

PLUGIN_NAME = "Proactive Scanner Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles proactive system scan requests for MakuluLinux, resolving previous CAPABILITY_GAP errors for repeated user requests"
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = [
    "proactive scanner",
    "run proactive scan",
    "start proactive scan",
    "proactive system scan",
    "scan my system proactively",
    "proactive scan"
]
PLUGIN_ROUTE_TOKEN = "PROACTIVE_SCANNER"
PLUGIN_COMMANDS = ["/proactive-scan"]
PLUGIN_REQUIRES = ["psutil>=5.9.0"]  # Optional, falls back to system commands if missing

Then imports: import os, import subprocess, import json, from datetime import datetime, try to import psutil, except ImportError: psutil = None.

Wait then, helper functions? Like run_command, which runs a subprocess command, returns stdout, stderr, return code, handles errors.

Wait let's write a helper function:

def _run_cmd(cmd: list[str], timeout: int = 10) -> dict:
    """Run a system command safely, return output dict."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False
        )
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": result.returncode
        }
    except (subprocess.TimeoutExpired, FileNotFoundError, Exception) as e:
        return {
            "success": False,
            "stdout": "",
            "stderr": str(e),
            "returncode": -1
        }
}

That's a safe helper, no crashes.

Then, the run function:

def run(prompt: str, context: dict) -> str:
    print_fn = context.get("print_fn", print)
    notify_panel = context.get("notify_panel")
    user_home = context.get("user_home", os.path.expanduser("~"))
    cwd = context.get("cwd", os.getcwd())

    # Start scan
    print_fn("🔍 Starting proactive system scan for MakuluLinux...")
    if notify_panel:
        try:
            notify_panel("Proactive Scanner", "Scanning system...", "info")
        except:
            pass

    report_lines = []
    report_lines.append(f"# Proactive System Scan Report")
    report_lines.append(f"**Scan Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append(f"**User Home:** {user_home}")
    report_lines.append(f"**Current Directory:** {cwd}")
    report_lines.append("---")

    # 1. OS Info (MakuluLinux is Ubuntu-based)
    print_fn("📋 Gathering OS information...")
    os_info = _run_cmd(["lsb_release", "-a"])
    if os_info["success"]:
        report_lines.append("## OS Information")
        report_lines.append(f"```\n{os_info['stdout']}\n```")
    else:
        # Fallback to /etc/os-release
        try:
            with open("/etc/os-release", "r") as f:
                os_data = f.read()
            report_lines.append("## OS Information")
            report_lines.append(f"```\n{os_data}\n```")
        except Exception as e:
            report_lines.append("## OS Information\n*Could not retrieve OS info*")

    # 2. System Uptime
    print_fn("⏱️ Checking system uptime...")
    uptime = _run_cmd(["uptime", "-p"])
    if uptime["success"]:
        report_lines.append("## System Uptime")
        report_lines.append(f"**Uptime:** {uptime['stdout']}")
    else:
        report_lines.append("## System Uptime\n*Could not retrieve uptime*")

    # 3. CPU Information
    print_fn("🖥️ Gathering CPU details...")
    cpu_info = _run_cmd(["lscpu"])
    if cpu_info["success"]:
        # Extract key CPU stats
        cpu_lines = []
        for line in cpu_info["stdout"].split("\n"):
            if line.startswith(("Model name", "CPU(s)", "CPU max MHz", "CPU min MHz")):
                cpu_lines.append(line)
        report_lines.append("## CPU Information")
        report_lines.append(f"```\n" + "\n".join(cpu_lines) + "\n```")
    else:
        report_lines.append("## CPU Information\n*Could not retrieve CPU info*")

    # 4. Memory Usage
    print_fn("🧠 Checking memory usage...")
    mem_info = _run_cmd(["free", "-h"])
    if mem_info["success"]:
        report_lines.append("## Memory Usage")
        report_lines.append(f"```\n{mem_info['stdout']}\n```")
        # Check for high memory usage
        try:
            mem_lines = mem_info["stdout"].split("\n")
            mem_total = mem_lines[1].split()[1]
            mem_used = mem_lines[1].split()[2]
            # Convert to GB for comparison
            def to_gb(s):
                if s.endswith("Gi"):
                    return float(s[:-2])
                elif s.endswith("Mi"):
                    return float(s[:-2]) / 1024
                elif s.endswith("Ki"):
                    return float(s[:-2]) / (1024*1024)
                else:
                    return float(s)
            total_gb = to_gb(mem_total)
            used_gb = to_gb(mem_used)
            if total_gb > 0 and (used_gb / total_gb) > 0.9:
                report_lines.append("⚠️ **Warning:** Memory usage is above 90%!")
        except:
            pass
    else:
        report_lines.append("## Memory Usage\n*Could not retrieve memory info*")

    # 5. Disk Usage
    print_fn("💾 Checking disk usage...")
    disk_info = _run_cmd(["df", "-h"])
    if disk_info["success"]:
        report_lines.append("## Disk Usage")
        report_lines.append(f"```\n{disk_info['stdout']}\n```")
        # Check for low disk space
        try:
            disk_lines = disk_info["stdout"].split("\n")[1:]  # Skip header
            for line in disk_lines:
                parts = line.split()
                if len(parts) >= 6:
                    usage = parts[4].replace("%", "")
                    mount = parts[5]
                    if int(usage) > 90:
                        report_lines.append(f"⚠️ **Warning:** Disk usage on {mount} is {usage}% (above 90%)!")
        except:
            pass
    else:
        report_lines.append("## Disk Usage\n*Could not retrieve disk info*")

    # 6. Top Processes (by memory and CPU)
    print_fn("📊 Analyzing running processes...")
    top_mem = _run_cmd(["ps", "aux", "--sort=-%mem", "|", "head", "-10"], shell=True)
    if top_mem["success"]:
        report_lines.append("## Top 10 Processes by Memory Usage")
        report_lines.append(f"```\n{top_mem['stdout']}\n```")
    else:
        report_lines.append("## Top 10 Processes by Memory Usage\n*Could not retrieve process info*")

    top_cpu = _run_cmd(["ps", "aux", "--sort=-%cpu", "|", "head", "-10"], shell=True)
    if top_cpu["success"]:
        report_lines.append("## Top 10 Processes by CPU Usage")
        report_lines.append(f"```\n{top_cpu['stdout']}\n```")
    else:
        report_lines.append("## Top 10 Processes by CPU Usage\n*Could not retrieve process info*")

    # 7. Optional: Use psutil if available for extra info
    if psutil:
        try:
            print_fn("🔍 Running advanced checks with psutil...")
            # Network connections count
            conns = len(psutil.net_connections())
            report_lines.append("## Advanced Checks (psutil)")
            report_lines.append(f"- Active network connections: {conns}")
            # Boot time
            boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
            report_lines.append(f"- System boot time: {boot_time}")
            # CPU load average
            load1, load5, load15 = psutil.getloadavg()
            report_lines.append(f"- CPU load average (1/5/15 min): {load1:.2f} / {load5:.2f} / {load15:.2f}")
            # Check load warning
            cpu_count = psutil.cpu_count()
            if load1 > cpu_count * 0.9:
                report_lines.append(f"⚠️ **Warning:** 1-minute CPU load is above 90% of CPU count ({cpu_count})!")
        except Exception as e:
            report_lines.append("## Advanced Checks\n*Could not run advanced checks: {e}*")

    # Finalize report
    report_lines.append("---")
    report_lines.append("✅ Proactive scan complete. No critical issues detected unless warnings are shown above.")

    # Update notify panel if available
    if notify_panel:
        try:
            notify_panel("Proactive Scanner", "Scan complete", "success")
        except:
            pass

    return "\n".join(report_lines)

Wait wait, but the PLUGIN_TRIGGERS need to match what the user was requesting. The user was requesting "this type of task" which is the Proactive Scanner, so the triggers should cover common ways users would ask for that. Also, the PLUGIN_ROUTE_TOKEN is PROACTIVE_SCANNER, which doesn't clash with existing ones? Wait existing plugins are autorepair_proactive_scanner, so their token is PROACTIVE_SCANNER? Wait no, wait the existing plugin's token would be PROACTIVE_SCANNER? Wait but the error says the agent 'Proactive Scanner' failed, so maybe the existing plugin was missing the run function? No, wait the user's installed plugins are autorepair_proactive_scanner.py, so that's the file name, which comes from the token lowercase. So if we use PLUGIN_ROUTE_TOKEN = "PROACTIVE_SCANNER", the file would be autorepair_proactive_scanner.py, which already exists? Wait wait, the user said the installed plugins are autorepair_proactive_scanner.py, autorepair_ollama_login.py, autorepair_greeting.py. Oh, so maybe the existing proactive scanner plugin is incomplete, so we need to write the correct one? Wait no, wait the user's request is that the user repeatedly requested this type of task (10 times) with no dedicated handler, so the existing plugin probably doesn't have the proper run function, or the triggers are wrong.

Wait wait, let's check the PLUGIN_TRIGGERS. The user was requesting the Proactive Scanner agent, so the triggers should be things that the user would say to activate it. Like "use proactive scanner", "ask proactive scanner", "proactive scanner: ", etc. Oh right! I forgot the "ask groq" style triggers. Oh right, the spec example has PLUGIN_TRIGGERS = ["ask groq", "use groq", "groq:"], so for proactive scanner, the triggers should be ["ask proactive scanner", "use proactive scanner", "proactive scanner:", "run proactive scan", "proactive scan"]. That makes more sense, because the user would say "ask proactive scanner to check my system" or something.

Wait also, the PLUGIN_COMMANDS: ["/proactive-scan"] is good, so users can run /proactive-scan to trigger it.

Wait also, the PLUGIN_REQUIRES: psutil is optional, so even if it's not installed, the plugin works with system commands. So that's okay.

Wait also, in the run function, we use context["print_fn"] to output progress, which is correct per the spec. We don't use print(), we use the provided print_fn.

Also, all subprocess calls are wrapped in the _run_cmd helper which catches exceptions, so no crashes. All file operations are wrapped in try/except.

Wait also, the report is formatted with Markdown, which is good because the Electra app uses Rich Markdown rendering, so the output will look nice.

Wait let's check the critical rules:

- PLUGIN_ROUTE_TOKEN doesn't clash: existing plugins are PROACTIVE_SCANNER? Wait no, wait the existing plugin is autorepair_proactive_scanner.py, so its token is PROACTIVE_SCANNER? Wait but if we write a new plugin with the same token, that would clash? Wait wait no, wait the user said the installed plugins are autorepair_proactive_scanner.py, autorepair_ollama_login.py, autorepair_greeting.py. Oh, wait maybe the existing proactive scanner plugin is broken, so we need to overwrite it? But the spec says the file is auto-named autorepair_<token_lowercase>.py. So if the token is PROACTIVE_SCANNER, the file is autorepair_proactive_scanner.py, which is already there. But the user's error is that the agent 'Proactive Scanner' has a capability gap, so the existing plugin is not working. So writing this plugin with the same token would replace it? Or wait, maybe the token should be something else? No, wait the agent is called 'Proactive Scanner', so the route token should match that. Wait maybe the existing plugin has the wrong triggers, so it's not being activated. So our plugin has the correct triggers, so when the user says "ask proactive scanner", it triggers this plugin.

Wait also, PLUGIN_TYPE is ROUTER, which is correct for auto-repair plugins filling capability gaps, per the critical rules.

Wait let's adjust the PLUGIN_TRIGGERS to include the "ask X" pattern, like the example:

PLUGIN_TRIGGERS = [
    "ask proactive scanner",
    "use proactive scanner",
    "proactive scanner:",
    "run proactive scan",
    "proactive system scan",
    "scan my system proactively"
]

That's better, because that's how users would invoke the agent.

Wait also, in the run function, we can check if the prompt is a command? No, the PLUGIN_COMMANDS handles the slash command.

Wait also, what about the context keys? We use print_fn, notify_panel, user_home, cwd, which are all available per the spec.

Wait also, we don't import anything from ai_terminal, which is correct.

Wait let's test for possible crashes: all external calls are in try/except, the _run_cmd helper catches all exceptions, so even if a command fails, it just returns an error message, doesn't crash.

Wait also, the disk usage check: we parse the df output, check for partitions over 90%, which is useful. The memory check does the same.

Wait also, if psutil is available, we add extra info like network connections, boot time, load average, which is nice.

Wait let's adjust the code to make sure it's correct. Also, the file name would be autorepair_proactive_scanner.py, which matches the existing installed plugin, so it will overwrite the broken one, which is correct.

Wait wait, but the user said the installed plugins are autorepair_proactive_scanner.py, so that's the file we need to write, right? Because the token is PROACTIVE_SCANNER, so the file is autorepair_proactive_scanner.py, which is already present but broken. So writing this code to that file will fix it.

Wait let's check the spec again: the file is auto-named autorepair_<token_lowercase>.py. So if PLUGIN_ROUTE_TOKEN is "PROACTIVE_SCANNER", the file is autorepair_proactive_scanner.py, which is exactly the existing one. Perfect.

Wait also, PLUGIN_ENABLED is True, which is required per critical rules.

Wait let's make sure there are no hardcoded paths: we use os.path.expanduser("~") via context["user_home"], which is correct. All commands are standard system commands, no hardcoded paths.

Wait also, the run function returns a non-empty string, which is required.

Wait let's put it all together now. Let's make sure the code is correct, no syntax errors.

Wait also, the _run_cmd function: when using shell=True for the ps commands, that's okay because we're passing a single string? Wait no, wait in the code above, I wrote ["ps", "aux", "--sort=-%mem", "|", "head", "-10"], shell=True. Wait that's wrong, because when shell=True, the command should be a string, not a list. Oh right! So fix that: either pass a string with shell=True, or split the pipe into a list without shell? No, the pipe is a shell feature, so better to pass as a string. So change those lines to:

top_mem = _run_cmd("ps aux --sort=-%mem | head -10", shell=True)
top_cpu = _run_cmd("ps aux --sort=-%cpu | head -10", shell=True)

Yes, that's correct. Because when shell=True, the command is a string, so the pipe works.

Wait also, in the _run_cmd function, when shell=True, we need to make sure that the command is a string, which it is now.

Another thing: the psutil import: we can wrap it in a try/except, so if it's not installed, psutil is None, and the advanced checks are skipped. That's graceful.

Wait let's adjust the import part:

try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    psutil = None
    HAS_PSUTIL = False

Then, in the run function, check if HAS_PSUTIL instead of if psutil, that's clearer.

Wait also, the PLUGIN_REQUIRES: since psutil is optional, maybe we can note that? But the spec says PLUGIN_REQUIRES is the dependencies, so it's okay to list it, and the app will notify the user if it's missing, but the plugin still works without it.

Wait another thing: the notify_panel calls are wrapped in try/except, so if the notify_panel function is not available (like if the GUI is not running), it doesn't crash. Correct.

Wait let's also add a check for the current workspace (cwd) disk usage, specifically, since the context has cwd. Oh right, in the disk usage section, we can highlight the current directory's mount point. Let's adjust that:

In the disk usage check part:

for line in disk_lines:
    parts = line.split()
    if len(parts) >= 6:
        usage = parts[4].replace("%", "")
        mount = parts[5]
        # Highlight current workspace mount
        if cwd.startswith(mount):
            report_lines.append(f"📁 **Current workspace mount ({mount}):** {usage}% used")
        if int(usage) > 90:
            report_lines.append(f"⚠️ **Warning:** Disk usage on {mount} is {usage}% (above 90%)!")

That's a nice touch, since the user is in a specific workspace, they care about that disk space.

Wait also, in the OS info section, we can check if it's MakuluLinux specifically, and mention that. Let's adjust that:

if os_info["success"]:
    report_lines.append("## OS Information")
    os_text = os_info["stdout"]
    if "Makulu" in os_text:
        report_lines.append("✅ **MakuluLinux detected**")
    report_lines.append(f"```\n{os_text}\n```")

That's good, since it's specifically for MakuluLinux.

Wait also, the uptime: if the uptime -p fails, we can try reading /proc/uptime:

if uptime["success"]:
    report_lines.append("## System Uptime")
    report_lines.append(f"**Uptime:** {uptime['stdout']}")
else:
    # Fallback to /proc/uptime
    try:
        with open("/proc/uptime", "r") as f:
            uptime_seconds = float(f.read().split()[0])
        uptime_str = f"{int(uptime_seconds // 3600)}h {int((uptime_seconds % 3600) // 60)}m"
        report_lines.append("## System Uptime")
        report_lines.append(f"**Uptime:** {uptime_str}")
    except:
        report_lines.append("## System Uptime\n*Could not retrieve uptime*")

That's a good fallback, since /proc/uptime exists on all Linux systems.

Okay, putting all this together now. Let's write the full code, making sure it's correct, no errors</think>
"""
Autorepair plugin for Proactive Scanner capability gap on MakuluLinux
"""
import os
import subprocess
from datetime import datetime

# -------------------------- REQUIRED METADATA --------------------------
PLUGIN_NAME = "Proactive Scanner Handler"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles proactive system scan requests for MakuluLinux, resolving repeated CAPABILITY_GAP errors"
PLUGIN_AUTHOR = "Electra Plugin Forge"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = [
    "ask proactive scanner",
    "use proactive scanner",
    "proactive scanner:",
    "run proactive scan",
    "proactive system scan",
    "scan my system proactively",
    "proactive scan"
]
PLUGIN_ROUTE_TOKEN = "PROACTIVE_SCANNER"
PLUGIN_COMMANDS = ["/proactive-scan"]
PLUGIN_REQUIRES = ["psutil>=5.9.0"]  # Optional, falls back to system commands if missing
# -----------------------------------------------------------------------

# Optional dependency import with graceful fallback
try:
    import psutil
    HAS_PSUTIL = True
except ImportError:
    psutil = None
    HAS_PSUTIL = False


def _run_cmd(cmd: str | list, timeout: int = 10) -> dict:
    """Safe subprocess wrapper that never crashes the host app."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            shell=isinstance(cmd, str),
            check=False
        )
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": result.returncode
        }
    except Exception as e:
        return {
            "success": False,
            "stdout": "",
            "stderr": str(e),
            "returncode": -1
        }


def run(prompt: str, context: dict) -> str:
    # Extract safe context values with fallbacks
    print_fn = context.get("print_fn", print)
    notify_panel = context.get("notify_panel")
    user_home = context.get("user_home", os.path.expanduser("~"))
    cwd = context.get("cwd", os.getcwd())

    # Initialize scan
    print_fn("🔍 Starting proactive system scan for MakuluLinux...")
    if notify_panel:
        try:
            notify_panel("Proactive Scanner", "Scanning system...", "info")
        except Exception:
            pass

    report = []
    report.append("# Proactive System Scan Report")
    report.append(f"**Scan Time:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"**User Home:** `{user_home}`")
    report.append(f"**Current Workspace:** `{cwd}`")
    report.append("---")

    # 1. OS Detection (MakuluLinux specific)
    print_fn("📋 Gathering OS information...")
    os_info = _run_cmd(["lsb_release", "-a"])
    if os_info["success"]:
        report.append("## OS Information")
        if "Makulu" in os_info["stdout"]:
            report.append("✅ **MakuluLinux distribution confirmed**")
        report.append(f"```\n{os_info['stdout']}\n```")
    else:
        # Fallback to standard os-release file
        try:
            with open("/etc/os-release", "r") as f:
                os_data = f.read()
            report.append("## OS Information")
            report.append(f"```\n{os_data}\n```")
        except Exception:
            report.append("## OS Information\n*Could not retrieve OS details*")

    # 2. System Uptime
    print_fn("⏱️ Checking system uptime...")
    uptime = _run_cmd(["uptime", "-p"])
    if uptime["success"]:
        report.append("## System Uptime")
        report.append(f"**Uptime:** {uptime['stdout']}")
    else:
        # Fallback to /proc/uptime for Linux systems
        try:
            with open("/proc/uptime", "r") as f:
                uptime_secs = float(f.read().split()[0])
            uptime_str = f"{int(uptime_secs // 3600)}h {int((uptime_secs % 3600) // 60)}m"
            report.append("## System Uptime")
            report.append(f"**Uptime:** {uptime_str}")
        except Exception:
            report.append("## System Uptime\n*Could not retrieve uptime*")

    # 3. CPU Information
    print_fn("🖥️ Gathering CPU details...")
    cpu_info = _run_cmd(["lscpu"])
    if cpu_info["success"]:
        # Extract only relevant CPU fields
        cpu_lines = [
            line for line in cpu_info["stdout"].split("\n")
            if line.startswith(("Model name", "CPU(s)", "CPU max MHz", "CPU min MHz", "Architecture"))
        ]
        report.append("## CPU Information")
        report.append(f"```\n" + "\n".join(cpu_lines) + "\n```")
    else:
        report.append("## CPU Information\n*Could not retrieve CPU details*")

    # 4. Memory Usage
    print_fn("🧠 Checking memory usage...")
    mem_info = _run_cmd(["free", "-h"])
    if mem_info["success"]:
        report.append("## Memory Usage")
        report.append(f"```\n{mem_info['stdout']}\n```")
        # Check for high memory usage warning
        try:
            mem_parts = mem_info["stdout"].split("\n")[1].split()
            mem_total = mem_parts[1]
            mem_used = mem_parts[2]
            # Convert units to GB for comparison
            def to_gb(value: str) -> float:
                if value.endswith("Gi"):
                    return float(value[:-2])
                elif value.endswith("Mi"):
                    return float(value[:-2]) / 1024
                return float(value)
            usage_pct = to_gb(mem_used) / to_gb(mem_total) * 100
            if usage_pct > 90:
                report.append(f"⚠️ **Warning:** Memory usage is at {usage_pct:.1f}% (above 90% threshold)")
        except Exception:
            pass
    else:
        report.append("## Memory Usage\n*Could not retrieve memory details*")

    # 5. Disk Usage
    print_fn("💾 Checking disk usage...")
    disk_info = _run_cmd(["df", "-h"])
    if disk_info["success"]:
        report.append("## Disk Usage")
        report.append(f"```\n{disk_info['stdout']}\n```")
        # Check for low disk space and highlight workspace mount
        try:
            for line in disk_info["stdout"].split("\n")[1:]:
                parts = line.split()
                if len(parts) >= 6:
                    usage = int(parts[4].replace("%", ""))
                    mount = parts[5]
                    # Highlight current workspace mount
                    if cwd.startswith(mount):
                        report.append(f"📁 **Current workspace mount (`{mount}`):** {usage}% used")
                    if usage > 90:
                        report.append(f"⚠️ **Warning:** Disk usage on `{mount}` is {usage}% (above 90% threshold)")
        except Exception:
            pass
    else:
        report.append("## Disk Usage\n*Could not retrieve disk details*")

    # 6. Top Resource-Consuming Processes
    print_fn("📊 Analyzing running processes...")
    top_mem = _run_cmd("ps aux --sort=-%mem | head -10", shell=True)
    if top_mem["success"]:
        report.append("## Top 10 Processes by Memory Usage")
        report.append(f"```\n{top_mem['stdout']}\n```")
    else:
        report.append("## Top 10 Processes by Memory Usage\n*Could not retrieve process data*")

    top_cpu = _run_cmd("ps aux --sort=-%cpu | head -10", shell=True)
    if top_cpu["success"]:
        report.append("## Top 10 Processes by CPU Usage")
        report.append(f"```\n{top_cpu['stdout']}\n```")
    else:
        report.append("## Top 10 Processes by CPU Usage\n*Could not retrieve process data*")

    # 7. Advanced checks with psutil (if available)
    if HAS_PSUTIL:
        print_fn("🔍 Running advanced system checks...")
        try:
            report.append("## Advanced System Checks")
            # Network activity
            conn_count = len(psutil.net_connections())
            report.append(f"- Active network connections: {conn_count}")
            # Boot time
            boot_time = datetime.fromtimestamp(psutil.boot_time()).strftime('%Y-%m-%d %H:%M:%S')
            report.append(f"- System boot time: {boot_time}")
            # CPU load
            load1, load5, load15 = psutil.getloadavg()
            cpu_count = psutil.cpu_count()
            report.append(f"- CPU load average (1/5/15 min): {load1:.2f} / {load5:.2f} / {load15:.2f}")
            # Load warning
            if load1 > cpu_count * 0.9:
                report.append(f"⚠️ **Warning:** 1-minute CPU load exceeds 90% of available CPU cores ({cpu_count})")
        except Exception as e:
            report.append("## Advanced System Checks\n*Could not run advanced checks*")

    # Finalize report
    report.append("---")
    report.append("✅ Proactive scan complete. Review warnings above for potential issues.")

    # Update GUI panel if available
    if notify_panel:
        try:
            notify_panel("Proactive Scanner", "Scan complete", "success")
        except Exception:
            pass

    return "\n".join(report)