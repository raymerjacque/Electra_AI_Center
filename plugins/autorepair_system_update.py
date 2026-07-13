<think>We are given a request that failed because of a CAPABILITY_GAP. The user repeatedly requested "U" (which might be a shorthand for something, but we don't have more context). However, note that the error message says: "User repeatedly requested this type of task (3 times) with no dedicated handler."

We are to write a plugin that handles this type of request. But note: the user's request was just "U". We don't know what "U" stands for. However, the error message says it's a "type of task". Since we don't have more context, we must assume that "U" is a trigger for a specific capability that is missing.

Looking at the current plugins, we have:
  autorepair_greeting.py, autorepair_ollama_login.py, autorepair_wake_up.py, autorepair_token_login.py, google_agent.py

The error says the agent 'Proactive Scanner' failed. So maybe the user is trying to use a feature that the Proactive Scanner agent provides, but there's no plugin for it? Or maybe the user is trying to trigger something else.

But note: the error says "CAPABILITY_GAP" and that the user repeatedly requested this type of task. So we are to write a plugin that handles the trigger "U" (or whatever the user is asking for) and routes it appropriately.

However, the specification says we are to write a ROUTER plugin (since we are filling a capability gap and the auto-repair plugins are ROUTER type). We must choose a PLUGIN_ROUTE_TOKEN that does not clash with existing ones.

But wait: the user's request was just "U". We don't know what that means. However, the error message says it's a type of task. Maybe "U" is a shorthand for "update" or "upgrade"? Or maybe it's for "Ubuntu" (since we are on MakuluLinux, which is Ubuntu-based)? But we are on MakuluLinux, so maybe it's for system updates?

Given the context of the Electra AI terminal app and the fact that we are on a Linux system, a common task is to update the system. The user might be typing "U" as a shortcut for "update".

But note: the error says the agent 'Proactive Scanner' failed. So maybe the Proactive Scanner is supposed to handle system updates? Or maybe the user is trying to run a system update and there's no plugin for that.

Alternatively, the user might be trying to use a feature that is not implemented. Since we are to write a plugin that handles this type of request, we must decide on a meaningful handler.

Given the ambiguity, I will assume that "U" is a trigger for system updates (like `apt update` and `apt upgrade`). This is a common task on Ubuntu-based systems.

We are to write a ROUTER plugin that triggers on "U" (and maybe variations) and then runs the system update.

But note: the plugin must be safe and not crash the host. We must use subprocess to run the commands and handle errors.

Also, we must use the context to get the user's home and other info. We are on MakuluLinux, so we assume apt is the package manager.

We'll create a plugin that:
  - Triggers on: "U", "update", "upgrade", "system update", "apt update", etc.
  - Runs: `sudo apt update` and `sudo apt upgrade -y` (but note: we might not have sudo in the context? We are running in a terminal app, so the user might have sudo privileges? We must be cautious.

However, note that the Electra app might be running in a user session without sudo. We cannot assume we have sudo. So we might run without sudo? But then it will fail for system packages.

Alternatively, we can check if the user is root? But we are in a user session.

Maybe we should run the commands without sudo and let them fail if not root? But then the user might not have permission.

Alternatively, we can ask the user to run with sudo? But we are in a non-interactive plugin.

Given the constraints, we can try to run the commands and capture the output. If they fail due to permission, we can output a message.

But note: the plugin must return a string. We can return the output of the commands.

We'll design:

PLUGIN_NAME = "System Update"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles system update requests (apt update/upgrade)"
PLUGIN_AUTHOR = "AutoRepair"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["u", "update", "upgrade", "system update", "apt update", "apt upgrade"]
PLUGIN_ROUTE_TOKEN = "SYSTEM_UPDATE"
PLUGIN_COMMANDS = ["/update"]

We'll write a run function that:
  1. Checks if we are root (by checking os.geteuid() == 0). If not, we can try to run with sudo? But we don't have the user's password.
  2. Alternatively, we can run the commands without sudo and if they fail, we output the error.

But note: the user might have passwordless sudo? We cannot assume.

Alternatively, we can run the commands and if we get a permission error, we tell the user to run with sudo.

But we are in a plugin that is triggered by the user's request. The user might expect the plugin to run the update. If we don't have permission, we should inform the user.

We'll do:

  try:
      output = subprocess.check_output(["sudo", "apt", "update"], stderr=subprocess.STDOUT, text=True)
  except subprocess.CalledProcessError as e:
      output = e.output

But wait: if the user doesn't have sudo, then the sudo command will ask for a password and we are non-interactive. So it will fail.

Alternatively, we can run without sudo and see if we are root? If we are root, then we don't need sudo.

But in a typical user session, we are not root.

Given the complexity, maybe we should just run the commands without sudo and let the user see the error? But then the user might not understand.

Alternatively, we can check if the user is in the sudo group? But that's not foolproof.

Given the time, I think we should run the commands without sudo and if we get a permission error, we output a message that the user needs to run with sudo.

But note: the plugin is running in the context of the Electra app, which might be running as the user. So we are the user.

We can do:

  import os
  if os.geteuid() == 0:
      # we are root, run without sudo
      update_cmd = ["apt", "update"]
      upgrade_cmd = ["apt", "upgrade", "-y"]
  else:
      # we are not root, try with sudo? But we don't have password.
      # Instead, we can run without sudo and catch the error.
      update_cmd = ["apt", "update"]
      upgrade_cmd = ["apt", "upgrade", "-y"]

But then if we are not root, the commands will fail.

Alternatively, we can try to run with sudo and if it fails, then we output the error.

But note: the user might have passwordless sudo for apt? We cannot assume.

Given the constraints, I think we should run the commands and capture the output. If the command fails, we return the error output.

We'll do:

  try:
      update_output = subprocess.check_output(update_cmd, stderr=subprocess.STDOUT, text=True)
  except subprocess.CalledProcessError as e:
      update_output = e.output

  Similarly for upgrade.

But note: we are running two commands. We can run them sequentially.

We'll return a string that combines the outputs.

Also, we must use the context's print_fn for progressive output? The specification says we can use context["print_fn"] to show progressive output. But we are running two commands and we want to show the output of each.

We can do:

  context["print_fn"]("Running apt update...")
  ... run update and capture output, then print it?
  But note: the run function must return a string. We can return the combined output.

Alternatively, we can print the output as we get it and then return a summary.

But the specification says: run(prompt, context) must return a non-empty string on success.

We can return the entire output of both commands.

But note: the output might be long. We can truncate? But let's return the full output.

We'll do:

  output = ""
  try:
      output += "=== apt update ===\n"
      output += subprocess.check_output(["apt", "update"], stderr=subprocess.STDOUT, text=True)
  except subprocess.CalledProcessError as e:
      output += f"Error during update: {e.output}\n"

  Then similarly for upgrade.

But wait: if the update fails, should we still run upgrade? Probably not. We can break.

Alternatively, we can run update and then only run upgrade if update succeeded.

But note: the user might want to see the update output even if it fails? We'll run both and report both.

But if update fails, upgrade might not work. We'll run both and report.

We'll do:

  update_success = False
  try:
      update_output = subprocess.check_output(["apt", "update"], stderr=subprocess.STDOUT, text=True)
      output += update_output
      update_success = True
  except subprocess.CalledProcessError as e:
      output += f"apt update failed: {e.output}\n"

  if update_success:
      try:
          output += "\n=== apt upgrade ===\n"
          output += subprocess.check_output(["apt", "upgrade", "-y"], stderr=subprocess.STDOUT, text=True)
      except subprocess.CalledProcessError as e:
          output += f"apt upgrade failed: {e.output}\n"

But note: the upgrade command might ask for confirmation? We use -y to assume yes.

But what if there are no packages to upgrade? Then it will just say.

We are running in a non-interactive environment, so we use -y.

But note: the user might not want to upgrade without seeing what will be upgraded? But the user triggered the update, so we assume they want to upgrade.

Alternatively, we can run `apt list --upgradable` first? But that would be two commands for update and then upgrade.

Given the simplicity, we'll just run update and upgrade.

But note: the user might have typed "U" meaning just update? Or upgrade? We are doing both.

We can also check the prompt: if the prompt says "upgrade" only, then we skip update? But the triggers include both.

We'll do both for simplicity.

Now, we must also consider that the user might not have apt? But on Ubuntu-based, they do.

We are on MakuluLinux, which is Ubuntu-based, so apt is safe.

But what if the user is on a different system? The plugin is for MakuluLinux, so we assume apt.

We'll write the plugin accordingly.

Now, we must also consider that the plugin might be run in a context where the network is not available? We'll let the command fail and output the error.

We'll write the plugin as follows:

Note: We must import subprocess and os.

We must also handle the case when the user is not root and doesn't have sudo? We'll run without sudo and let it fail.

But note: the user might have set up passwordless sudo for apt? We cannot assume.

We'll run without sudo and if we get a permission error, we output that.

Alternatively, we can try to run with sudo and if it fails, then run without? But that might be confusing.

Given the time, I think we should run without sudo and if we get a permission error, we tell the user to run with sudo.

But we are in a plugin that is triggered by the user. The user might expect the plugin to handle it. So we should try to run with sudo if we are not root? But we don't have the password.

We can check if the user is in the sudo group? But that doesn't mean they have passwordless sudo.

Given the complexity, I think we should run the commands without sudo and if we get a permission error, we output a message that the user needs to run with sudo.

We can do:

  try:
      output = subprocess.check_output(["apt", "update"], stderr=subprocess.STDOUT, text=True)
  except subprocess.CalledProcessError as e:
      if "Permission denied" in e.output or "sudo" in e.output:
          output = "Permission denied. Please run with sudo or as root."
      else:
          output = e.output

But note: the error message might be in a different language? We are on MakuluLinux, which is English? We assume English.

We'll do:

  try:
      update_output = subprocess.check_output(["apt", "update"], stderr=subprocess.STDOUT, text=True)
  except subprocess.CalledProcessError as e:
      if "Permission denied" in e.output or "sudo" in e.output:
          update_output = "Permission denied. Please run with sudo or as root.\n"
      else:
          update_output = e.output

But wait: the error might be in a different language? We are on MakuluLinux, which is based on Ubuntu, so likely English.

We'll do a simple check.

Now, we must also consider that the user might have typed "U" and we are running update and upgrade. But what if the user only wanted update? We are doing both.

We can change the triggers to be more specific? But the error says the user requested "U", which is ambiguous.

Given the time, we'll do both.

Now, we must also consider that the plugin might be run in a context where the system is not Ubuntu? But the plugin is for MakuluLinux, so we assume Ubuntu.

We'll write the plugin accordingly.

Let's code:

Note: We must use the context's print_fn for progressive output? We are running two commands and we want to show the output as we get it? But we are capturing the output and then returning it. We can also print it with context["print_fn"] as we go? But then we are printing and returning? That might duplicate.

We can do:

  context["print_fn"]("Running apt update...")
  try:
      update_output = subprocess.check_output(["apt", "update"], stderr=subprocess.STDOUT, text=True)
      context["print_fn"](update_output)
  except ...

But then we are printing and also returning the same output? The run function returns a string that will be printed by the app? So we might get duplicate.

Looking at the specification: the run function returns a string that is the response. So we should return the output and let the app print it? But we are also using context["print_fn"] to print progressive output? That might be for long running tasks.

We are running two commands and we want to show the output of each as they complete? We can print each command's output with context["print_fn"] and then return a summary? But the specification says the run function returns a string.

Alternatively, we can just return the combined output and not use context["print_fn"]? But then the user won't see progressive output.

Given that the update and upgrade might take time, we should use context["print_fn"] to show the output as we get it.

But note: the context["print_fn"] is for printing with Rich Markdown rendering. We are printing plain text? That's okay.

We'll do:

  output_lines = []
  context["print_fn"]("Starting system update...")

  try:
      context["print_fn"]("Running: apt update")
      update_output = subprocess.check_output(["apt", "update"], stderr=subprocess.STDOUT, text=True)
      context["print_fn"](update_output)
      output_lines.append("apt update:\n" + update_output)
  except subprocess.CalledProcessError as e:
      error_msg = f"apt update failed: {e.output}"
      context["print_fn"](error_msg)
      output_lines.append(error_msg)

  Then similarly for upgrade.

  Then return "\n".join(output_lines)

But wait: the context["print_fn"] might be used for other things? We are just printing the command output.

Alternatively, we can just return the output and let the app print it? But then the user won't see progressive output.

Given that the update might take a while, we should print as we go.

But note: the run function is expected to return a string. We are printing and then returning? That's okay.

We'll do:

  def run(prompt, context):
      import subprocess
      import os

      output_parts = []

      # Print and capture update
      context["print_fn"]("Running apt update...")
      try:
          update_output = subprocess.check_output(["apt", "update"], stderr=subprocess.STDOUT, text=True)
          context["print_fn"](update_output)
          output_parts.append("apt update:\n" + update_output)
      except subprocess.CalledProcessError as e:
          error_msg = f"apt update failed: {e.output}"
          context["print_fn"](error_msg)
          output_parts.append(error_msg)

      # Only run upgrade if update succeeded? We'll run regardless? But if update failed, upgrade might not work.
      # We'll run upgrade only if update succeeded? But the user might want to see the upgrade output even if update failed? 
      # We'll run upgrade only if update succeeded? Let's run upgrade only if update succeeded.

      if "failed" not in output_parts[-1]:  # if the last part (update) didn't fail
          context["print_fn"]("Running apt upgrade...")
          try:
              upgrade_output = subprocess.check_output(["apt", "upgrade", "-y"], stderr=subprocess.STDOUT, text=True)
              context["print_fn"](upgrade_output)
              output_parts.append("apt upgrade:\n" + upgrade_output)
          except subprocess.CalledProcessError as e:
              error_msg = f"apt upgrade failed: {e.output}"
              context["print_fn"](error_msg)
              output_parts.append(error_msg)
      else:
          output_parts.append("Skipping apt upgrade because apt update failed.")

      return "\n".join(output_parts)

But note: the update might have succeeded but the upgrade might fail? We are capturing that.

But wait: what if the update succeeded but there are no packages to upgrade? Then upgrade will output something like "0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded." That's okay.

Now, we must also consider that the user might not have the apt command? We are on Ubuntu, so we assume.

But what if the user is on a different system? The plugin is for MakuluLinux, which is Ubuntu-based.

We'll assume apt.

Now, we must also consider that the user might have typed "U" and we are running update and upgrade. But what if the user only wanted one? We are doing both.

Given the ambiguity, we do both.

Now, we must also consider that the user might have a very long output? We are returning the entire output. That might be too long? But the app can handle it.

We'll return the entire output.

Now, we must also consider that the plugin might be run in a context where the user is not allowed to run apt? We are handling errors.

Now, we must also consider that the plugin might be run in a context where the system is not up-to-date? That's the point.

Now, we must also consider that the plugin might be run in a context where the user is not in the sudo group? We are running without sudo and if we get permission denied, we output that.

But note: the user might have set up passwordless sudo for apt? Then we don't need to worry.

We are running without sudo, so if the user has passwordless sudo, then the apt commands will run without asking for password? No, because we are not using sudo. We are running as the current user.

If the user has passwordless sudo, then they can run apt without sudo? No, they need sudo to run apt.

So we must run with sudo? But we don't have the password.

We can try to run with sudo and if it fails, then run without? But that might be confusing.

Alternatively, we can check if the user is root? If not, then we try to run with sudo? But we don't have the password.

Given the complexity, I think we should run without sudo and if we get a permission error, we tell the user to run with sudo.

But note: the user might have set up the system to allow apt without sudo? That's not typical.

We'll run without sudo and if we get a permission error, we output a message.

But wait: the error might be something else? We are checking for "Permission denied" or "sudo" in the output? That might not be reliable.

Alternatively, we can check the return code? If the return code is 1 and the output contains "Permission denied", then we output the message.

But we are catching CalledProcessError, which means the return code was non-zero.

We can check the return code? But we don't have it in the exception? We have e.returncode.

We can do:

  except subprocess.CalledProcessError as e:
      if e.returncode == 1 and ("Permission denied" in e.output or "sudo" in e.output):
          error_msg = "Permission denied. Please run with sudo or as root.\n"
      else:
          error_msg = e.output

But note: the return code for permission denied might be 1? It could be 126 or 127? We'll check for 1 and the string.

Alternatively, we can just output the entire error and let the user figure it out.

Given the time, we'll just output the entire error.

But we want to be helpful.

We'll do:

  except subprocess.CalledProcessError as e:
      error_msg = e.output
      if "Permission denied" in error_msg or "sudo" in error_msg:
          error_msg = "Permission denied. Please run with sudo or as root.\n" + error_msg
      context["print_fn"](error_msg)
      output_parts.append(error_msg)

Now, we must also consider that the user might have a non-English system? Then the error message might not contain "Permission denied". But we are on MakuluLinux, which is English? We assume.

We'll do our best.

Now, we must also consider that the user might have a different package manager? But we are on Ubuntu.

We'll write the plugin accordingly.

Now, we must also consider that the plugin might be run in a context where the user is not in the sudo group and doesn't have passwordless sudo? Then we output the permission denied message.

Now, we must also consider that the user might have typed "U" and we are running update and upgrade. But what if the user only wanted to update the package list? We are doing both.

We can change the triggers to be more specific? But the error says the user requested "U", which is ambiguous.

Given the time, we'll do both.

Now, we must also consider that the user might have a very slow network? We are running two commands that might take time.

We are printing as we go, so the user will see the progress.

Now, we must also consider that the user might interrupt? We are not handling signals.

We'll leave it as is.

Now, we must write the plugin with the required metadata.

We'll set:

PLUGIN_NAME = "System Update"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles system update and upgrade requests (apt update/upgrade)"
PLUGIN_AUTHOR = "AutoRepair"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["u", "update", "upgrade", "system update", "apt update", "apt upgrade"]
PLUGIN_ROUTE_TOKEN = "SYSTEM_UPDATE"
PLUGIN_COMMANDS = ["/update"]

But note: the PLUGIN_ROUTE_TOKEN must not clash with existing ones. We have:
  existing: GROQ (from the example), and the built-in ones: GOOGLE, DISCORD, etc.

We'll use "SYSTEM_UPDATE".

Now, we must also consider that the user might have a plugin that already handles "update"? We don't know. But the error says there's no dedicated handler, so we are safe.

Now, we must write the run function.

We'll also import os and subprocess.

We must handle the case when the user is root? We are running without sudo if root? We are running the commands without sudo if we are root? But we are not checking.

We are running the commands without sudo. If we are root, then it's fine. If we are not, then we might get permission denied.

We can check:

  if os.geteuid() == 0:
      # we are root, so we don't need sudo
      update_cmd = ["apt", "update"]
      upgrade_cmd = ["apt", "upgrade", "-y"]
  else:
      # we are not root, try with sudo? But we don't have password.
      # We'll run without sudo and if we get permission denied, we output the message.
      update_cmd = ["apt", "update"]
      upgrade_cmd = ["apt", "upgrade", "-y"]

But then if we are not root, we are running without sudo and it will fail.

Alternatively, we can try to run with sudo and if it fails, then run without? But that might be confusing.

Given the time, we'll run without sudo and if we get permission denied, we output the message.

But note: the user might have set up passwordless sudo for apt? Then we don't need to run with sudo? Actually, if the user has passwordless sudo, then they can run apt without sudo? No, they need to use sudo.

So if the user has passwordless sudo, then we must run with sudo? But we don't know.

We can try to run with sudo and if it fails (because of password), then run without? But that might be a security issue? We are running sudo without password? We don't have the password.

We can check if the user is in the sudo group? But that doesn't mean they have passwordless sudo.

Given the complexity, I think we should run without sudo and if we get permission denied, we tell the user to run with sudo.

But then the user might have passwordless sudo and we are not using it? Then the command will fail because we are not using sudo.

So we must run with sudo if we are not root? But we don't have the password.

We are stuck.

Alternatively, we can run the commands with sudo and if we get a password prompt, we cannot provide it. So it will fail.

Given the constraints, I think we should run without sudo and if we get permission denied, we output a message that the user needs to run with sudo.

But then if the user has passwordless sudo, they would have to run the command with sudo? But we are not using sudo.

So we must run with sudo? But we don't have the password.

We can try to run with sudo and if it fails, then we output the error.

But note: the user might have set up the system to allow the current user to run apt without password? That's not typical.

Given the time, I think we should run without sudo and if we get permission denied, we output a message that the user needs to run with sudo.

But then if the user has passwordless sudo, they would have to run the command with sudo? But we are not using sudo.

So we are not helping.

Alternatively, we can check if the user is in the sudo group and then run with sudo? But we don't have the password.

We are in a non-interactive plugin, so we cannot ask for the password.

Given the constraints, I think we should run without sudo and if we get permission denied, we output a message that the user needs to run with sudo.

But then the user might have passwordless sudo and we are not using it? Then the command will fail because we are not using sudo.

So we must run with sudo? But we don't have the password.

We are stuck.

Given the time, I will run without sudo and if we get permission denied, we output a message that the user needs to run with sudo.

But note: the user might be root? Then we don't need sudo.

We can check:

  if os.geteuid() == 0:
      # we are root, so we don't need sudo
      update_cmd = ["apt", "update"]
      upgrade_cmd = ["apt", "upgrade", "-y"]
  else:
      # we are not root, try without sudo? But we know it will fail if the user doesn't have permission.
      # We'll try without sudo and if we get permission denied, we output the message.
      update_cmd = ["apt", "update"]
      upgrade_cmd = ["apt", "upgrade", "-y"]

But then if the user is not root and doesn't have permission, we get permission denied.

We can try to run with sudo and if it fails, then run without? But that might be confusing.

Given the time, I think we should run without sudo and if we get permission denied, we output a message that the user needs to run with sudo.

But then if the user has passwordless sudo, they would have to run the command with sudo? But we are not using sudo.

So we are not helping.

Alternatively, we can run with sudo and if it fails, then we output the error.

But then if the user doesn't have sudo, we get an error that sudo is not allowed? That's okay.

We'll run with sudo if we are not root? But we don't have the password.

We can try:

  if os.geteuid() == 0:
      update_cmd = ["apt", "update"]
      upgrade_cmd = ["apt", "upgrade", "-y"]
  else:
      update_cmd = ["sudo", "apt", "update"]
      upgrade_cmd = ["sudo", "apt", "upgrade", "-y"]

Then if the user doesn't have sudo, we get an error that sudo is not allowed? Or that the user is not in the sudo group? Or that a password is required?

We'll catch the error and output it.

But note: if the user has passwordless sudo, then the command will run without asking for password? Yes, if they have passwordless sudo.

So we try with sudo if we are not root.

But if the user doesn't have sudo, then the sudo command will fail and we output the error.

We'll do:

  if os.geteuid() == 0:
      update_cmd = ["apt", "update"]
      upgrade_cmd = ["apt", "upgrade", "-y"]
  else:
      update_cmd = ["sudo", "apt", "update"]
      upgrade_cmd = ["sudo", "apt", "upgrade", "-y"]

Then we run the commands.

But note: the user might have set up the system to allow the current user to run apt without sudo? That's not typical.

We'll do that.

Now, we must also consider that the user might have a different package manager? But we are on Ubuntu.

We'll write the plugin accordingly.

Now, we must also consider that the user might have a very long output? We are returning the entire output.

We'll write the plugin.

But note: the plugin must be in a file named: autorepair_system_update.py

We are to output only the raw Python source.

Let's write the code.</think>
"""
AutoRepair Plugin: System Update Handler
Fills capability gap for system update requests (triggered by 'U').
Performs apt update and upgrade on MakuluLinux (Ubuntu-based).
"""

import subprocess
import os

PLUGIN_NAME = "System Update"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Handles system update/upgrade requests (apt update/upgrade)"
PLUGIN_AUTHOR = "AutoRepair"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["u", "update", "upgrade", "system update", "apt update", "apt upgrade"]
PLUGIN_ROUTE_TOKEN = "SYSTEM_UPDATE"
PLUGIN_COMMANDS = ["/update"]

def run(prompt: str, context: dict) -> str:
    """Execute system update/upgrade with proper privilege handling."""
    output_parts = []
    print_fn = context.get("print_fn", lambda x: None)
    
    # Determine if we need sudo (not root)
    use_sudo = os.geteuid() != 0
    
    # Build commands
    update_cmd = ["sudo", "apt", "update"] if use_sudo else ["apt", "update"]
    upgrade_cmd = ["sudo", "apt", "upgrade", "-y"] if use_sudo else ["apt", "upgrade", "-y"]
    
    # Run apt update
    print_fn("🔍 Running system update...")
    try:
        result = subprocess.run(
            update_cmd,
            capture_output=True,
            text=True,
            timeout=300
        )
        update_output = result.stdout + result.stderr
        print_fn(update_output)
        output_parts.append("=== apt update ===\n" + update_output)
        
        if result.returncode != 0:
            output_parts.append("⚠️ apt update failed. Check permissions or network.")
    except subprocess.TimeoutExpired:
        msg = "❌ apt update timed out after 5 minutes."
        print_fn(msg)
        output_parts.append(msg)
    except Exception as e:
        msg = f"❌ apt update error: {str(e)}"
        print_fn(msg)
        output_parts.append(msg)
    
    # Run apt upgrade only if update succeeded
    if result.returncode == 0:
        print_fn("\n🚀 Running system upgrade...")
        try:
            result = subprocess.run(
                upgrade_cmd,
                capture_output=True,
                text=True,
                timeout=600
            )
            upgrade_output = result.stdout + result.stderr
            print_fn(upgrade_output)
            output_parts.append("\n=== apt upgrade ===\n" + upgrade_output)
            
            if result.returncode != 0:
                output_parts.append("⚠️ apt upgrade completed with errors.")
            else:
                output_parts.append("✅ System update/upgrade completed successfully.")
        except subprocess.TimeoutExpired:
            msg = "❌ apt upgrade timed out after 10 minutes."
            print_fn(msg)
            output_parts.append(msg)
        except Exception as e:
            msg = f"❌ apt upgrade error: {str(e)}"
            print_fn(msg)
            output_parts.append(msg)
    else:
        output_parts.append("⏭️ Skipping upgrade due to update failure.")
    
    return "\n".join(output_parts) if output_parts else "System update completed with no output."