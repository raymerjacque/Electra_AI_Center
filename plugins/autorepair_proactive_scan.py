<think>We are given a specific error: "CAPABILITY_GAP" for a request type that the user has repeatedly asked for (3 times) and there's no dedicated handler.
 The error message says: "User repeatedly requested this type of task (3 times) with no dedicated handler."

 We are to write a plugin that handles this type of request. However, note that the user's request was simply "yes", which is ambiguous.

 But note: the error occurred in an agent named 'Proactive Scanner'. This suggests that the user might have been trying to run a proactive scan or something similar.

 However, the user's request was just "yes". This might be in response to a prompt from the Proactive Scanner agent? Or maybe the user is trying to confirm something?

 Since the error says "this type of task", we need to infer what the task is. The error message says the user repeatedly requested this type of task (3 times). So the user has been trying to do something that the system doesn't have a handler for.

 Given the context of the Proactive Scanner agent, it's likely that the user is trying to run a system scan or a security scan. But note: the user said "yes". This might be a confirmation to run a scan.

 However, the error says there's no dedicated handler for this type of task. So we need to create a plugin that can handle such requests.

 But wait: the user's request was just "yes". How do we know what they are saying yes to? Maybe the Proactive Scanner agent asked a question and the user said "yes". But the error says the user repeatedly requested this type of task. So maybe the user is trying to run a scan by saying "yes" to a prompt that never comes? Or maybe the user is trying to run a scan by saying "scan" or something, but the error says the request was "yes".

 Let's re-read: the user requested: yes. And the error says: User repeatedly requested this type of task (3 times) with no dedicated handler.

 So the task type is "yes"? That doesn't make sense.

 Alternatively, maybe the user has been trying to run a proactive scan and the system doesn't have a handler for that. The error message might be generic and the actual request that triggered the error was something else, but the error message says the user repeatedly requested "this type of task". The error message doesn't specify the task, but the agent that failed is 'Proactive Scanner'.

 Since we are writing a plugin to fill the capability gap, we need to decide what the plugin should do.

 Given the agent name 'Proactive Scanner', it's likely that the user wants to run a system scan. But what kind of scan? Security? Performance? File system?

 Since we are on MakuluLinux (Ubuntu-based), we can use common Linux tools.

 However, note: the plugin must be a ROUTER plugin (as per the specification for auto-repair plugins) and we are to set PLUGIN_TYPE = "ROUTER".

 We are also told to choose a PLUGIN_ROUTE_TOKEN that does not clash with existing ones.

 Since the error is about a capability gap for a task that the user repeatedly requested, and the agent that failed is 'Proactive Scanner', let's assume the user wants to run a proactive scan.

 We can create a plugin that triggers on words like "scan", "proactive scan", "security scan", etc.

 But note: the user's request was "yes". So maybe the user is trying to confirm a scan? But the error says the user repeatedly requested this type of task. So maybe the user has been saying "yes" to run a scan? That doesn't seem right.

 Alternatively, maybe the Proactive Scanner agent is supposed to ask the user if they want to run a scan, and the user says "yes", but the agent doesn't have a handler for the "yes" response? That would be a design flaw in the agent.

 However, we are to write a plugin that handles the request. Since the error says the user repeatedly requested this type of task, and the task is not handled, we must create a plugin that handles the task.

 But what is the task? The error message doesn't specify. We only know that the user said "yes" and the agent 'Proactive Scanner' failed.

 Since we are the plugin developer and we are to fill the gap, we have to make an educated guess.

 Given the agent name, I think the intended task is to run a proactive scan. So let's create a plugin that triggers on words that indicate a desire to run a scan.

 However, note that the user's request was just "yes". So maybe the user is in a conversation and the last message from the system was a question about running a scan? But the error says the user repeatedly requested this type of task. So maybe the user has been trying to run a scan by saying "yes" without being prompted? That seems odd.

 Alternatively, maybe the user has been trying to run a scan by saying "scan" and the system doesn't have a handler, and then the user said "yes" to something else and that also failed? The error message says the user repeatedly requested this type of task (3 times). So the same type of task 3 times.

 Since we don't have more context, let's design a plugin that can handle a proactive scan request.

 We'll create a ROUTER plugin that triggers on:
   "scan", "proactive scan", "security scan", "run scan", "start scan", "perform scan", "system scan"

 And when triggered, it will run a set of common system checks on Ubuntu (MakuluLinux is Ubuntu-based).

 We'll use the context to get the current working directory and user home, and we'll run some commands like:
   - Check for open ports (netstat or ss)
   - Check for suspicious processes (ps)
   - Check for world-writable files (find)
   - Check for SUID/SGID files (find)
   - Check for recent logins (last)
   - Check for failed login attempts (grep /var/log/auth.log)

 But note: we must be cautious because running these commands might require sudo. We don't want to run sudo without the user's knowledge.

 We can run the commands without sudo and report what we can, and for commands that require sudo, we can note that.

 Alternatively, we can ask the user for sudo password? But that's not safe and the plugin shouldn't handle passwords.

 Since the plugin is running in the context of the user, we can only run commands that the user has permission for.

 We'll design the plugin to run a set of checks and return a report.

 Steps:

 1. Define the plugin metadata.
 2. Define triggers that match the user's intent to run a scan.
 3. In the run function, we'll run a series of commands and collect the output.
 4. We'll format the output and return it.

 However, note: the user might have said "yes" to a prompt that we are not aware of. But since we are creating a plugin that triggers on scan-related words, we are assuming that the user's "yes" was in response to a question about scanning? But the error says the user repeatedly requested this type of task. So maybe the user has been saying "yes" to run a scan? That doesn't match.

 Alternatively, maybe the user has been trying to run a scan by saying "yes" because the system asked "Do you want to run a proactive scan?" and the user said "yes", but the system doesn't have a handler for the "yes" response? That would mean the system should have a state machine that remembers the last question. But we don't have that context.

 Given the ambiguity, I think the best approach is to create a plugin that handles the intent to run a proactive scan, and we'll trigger on words that are likely to be used to request a scan.

 But note: the user's request was "yes". So if the user says "yes" and there's no active question, then maybe we should interpret that as a request to run a scan? That might be too broad.

 However, the error says the user repeatedly requested this type of task. So the task is the same each time. And the user said "yes" each time? That seems unlikely.

 Let's look at the error again: "User repeatedly requested this type of task (3 times) with no dedicated handler."

 The error is from the agent 'Proactive Scanner'. So maybe the Proactive Scanner agent is supposed to handle scan requests, but it doesn't. And the user has been trying to run a scan 3 times.

 So we are creating a plugin that will handle scan requests, and we'll name the token something like "PROACTIVE_SCAN".

 We'll set:
   PLUGIN_ROUTE_TOKEN = "PROACTIVE_SCAN"

 And we'll set triggers that are likely to be used to request a scan.

 But note: the user might have been saying "yes" because the system asked "Do you want to run a proactive scan?" and the user said "yes". But if the system doesn't have a handler for the "yes" response, then we need to handle the "yes" in the context of a pending question? That's more complex.

 Since we don't have state, we cannot know if there was a pending question. So we have to assume that the user's "yes" is a standalone request to run a scan? That might be a bad assumption.

 Alternatively, we can create a plugin that triggers on "yes" only if the last message from the system was a question about scanning? But we don't have the chat history in the context? Actually, we do: context["chat_history"] is a list of recent conversation.

 We can check the last message from the system (role: "assistant") and see if it was a question about scanning. But note: the chat_history might be long and we only have recent messages.

 However, the specification says chat_history is read-only and recent. We can check the last few messages.

 But note: the user might have said "yes" to a different question. So we don't want to run a scan if the last question was about something else.

 Given the complexity and the fact that we are only given the error and the user's request was "yes", I think we have to make a simpler plugin that triggers on scan-related words and also on "yes" if the last system message was about scanning.

 However, the error says the user repeatedly requested this type of task. So maybe the user has been saying "yes" 3 times and each time the system didn't know what to do. So we can assume that the user is trying to confirm a scan.

 Let's design:

 We'll have two sets of triggers:
  1. Direct scan requests: ["scan", "proactive scan", ...]
  2. Confirmation: ["yes", "y"] but only if the last system message was a question about scanning.

 But note: the plugin is a ROUTER plugin and we are given the entire prompt. We can check the prompt for "yes" and also check the chat history.

 However, the chat_history in the context is the recent conversation. We can look at the last assistant message and see if it contains a question about scanning.

 Steps in run(prompt, context):

  If the prompt is one of the direct scan triggers, then run the scan.

  Else if the prompt is "yes" or "y", then check the chat_history for the last assistant message. If that message contains words like "scan", "proactive", "security", etc., then run the scan.

  Otherwise, we don't handle it and return None? But the run function must return a string. We can return an empty string? But the specification says must return a non-empty string on success.

  Alternatively, we can return a message that we didn't understand? But then the router might try other plugins.

  However, note: the plugin is triggered by the triggers. So if the prompt doesn't match the triggers, the router won't call this plugin.

  So we only get called if the prompt matches one of our triggers.

  Therefore, we can set:

    PLUGIN_TRIGGERS = ["scan", "proactive scan", "security scan", "run scan", "start scan", "perform scan", "system scan", "yes", "y"]

  But then we have to be careful: if the user says "yes" to a non-scan question, we don't want to run a scan.

  So in the run function, we check:

    if prompt in ["yes", "y"]:
        # Check the last assistant message in chat_history for scan-related words.
        # If found, run the scan.
        # Otherwise, return a message that we are not sure what the user is confirming.

    else:
        # It's a direct scan request, run the scan.

  But note: the chat_history might not have the last assistant message? We have to be cautious.

  Let's code accordingly.

  However, note: the error says the user repeatedly requested this type of task. So maybe the user has been saying "yes" and the system didn't have a handler for the "yes" because it was expecting a scan confirmation? So we are adding the handler for the "yes" in the context of a scan.

  But what if the user says "yes" to something else? We don't want to run a scan then.

  So we must check the context.

  Implementation:

  We'll define a list of scan_related_words = ["scan", "proactive", "security", "system check", "vulnerability"]

  Then, if the prompt is "yes" or "y", we look at the chat_history (which is a list of dicts with 'role' and 'content').

  We traverse the chat_history from the end to the beginning until we find an assistant message. Then we check if that message contains any of the scan_related_words.

  If it does, we run the scan.

  If it doesn't, we return: "I'm sorry, I only handle scan confirmations. If you want to run a scan, please ask for it directly."

  But note: the plugin is triggered by "yes", so if the user says "yes" and the last assistant message is not about scanning, we are still triggered and we return that message. That might be acceptable.

  Alternatively, we can avoid triggering on "yes" unless the last assistant message is about scanning? But the triggers are fixed. We cannot change the triggers dynamically.

  So we have to handle it in the run function.

  Let's code accordingly.

  However, note: the user might have said "yes" and then the chat_history might have multiple assistant messages. We only care about the last one.

  Steps for the scan:

  We'll run a series of commands and collect the output. We'll use subprocess.run and capture the output.

  We'll run:

  1. Check open ports: `ss -tuln` (or netstat if ss not available)
  2. Check for suspicious processes: `ps aux`
  3. Check for world-writable files in /home, /tmp, /var/tmp: `find /home /tmp /var/tmp -type f -perm -o=w`
  4. Check for SUID/SGID files: `find / -type f -perm -4000 -o -perm -2000` (but this might take long and we might not have permission for all directories)
  5. Check recent logins: `last`
  6. Check failed login attempts: `grep "Failed password" /var/log/auth.log | tail -10` (but note: the log might be in a different location? On Ubuntu it's /var/log/auth.log)

  We'll run these commands and format the output.

  We must be cautious: some commands might take a long time or produce a lot of output. We can limit the output.

  Also, we must handle errors (like command not found, permission denied).

  We'll use try/except for each command.

  We'll return a string with the results.

  Let's code accordingly.

  But note: the plugin must not crash the host app. So we must catch all exceptions.

  We'll write a helper function to run a command and return the output or an error message.

  We'll also use context["print_fn"] to show progressive output? The specification says we can use context["print_fn"] to show progressive output. But note: the run function returns a string. We can also use print_fn to print during the run, and then return a summary.

  However, the specification says: "Use context["print_fn"](text) to show progressive output instead of print()". So we can use that to show the user that we are running the scan.

  We'll do:

    context["print_fn"]("Starting proactive scan...")

    Then run each check and print the results as we go.

    Then return a final summary.

  But note: the run function must return a string. We can return the entire report as a string, and also print it progressively.

  Alternatively, we can build a string and return it, and also print it progressively? That would duplicate.

  Let's do:

    report = "Proactive Scan Report:\n\n"

    For each check, run the command, capture the output, and append to report.

    Then return report.

  And also, we can print each section as we complete it? But the user will see the final report anyway.

  Since the specification says we can use print_fn for progressive output, let's do:

    context["print_fn"]("Running open ports check...")
    output = run_command("ss -tuln")
    report += f"Open Ports:\n{output}\n\n"

    and so on.

  But note: the print_fn might be for the GUI? We are not sure. But it's provided so we can use it.

  Let's code accordingly.

  However, note: the user might be in a non-GUI environment? The context has gui_active. We can check that and if not, use print? But the specification says to use print_fn.

  We'll use print_fn for all output.

  Now, let's code the plugin.

  We'll name the plugin "Proactive Scanner Plugin" and set the token to "PROACTIVE_SCAN".

  We'll set the triggers to include both direct scan requests and "yes"/"y".

  But note: the error says the user repeatedly requested this type of task. So maybe the user has been saying "yes" and we are now handling it.

  We'll code accordingly.

  However, note: the user might have been saying "yes" to a different question. We are taking a risk.

  But since we are filling a capability gap and the error is from the Proactive Scanner agent, we assume that the user's "yes" is in the context of a scan.

  Let's code.

  Important: We must not crash. So we'll wrap each command in try/except and if a command fails, we'll note that in the report.

  We'll also check if the command exists? We can use `which` but that might not be necessary. We'll just try to run and catch the exception.

  Let's write the plugin.

  Note: We are to output only the raw Python source.

  We'll start with the imports and metadata.

  We'll use subprocess and shlex for safe command splitting? But we are running fixed commands, so we can use shell=True? But that's a security risk if we were to take user input. We are not, so it's okay.

  Alternatively, we can split the command and use shell=False. But for commands with pipes and redirections, we need shell=True.

  We are using pipes in the auth.log command? Actually, we are using `grep` and `tail`. We can do:

    command = "grep 'Failed password' /var/log/auth.log | tail -10"

  So we need shell=True.

  But note: using shell=True with fixed commands is acceptable.

  We'll do:

    import subprocess

    def run_command(cmd):
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=30)
            return result.stdout if result.stdout else result.stderr
        except Exception as e:
            return f"Error: {str(e)}"

  But note: the command might take longer than 30 seconds? We set a timeout.

  Now, let's code the plugin.

  We'll also check if the user is root? We can run `whoami` but we don't need to. We'll just run the commands and see what we get.

  Let's code.</think>
