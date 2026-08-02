<think>Got it, let's tackle this. First, the user needs a plugin for the Proactive Scanner capability gap on MakuluLinux. Let's start with the required metadata.

First, PLUGIN_NAME should be "Proactive Scanner" right? Wait, the error was from agent 'Proactive Scanner' so the plugin name matches that. PLUGIN_VERSION let's do "1.0.0". Description: "Handles proactive system scanning tasks on MakuluLinux including security, package, and system health checks". Author can be "Electra Plugin Community". PLUGIN_ENABLED is True, PLUGIN_TYPE is ROUTER? Wait no, wait the error says it's a capability gap for Proactive Scanner tasks. Wait, what triggers would users use? Let's think: triggers like "run proactive scan", "proactive scanner", "scan system", "check system health", "security scan", "package audit". Oh right, PLUGIN_TRIGGERS should cover those common phrases. PLUGIN_ROUTE_TOKEN can be "PROACTIVE_SCANNER" that's unique, no clash. PLUGIN_COMMANDS can be ["/proactive-scan", "/sysscan", "/healthcheck"].

Now, the run function. First, we need to handle different scan types. Let's see, on MakuluLinux (Ubuntu-based, Cinnamon), common scans are: system health, security updates, package audit, log check, disk usage. Let's make the run function parse the prompt to determine what scan to run.

Wait, first, we need to use subprocess for system commands, right? Because it's a system scanner. Also, wrap all external calls in try/except so it doesn't crash the app. Also, use context["print_fn"] to output progressive results, that's better than print.

Wait, let's outline the run function steps:
1. Normalize the prompt to lowercase to detect scan type.
2. If prompt mentions health, system status, run system health checks: uptime, disk usage, memory usage, CPU load, running processes count.
3. If mentions security, updates, run apt update check, list security updates, check for failed login attempts in auth.log.
4. If mentions packages, audit, list outdated packages, check for unnecessary packages.
5. If mentions logs, check recent system logs for errors.
6. If generic "scan" or "proactive scan", run a combined quick scan of all the above.
7. Also, handle errors gracefully, if a command fails, note it but continue.
8. Return a summary of the scan results.

Wait, also, need to make sure paths are correct. For example, auth.log is in /var/log/auth.log on Ubuntu-based systems, which MakuluLinux is. Also, use subprocess.run with capture_output=True, text=True, check=False so it doesn't throw exceptions if a command fails, we can handle the output.

Also, PLUGIN_REQUIRES? Wait, do we need any external packages? No, all the commands are standard system utilities: uptime, df, free, ps, apt, grep, journalctl? Wait, but maybe we don't need any, so PLUGIN_REQUIRES can be empty list, or maybe []? Wait no, if we don't need any, just leave it as [] or omit? Wait the spec says optional, default []. So we can set PLUGIN_REQUIRES = [] but maybe if we want, but no, all commands are built-in.

Wait also, the plugin file name should be autorepair_proactive_scanner.py right? Because the token is PROACTIVE_SCANNER, lowercase. Oh right, the output is the raw Python file, so the code should start with the docstring? Wait no, first the required metadata, then imports, then the run function.

Wait let's structure it:

First, the module docstring? Maybe, but not required, but can have. Then the required metadata variables:

PLUGIN_NAME = "Proactive Scanner"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles proactive system scanning, health checks, security audits, and package management tasks on MakuluLinux"
PLUGIN_AUTHOR = "Electra Plugin Community"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = [
    "run proactive scan",
    "proactive scanner",
    "scan my system",
    "check system health",
    "security scan",
    "package audit",
    "check for updates",
    "review system logs",
    "proactive:"
]
PLUGIN_ROUTE_TOKEN = "PROACTIVE_SCANNER"
PLUGIN_COMMANDS = ["/proactive-scan", "/syshealth", "/secaudit", "/pkgaudit"]
PLUGIN_REQUIRES = []  # No external Python dependencies, uses standard system utilities

Then imports: we need os, subprocess, re maybe? Wait, import os, subprocess, re? Or just os and subprocess. Let's import os and subprocess.

Then the run function:

