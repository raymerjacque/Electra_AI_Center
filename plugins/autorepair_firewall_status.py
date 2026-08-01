"""
Electra AI Plugin: Firewall Status Checker
Author: Auto-Repair
Version: 1.0.0
Description: Answers firewall-related questions by checking UFW, iptables,
             nftables, and firewalld status on MakuluLinux / Ubuntu systems.
"""

import os
import shutil
import subprocess

PLUGIN_NAME = "Firewall Status Checker"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Checks firewall status (ufw, iptables, nftables, firewalld)"
PLUGIN_AUTHOR = "Auto-Repair"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_TRIGGERS = [
    "firewall",
    "fire wall",
    "ufw",
    "iptables",
    "nftables",
    "firewalld",
    "do i have a firewall",
    "is my firewall on",
    "firewall status",
    "is firewall active",
]
PLUGIN_ROUTE_TOKEN = "FIREWALL_STATUS"
PLUGIN_COMMANDS = ["/firewall"]
PLUGIN_REQUIRES = []


def _find_command(cmd):
    """Locate a command in PATH or common Linux sbin directories."""
    path = shutil.which(cmd)
    if path:
        return path
    for base in ("/usr/sbin", "/sbin", "/usr/bin", "/bin"):
        candidate = os.path.join(base, cmd)
        if os.path.exists(candidate):
            return candidate
    return None


def _run_command(args, timeout=8):
    """
    Run a system command safely.

    Returns (returncode, stdout, stderr).
    returncode is None if the command could not be executed.
    """
    try:
        proc = subprocess.run(
            args,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=timeout,
        )
        return proc.returncode, proc.stdout.strip(), proc.stderr.strip()
    except FileNotFoundError:
        return None, "", "command not found"
    except subprocess.TimeoutExpired:
        return None, "", "timeout"
    except Exception as exc:  # noqa: BLE001 - must never crash host
        return None, "", str(exc)


def _systemd_unit_state(unit):
    """Return (enabled, active) state strings for a systemd unit."""
    systemctl = _find_command("systemctl")
    if not systemctl:
        return "unknown", "unknown"

    _, out_enabled, _ = _run_command([systemctl, "is-enabled", unit])
    _, out_active, _ = _run_command([systemctl, "is-active", unit])

    enabled = out_enabled.strip() if out_enabled else "unknown"
    active = out_active.strip() if out_active else "unknown"
    return enabled, active


def _maybe_sudo(args, euid):
    """Prefix with sudo non-interactive if not root."""
    if euid == 0:
        return args
    return ["sudo", "-n"] + args


def _check_ufw(print_fn, euid):
    """Return a human-readable UFW status line."""
    ufw = _find_command("ufw")
    if not ufw:
        return "**UFW**: not installed"

    print_fn("🛡️ Checking UFW...")

    # Try with sudo (non-interactive) first, then without.
    for args in (
        _maybe_sudo([ufw, "status", "verbose"], euid),
        [ufw, "status", "verbose"],
        [ufw, "status"],
    ):
        rc, out, _ = _run_command(args)
        if rc == 0 and "Status:" in out:
            active = "status: active" in out.lower()
            if "verbose" in args:
                return (
                    f"**UFW** (installed): **{'ACTIVE' if active else 'INACTIVE'}**\n"
                    f"```\n{out}\n```"
                )
            return (
                f"**UFW** (installed): **{'ACTIVE' if active else 'INACTIVE'}**\n"
                f"`{out}`"
            )

    # Fallback to systemd state.
    enabled, active = _systemd_unit_state("ufw")
    return (
        f"**UFW** (installed): status requires root - systemd enabled={enabled}, "
        f"active={active}"
    )


