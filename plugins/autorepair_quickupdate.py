"""
Electra AI Plugin: Quick System Update Handler
Intercepts 'u', 'up', 'update', 'upgrade' commands and performs system updates on MakuluLinux.
"""

import os
import subprocess
import shutil

PLUGIN_NAME        = "Quick System Update"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Handles 'u', 'up', 'update' shortcuts for system package updates"
PLUGIN_AUTHOR      = "Electra Plugin Forge"
PLUGIN_TYPE        = "ROUTER"
PLUGIN_ENABLED     = True
PLUGIN_TRIGGERS    = ["u\n", "u ", "u\r", "u\r\n", "up\n", "up ", "up\r", "up\r\n",
                       "update\n", "update ", "upgrade\n", "upgrade ",
                       "apt update", "sudo apt", "system update"]
PLUGIN_ROUTE_TOKEN = "QUICKUPDATE"
PLUGIN_COMMANDS    = ["/u", "/update", "/upgrade"]

def run(prompt: str, context: dict) -> str:
    pfn = context["print_fn"]
    
    # Normalize prompt
    normalized = prompt.strip().lower()
    
    # Check if this is a system update request
    update_patterns = ["u", "up", "update", "upgrade", "apt update", "system update"]
    if not any(normalized.startswith(p) for p in update_patterns):
        return ""  # Not our responsibility
    
    pfn("\n🔄 Quick Update Handler Activated\n")
    pfn("=" * 40 + "\n")
    
    results = []
    
    # Step 1: Check for sudo/elevation
    pfn("📦 Checking package manager availability...\n")
    
    if shutil.which("apt-get"):
        try:
            # Check if we can run sudo without password (common in dev environments)
            check = subprocess.run(
                ["sudo", "-n", "true"],
                capture_output=True,
                timeout=5
            )
            needs_sudo = check.returncode != 0
        except:
            needs_sudo = True
        
        sudo_cmd = "sudo " if needs_sudo else ""
        
        # Step 2: Refresh package lists
        pfn("🔍 Refreshing package lists...\n")
        try:
            refresh = subprocess.run(
                f"{sudo_cmd}apt-get update".split(),
                capture_output=True,
                text=True,
                timeout=120
            )
            if refresh.returncode == 0:
                pfn("✅ Package lists refreshed successfully\n")
                results.append("Package lists updated")
            else:
                pfn(f"⚠️ Refresh warning: {refresh.stderr.strip()}\n")
        except subprocess.TimeoutExpired:
            pfn("⚠️ Timeout refreshing package lists (continuing...)\n")
        except Exception as e:
            pfn(f"⚠️ Could not refresh packages: {e}\n")
        
        # Step 3: List upgradable packages
        pfn("\n📋 Checking for upgrades...\n")
        try:
            list_upgrades = subprocess.run(
                f"{sudo_cmd}apt list --upgradable 2>/dev/null".split(),
                capture_output=True,
                text=True,
                timeout=30
            )
            if list_upgrades.stdout.strip():
                lines = list_upgrades.stdout.strip().split('\n')
                upgrade_count = len(lines) - 1  # subtract header line
                pfn(f"   Found {upgrade_count} upgradeable package(s)\n")
                for line in lines[1:6]:  # Show first 5
                    if line:
                        pfn(f"   • {line}\n")
                if upgrade_count > 5:
                    pfn(f"   ... and {upgrade_count - 5} more\n")
            else:
                pfn("   ✅ All packages are up to date\n")
        except:
            pass
        
        # Step 4: Ask about full upgrade
        pfn("\n" + "=" * 40)
        pfn("\n💡 To perform full system upgrade, say 'yes' or run manually:")
        pfn(f"\n   {sudo_cmd}apt-get upgrade -y\n")
        pfn(f"   {sudo_cmd}apt-get dist-upgrade -y\n")
        pfn("=" * 40 + "\n")
        
        results.append("Update check complete")
        
    elif shutil.which("dnf"):
        pfn("🔄 Detected DNF package manager (Fedora/RHEL)\n")
        try:
            check = subprocess.run(["sudo", "-n", "true"], capture_output=True, timeout=5)
            sudo_cmd = "" if check.returncode == 0 else "sudo "
            
            pfn("🔍 Checking for updates...\n")
            result = subprocess.run(
                f"{sudo_cmd}dnf check-update".split(),
                capture_output=True,
                text=True,
                timeout=60
            )
            if result.returncode == 0:
                pfn("✅ All packages are up to date\n")
                results.append("No pending updates")
            else:
                pfn("📦 Updates available. Run manually: dnf update -y\n")
                results.append("Updates available")
        except Exception as e:
            pfn(f"⚠️ Update check failed: {e}\n")
            
    elif shutil.which("pacman"):
        pfn("🔄 Detected Pacman package manager (Arch)\n")
        try:
            pfn("🔍 Checking for updates...\n")
            result = subprocess.run(
                ["checkupdates"],
                capture_output=True,
                text=True,
                timeout=60
            )
            if result.stdout.strip():
                count = len(result.stdout.strip().split('\n'))
                pfn(f"📦 {count} package(s) can be updated\n")
                pfn("   Run: sudo pacman -Syu\n")
                results.append(f"{count} updates available")
            else:
                pfn("✅ System is up to date\n")
                results.append("No pending updates")
        except FileNotFoundError:
            pfn("📦 Run manually: sudo pacman -Syu\n")
        except Exception as e:
            pfn(f"⚠️ {e}\n")
            
    else:
        pfn("⚠️ No recognized package manager found\n")
        results.append("Package manager not detected")
    
    pfn("\n✨ Quick Update Check Complete!\n")
    
    return f"[Quick Update] Completed: {', '.join(results) if results else 'Finished'}"