def run(prompt: str, context: dict) -> str:
    # Normalize prompt for parsing
    prompt_lower = prompt.lower().strip()
    results = []
    print_fn = context.get("print_fn", print)  # Fallback to print if not available, though spec says it's provided

    try:
        # Determine scan type from prompt
        if any(term in prompt_lower for term in ["health", "system status", "syshealth"]):
            results.append("=== System Health Check ===")
            # Uptime
            try:
                uptime = subprocess.run(["uptime", "-p"], capture_output=True, text=True, check=False).stdout.strip()
                results.append(f"System Uptime: {uptime}")
            except Exception as e:
                results.append(f"Failed to get uptime: {str(e)}")
            # Disk usage
            try:
                df = subprocess.run(["df", "-h", "--total"], capture_output=True, text=True, check=False).stdout.strip()
                results.append(f"Disk Usage:\n{df}")
            except Exception as e:
                results.append(f"Failed to get disk usage: {str(e)}")
            # Memory usage
            try:
                free = subprocess.run(["free", "-h"], capture_output=True, text=True, check=False).stdout.strip()
                results.append(f"Memory Usage:\n{free}")
            except Exception as e:
                results.append(f"Failed to get memory usage: {str(e)}")
            # CPU load
            try:
                cpu = subprocess.run(["top", "-bn1", "|", "grep", "load average"], shell=True, capture_output=True, text=True, check=False).stdout.strip()
                results.append(f"CPU Load: {cpu}")
            except Exception as e:
                results.append(f"Failed to get CPU load: {str(e)}")
            # Running processes count
            try:
                ps = subprocess.run(["ps", "-e", "--no-headers"], capture_output=True, text=True, check=False).stdout.strip().split('\n')
                proc_count = len([p for p in ps if p.strip()])
                results.append(f"Running Processes: {proc_count}")
            except Exception as e:
                results.append(f"Failed to get process count: {str(e)}")

        elif any(term in prompt_lower for term in ["security", "secaudit", "updates", "vulnerabilities"]):
            results.append("=== Security & Update Audit ===")
            # Check for available updates
            try:
                # Run apt update silently first to get latest package lists
                subprocess.run(["apt", "update", "-qq"], capture_output=True, text=True, check=False)
                # List upgradable packages
                upgradable = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True, check=False).stdout.strip()
                if upgradable:
                    results.append(f"Available Updates ({len(upgradable.splitlines())} packages):\n{upgradable[:2000]}...")  # Truncate to avoid huge output
                else:
                    results.append("All packages are up to date.")
            except Exception as e:
                results.append(f"Failed to check for updates: {str(e)}")
            # Check security updates specifically
            try:
                sec_updates = subprocess.run(
                    ["apt", "list", "--upgradable", "|", "grep", "-i", "security"],
                    shell=True, capture_output=True, text=True, check=False
                ).stdout.strip()
                if sec_updates:
                    results.append(f"Security Updates Available:\n{sec_updates}")
                else:
                    results.append("No pending security updates.")
            except Exception as e:
                results.append(f"Failed to check security updates: {str(e)}")
            # Check failed login attempts
            try:
                auth_log = "/var/log/auth.log"
                if os.path.exists(auth_log):
                    failed_logins = subprocess.run(
                        ["grep", "Failed password", auth_log, "|", "tail", "-10"],
                        shell=True, capture_output=True, text=True, check=False
                    ).stdout.strip()
                    if failed_logins:
                        results.append(f"Recent Failed Login Attempts:\n{failed_logins}")
                    else:
                        results.append("No recent failed login attempts found.")
                else:
                    results.append("Auth log not found (may require sudo to access).")
            except Exception as e:
                results.append(f"Failed to check login attempts: {str(e)}")

        elif any(term in prompt_lower for term in ["package", "pkgaudit", "outdated", "unnecessary"]):
            results.append("=== Package Audit ===")
            # List manually installed packages
            try:
                manual_pkgs = subprocess.run(
                    ["apt", "list", "--manual-installed"],
                    capture_output=True, text=True, check=False
                ).stdout.strip().splitlines()[1:]  # Skip header
                results.append(f"Manually Installed Packages: {len(manual_pkgs)} total")
            except Exception as e:
                results.append(f"Failed to get installed packages: {str(e)}")
            # List orphaned packages (no dependencies)
            try:
                orphaned = subprocess.run(
                    ["deborphan"],
                    capture_output=True, text=True, check=False
                ).stdout.strip()
                if orphaned:
                    results.append(f"Orphaned Packages (can be removed):\n{orphaned}")
                else:
                    results.append("No orphaned packages found.")
            except Exception as e:
                results.append("deborphan not installed, skipping orphan check. Install with `sudo apt install deborphan` for full audit.")
            # List large packages
            try:
                large_pkgs = subprocess.run(
                    ["dpkg-query", "-W", "--showformat='${Installed-Size}\t${Package}\n'", "|", "sort", "-nr", "|", "head", "-10"],
                    shell=True, capture_output=True, text=True, check=False
                ).stdout.strip()
                results.append(f"Top 10 Largest Installed Packages:\n{large_pkgs}")
            except Exception as e:
                results.append(f"Failed to get large packages: {str(e)}")

        elif any(term in prompt_lower for term in ["logs", "log check", "errors"]):
            results.append("=== Recent System Log Review ===")
            # Check journal for recent errors
            try:
                journal_errors = subprocess.run(
                    ["journalctl", "-p", "err", "-b", "--no-pager", "-n", "20"],
                    capture_output=True, text=True, check=False
                ).stdout.strip()
                if journal_errors:
                    results.append(f"Recent System Errors (last 20):\n{journal_errors}")
                else:
                    results.append("No recent system errors found in journal.")
            except Exception as e:
                results.append(f"Failed to check journal logs: {str(e)}")
            # Check syslog for recent critical messages
            try:
                syslog = "/var/log/syslog"
                if os.path.exists(syslog):
                    syslog_errors = subprocess.run(
                        ["grep", "-i", "error", syslog, "|", "tail", "-10"],
                        shell=True, capture_output=True, text=True, check=False
                    ).stdout.strip()
                    if syslog_errors:
                        results.append(f"Recent Syslog Errors:\n{syslog_errors}")
                    else:
                        results.append("No recent errors in syslog.")
                else:
                    results.append("Syslog not found (may require sudo to access).")
            except Exception as e:
                results.append(f"Failed to check syslog: {str(e)}")

        else:
            # Default combined quick scan
            results.append("=== Quick Proactive System Scan ===")
            # Add health checks
            try:
                uptime = subprocess.run(["uptime", "-p"], capture_output=True, text=True, check=False).stdout.strip()
                results.append(f"Uptime: {uptime}")
                df = subprocess.run(["df", "-h", "/"], capture_output=True, text=True, check=False).stdout.strip().splitlines()[-1]
                results.append(f"Root Disk Usage: {df}")
                free = subprocess.run(["free", "-h"], capture_output=True, text=True, check=False).stdout.strip().splitlines()[1]
                results.append(f"Memory Usage: {free}")
            except Exception as e:
                results.append(f"Health check failed: {str(e)}")
            # Add update check
            try:
                subprocess.run(["apt", "update", "-qq"], capture_output=True, text=True, check=False)
                upgradable = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True, check=False).stdout.strip()
                update_count = len(upgradable.splitlines()) if upgradable else 0
                results.append(f"Available Updates: {update_count} packages")
                sec_updates = subprocess.run(
                    ["apt", "list", "--upgradable", "|", "grep", "-i", "security"],
                    shell=True, capture_output=True, text=True, check=False
                ).stdout.strip()
                sec_count = len(sec_updates.splitlines()) if sec_updates else 0
                results.append(f"Pending Security Updates: {sec_count}")
            except Exception as e:
                results.append(f"Update check failed: {str(e)}")
            # Add failed login check
            try:
                auth_log = "/var/log/auth.log"
                if os.path.exists(auth_log):
                    failed = subprocess.run(
                        ["grep", "Failed password", auth_log, "|", "wc", "-l"],
                        shell=True, capture_output=True, text=True, check=False
                    ).stdout.strip()
                    results.append(f"Total Failed Login Attempts (all time): {failed}")
                else:
                    results.append("Auth log not accessible (requires sudo for full check).")
            except Exception as e:
                results.append(f"Login check failed: {str(e)}")
            results.append("\nRun a specific scan with: 'security scan', 'package audit', 'check system health', or 'review logs'")

        # Join all results
        final_output = "\n".join(results)
        # Use print_fn if available for progressive output
        if "print_fn" in context:
            context["print_fn"](final_output)
        return final_output

    except Exception as e:
        error_msg = f"Proactive Scanner failed: {str(e)}"
        if "print_fn" in context:
            context["print_fn"](error_msg)
        return error_msg

