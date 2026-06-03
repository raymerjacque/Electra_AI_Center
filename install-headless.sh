#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════════════════
#  Electra AI Center — Headless Server Installer
#  For: Ubuntu/Debian servers, VPS, WSL, SSH-only machines (no desktop/GUI)
#
#  Usage:
#    curl -fsSL https://raw.githubusercontent.com/raymerjacque/Electra_AI_Center/main/install-headless.sh | bash
#
#  What this installs:
#    - ai_terminal.bin only (no electra_bar — bar requires a desktop display)
#    - All Python + system dependencies for terminal features
#    - No GTK, no terminator, no audio, no GUI packages
#    - Optional: systemd service to keep ai_terminal accessible via socket
# ═══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

# ── Colours ───────────────────────────────────────────────────────────────────
BOLD="\033[1m"; RESET="\033[0m"
GREEN="\033[1;32m"; CYAN="\033[1;36m"; YELLOW="\033[1;33m"; RED="\033[1;31m"; GREY="\033[0;37m"

_info()    { echo -e "${CYAN}${BOLD}  ▸ $*${RESET}"; }
_ok()      { echo -e "${GREEN}${BOLD}  ✔ $*${RESET}"; }
_warn()    { echo -e "${YELLOW}  ⚠ $*${RESET}"; }
_err()     { echo -e "${RED}${BOLD}  ✖ $*${RESET}"; exit 1; }
_section() { echo -e "\n${BOLD}${CYAN}━━━ $* ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"; }

# ── Banner ────────────────────────────────────────────────────────────────────
echo ""
echo -e "${CYAN}${BOLD}"
echo "  ███████╗██╗     ███████╗ ██████╗████████╗██████╗  █████╗ "
echo "  ██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗"
echo "  █████╗  ██║     █████╗  ██║        ██║   ██████╔╝███████║"
echo "  ██╔══╝  ██║     ██╔══╝  ██║        ██║   ██╔══██╗██╔══██║"
echo "  ███████╗███████╗███████╗╚██████╗   ██║   ██║  ██║██║  ██║"
echo "  ╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝"
echo -e "${RESET}"
echo -e "  ${BOLD}Electra AI Center${RESET} — Headless / Server Edition"
echo -e "  ${GREY}Terminal-only install: no GUI, no desktop, no display required${RESET}"
echo ""

# ── Privilege check ───────────────────────────────────────────────────────────
if [[ $EUID -ne 0 ]]; then
    _warn "This installer needs sudo for system directories."
    _warn "Re-running with sudo..."
    exec sudo bash "$0" "$@"
fi

REAL_USER="${SUDO_USER:-$USER}"
REAL_HOME=$(getent passwd "$REAL_USER" | cut -d: -f6)

# ── Config ────────────────────────────────────────────────────────────────────
INSTALL_DIR="/usr/share/MakuluSetup/tools"
BIN_TERMINAL="${INSTALL_DIR}/ai_terminal.bin"
GITHUB_BASE="https://github.com/raymerjacque/Electra_AI_Center/releases/latest/download"