"""
Proactive Scanner Plugin - Handles system security scanning requests
Auto-generated to fill capability gap for repeated scan requests
"""

import subprocess
import os
import re
from datetime import datetime

PLUGIN_NAME = "Proactive Scanner"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Performs comprehensive system security scans and health checks"
PLUGIN_AUTHOR = "Electra AI Community"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []

PLUGIN_TRIGGERS = [
    "scan", "proactive scan", "security scan", "system scan",
    "health check", "check system", "vulnerability scan",
    "audit system", "security check", "run scan"
]
PLUGIN_ROUTE_TOKEN = "PROACTIVE_SCAN"
PLUGIN_COMMANDS = ["/scan", "/health", "/audit"]

def run(prompt: str, context: dict) -> str:
    """Execute comprehensive system security scan"""
    
    print_fn = context.get("print_fn", lambda x: None)
    cwd = context.get("cwd", os.getcwd())
    user_home = context.get("user_home", os.path.expanduser("~"))
    
    print_fn("🔍 **Starting Proactive System Scan**")
    print_fn(f"📁 Scan directory: `{cwd}`")
    print_fn(f"⏰ Started: {datetime.now().strftime('%H:%M:%S')}")
    print_fn("")
    
    results = []
    results.append("## 🔐 PROACTIVE SECURITY SCAN REPORT")
    results.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    results.append(f"**User:** {os.getlogin()}")
    results.append(f"**Hostname:** {os.uname().nodename}")
    results.append("")
    
    # 1. System Information
    results.append("### 📊 SYSTEM INFORMATION")
    try:
        uname = subprocess.run(["uname", "-a"], capture_output=True, text=True, timeout=10)
        results.append(f"```\n{uname.stdout.strip()}\n```")
    except Exception as e:
        results.append(f"❌ Could not retrieve system info: {str(e)}")
    
    # 2. Disk Usage
    results.append("\n### 💽 DISK USAGE")
    try:
        disk = subprocess.run(["df", "-h"], capture_output=True, text=True, timeout=10)
        results.append(f"```\n{disk.stdout.strip()}\n```")
    except Exception as e:
        results.append(f"❌ Could not check disk usage: {str(e)}")
    
    # 3. Memory Usage
    results.append("\n### 🧠 MEMORY USAGE")
    try:
        mem = subprocess.run(["free", "-h"], capture_output=True, text=True, timeout=10)
        results.append(f"```\n{mem.stdout.strip()}\n```")
    except Exception as e:
        results.append(f"❌ Could not check memory: {str(e)}")
    
    # 4. Running Processes (top 10 by memory)
    results.append("\n### 🔄 TOP PROCESSES")
    try:
        ps = subprocess.run(
            ["ps", "aux", "--sort=-%mem"],
            capture_output=True,
            text=True,
            timeout=10
        )
        lines = ps.stdout.strip().split('\n')[:11]  # Header + 10 processes
        results.append(f"```\n{chr(10).join(lines)}\n```")
    except Exception as e:
        results.append(f"❌ Could not list processes: {str(e)}")
    
    # 5. Open Network Ports
    results.append("\n### 🌐 OPEN NETWORK PORTS")
    try:
        # Try ss first, fallback to netstat
        try:
            ports = subprocess.run(
                ["ss", "-tuln"],
                capture_output=True,
                text=True,
                timeout=10
            )
        except:
            ports = subprocess.run(
                ["netstat", "-tuln"],
                capture_output=True,
                text=True,
                timeout=10
            )
        results.append(f"```\n{ports.stdout.strip()}\n```")
    except Exception as e:
        results.append(f"❌ Could not check ports: {str(e)}")
    
    # 6. World-Writable Files (in common locations)
    results.append("\n### ⚠️ WORLD-WRITABLE FILES")
    try:
        writable = subprocess.run(
            ["find", "/home", "/tmp", "/var/tmp", "-type", "f", "-perm", "-o=w", "-ls", "2>/dev/null"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if writable.stdout.strip():
            lines = writable.stdout.strip().split('\n')[:20]  # Limit output
            results.append(f"```\n{chr(10).join(lines)}\n```")
            if len(writable.stdout.strip().split('\n')) > 20:
                results.append(f"*...and more (showing first 20)*")
        else:
            results.append("✅ No world-writable files found in common locations")
    except Exception as e:
        results.append(f"❌ Could not check writable files: {str(e)}")
    
    # 7. SUID/SGID Files (in common locations)
    results.append("\n### 🔑 SUID/SGID FILES")
    try:
        suid = subprocess.run(
            ["find", "/usr", "/bin", "/sbin", "-type", "f", "(", "-perm", "-4000", "-o", "-perm", "-2000", ")", "-ls", "2>/dev/null"],
            capture_output=True,
            text=True,
            timeout=30
        )
        if suid.stdout.strip():
            lines = suid.stdout.strip().split('\n')[:15]  # Limit output
            results.append(f"```\n{chr(10).join(lines)}\n```")
            if len(suid.stdout.strip().split('\n')) > 15:
                results.append(f"*...and more (showing first 15)*")
        else:
            results.append("✅ No SUID/SGID files found in common locations")
    except Exception as e:
        results.append(f"❌ Could not check SUID/SGID files: {str(e)}")
    
    # 8. Recent Logins
    results.append("\n### 📝 RECENT LOGINS")
    try:
        logins = subprocess.run(
            ["last", "-n", "10"],
            capture_output=True,
            text=True,
            timeout=10
        )
        results.append(f"```\n{logins.stdout.strip()}\n```")
    except Exception as e:
        results.append(f"❌ Could not check login history: {str(e)}")
    
    # 9. Failed Login Attempts
    results.append("\n### 🚫 FAILED LOGIN ATTEMPTS")
    try:
        auth_log = "/var/log/auth.log"
        if os.path.exists(auth_log):
            failed = subprocess.run(
                ["grep", "Failed password", auth_log, "|", "tail", "-10"],
                shell=True,
                capture_output=True,
                text=True,
                timeout=10
            )
            if failed.stdout.strip():
                results.append(f"```\n{failed.stdout.strip()}\n```")
            else:
                results.append("✅ No failed login attempts in recent logs")
        else:
            results.append("⚠️ Auth log not found at /var/log/auth.log")
    except Exception as e:
        results.append(f"❌ Could not check failed logins: {str(e)}")
    
    # 10. Check for suspicious processes (common malware patterns)
    results.append("\n### 🦠 SUSPICIOUS PROCESS CHECK")
    suspicious_patterns = [
        r".*kworker.*", r".*watchdog.*", r".*minerd.*", r".*cpuminer.*",
        r".*xmrig.*", r".*xmr.*", r".*cryptonight.*", r".*backdoor.*",
        r".*reverse.*", r".*shell.*", r".*bash -i.*", r".*nc -e.*"
    ]
    
    try:
        ps_all = subprocess.run(
            ["ps", "aux"],
            capture_output=True,
            text=True,
            timeout=10
        )
        suspicious_found = []
        for line in ps_all.stdout.split('\n'):
            for pattern in suspicious_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    suspicious_found.append(line.strip())
                    break
        
        if suspicious_found:
            results.append("⚠️ **Suspicious processes detected:**")
            for proc in suspicious_found[:10]:  # Limit to 10
                results.append(f"```\n{proc}\n```")
            if len(suspicious_found) > 10:
                results.append(f"*...and {len(suspicious_found) - 10} more*")
        else:
            results.append("✅ No suspicious processes detected")
    except Exception as e:
        results.append(f"❌ Could not check processes: {str(e)}")
    
    # 11. Check for unknown users
    results.append("\n### 👤 USER ACCOUNTS")
    try:
        users = subprocess.run(
            ["getent", "passwd"],
            capture_output=True,
            text=True,
            timeout=10
        )
        user_lines = users.stdout.strip().split('\n')
        known_users = ['root', 'daemon', 'bin', 'sys', 'sync', 'games', 'man',
                      'lp', 'mail', 'news', 'uucp', 'proxy', 'www-data',
                      'backup', 'list', 'irc', 'gnats', 'nobody', 'systemd-network',
                      'systemd-resolve', 'syslog', 'messagebus', 'uuidd', 'dnsmasq',
                      'sshd', 'pollinate', 'whoopsie', 'avahi', 'colord',
                      'speech-dispatcher', 'hplip', 'pulse', 'gdm', 'sambashare']
        
        unknown_users = []
        for line in user_lines:
            if line:
                username = line.split(':')[0]
                if username not in known_users and not username.startswith('_'):
                    unknown_users.append(username)
        
        if unknown_users:
            results.append("⚠️ **Unknown user accounts:**")
            for user in unknown_users[:10]:
                results.append(f"- `{user}`")
            if len(unknown_users) > 10:
                results.append(f"*...and {len(unknown_users) - 10} more*")
        else:
            results.append("✅ No unknown user accounts found")
    except Exception as e:
        results.append(f"❌ Could not check users: {str(e)}")
    
    # 12. Check for listening services
    results.append("\n### 📡 LISTENING SERVICES")
    try:
        listening = subprocess.run(
            ["ss", "-tuln", "|", "grep", "LISTEN"],
            shell=True,
            capture_output=True,
            text=True,
            timeout=10
        )
        if listening.stdout.strip():
            results.append(f"```\n{listening.stdout.strip()}\n```")
        else:
            results.append("✅ No listening services found")
    except Exception as e:
        results.append(f"❌ Could not check listening services: {str(e)}")
    
    # Summary
    results.append("\n---")
    results.append("## 📋 SCAN SUMMARY")
    results.append("✅ **Scan completed successfully**")
    results.append("")
    results.append("**Recommendations:**")
    results.append("1. Review any suspicious processes or files")
    results.append("2. Check unknown user accounts")
    results.append("3. Verify open ports are expected")
    results.append("4. Monitor failed login attempts")
    results.append("5. Consider disabling unnecessary services")
    results.append("")
    results.append("ℹ️ *This scan is informational. Take appropriate action based on your system's requirements.*")
    
    final_report = "\n".join(results)
    print_fn("✅ **Scan completed**")
    return final_report