Wait, that's good. Let's check for clashes: PLUGIN_ROUTE_TOKEN is PROACTIVE_SCANNER, which is unique, right? The existing plugin is autorepair_greet_tr.py, so no clash. Triggers cover all the common phrases users would use for proactive scanning. Commands are useful slash commands.

Wait, also, the spec says for ROUTER plugins, PLUGIN_TRIGGERS are the phrases that trigger routing to this plugin. That's correct. Also, the run function returns a non-empty string, even on error, so it doesn't crash the app. All external calls are wrapped in try/except, so no crashes. Uses context["print_fn"] for output, which is correct. No hardcoded paths except standard system paths like /var/log/auth.log which are standard on Ubuntu/MakuluLinux, that's okay. Wait, but the spec says use os.path.expanduser("~") or context["user_home"], but those are system paths, not user-specific, so that's fine.

Wait, also, what about if deborphan is not installed? We handle that with a message telling the user to install it, that's good. Also, we truncate the upgradable packages list to 2000 characters so it doesn't flood the output, that's a good touch.

Wait, let's check the required metadata: all are present. PLUGIN_TYPE is ROUTER, which is correct for auto-repair plugins filling a capability gap. PLUGIN_ENABLED is True. PLUGIN_REQUIRES is empty, which is fine because we don't need any external Python packages, all are system utilities.