def _check_iptables(print_fn, euid):
    """Return a human-readable iptables status line."""
    ipt = _find_command("iptables")
    if not ipt:
        return "**iptables**: not installed"

    print_fn("🕵️ Checking iptables...")

    rc, out, _ = _run_command(_maybe_sudo([ipt, "-L", "-n"], euid))
    if rc == 0:
        # Count actual rule lines (skip headers and chain declarations).
        rule_count = 0
        for line in out.splitlines():
            line = line.strip()
            if (
                line
                and not line.startswith("Chain ")
                and line != "target prot opt source destination"
                and line != "pkts bytes target prot opt in out source destination"
            ):
                rule_count += 1
        active = rule_count > 0 or "Chain INPUT" in out
        state = "ACTIVE" if active else "NO RULES / INACTIVE"
        return f"**iptables** (installed): **{state}** ({rule_count} rules found)"

    # Check kernel module/table presence as a fallback.
    try:
        with open("/proc/net/ip_tables_names", "r") as f:
            tables = [line.strip() for line in f if line.strip()]
        if tables:
            return (
                f"**iptables**: installed - kernel tables loaded "
                f"({', '.join(tables)}), may have rules"
            )
        return "**iptables**: installed but no kernel tables loaded (no rules)"
    except Exception:
        return "**iptables**: installed but status requires root (or sudo unavailable)"


def _check_nftables(print_fn, euid):
    """Return a human-readable nftables status line."""
    nft = _find_command("nft")
    if not nft:
        return "**nftables**: not installed"

    print_fn("🔧 Checking nftables...")

    rc, out, _ = _run_command(_maybe_sudo([nft, "list", "ruleset"], euid))
    if rc == 0:
        if out.strip():
            return f"**nftables** (installed): **ACTIVE**\n```\n{out}\n```"
        return "**nftables** (installed): active but **no rules**"

    return "**nftables**: installed but status requires root (or sudo unavailable)"


def _check_firewalld(print_fn):
    """Return a human-readable firewalld status line."""
    if not (_find_command("firewalld") or _find_command("firewall-cmd")):
        return "**firewalld**: not installed"

    print_fn("🔥 Checking firewalld...")
    enabled, active = _systemd_unit_state("firewalld")
    return f"**firewalld** (installed): systemd enabled={enabled}, active={active}"


def run(prompt: str, context: dict) -> str:
    """Handle firewall status requests."""
    print_fn = context.get("print_fn") or print
    euid = os.geteuid() if hasattr(os, "geteuid") else None

    results = []

    # UFW
    ufw_result = _check_ufw(print_fn, euid)
    results.append(ufw_result)

    # iptables
    ipt_result = _check_iptables(print_fn, euid)
    results.append(ipt_result)

    # nftables
    nft_result = _check_nftables(print_fn, euid)
    results.append(nft_result)

    # firewalld
    fw_result = _check_firewalld(print_fn)
    results.append(fw_result)

    # Determine active firewalls for the summary.
    active_firewalls = []
    if "**UFW**" in ufw_result and "**ACTIVE**" in ufw_result:
        active_firewalls.append("UFW")
    if "**iptables**" in ipt_result and "**ACTIVE**" in ipt_result:
        active_firewalls.append("iptables")
    if "**nftables**" in nft_result and "**ACTIVE**" in nft_result:
        active_firewalls.append("nftables")
    if "**firewalld**" in fw_result and "active=active" in fw_result:
        active_firewalls.append("firewalld")

    if active_firewalls:
        summary = (
            f"🟢 **Yes** — you have an active firewall: "
            f"**{', '.join(active_firewalls)}**."
        )
    else:
        summary = (
            "🔴 **No active firewall detected** — review the details below."
        )

    # Build suggestion list only for systems with UFW installed but inactive.
    suggestions = []
    if (
        "**UFW**" in ufw_result
        and "not installed" not in ufw_result
        and ("**INACTIVE**" in ufw_result or "systemd active=inactive" in ufw_result)
    ):
        suggestions.append(
            "Consider enabling UFW with `sudo ufw enable` "
            "(make sure SSH access is allowed first)."
        )
    if "**firewalld**" in fw_result and "active=inactive" in fw_result:
        suggestions.append(
            "Firewalld is installed but not running; use "
            "`sudo systemctl enable --now firewalld` to activate it."
        )

    output = [
        "## Firewall Status",
        "",
        summary,
        "",
        *results,
        "",
    ]
    if suggestions:
        output.append("### Suggestions")
        output.extend(f"- {s}" for s in suggestions)
        output.append("")

    output.append("---")
    output.append("_Checked via UFW, iptables, nftables, and firewalld._")

    print_fn("✅ Firewall status check complete.")
    return "\n".join(output)