# ── Helper functions ──────────────────────────────────────────────────────────
apt_install() {
    local missing=()
    for pkg in "$@"; do
        dpkg -s "$pkg" &>/dev/null || missing+=("$pkg")
    done
    if [[ ${#missing[@]} -gt 0 ]]; then
        _info "apt installing: ${missing[*]}"
        apt-get install -y -qq "${missing[@]}"
    else
        _ok "Already installed: $*"
    fi
}

pip_install() {
    local missing=()
    for pkg in "$@"; do
        local import_name="${pkg//-/_}"
        import_name="${import_name%%[>=<!]*}"
        python3 -c "import ${import_name}" 2>/dev/null || missing+=("$pkg")
    done
    if [[ ${#missing[@]} -gt 0 ]]; then
        _info "pip installing: ${missing[*]}"
        pip3 install -q --break-system-packages "${missing[@]}" 2>/dev/null || \
        pip3 install -q "${missing[@]}" 2>/dev/null || true
    else
        _ok "Already installed: $*"
    fi
}

# ══════════════════════════════════════════════════════════════════════════════
_section "Step 1 — System package dependencies"
# ══════════════════════════════════════════════════════════════════════════════

_info "Updating package lists…"
apt-get update -qq

# ── Core runtime ──────────────────────────────────────────────────────────────
_info "Installing core runtime packages…"
apt_install \
    python3 \
    python3-pip \
    curl \
    wget \
    git \
    ffmpeg \
    inotify-tools

# ── Optional but useful on servers ────────────────────────────────────────────
_info "Installing server tools…"
apt_install \
    bat \
    xdotool \
    tmux \
    screen || true   # non-fatal

_ok "System packages ready."

# ══════════════════════════════════════════════════════════════════════════════
_section "Step 2 — Python package dependencies"
# ══════════════════════════════════════════════════════════════════════════════
# Headless installs only what the terminal backend actually uses.
# Skipped vs desktop install:
#   - pyaudio        (needs PortAudio hardware — no audio on headless)
#   - faster-whisper (voice input — no mic on headless)
#   - qrcode         (display only — no screen)

_info "Installing Python runtime dependencies…"

pip_install \
    chromadb \
    paramiko \
    geocoder \
    python-docx \
    markdown \
    "pdfminer.six" \
    pypdf \
    requests \
    feedparser \
    pyyaml \
    rich \
    termcolor \
    prompt_toolkit

_ok "Python packages ready."

# ══════════════════════════════════════════════════════════════════════════════
_section "Step 3 — Downloading Electra AI Center binary"
# ══════════════════════════════════════════════════════════════════════════════

_info "Creating install directory: ${INSTALL_DIR}"
mkdir -p "${INSTALL_DIR}"

_info "Downloading ai_terminal.bin…"
if curl -fsSL --progress-bar \
    "${GITHUB_BASE}/ai_terminal.bin" \
    -o "${BIN_TERMINAL}"; then
    _ok "ai_terminal.bin downloaded."
else
    _err "Failed to download ai_terminal.bin. Check your connection and try again."
fi

# ── Permissions ───────────────────────────────────────────────────────────────
_section "Step 4 — Setting permissions"

chmod 777 "${INSTALL_DIR}"
chmod 755 "${BIN_TERMINAL}"

# ── Convenience symlink so you can just type "electra" anywhere ───────────────
if [[ ! -f /usr/local/bin/electra ]]; then
    ln -s "${BIN_TERMINAL}" /usr/local/bin/electra
    _ok "Symlink created: electra → ${BIN_TERMINAL}"
else
    _ok "Symlink already exists at /usr/local/bin/electra"
fi

_ok "Permissions set."

# ══════════════════════════════════════════════════════════════════════════════
_section "Step 5 — Shell alias (optional convenience)"
# ══════════════════════════════════════════════════════════════════════════════

# Add alias to the real user's shell config if not already there
SHELL_RC="${REAL_HOME}/.bashrc"
[[ -f "${REAL_HOME}/.zshrc" ]] && SHELL_RC="${REAL_HOME}/.zshrc"

ALIAS_LINE="alias electra='${BIN_TERMINAL}'"
if ! grep -q "alias electra=" "${SHELL_RC}" 2>/dev/null; then
    echo "" >> "${SHELL_RC}"
    echo "# Electra AI Center" >> "${SHELL_RC}"
    echo "${ALIAS_LINE}" >> "${SHELL_RC}"
    chown "${REAL_USER}:${REAL_USER}" "${SHELL_RC}"
    _ok "Alias added to ${SHELL_RC}"
else
    _ok "Alias already in ${SHELL_RC}"
fi

# ══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${GREEN}${BOLD}  ════════════════════════════════════════════════════════${RESET}"
echo -e "${GREEN}${BOLD}  ✔  Electra AI Center (Headless) installed successfully!${RESET}"
echo -e "${GREEN}${BOLD}  ════════════════════════════════════════════════════════${RESET}"
echo ""
echo -e "  ${BOLD}Start the AI terminal:${RESET}"
echo -e "  ${CYAN}  electra${RESET}                        # via symlink (after re-login or: source ~/.bashrc)"
echo -e "  ${CYAN}  ${BIN_TERMINAL}${RESET}     # direct path"
echo ""
echo -e "  ${BOLD}Modes available on headless:${RESET}"
echo -e "  ${GREY}  /chat     — AI chat${RESET}"
echo -e "  ${GREY}  /coder    — AI coding agent${RESET}"
echo -e "  ${GREY}  /writer   — document & content generation${RESET}"
echo -e "  ${GREY}  /command  — autonomous system command execution${RESET}"
echo ""
echo -e "  ${BOLD}Not available on headless (requires desktop):${RESET}"
echo -e "  ${GREY}  electra_bar  (floating input widget — needs display)${RESET}"
echo -e "  ${GREY}  /gui         (IDE mode — needs GTK display)${RESET}"
echo -e "  ${GREY}  voice input  (needs microphone + PortAudio)${RESET}"
echo ""
echo -e "  ${GREY}Optional extras:${RESET}"
echo -e "  ${GREY}  pip3 install playwright && playwright install chromium   # Finance bot${RESET}"
echo ""