Wait, also, the file name should be autorepair_proactive_scanner.py, which matches the token lowercase, that's correct.

Is there anything missing? Let's see: the context keys are used correctly: print_fn is used, user_home is not needed here, but if we needed it we'd use context["user_home"], which we don't here. All system commands are run with subprocess.run, no shell=True unless necessary (like when using grep with pipes, which is needed for some commands). Wait, but when using shell=True, we need to make sure the commands are safe, which they are here, no user input passed directly to shell, right? Because the prompt is only used to detect the scan type, not passed to the shell commands. Oh right! All the subprocess commands are hardcoded, no user input is interpolated into the shell commands, so that's safe, no command injection risk. Perfect.

Wait, let's test the logic: if a user says "run a proactive scan", it goes to the default combined scan. If they say "check system health", it runs the health checks. If "security scan", runs security audit. If "package audit", runs package checks. If "review logs", runs log checks. That covers all the proactive scanner requests.

Also, error handling: if any command fails, it catches the exception, adds an error message to the results, so the plugin doesn't crash, and returns the partial results plus error, which is better than nothing.

Yes, that should work. Now, output the raw Python code, no markdown, no preamble, just the</think>
PLUGIN_NAME = "Proactive Scanner"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles proactive system scanning, health checks, security audits, and package management tasks on MakuluLinux"
PLUGIN_AUTHOR = "Electra Plugin Community"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = [
    "run proactive scan",
    "proactive scanner",
    "scan my system",
    "check system health",
    "security scan",
    "package audit",
    "check for updates",
    "review system logs",
    "proactive:"
]
PLUGIN_ROUTE_TOKEN = "PROACTIVE_SCANNER"
PLUGIN_COMMANDS = ["/proactive-scan", "/syshealth", "/secaudit", "/pkgaudit"]
PLUGIN_REQUIRES = []

import os
import subprocess

