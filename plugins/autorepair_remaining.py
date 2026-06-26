"""
Auto-repair plugin for /remaining command.
Provides system resource information including disk space, memory, and swap usage.
"""

import os

PLUGIN_NAME = "Remaining Resources"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Check remaining disk space, memory, and system resources"
PLUGIN_AUTHOR = "Electra AI"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = ["/remaining", "remaining", "check remaining", "disk space", "free space", "storage left"]
PLUGIN_ROUTE_TOKEN = "REMAINING"
PLUGIN_COMMANDS = ["/remaining"]
PLUGIN_REQUIRES = []

def run(prompt: str, context: dict) -> str:
    """Check system resources and return formatted status."""
    try:
        context["print_fn"]("🔍 Checking system resources...")
        
        output = ["=== System Resource Status ===\n"]
        
        # Root partition
        try:
            usage = os.statvfs('/')
            free_gb = (usage.f_bavail * usage.f_frsize) // (1024**3)
            total_gb = (usage.f_blocks * usage.f_frsize) // (1024**3)
            used_gb = total_gb - free_gb
            percent_free = (free_gb / total_gb * 100) if total_gb > 0 else 0
            
            output.append(f"📁 Root Filesystem (/):")
            output.append(f"   Total: {total_gb:.1f} GB")
            output.append(f"   Used: {used_gb:.1f} GB")
            output.append(f"   Free: {free_gb:.1f} GB ({percent_free:.1f}% free)")
            
            if percent_free < 15:
                output.append("   ⚠️  Warning: Low disk space!")
            output.append("")
        except Exception as e:
            output.append(f"📁 Root Filesystem: Unable to check ({e})\n")
        
        # Memory
        try:
            with open('/proc/meminfo', 'r') as f:
                lines = f.readlines()
            
            mem = {}
            for line in lines:
                if ':' in line:
                    k, v = line.split(':', 1)
                    mem[k.strip()] = int(v.strip().split()[0])
            
            total_mb = mem.get('MemTotal', 0) // 1024
            available_mb = mem.get('MemAvailable', 0) // 1024
            used_mb = total_mb - available_mb
            percent_used = (used_mb / total_mb * 100) if total_mb > 0 else 0
            
            output.append(f"💾 Memory (RAM):")
            output.append(f"   Total: {total_mb:,} MB")
            output.append(f"   Used: {used_mb:,} MB")
            output.append(f"   Available: {available_mb:,} MB ({100-percent_used:.1f}% free)")
            
            if percent_used > 90:
                output.append("   ⚠️  Warning: High memory usage!")
            output.append("")
        except Exception as e:
            output.append(f"💾 Memory: Unable to check ({e})\n")
        
        # Swap
        try:
            with open('/proc/swaps', 'r') as f:
                swap_lines = f.readlines()[1:]
            
            if swap_lines:
                output.append("🔄 Swap:")
                for line in swap_lines:
                    if line.strip():
                        parts = line.split()
                        if len(parts) >= 3:
                            name = parts[0]
                            size_kb = int(parts[1])
                            used_kb = int(parts[2])
                            size_mb = size_kb // 1024
                            used_mb = used_kb // 1024
                            percent = (used_mb / size_mb * 100) if size_mb > 0 else 0
                            output.append(f"   {name}: {used_mb} MB / {size_mb} MB ({percent:.0f}% used)")
            else:
                output.append("🔄 Swap: None active\n")
        except Exception as e:
            output.append(f"🔄 Swap: Unable to check ({e})\n")
        
        result = "\n".join(output)
        context["print_fn"](result)
        return result
        
    except Exception as e:
        error_msg = f"❌ Error checking system resources: {str(e)}"
        context["print_fn"](error_msg)
        return error_msg