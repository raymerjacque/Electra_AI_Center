<think>Got it, let's tackle this. First, the user needs a plugin for the Proactive Scanner capability gap. Let's start with the required metadata.

First, PLUGIN_NAME should be "Proactive Scanner" right? Because that's the agent that failed. PLUGIN_VERSION "1.0.0", PLUGIN_DESCRIPTION something like "Handles proactive system scanning tasks on MakuluLinux", PLUGIN_AUTHOR can be "Electra Plugin Community", PLUGIN_ENABLED True, PLUGIN_TYPE ROUTER? Wait no, wait the error says it's an agent? Wait no, wait the spec says for capability gap, if it's a missing handler, wait the failed agent is Proactive Scanner, so wait let's check the spec. Wait the user said the error is from agent 'Proactive Scanner' with CAPABILITY_GAP, user asked 3 times for this task. So we need a plugin that handles proactive scanning tasks.

Wait first, PLUGIN_TYPE: wait, should it be AGENT? Wait no, wait the critical rules say for auto-repair plugins that fill capability gap, PLUGIN_TYPE is ROUTER? Wait no wait let's recheck the critical rules: "- PLUGIN_TYPE = "ROUTER" (for auto-repair plugins that fill a capability gap)". Oh right, that's the rule. Wait but the failed one was an agent? Wait no, maybe the router was supposed to route to a handler but there was none. Wait no, let's make sure the triggers are right. What triggers would a user use for proactive scanning? Like "run proactive scan", "scan system for issues", "proactive scanner check", "check system health proactively", right? So PLUGIN_TRIGGERS would be those. PLUGIN_ROUTE_TOKEN should be something unique, like "PROACTIVE_SCANNER" — wait make sure it doesn't clash, yeah that's unique. PLUGIN_COMMANDS can be ["/proactive-scan", "/sysscan"].

Then the run function. What does a proactive scanner do on MakuluLinux? Let's think: common checks: system updates available, disk usage, memory usage, running suspicious processes, log errors, maybe check for failed services. All using standard Linux commands, no extra packages needed? Wait wait, do we need any? Let's see, we can use subprocess to run commands like apt list --upgradable, df -h, free -h, systemctl --failed, journalctl -p err -n 10, ps aux for high resource processes. All those are standard on Ubuntu/MakuluLinux, no extra pip packages needed, so PLUGIN_REQUIRES can be empty list.

Wait also, need to handle errors, wrap all subprocess calls in try/except so it doesn't crash the app. Use context["print_fn"] to output progressive results, right? Because the spec says use print_fn instead of print.

Wait let's outline the run function steps:
1. First, print a header saying starting proactive system scan.
2. Check for available system updates: run apt update? Wait no, maybe just check upgradable without updating, so apt list --upgradable 2>/dev/null, count how many, report.
3. Check disk usage: run df -h, parse the output, flag any partitions over 90% usage.
4. Check memory usage: run free -h, report used vs total, flag if over 85% used.
5. Check for failed system services: systemctl --failed, list any.
6. Check recent critical journal errors: journalctl -p err -n 10 --no-pager, list any.
7. Check for high CPU/memory processes: ps aux --sort=-%cpu | head -n 6, ps aux --sort=-%mem | head -n 6, flag any over 80% CPU or memory.
8. Compile all results into a summary, return that.