def run(prompt: str, context: dict) -> str:
    prompt_lower = prompt.lower().strip()
    results = []
    print_fn = context.get("print_fn", print)

    try:
        if any(term in prompt_lower for term in ["health", "system status", "syshealth"]):
            results.append("=== System Health Check ===")
            try:
                uptime = subprocess.run(["uptime", "-p"], capture_output=True, text=True, check=False).stdout.strip()
                results.append(f"System Uptime: {uptime}")
            except Exception as e:
                results.append(f"Failed to retrieve uptime: {str(e)}")
            try:
                disk = subprocess.run(["df", "-h", "/"], capture_output=True, text=True, check=False).stdout.strip().splitlines()[-1]
                results.append(f"Root Disk Usage: {disk}")
            except Exception as e:
                results.append(f"Failed to retrieve disk usage: {str(e)}")
            try:
                mem = subprocess.run(["free", "-h"], capture_output=True, text=True, check=False).stdout.strip().splitlines()[1]
                results.append(f"Memory Usage: {mem}")
            except Exception as e:
                results.append(f"Failed to retrieve memory usage: {str(e)}")
            try:
                cpu = subprocess.run("top -bn1 | grep 'load average'", shell=True, capture_output=True, text=True, check=False).stdout.strip()
                results.append(f"CPU Load Average: {cpu.split('load average:')[-1].strip()}")
            except Exception as e:
                results.append(f"Failed to retrieve CPU load: {str(e)}")
            try:
                proc_count = len(subprocess.run(["ps", "-e", "--no-headers"], capture_output=True, text=True, check=False).stdout.strip().splitlines())
                results.append(f"Running Processes: {proc_count}")
            except Exception as e:
                results.append(f"Failed to retrieve process count: {str(e)}")

        elif any(term in prompt_lower for term in ["security", "secaudit", "updates", "vulnerabilities"]):
            results.append("=== Security & Update Audit ===")
            try:
                subprocess.run(["apt", "update", "-qq"], capture_output=True, text=True, check=False)
                upgradable = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True, check=False).stdout.strip()
                if upgradable:
                    results.append(f"Available Updates ({len(upgradable.splitlines())} packages):\n{upgradable[:1500]}... [truncated]")
                else:
                    results.append("All system packages are up to date.")
            except Exception as e:
                results.append(f"Failed to check for updates: {str(e)}")
            try:
                sec_updates = subprocess.run(
                    "apt list --upgradable 2>/dev/null | grep -i security",
                    shell=True, capture_output=True, text=True, check=False
                ).stdout.strip()
                if sec_updates:
                    results.append(f"Pending Security Updates:\n{sec_updates}")
                else:
                    results.append("No pending security updates detected.")
            except Exception as e:
                results.append(f"Failed to check security updates: {str(e)}")
            try:
                auth_log = "/var/log/auth.log"
                if os.path.exists(auth_log):
                    failed_logins = subprocess.run(
                        f"grep 'Failed password' {auth_log} | tail -10",
                        shell=True, capture_output=True, text=True, check=False
                    ).stdout.strip()
                    if failed_logins:
                        results.append(f"Recent Failed Login Attempts:\n{failed_logins}")
                    else:
                        results.append("No recent failed login attempts found.")
                else:
                    results.append("Auth log not accessible (requires sudo privileges for full access).")
            except Exception as e:
                results.append(f"Failed to check login history: {str(e)}")

        elif any(term in prompt_lower for term in ["package", "pkgaudit", "outdated", "unnecessary"]):
            results.append("=== Package Audit ===")
            try:
                manual_pkgs = subprocess.run(
                    ["apt", "list", "--manual-installed"],
                    capture_output=True, text=True, check=False
                ).stdout.strip().splitlines()[1:]
                results.append(f"Manually Installed Packages: {len(manual_pkgs)} total")
            except Exception as e:
                results.append(f"Failed to retrieve installed package list: {str(e)}")
            try:
                orphaned = subprocess.run(["deborphan"], capture_output=True, text=True, check=False).stdout.strip()
                if orphaned:
                    results.append(f"Orphaned Packages (safe to remove):\n{orphaned}")
                else:
                    results.append("No orphaned packages found. Install `deborphan` for full orphan detection: sudo apt install deborphan")
            except Exception as e:
                results.append("deborphan not installed, skipping orphan check. Install with `sudo apt install deborphan` for full audit.")
            try:
                large_pkgs = subprocess.run(
                    "dpkg-query -W --showformat='${Installed-Size}\t${Package}\n' | sort -nr | head -10",
                    shell=True, capture_output=True, text=True, check=False
                ).stdout.strip()
                results.append(f"Top 10 Largest Installed Packages:\n{large_pkgs}")
            except Exception as e:
                results.append(f"Failed to retrieve large package list: {str(e)}")

        elif any(term in prompt_lower for term in ["logs", "log check", "errors"]):
            results.append("=== Recent System Log Review ===")
            try:
                journal_errors = subprocess.run(
                    ["journalctl", "-p", "err", "-b", "--no-pager", "-n", "20"],
                    capture_output=True, text=True, check=False
                ).stdout.strip()
                if journal_errors:
                    results.append(f"Recent System Errors (last 20 entries):\n{journal_errors}")
                else:
                    results.append("No recent system errors found in journal.")
            except Exception as e:
                results.append(f"Failed to check system journal: {str(e)}")
            try:
                syslog = "/var/log/syslog"
                if os.path.exists(syslog):
                    syslog_errors = subprocess.run(
                        f"grep -i error {syslog} | tail -10",
                        shell=True, capture_output=True, text=True, check=False
                    ).stdout.strip()
                    if syslog_errors:
                        results.append(f"Recent Syslog Errors:\n{syslog_errors}")
                    else:
                        results.append("No recent errors found in syslog.")
                else:
                    results.append("Syslog not accessible (requires sudo privileges for full access).")
            except Exception as e:
                results.append(f"Failed to check syslog: {str(e)}")

        else:
            results.append("=== Quick Proactive System Scan ===")
            try:
                uptime = subprocess.run(["uptime", "-p"], capture_output=True, text=True, check=False).stdout.strip()
                results.append(f"Uptime: {uptime}")
                disk = subprocess.run(["df", "-h", "/"], capture_output=True, text=True, check=False).stdout.strip().splitlines()[-1]
                results.append(f"Root Disk Usage: {disk}")
                mem = subprocess.run(["free", "-h"], capture_output=True, text=True, check=False).stdout.strip().splitlines()[1]
                results.append(f"Memory Usage: {mem}")
            except Exception as e:
                results.append(f"Health check failed: {str(e)}")
            try:
                subprocess.run(["apt", "update", "-qq"], capture_output=True, text=True, check=False)
                upgradable = subprocess.run(["apt", "list", "--upgradable"], capture_output=True, text=True, check=False).stdout.strip()
                update_count = len(upgradable.splitlines()) if upgradable else 0
                results.append(f"Available Updates: {update_count} packages")
                sec_updates = subprocess.run(
                    "apt list --upgradable 2>/dev/null | grep -i security",
                    shell=True, capture_output=True, text=True, check=False
                ).stdout.strip()
                sec_count = len(sec_updates.splitlines()) if sec_updates else 0
                results.append(f"Pending Security Updates: {sec_count}")
            except Exception as e:
                results.append(f"Update check failed: {str(e)}")
            try:
                auth_log = "/var/log/auth.log"
                if os.path.exists(auth_log):
                    failed = subprocess.run(
                        f"grep 'Failed password' {auth_log} | wc -l",
                        shell=True, capture_output=True, text=True, check=False
                    ).stdout.strip()
                    results.append(f"Total Failed Login Attempts (all time): {failed}")
                else:
                    results.append("Auth log not accessible (requires sudo for full check).")
            except Exception as e:
                results.append(f"Login check failed: {str(e)}")
            results.append("\nRun a targeted scan with: 'security scan', 'package audit', 'check system health', or 'review logs'")

        final_output = "\n".join(results)
        if "print_fn" in context:
            context["print_fn"](final_output)
        return final_output

    except Exception as e:
        error_msg = f"Proactive Scanner encountered a critical error: {str(e)}"
        if "print_fn" in context:
            context["print_fn"](error_msg)
        return error_msg