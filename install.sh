#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════════════════
#  Electra AI Center — Installer
#  Usage:  curl -fsSL https://raw.githubusercontent.com/raymerjacque/Electra_AI_Center/main/install.sh | bash
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
_grey()    { echo -e "${GREY}    $*${RESET}"; }

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
echo -e "  ${BOLD}Electra AI Center${RESET} — MakuluLinux"
echo -e "  ${GREY}An all-in-one AI terminal: Chat · Coder · Writer · Command${RESET}"
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
BIN_BAR="${INSTALL_DIR}/electra_bar.bin"
AUTOSTART_DIR="${REAL_HOME}/.config/autostart"
AUTOSTART_FILE="${AUTOSTART_DIR}/electra-bar.desktop"
GITHUB_BASE="https://github.com/raymerjacque/Electra_AI_Center/releases/latest/download"

# ── Functions ─────────────────────────────────────────────────────────────────
apt_install() {
    # Install apt packages only if not already present
    local missing=()
    for pkg in "$@"; do
        dpkg -s "$pkg" &>/dev/null || missing+=("$pkg")
    done
    if [[ ${#missing[@]} -gt 0 ]]; then
        _info "apt installing: ${missing[*]}"
        apt-get install -y -qq "${missing[@]}"
    fi
}

pip_install() {
    # Install pip packages only if not already importable
    local missing=()
    for pkg in "$@"; do
        # Map pip name → importable name where they differ
        local import_name="${pkg//-/_}"
        import_name="${import_name%%[>=<!]*}"   # strip version specifiers
        python3 -c "import ${import_name}" 2>/dev/null || missing+=("$pkg")
    done
    if [[ ${#missing[@]} -gt 0 ]]; then
        _info "pip installing: ${missing[*]}"
        pip3 install -q --break-system-packages "${missing[@]}" 2>/dev/null || \
        pip3 install -q "${missing[@]}" 2>/dev/null || true
    fi
}

# ══════════════════════════════════════════════════════════════════════════════
_section "Step 1 — System package dependencies"
# ══════════════════════════════════════════════════════════════════════════════

_info "Updating package lists…"
apt-get update -qq

# ── Core runtime: required for the binary to function ─────────────────────────
_info "Installing core runtime libraries…"
apt_install \
    python3 python3-pip \
    libportaudio2 \
    ffmpeg \
    terminator \
    python3-tk

# ── GTK3 runtime: required by electra_bar.bin ─────────────────────────────────
_info "Installing GTK3 runtime…"
apt_install \
    gir1.2-gtk-3.0 \
    gir1.2-gdk-3.0 \
    gir1.2-pango-1.0 \
    libgirepository1.0-dev \
    python3-gi \
    python3-gi-cairo

# ── Optional but highly recommended tools ─────────────────────────────────────
_info "Installing optional tools (mpv for audio, bat for IDE preview, xdotool for clipboard)…"
apt_install \
    mpv \
    bat \
    xdotool \
    scrot \
    curl \
    wget || true   # non-fatal if any optional package is unavailable

_ok "System packages ready."

# ══════════════════════════════════════════════════════════════════════════════
_section "Step 2 — Python package dependencies"
# ══════════════════════════════════════════════════════════════════════════════
# These are lazy imports NOT bundled in ai_terminal.bin — loaded at runtime.
# The binary works without them, but these features won't function until installed:
#   chromadb        → long-term memory / MemPalace (coder + chat)
#   qrcode          → /qr command
#   paramiko        → /ssh command
#   geocoder        → weather auto-location fallback
#   python-docx     → read/write Word documents (writer mode)
#   markdown        → Markdown rendering in writer/export
#   pdfminer-six    → read PDFs in coder/writer mode
#   pypdf           → PDF page manipulation
#   faster-whisper  → voice input (mic button in electra_bar)
#   pyaudio         → microphone audio capture

_info "Installing Python runtime dependencies…"

pip_install \
    chromadb \
    qrcode \
    paramiko \
    geocoder \
    python-docx \
    markdown \
    "pdfminer.six" \
    pypdf \
    faster-whisper \
    pyaudio

_ok "Python packages ready."

# ══════════════════════════════════════════════════════════════════════════════
_section "Step 3 — Downloading Electra AI Center binaries"
# ══════════════════════════════════════════════════════════════════════════════

_info "Creating install directory: ${INSTALL_DIR}"
mkdir -p "${INSTALL_DIR}"

# ── Download ai_terminal.bin ──────────────────────────────────────────────────
_info "Downloading ai_terminal.bin…"
if curl -fsSL --progress-bar \
    "${GITHUB_BASE}/ai_terminal.bin" \
    -o "${BIN_TERMINAL}"; then
    _ok "ai_terminal.bin downloaded."
else
    _err "Failed to download ai_terminal.bin from ${GITHUB_BASE}. Check the URL and try again."
fi

# ── Download electra_bar.bin ──────────────────────────────────────────────────
_info "Downloading electra_bar.bin…"
if curl -fsSL --progress-bar \
    "${GITHUB_BASE}/electra_bar.bin" \
    -o "${BIN_BAR}"; then
    _ok "electra_bar.bin downloaded."
else
    _err "Failed to download electra_bar.bin from ${GITHUB_BASE}. Check the URL and try again."
fi

# ══════════════════════════════════════════════════════════════════════════════
_section "Step 4 — Setting permissions"
# ══════════════════════════════════════════════════════════════════════════════

_info "Setting directory and binary permissions…"
chmod 777 "${INSTALL_DIR}"
chmod 755 "${BIN_TERMINAL}"
chmod 755 "${BIN_BAR}"
_ok "Permissions set."

# ══════════════════════════════════════════════════════════════════════════════
_section "Step 5 — Autostart (Electra Bar on login)"
# ══════════════════════════════════════════════════════════════════════════════

_info "Installing autostart entry for ${REAL_USER}…"
mkdir -p "${AUTOSTART_DIR}"

cat > "${AUTOSTART_FILE}" << DESKTOP
[Desktop Entry]
Type=Application
Name=Electra Bar
Comment=Electra AI Center floating input bar
Exec=${BIN_BAR}
Icon=utilities-terminal
Terminal=false
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
X-GNOME-Autostart-Delay=3
DESKTOP

# Fix ownership back to the real user (we're running as root)
chown "${REAL_USER}:${REAL_USER}" "${AUTOSTART_FILE}"
_ok "Autostart entry created: ${AUTOSTART_FILE}"

# ══════════════════════════════════════════════════════════════════════════════
_section "Step 6 — Launching Electra Bar"
# ══════════════════════════════════════════════════════════════════════════════

_info "Starting Electra Bar for ${REAL_USER}…"

# Launch as the real (non-root) user so GTK connects to the correct display
if [[ -n "${DISPLAY:-}" ]] || [[ -n "${WAYLAND_DISPLAY:-}" ]]; then
    sudo -u "${REAL_USER}" \
        DISPLAY="${DISPLAY:-:0}" \
        DBUS_SESSION_BUS_ADDRESS="${DBUS_SESSION_BUS_ADDRESS:-unix:path=/run/user/$(id -u "${REAL_USER}")/bus}" \
        nohup "${BIN_BAR}" >/dev/null 2>&1 &
    _ok "Electra Bar launched."
else
    _warn "No display detected (DISPLAY/WAYLAND_DISPLAY not set)."
    _warn "Electra Bar will start automatically on your next login."
fi

# ══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${GREEN}${BOLD}  ════════════════════════════════════════════════════════${RESET}"
echo -e "${GREEN}${BOLD}  ✔  Electra AI Center installed successfully!${RESET}"
echo -e "${GREEN}${BOLD}  ════════════════════════════════════════════════════════${RESET}"
echo ""
echo -e "  ${BOLD}To start the AI terminal:${RESET}"
echo -e "  ${CYAN}  ${BIN_TERMINAL}${RESET}"
echo ""
echo -e "  ${BOLD}The floating bar starts automatically on every login.${RESET}"
echo ""
echo -e "  ${GREY}Optional extras (install anytime):${RESET}"
echo -e "  ${GREY}  pip3 install playwright && playwright install chromium   # Finance bot${RESET}"
echo -e "  ${GREY}  pip3 install chromadb                                    # Enhanced memory (already installed above)${RESET}"
echo ""

# ══════════════════════════════════════════════════════════════════════════════
_section "Step 7 — Nemo right-click integration"
# ══════════════════════════════════════════════════════════════════════════════

_info "Installing Nemo file manager right-click action..."

NEMO_ACTIONS_DIR="${REAL_HOME}/.local/share/nemo/actions"
mkdir -p "${NEMO_ACTIONS_DIR}"

# Nemo action definition
cat > "${NEMO_ACTIONS_DIR}/electra-open.nemo_action" << 'NEMO_ACTION'
[Nemo Action]
Name=Open in Electra AI
Comment=Open selected file or folder in Electra AI coder mode
Exec=/usr/share/MakuluSetup/tools/electra-nemo-open.sh %F
Icon-Name=utilities-terminal
Selection=Any
Extensions=any;
Quote=double
NEMO_ACTION

# Shell script Nemo calls
cat > "/usr/share/MakuluSetup/tools/electra-nemo-open.sh" << 'NEMO_SCRIPT'
#!/usr/bin/env bash
TARGET="${1:-$HOME}"
BIN="/usr/share/MakuluSetup/tools/ai_terminal.bin"
if [[ -f "$TARGET" ]]; then
    WORKDIR=$(dirname "$TARGET")
elif [[ -d "$TARGET" ]]; then
    WORKDIR="$TARGET"
else
    WORKDIR="$HOME"
fi
cd "$WORKDIR"
if command -v gnome-terminal &>/dev/null; then
    gnome-terminal -- bash -c "\"$BIN\" --gui --coder; exec bash" &
elif command -v xterm &>/dev/null; then
    xterm -e bash -c "\"$BIN\" --gui --coder; exec bash" &
else
    "$BIN" --gui --coder &
fi
NEMO_SCRIPT

chmod +x "/usr/share/MakuluSetup/tools/electra-nemo-open.sh"
chown "${REAL_USER}:${REAL_USER}" "${NEMO_ACTIONS_DIR}/electra-open.nemo_action"
_ok "Nemo action installed — right-click any file/folder → 'Open in Electra AI'"

# ══════════════════════════════════════════════════════════════════════════════
_section "Step 8 — Cinnamon global hotkey (Super+E → Electra Bar)"
# ══════════════════════════════════════════════════════════════════════════════

CURRENT_DE="${XDG_CURRENT_DESKTOP:-}"
if [[ "$CURRENT_DE" == *"Cinnamon"* ]] || [[ "$CURRENT_DE" == *"X-Cinnamon"* ]] || \
   command -v cinnamon &>/dev/null; then

    _run_as_user() {
        sudo -u "${REAL_USER}" \
            DISPLAY="${DISPLAY:-:0}" \
            DBUS_SESSION_BUS_ADDRESS="${DBUS_SESSION_BUS_ADDRESS:-unix:path=/run/user/$(id -u "${REAL_USER}")/bus}" \
            "$@" 2>/dev/null || true
    }

    HKPATH="/org/cinnamon/desktop/keybindings/custom-keybindings/electra-bar/"
    HKSCHEMA="org.cinnamon.desktop.keybindings.custom-keybindings"

    _run_as_user gsettings set "${HKSCHEMA}:${HKPATH}" name    "Electra AI Bar"
    _run_as_user gsettings set "${HKSCHEMA}:${HKPATH}" command "${BIN_BAR}"
    _run_as_user gsettings set "${HKSCHEMA}:${HKPATH}" binding "['<Super>e']"

    EXISTING=$(_run_as_user gsettings get org.cinnamon.desktop.keybindings custom-list || echo "[]")
    if [[ "$EXISTING" != *"electra-bar"* ]]; then
        if [[ "$EXISTING" == "[]" ]]; then
            NEW_LIST="['electra-bar']"
        else
            NEW_LIST=$(echo "$EXISTING" | sed "s/]$/, 'electra-bar']/")
        fi
        _run_as_user gsettings set org.cinnamon.desktop.keybindings custom-list "${NEW_LIST}"
    fi

    _ok "Global hotkey registered: Super+E → Electra Bar"
    _grey "Takes effect after logging out and back in (or: killall -HUP cinnamon)"
else
    _warn "Cinnamon desktop not detected — skipping global hotkey."
    _grey "To add manually: System Settings → Keyboard → Shortcuts → Custom Shortcuts"
fi

echo ""
echo -e "  ${GREY}LSP language servers (optional, enables AI go-to-definition):${RESET}"
echo -e "  ${GREY}  pip3 install pyright                                     # Python${RESET}"
echo -e "  ${GREY}  npm install -g typescript-language-server typescript     # JS/TS${RESET}"
echo -e "  ${GREY}  sudo apt install clangd                                  # C/C++${RESET}"
echo -e "  ${GREY}  rustup component add rust-analyzer                      # Rust${RESET}"
echo -e "  ${GREY}  go install golang.org/x/tools/gopls@latest              # Go${RESET}"
echo ""