Wait also, need to make sure all subprocess calls use subprocess.run, capture output, text=True, check for errors. Also, handle cases where commands fail (like if user isn't root? Wait but the plugin is in /root/.config, so running as root, right? But still, wrap in try/except.

Wait also, the setup function? Wait the spec mentions setup()? Wait let's check the spec again. Oh right, the AGENT section had a setup() example? Wait no, let's check: the spec says for plugins, if you need to install dependencies, do it in setup(). But since we don't need any extra packages, maybe setup can just pass, or do a quick check? Wait no, let's include a setup function that's optional, just returns True, or maybe checks if required commands exist? But no, the commands are standard.

Wait also, the required metadata: let's list them all correctly. Let's make sure PLUGIN_TRIGGERS are natural phrases a user would say to trigger the proactive scanner. Like "run proactive scan", "proactive system scan", "scan my system for issues", "check system health proactively", "proactive scanner check". That makes sense.

PLUGIN_ROUTE_TOKEN: "PROACTIVE_SCANNER" — that's unique, no clash.

PLUGIN_COMMANDS: ["/proactive-scan", "/sys-health-scan"] — those are useful slash commands.

Then the run function: takes prompt and context. Let's use context["print_fn"] to output each step as it runs, so the user sees progressive output. Then compile all the results into a final summary string to return.

Wait also, need to import subprocess, maybe shlex? No, the commands are simple, no user input, so safe. Wait but make sure to use subprocess.run with shell=False? Wait no, for commands like apt list --upgradable, we can run as a list: ["apt", "list", "--upgradable"], but redirect stderr to devnull, so capture stderr=subprocess.DEVNULL. Or use text=True, capture_output=True.

Wait let's test the commands:
- apt list --upgradable: returns lines like "Listing... Done", then the packages. So we can count the lines after "Listing... Done" to get the number of upgradable packages.
- df -h: output has columns, we can parse each line, split by whitespace, get the usage percentage (strip the %), convert to int, flag if >90.
- free -h: get the "Mem" line, used and total, calculate percentage, flag >85.
- systemctl --failed: if output is empty, no failed services, else list them.
- journalctl -p err -n 10 --no-pager: if empty, no recent critical errors, else list them.
- ps aux --sort=-%cpu | head -n 6: get the top 5 processes (since first line is header), check if any CPU usage >80, flag.
- ps aux --sort=-%mem | head -n 6: same for memory >80.

Also, handle exceptions: if any command fails, just note that in the report, don't crash.

Wait also, the context has cwd, user_home, etc., but we don't need those here. Just use print_fn for output.

Wait let's structure the code:

First, the module docstring? Or start with imports. Let's start with imports: import subprocess, maybe from typing import Dict, Any? No, not necessary, but okay.

Then the required metadata:

PLUGIN_NAME = "Proactive Scanner"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles proactive system health and security scanning tasks on MakuluLinux"
PLUGIN_AUTHOR = "Electra Plugin Community"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []  # No external pip dependencies, uses standard Linux utilities
PLUGIN_TRIGGERS = [
    "run proactive scan",
    "proactive system scan",
    "scan my system for issues",
    "check system health proactively",
    "proactive scanner check",
    "run system health scan"
]
PLUGIN_ROUTE_TOKEN = "PROACTIVE_SCANNER"
PLUGIN_COMMANDS = ["/proactive-scan", "/sys-health-scan"]

Then the setup function? Wait the spec mentions setup()? Let's check the spec again. Oh right, in the AGENT section there's a setup() example, but for ROUTER plugins, do we need it? Wait the spec says "If a pip package is needed, declare it in PLUGIN_REQUIRES and install gracefully in setup()". Since we don't need any, we can either omit setup, or include a no-op setup. Let's include a setup function that returns True, just in case.

def setup() -> bool:
    """Optional setup function, runs once when plugin is loaded."""
    return True

Then the run function:

def run(prompt: str, context: Dict[str, Any]) -> str:
    print_fn = context.get("print_fn", print)
    results = []
    issues_found = 0

    try:
        print_fn("🔍 Starting Proactive System Scan on MakuluLinux...")
        print_fn("=" * 50)
        results.append("🔍 Proactive System Scan Report")
        results.append("=" * 50)

        # 1. Check for available system updates
        try:
            print_fn("\n[1/6] Checking for available system updates...")
            update_cmd = subprocess.run(
                ["apt", "list", "--upgradable"],
                capture_output=True,
                text=True,
                timeout=30
            )
            upgradable = [line for line in update_cmd.stdout.splitlines() if line and not line.startswith("Listing...")]
            if upgradable:
                issues_found += 1
                results.append(f"\n⚠️  {len(upgradable)} system updates available:")
                results.extend([f"  • {pkg}" for pkg in upgradable[:10]])  # Show first 10
                if len(upgradable) > 10:
                    results.append(f"  ... and {len(upgradable)-10} more")
            else:
                results.append("\n✅ System is up to date, no pending updates.")
        except Exception as e:
            results.append(f"\n❌ Failed to check for updates: {str(e)}")

        # 2. Check disk usage
        try:
            print_fn("\n[2/6] Checking disk usage...")
            df_cmd = subprocess.run(
                ["df", "-h"],
                capture_output=True,
                text=True,
                timeout=15
            )
            high_usage = []
            for line in df_cmd.stdout.splitlines()[1:]:  # Skip header
                parts = line.split()
                if len(parts) >= 5:
                    usage = parts[4].strip("%")
                    try:
                        if int(usage) > 90:
                            high_usage.append(f"{parts[5]} ({usage}% used)")
                    except ValueError:
                        continue
            if high_usage:
                issues_found += 1
                results.append(f"\n⚠️  High disk usage detected on {len(high_usage)} partitions:")
                results.extend([f"  • {part}" for part in high_usage])
            else:
                results.append("\n✅ All partitions have healthy disk usage (<90%).")
        except Exception as e:
            results.append(f"\n❌ Failed to check disk usage: {str(e)}")

        # 3. Check memory usage
        try:
            print_fn("\n[3/6] Checking memory usage...")
            mem_cmd = subprocess.run(
                ["free", "-h"],
                capture_output=True,
                text=True,
                timeout=15
            )
            for line in mem_cmd.stdout.splitlines():
                if line.startswith("Mem:"):
                    parts = line.split()
                    total = parts[1]
                    used = parts[2]
                    usage_pct = round((float(used.replace('Gi', '').replace('Mi', '')) / float(total.replace('Gi', '').replace('Mi', ''))) * 100)
                    if usage_pct > 85:
                        issues_found += 1
                        results.append(f"\n⚠️  High memory usage: {used} / {total} ({usage_pct}% used)")
                    else:
                        results.append(f"\n✅ Memory usage healthy: {used} / {total} ({usage_pct}% used)")
                    break
        except Exception as e:
            results.append(f"\n❌ Failed to check memory usage: {str(e)}")

        # 4. Check for failed system services
        try:
            print_fn("\n[4/6] Checking for failed system services...")
            failed_cmd = subprocess.run(
                ["systemctl", "--failed"],
                capture_output=True,
                text=True,
                timeout=15
            )
            failed_services = [line for line in failed_cmd.stdout.splitlines() if line and not line.startswith("UNIT")]
            if failed_services:
                issues_found += 1
                results.append(f"\n⚠️  {len(failed_services)} failed system services detected:")
                results.extend([f"  • {svc}" for svc in failed_services[:5]])
                if len(failed_services) > 5:
                    results.append(f"  ... and {len(failed_services)-5} more")
            else:
                results.append("\n✅ No failed system services found.")
        except Exception as e:
            results.append(f"\n❌ Failed to check system services: {str(e)}")

        # 5. Check recent critical journal errors
        try:
            print_fn("\n[5/6] Checking for recent critical system errors...")
            journal_cmd = subprocess.run(
                ["journalctl", "-p", "err", "-n", "10", "--no-pager"],
                capture_output=True,
                text=True,
                timeout=15
            )
            errors = [line for line in journal_cmd.stdout.splitlines() if line.strip()]
            if errors:
                issues_found += 1
                results.append(f"\n⚠️  {len(errors)} recent critical errors found in system logs:")
                results.extend([f"  • {err}" for err in errors[:5]])
                if len(errors) > 5:
                    results.append(f"  ... and {len(errors)-5} more")
            else:
                results.append("\n✅ No recent critical system errors found.")
        except Exception as e:
            results.append(f"\n❌ Failed to check system logs: {str(e)}")

        # 6. Check for high resource processes
        try:
            print_fn("\n[6/6] Checking for high resource usage processes...")
            # High CPU
            cpu_cmd = subprocess.run(
                ["ps", "aux", "--sort=-%cpu"],
                capture_output=True,
                text=True,
                timeout=15
            )
            high_cpu = []
            for line in cpu_cmd.stdout.splitlines()[1:6]:  # Top 5 processes
                parts = line.split()
                if len(parts) >= 11:
                    cpu = parts[2].replace(',', '.')
                    try:
                        if float(cpu) > 80:
                            high_cpu.append(f"{parts[10]} ({cpu}% CPU)")
                    except ValueError:
                        continue
            # High Memory
            mem_cmd = subprocess.run(
                ["ps", "aux", "--sort=-%mem"],
                capture_output=True,
                text=True,
                timeout=15
            )
            high_mem = []
            for line in mem_cmd.stdout.splitlines()[1:6]:
                parts = line.split()
                if len(parts) >= 11:
                    mem = parts[3].replace(',', '.')
                    try:
                        if float(mem) > 80:
                            high_mem.append(f"{parts[10]} ({mem}% MEM)")
                    except ValueError:
                        continue

            if high_cpu or high_mem:
                issues_found += 1
                if high_cpu:
                    results.append(f"\n⚠️  High CPU usage processes:")
                    results.extend([f"  • {proc}" for proc in high_cpu])
                if high_mem:
                    results.append(f"\n⚠️  High memory usage processes:")
                    results.extend([f"  • {proc}" for proc in high_mem])
            else:
                results.append("\n✅ No abnormally high resource usage processes detected.")
        except Exception as e:
            results.append(f"\n❌ Failed to check running processes: {str(e)}")

        # Final summary
        print_fn("\n" + "=" * 50)
        if issues_found == 0:
            results.append("\n🎉 Scan complete: No issues found! System is healthy.")
        else:
            results.append(f"\n✅ Scan complete: {issues_found} issue(s) found that may need attention.")
        results.append("=" * 50)

        return "\n".join(results)

    except Exception as e:
        error_msg = f"❌ Proactive scan failed with critical error: {str(e)}"
        print_fn(error_msg)
        return error_msg

Wait wait, but the memory calculation: if it's in Mi or Gi, replacing Gi with empty and converting to float? Wait maybe better to use a helper to convert to Mi? Or just approximate, since it's a scan. Alternatively, use the percentage from free? Wait no, free -h doesn't show percentage. Oh right, free -m gives in Mi, and we can calculate percentage. Let's adjust that part:

Wait for memory check:
mem_cmd = subprocess.run(
    ["free", "-m"],
    capture_output=True,
    text=True,
    timeout=15
)
for line in mem_cmd.stdout.splitlines():
    if line.startswith("Mem:"):
        parts = line.split()
        total = int(parts[1])
        used = int(parts[2])
        usage_pct = round((used / total) * 100) if total > 0 else 0
        if usage_pct > 85:
            issues_found += 1
            results.append(f"\n⚠️  High memory usage: {used}Mi / {total}Mi ({usage_pct}% used)")
        else:
            results.append(f"\n✅ Memory usage healthy: {used}Mi / {total}Mi ({usage_pct}% used)")
        break

That's better, no unit conversion issues.

Also, for the apt list --upgradable, if the user is not root, does it work? Wait the plugin is in /root/.config, so running as root, right? But if not, apt list --upgradable still works for regular user, just shows user packages. But maybe add a note? No, it's okay.

Also, the journalctl command: if running as non-root, it might not show all logs, but again, since the plugin is in root's config, it's running as root, so that's fine.

Wait also, the PLUGIN_TYPE is ROUTER as per the critical rules for auto-repair plugins. That's correct.

Wait let's check all required metadata are present: yes, PLUGIN_NAME, VERSION, DESCRIPTION, AUTHOR, ENABLED, TYPE, TRIGGERS, ROUTE_TOKEN, COMMANDS, REQUIRES. All there.

Wait also, the run function returns a non-empty string, which it does. All external calls are wrapped in try/except, so no crashes. No hardcoded paths, uses standard commands. Uses print_fn from context for output.

Wait what about the context keys? We're using print_fn, which is in v2.0 context, that's correct.

Wait also, the file name should be autorepair_proactive_scanner.py, right? Because the route token is PROACTIVE_SCANNER, lowercase is proactive_scanner, so the file is autorepair_proactive_scanner.py. But the user just wants the plugin code, right? The output is just the Python source.

Wait let's check for any issues: the subprocess commands are all standard on Ubuntu/MakuluLinux, no extra packages needed, so PLUGIN_REQUIRES is empty, correct.

Wait also, the triggers are natural language, so when a user says "run a proactive scan" or "check my system proactively", it triggers the plugin. That matches the error where the user repeatedly requested this type of task, so the triggers cover those phrases.

Wait let's adjust the triggers to be more natural: maybe add "proactive scanner" as a trigger, since the failed agent was called Proactive Scanner. So PLUGIN_TRIGGERS can be:
PLUGIN_TRIGGERS = [
    "run proactive scan",
    "proactive system scan",
    "scan my system for issues",
    "check system health proactively",
    "proactive scanner check",
    "use proactive scanner",
    "proactive scanner"
]
That's better, covers more natural phrases.

Also, the PLUGIN_DESCRIPTION: "Handles proactive system health, security, and update scanning tasks for MakuluLinux" — that's more accurate.

Wait also, in the run function, when we get the top processes, the ps aux output: the command is the last field, right? Let's confirm: ps aux fields are: USER PID %CPU %MEM VSZ RSS TTY STAT START TIME COMMAND. So yes, parts[10] is the command, that's correct.

Wait also, for the high CPU check: parts[2] is %CPU, which is a float, so converting to float is correct. Same for %MEM in parts[3].

What about if the system doesn't have systemctl? No, MakuluLinux is Ubuntu-based, uses systemd, so systemctl is present. journalctl is also present.

What about if apt is not present? No, it's Ubuntu-based, apt is there.

All right, that should work. Let's put it all together now, making sure there are no mark</think>
import subprocess
from typing import Dict, Any

PLUGIN_NAME = "Proactive Scanner"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles proactive system health, security, and update scanning tasks for MakuluLinux"
PLUGIN_AUTHOR = "Electra Plugin Community"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []  # Uses standard Linux utilities, no external pip dependencies
PLUGIN_TRIGGERS = [
    "run proactive scan",
    "proactive system scan",
    "scan my system for issues",
    "check system health proactively",
    "proactive scanner check",
    "use proactive scanner",
    "proactive scanner"
]
PLUGIN_ROUTE_TOKEN = "PROACTIVE_SCANNER"
PLUGIN_COMMANDS = ["/proactive-scan", "/sys-health-scan"]

def setup() -> bool:
    """Optional setup function, runs once when plugin is loaded."""
    return True

def run(prompt: str, context: Dict[str, Any]) -> str:
    print_fn = context.get("print_fn", print)
    results = []
    issues_found = 0

    try:
        print_fn("🔍 Starting Proactive System Scan on MakuluLinux...")
        print_fn("=" * 50)
        results.append("🔍 Proactive System Scan Report")
        results.append("=" * 50)

        # 1. Check for available system updates
        try:
            print_fn("\n[1/6] Checking for available system updates...")
            update_cmd = subprocess.run(
                ["apt", "list", "--upgradable"],
                capture_output=True,
                text=True,
                timeout=30
            )
            upgradable = [line for line in update_cmd.stdout.splitlines() if line and not line.startswith("Listing...")]
            if upgradable:
                issues_found += 1
                results.append(f"\n⚠️  {len(upgradable)} system updates available:")
                results.extend([f"  • {pkg}" for pkg in upgradable[:10]])
                if len(upgradable) > 10:
                    results.append(f"  ... and {len(upgradable)-10} more")
            else:
                results.append("\n✅ System is up to date, no pending updates.")
        except Exception as e:
            results.append(f"\n❌ Failed to check for updates: {str(e)}")

        # 2. Check disk usage
        try:
            print_fn("\n[2/6] Checking disk usage...")
            df_cmd = subprocess.run(
                ["df", "-h"],
                capture_output=True,
                text=True,
                timeout=15
            )
            high_usage = []
            for line in df_cmd.stdout.splitlines()[1:]:
                parts = line.split()
                if len(parts) >= 5:
                    usage = parts[4].strip("%")
                    try:
                        if int(usage) > 90:
                            high_usage.append(f"{parts[5]} ({usage}% used)")
                    except ValueError:
                        continue
            if high_usage:
                issues_found += 1
                results.append(f"\n⚠️  High disk usage detected on {len(high_usage)} partitions:")
                results.extend([f"  • {part}" for part in high_usage])
            else:
                results.append("\n✅ All partitions have healthy disk usage (<90%).")
        except Exception as e:
            results.append(f"\n❌ Failed to check disk usage: {str(e)}")

        # 3. Check memory usage
        try:
            print_fn("\n[3/6] Checking memory usage...")
            mem_cmd = subprocess.run(
                ["free", "-m"],
                capture_output=True,
                text=True,
                timeout=15
            )
            for line in mem_cmd.stdout.splitlines():
                if line.startswith("Mem:"):
                    parts = line.split()
                    total = int(parts[1])
                    used = int(parts[2])
                    usage_pct = round((used / total) * 100) if total > 0 else 0
                    if usage_pct > 85:
                        issues_found += 1
                        results.append(f"\n⚠️  High memory usage: {used}Mi / {total}Mi ({usage_pct}% used)")
                    else:
                        results.append(f"\n✅ Memory usage healthy: {used}Mi / {total}Mi ({usage_pct}% used)")
                    break
        except Exception as e:
            results.append(f"\n❌ Failed to check memory usage: {str(e)}")

        # 4. Check for failed system services
        try:
            print_fn("\n[4/6] Checking for failed system services...")
            failed_cmd = subprocess.run(
                ["systemctl", "--failed"],
                capture_output=True,
                text=True,
                timeout=15
            )
            failed_services = [line for line in failed_cmd.stdout.splitlines() if line and not line.startswith("UNIT")]
            if failed_services:
                issues_found += 1
                results.append(f"\n⚠️  {len(failed_services)} failed system services detected:")
                results.extend([f"  • {svc}" for svc in failed_services[:5]])
                if len(failed_services) > 5:
                    results.append(f"  ... and {len(failed_services)-5} more")
            else:
                results.append("\n✅ No failed system services found.")
        except Exception as e:
            results.append(f"\n❌ Failed to check system services: {str(e)}")

        # 5. Check recent critical journal errors
        try:
            print_fn("\n[5/6] Checking for recent critical system errors...")
            journal_cmd = subprocess.run(
                ["journalctl", "-p", "err", "-n", "10", "--no-pager"],
                capture_output=True,
                text=True,
                timeout=15
            )
            errors = [line for line in journal_cmd.stdout.splitlines() if line.strip()]
            if errors:
                issues_found += 1
                results.append(f"\n⚠️  {len(errors)} recent critical errors found in system logs:")
                results.extend([f"  • {err}" for err in errors[:5]])
                if len(errors) > 5:
                    results.append(f"  ... and {len(errors)-5} more")
            else:
                results.append("\n✅ No recent critical system errors found.")
        except Exception as e:
            results.append(f"\n❌ Failed to check system logs: {str(e)}")

        # 6. Check for high resource processes
        try:
            print_fn("\n[6/6] Checking for high resource usage processes...")
            # High CPU check
            cpu_cmd = subprocess.run(
                ["ps", "aux", "--sort=-%cpu"],
                capture_output=True,
                text=True,
                timeout=15
            )
            high_cpu = []
            for line in cpu_cmd.stdout.splitlines()[1:6]:
                parts = line.split()
                if len(parts) >= 11:
                    try:
                        cpu_usage = float(parts[2].replace(',', '.'))
                        if cpu_usage > 80:
                            high_cpu.append(f"{parts[10]} ({cpu_usage}% CPU)")
                    except ValueError:
                        continue
            # High Memory check
            mem_cmd = subprocess.run(
                ["ps", "aux", "--sort=-%mem"],
                capture_output=True,
                text=True,
                timeout=15
            )
            high_mem = []
            for line in mem_cmd.stdout.splitlines()[1:6]:
                parts = line.split()
                if len(parts) >= 11:
                    try:
                        mem_usage = float(parts[3].replace(',', '.'))
                        if mem_usage > 80:
                            high_mem.append(f"{parts[10]} ({mem_usage}% MEM)")
                    except ValueError:
                        continue

            if high_cpu or high_mem:
                issues_found += 1
                if high_cpu:
                    results.append(f"\n⚠️  High CPU usage processes:")
                    results.extend([f"  • {proc}" for proc in high_cpu])
                if high_mem:
                    results.append(f"\n⚠️  High memory usage processes:")
                    results.extend([f"  • {proc}" for proc in high_mem])
            else:
                results.append("\n✅ No abnormally high resource usage processes detected.")
        except Exception as e:
            results.append(f"\n❌ Failed to check running processes: {str(e)}")

        # Final summary
        print_fn("\n" + "=" * 50)
        if issues_found == 0:
            results.append("\n🎉 Scan complete: No issues found! System is healthy.")
        else:
            results.append(f"\n✅ Scan complete: {issues_found} issue(s) found that may need attention.")
        results.append("=" * 50)

        return "\n".join(results)

    except Exception as e:
        error_msg = f"❌ Proactive scan failed with critical error: {str(e)}"
        print_fn(error_msg)
        return error_msg