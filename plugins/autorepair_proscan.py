<think>The user requested "1" which failed in an agent called 'Proactive Scanner' with a CAPABILITY_GAP error. This suggests the request involves some kind of proactive scanning or system monitoring task.

Looking at the error: "User repeatedly requested this type of task (3 times) with no dedicated handler."

On MakuluLinux (which is a Linux distribution), the user likely wants some kind of system scan, health check, or proactive monitoring functionality.

Since the request was just "1", this is vague but appears to be related to system scanning/proactive monitoring. I should create a plugin that handles this type of request on MakuluLinux.

Let me create a plugin that can:
1. Perform system health checks
2. Scan for available updates
3. Check system resources
4. Perform disk/performance scans

I'll name it something like "System Proactive Scanner" or "Auto Repair Scanner".
</think>

"""
Electra AI Plugin: Proactive System Scanner
Handles system monitoring, health checks, and diagnostic scans on MakuluLinux.
"""

PLUGIN_NAME        = "Proactive System Scanner"
PLUGIN_VERSION     = "1.0.0"
PLUGIN_DESCRIPTION = "Performs system health checks, disk scans, and proactive diagnostics on MakuluLinux"
PLUGIN_AUTHOR      = "Plugin Forge"
PLUGIN_TYPE        = "ROUTER"
PLUGIN_ENABLED     = True
PLUGIN_REQUIRES    = []

PLUGIN_TRIGGERS    = [
    "scan system", "system check", "health check", "disk scan",
    "proactive", "diagnostic", "system report", "1", "proactive scan",
    "run scan", "system status", "linux scan", "system diagnostic"
]
PLUGIN_ROUTE_TOKEN = "PROSCAN"
PLUGIN_COMMANDS    = ["/scan", "/proscan", "/diagnostic"]

import subprocess
import os
import re
from datetime import datetime


def run(prompt: str, context: dict) -> str:
    print_fn = context.get("print_fn", print)
    user_home = context.get("user_home", os.path.expanduser("~"))
    
    results = []
    results.append("=" * 50)
    results.append("  PROACTIVE SYSTEM SCANNER")
    results.append("=" * 50)
    results.append(f"  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    results.append("=" * 50)
    results.append("")
    
    try:
        print_fn("🔍 Initiating system scan...")
        
        # System Information
        print_fn("\n📊 Gathering system information...")
        try:
            result = subprocess.run(
                ["uname", "-a"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                results.append("SYSTEM:")
                results.append(f"  Kernel: {result.stdout.strip()}")
        except Exception:
            pass
        
        # Memory Usage
        print_fn("💾 Checking memory usage...")
        try:
            result = subprocess.run(
                ["free", "-h"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                results.append("\nMEMORY:")
                for line in result.stdout.strip().split('\n'):
                    if line:
                        results.append(f"  {line}")
        except Exception:
            pass
        
        # Disk Usage
        print_fn("💿 Checking disk usage...")
        try:
            result = subprocess.run(
                ["df", "-h", "--output=source,size,used,avail,pcent,target"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                results.append("\nDISK:")
                for line in result.stdout.strip().split('\n'):
                    if line and '/dev' in line:
                        parts = line.split()
                        if len(parts) >= 6:
                            results.append(f"  {parts[5]}: {parts[3]} free of {parts[1]} ({parts[4]} used)")
        except Exception:
            pass
        
        # CPU Load
        print_fn("⚙️ Checking CPU load...")
        try:
            result = subprocess.run(
                ["uptime"],
                capture_output=True, text=True, timeout=5
            )
            if result.returncode == 0:
                results.append("\nCPU LOAD:")
                load = result.stdout.strip()
                results.append(f"  {load}")
        except Exception:
            pass
        
        # System Services Status
        print_fn("🔧 Checking critical services...")
        services_status = []
        critical_services = ["systemd", "NetworkManager", "cups", "bluetooth"]
        for service in critical_services:
            try:
                result = subprocess.run(
                    ["systemctl", "is-active", service],
                    capture_output=True, text=True, timeout=3
                )
                status = "✓ Active" if result.returncode == 0 and "active" in result.stdout else "✗ Inactive"
                services_status.append(f"  {service}: {status}")
            except Exception:
                services_status.append(f"  {service}: Unknown")
        
        if services_status:
            results.append("\nSERVICES:")
            results.extend(services_status)
        
        # Package Updates Check
        print_fn("📦 Checking for system updates...")
        try:
            result = subprocess.run(
                ["apt", "list", "--upgradable"],
                capture_output=True, text=True, timeout=30
            )
            if result.returncode == 0:
                lines = result.stdout.strip().split('\n')
                upgrade_count = len([l for l in lines if 'upgradable' in l])
                if upgrade_count > 0:
                    results.append(f"\nUPDATES: {upgrade_count} packages can be upgraded")
                else:
                    results.append("\nUPDATES: System is up to date ✓")
        except Exception:
            results.append("\nUPDATES: Unable to check (requires sudo)")
        
        # Temperature (if available)
        print_fn("🌡️ Checking system temperature...")
        try:
            temp_files = [
                "/sys/class/thermal/thermal_zone0/temp",
                "/sys/class/hwmon/hwmon0/temp1_input"
            ]
            for tf in temp_files:
                if os.path.exists(tf):
                    with open(tf, 'r') as f:
                        temp = int(f.read().strip()) / 1000
                        results.append(f"\nTEMPERATURE: {temp}°C")
                        break
        except Exception:
            pass
        
        # Makulu-specific check
        print_fn("🔎 Checking Makulu-specific components...")
        makulu_dirs = [
            f"{user_home}/.config/makulu",
            f"{user_home}/.config/makulishell",
        ]
        found_configs = []
        for d in makulu_dirs:
            if os.path.exists(d):
                found_configs.append(d)
        if found_configs:
            results.append("\nMAKULU CONFIG:")
            for c in found_configs:
                results.append(f"  ✓ {c}")
        
        # Security Check - failed services
        print_fn("🔒 Checking failed units...")
        try:
            result = subprocess.run(
                ["systemctl", "--failed", "--no-pager"],
                capture_output=True, text=True, timeout=10
            )
            if result.returncode == 0 and "0 loaded units" not in result.stdout:
                results.append("\n⚠️  FAILED UNITS DETECTED:")
                for line in result.stdout.split('\n')[1:]:
                    if '.service' in line or '.socket' in line:
                        results.append(f"  {line.strip()}")
            else:
                results.append("\nSECURITY: No failed units ✓")
        except Exception:
            pass
        
        results.append("")
        results.append("=" * 50)
        results.append("  SCAN COMPLETE")
        results.append("=" * 50)
        
        print_fn("✅ System scan completed successfully!")
        
        return "\n".join(results)
        
    except subprocess.TimeoutExpired:
        return "⚠️ Scan timeout - some checks did not complete"
    except Exception as e:
        return f"⚠️ Scan encountered an error: {str(e)}\n\nSystem scan may require elevated permissions for some checks."