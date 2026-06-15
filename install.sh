#!/usr/bin/env bash
# ═══════════════════════════════════════════════════════════════════════════════
#  Electra AI Center — Universal Installer
#  Supports: Debian · Ubuntu · Fedora · RHEL · Arch · openSUSE · Void · Alpine
#            Gentoo · and any distro with a known package manager
#
#  Usage:
#    curl -fsSL https://raw.githubusercontent.com/raymerjacque/Electra_AI_Center/main/install.sh | bash
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
_skip()    { echo -e "${GREY}  ─ $* (skipped)${RESET}"; }

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
echo -e "  ${BOLD}Electra AI Center${RESET} — Universal Linux Installer"
echo -e "  ${GREY}Chat · Coder · Writer · Novel · Command · GUI${RESET}"
echo ""

# ═══════════════════════════════════════════════════════════════════════════════
#  PRIVILEGE CHECK
#  When piped via curl, $0 is "bash" so we can't re-exec the file directly.
#  We re-download and pipe into sudo/doas bash instead.
# ═══════════════════════════════════════════════════════════════════════════════
if [[ $EUID -ne 0 ]]; then
    if command -v sudo &>/dev/null; then
        _warn "Root required. Re-running with sudo…"
        exec sudo bash -c "$(curl -fsSL https://raw.githubusercontent.com/raymerjacque/Electra_AI_Center/main/install.sh)"
    elif command -v doas &>/dev/null; then
        _warn "Root required. Re-running with doas…"
        exec doas bash -c "$(curl -fsSL https://raw.githubusercontent.com/raymerjacque/Electra_AI_Center/main/install.sh)"
    else
        _err "Root privileges required. Please run as root or install sudo."
    fi
fi

REAL_USER="${SUDO_USER:-${DOAS_USER:-$USER}}"
REAL_HOME="$(getent passwd "$REAL_USER" | cut -d: -f6)" || REAL_HOME="$HOME"

# ═══════════════════════════════════════════════════════════════════════════════
#  PRE-INSTALL CLEANUP — remove stale plugin cache
# ═══════════════════════════════════════════════════════════════════════════════
AI_PLUGINS_DIR="${REAL_HOME}/.config/ai_plugins"
if [[ -d "${AI_PLUGINS_DIR}" ]]; then
    _info "Removing stale plugin cache: ${AI_PLUGINS_DIR}"
    rm -rf "${AI_PLUGINS_DIR}"
    _ok "Removed ${AI_PLUGINS_DIR}"
else
    _skip "Plugin cache not found — nothing to remove (${AI_PLUGINS_DIR})"
fi

# ═══════════════════════════════════════════════════════════════════════════════
#  PATHS & URLS
# ═══════════════════════════════════════════════════════════════════════════════
INSTALL_DIR="/usr/share/MakuluSetup/tools"
BIN_TERMINAL="${INSTALL_DIR}/ai_terminal.bin"
BIN_BAR="${INSTALL_DIR}/electra_bar.bin"
AUTOSTART_DIR="${REAL_HOME}/.config/autostart"
AUTOSTART_FILE="${AUTOSTART_DIR}/electra-bar.desktop"
GITHUB_BASE="https://github.com/raymerjacque/Electra_AI_Center/releases/latest/download"

# ═══════════════════════════════════════════════════════════════════════════════
#  DISTRO DETECTION
# ═══════════════════════════════════════════════════════════════════════════════
DISTRO_ID=""
DISTRO_LIKE=""
FAMILY=""
PKG_MGR=""
PKG_INSTALL=""
PKG_QUERY=""
PKG_UPDATE=""
PIP_PKG=""          # distro pip package name
HAS_DISPLAY=false   # true when a graphical display is available
DESKTOP_ENV=""      # detected DE: gnome | kde | cinnamon | xfce | mate | lxde | lxqt | budgie | unknown

detect_distro() {
    if [[ -f /etc/os-release ]]; then
        # shellcheck disable=SC1091
        . /etc/os-release
        DISTRO_ID="$(echo "${ID:-}" | tr '[:upper:]' '[:lower:]')"
        DISTRO_LIKE="$(echo "${ID_LIKE:-}" | tr '[:upper:]' '[:lower:]')"
    fi

    # Map distro ID → family
    case "$DISTRO_ID" in
        debian|ubuntu|pop|mint|linuxmint|zorin|elementary|kali|raspbian|deepin|uos|neon|devuan|trisquel|makulu|mxlinux|mx)
            FAMILY="debian" ;;
        fedora|rhel|centos|rocky|almalinux|amzn|ol|redhat|nobara|ultramarine)
            FAMILY="fedora" ;;
        arch|manjaro|endeavour|arcolinux|garuda|artix|cachyos|crystal|xerolinux)
            FAMILY="arch" ;;
        alpine)
            FAMILY="alpine" ;;
        opensuse*|suse*|sles|tumbleweed|leap)
            FAMILY="opensuse" ;;
        void)
            FAMILY="void" ;;
        gentoo|funtoo|calculate)
            FAMILY="gentoo" ;;
        slackware|salix)
            FAMILY="slackware" ;;
        *)
            # Fallback: check ID_LIKE
            case " $DISTRO_LIKE " in
                *"debian"*|*"ubuntu"*)  FAMILY="debian"   ;;
                *"fedora"*|*"rhel"*)    FAMILY="fedora"   ;;
                *"arch"*)               FAMILY="arch"     ;;
                *"suse"*)               FAMILY="opensuse" ;;
                *"alpine"*)             FAMILY="alpine"   ;;
                *)
                    # Last resort: detect by available binary
                    if   command -v apt-get    &>/dev/null; then FAMILY="debian"
                    elif command -v dnf         &>/dev/null; then FAMILY="fedora"
                    elif command -v pacman      &>/dev/null; then FAMILY="arch"
                    elif command -v zypper      &>/dev/null; then FAMILY="opensuse"
                    elif command -v apk         &>/dev/null; then FAMILY="alpine"
                    elif command -v xbps-install &>/dev/null; then FAMILY="void"
                    elif command -v emerge      &>/dev/null; then FAMILY="gentoo"
                    else _err "Unsupported distribution — no known package manager found."
                    fi
                    _warn "Could not identify distro from /etc/os-release; detected by package manager."
                    ;;
            esac
            ;;
    esac

    # Set package manager commands
    case "$FAMILY" in
        debian)
            PKG_MGR="apt-get"
            PKG_INSTALL="install -y -qq"
            PKG_QUERY="dpkg -s"
            PKG_UPDATE="apt-get update -qq"
            PIP_PKG="python3-pip"
            ;;
        fedora)
            if command -v dnf5 &>/dev/null; then
                PKG_MGR="dnf5"
            elif command -v dnf &>/dev/null; then
                PKG_MGR="dnf"
            else
                PKG_MGR="yum"
            fi
            PKG_INSTALL="install -y"
            PKG_QUERY="rpm -q"
            PKG_UPDATE="${PKG_MGR} makecache -y -q"
            PIP_PKG="python3-pip"
            ;;
        arch)
            PKG_MGR="pacman"
            PKG_INSTALL="-S --noconfirm --needed"
            PKG_QUERY="pacman -Qi"
            PKG_UPDATE="pacman -Sy --noconfirm"
            PIP_PKG="python-pip"
            ;;
        alpine)
            PKG_MGR="apk"
            PKG_INSTALL="add --no-interactive"
            PKG_QUERY="apk info -e"
            PKG_UPDATE="apk update -q"
            PIP_PKG="py3-pip"
            ;;
        opensuse)
            PKG_MGR="zypper"
            PKG_INSTALL="install -y --no-recommends"
            PKG_QUERY="rpm -q"
            PKG_UPDATE="zypper refresh -q"
            PIP_PKG="python3-pip"
            ;;
        void)
            PKG_MGR="xbps-install"
            PKG_INSTALL="-y"
            PKG_QUERY="xbps-query -S"
            PKG_UPDATE="xbps-install -Su -y"
            PIP_PKG="python3-pip"
            ;;
        gentoo)
            PKG_MGR="emerge"
            PKG_INSTALL="--noreplace --quiet"
            PKG_QUERY="qlist -I"
            PKG_UPDATE="emerge --sync -q"
            PIP_PKG="dev-python/pip"
            ;;
        slackware)
            PKG_MGR="slackpkg"
            PKG_INSTALL="install"
            PKG_QUERY="slackpkg search"
            PKG_UPDATE="slackpkg update"
            PIP_PKG="python3-pip"
            ;;
    esac

    # Detect display
    if [[ -n "${DISPLAY:-}" ]] || [[ -n "${WAYLAND_DISPLAY:-}" ]]; then
        HAS_DISPLAY=true
    fi

    # Detect desktop environment
    # Check env vars first (set by the running session), then fall back to
    # probing installed session files — works even when run via sudo.
    local de_raw="${XDG_CURRENT_DESKTOP:-${DESKTOP_SESSION:-${XDG_SESSION_DESKTOP:-}}}"
    de_raw="${de_raw,,}"  # lowercase
    case "$de_raw" in
        *kde*|*plasma*)           DESKTOP_ENV="kde"      ;;
        *cinnamon*)               DESKTOP_ENV="cinnamon" ;;
        *gnome*)                  DESKTOP_ENV="gnome"    ;;
        *xfce*)                   DESKTOP_ENV="xfce"     ;;
        *mate*)                   DESKTOP_ENV="mate"     ;;
        *lxqt*)                   DESKTOP_ENV="lxqt"     ;;
        *lxde*)                   DESKTOP_ENV="lxde"     ;;
        *budgie*)                 DESKTOP_ENV="budgie"   ;;
        *pantheon*)               DESKTOP_ENV="pantheon" ;;
        *)
            # Fallback: probe for running DE processes
            if   pgrep -x plasmashell   &>/dev/null; then DESKTOP_ENV="kde"
            elif pgrep -x cinnamon      &>/dev/null; then DESKTOP_ENV="cinnamon"
            elif pgrep -x gnome-shell   &>/dev/null; then DESKTOP_ENV="gnome"
            elif pgrep -x xfce4-session &>/dev/null; then DESKTOP_ENV="xfce"
            elif pgrep -x mate-session  &>/dev/null; then DESKTOP_ENV="mate"
            elif pgrep -x lxqt-session  &>/dev/null; then DESKTOP_ENV="lxqt"
            elif pgrep -x lxsession     &>/dev/null; then DESKTOP_ENV="lxde"
            elif pgrep -x budgie-daemon &>/dev/null; then DESKTOP_ENV="budgie"
            else
                # Last resort: check installed session files
                if   [[ -f /usr/share/xsessions/plasma.desktop ]]   || \
                     [[ -f /usr/share/wayland-sessions/plasmawayland.desktop ]]; then
                    DESKTOP_ENV="kde"
                elif [[ -f /usr/share/xsessions/cinnamon.desktop ]]; then
                    DESKTOP_ENV="cinnamon"
                elif [[ -f /usr/share/xsessions/gnome.desktop ]];    then
                    DESKTOP_ENV="gnome"
                elif [[ -f /usr/share/xsessions/xfce.desktop ]];     then
                    DESKTOP_ENV="xfce"
                elif [[ -f /usr/share/xsessions/mate.desktop ]];     then
                    DESKTOP_ENV="mate"
                else
                    DESKTOP_ENV="unknown"
                fi
            fi
            ;;
    esac

    local display_label="headless (no display)"
    $HAS_DISPLAY && display_label="desktop (display detected)"

    _ok "Distro  : ${DISTRO_ID:-unknown} → family: ${FAMILY}  (manager: ${PKG_MGR})"
    _ok "Mode    : ${display_label}"
    $HAS_DISPLAY && _ok "Desktop : ${DESKTOP_ENV}"
}

# ═══════════════════════════════════════════════════════════════════════════════
#  PACKAGE INSTALL HELPERS
# ═══════════════════════════════════════════════════════════════════════════════

# pkg_install <pkg> [pkg...] — installs only what's missing, non-fatal by default
pkg_install() {
    local missing=()
    for pkg in "$@"; do
        case "$FAMILY" in
            debian)   $PKG_QUERY "$pkg" &>/dev/null || missing+=("$pkg") ;;
            fedora|opensuse|slackware) $PKG_QUERY "$pkg" &>/dev/null || missing+=("$pkg") ;;
            arch)     $PKG_QUERY "$pkg" &>/dev/null || missing+=("$pkg") ;;
            alpine)   $PKG_QUERY "$pkg" &>/dev/null || missing+=("$pkg") ;;
            void)     $PKG_QUERY "$pkg" &>/dev/null || missing+=("$pkg") ;;
            gentoo)
                if command -v qlist &>/dev/null; then
                    qlist -I "$pkg" &>/dev/null || missing+=("$pkg")
                else
                    missing+=("$pkg")
                fi ;;
        esac
    done

    if [[ ${#missing[@]} -gt 0 ]]; then
        _info "Installing: ${missing[*]}"
        # shellcheck disable=SC2086
        "$PKG_MGR" $PKG_INSTALL "${missing[@]}" || {
            _warn "Some packages failed to install: ${missing[*]} — continuing."
            return 1
        }
    fi
}

# pkg_install_optional — same but always non-fatal (swallows errors silently)
pkg_install_optional() {
    pkg_install "$@" 2>/dev/null || true
}

# Map generic package names to distro-specific equivalents
# Usage: pkg_name <generic-name>  → echoes the right name for this distro
pkg_name() {
    local generic="$1"
    case "$FAMILY" in
        debian)
            case "$generic" in
                portaudio)          echo "libportaudio2" ;;
                python-gobject)     echo "python3-gi" ;;
                python-gobject-cairo) echo "python3-gi-cairo" ;;
                gobject-introspection) echo "libgirepository1.0-dev" ;;
                gtk3)               echo "gir1.2-gtk-3.0" ;;
                gdk3)               echo "gir1.2-gdk-3.0" ;;
                pango)              echo "gir1.2-pango-1.0" ;;
                python-tk)          echo "python3-tk" ;;
                inotify)            echo "inotify-tools" ;;
                bat)                echo "bat" ;;
                screenshot)         echo "scrot" ;;
                *)                  echo "$generic" ;;
            esac ;;
        fedora)
            case "$generic" in
                portaudio)          echo "portaudio" ;;
                python-gobject)     echo "python3-gobject" ;;
                python-gobject-cairo) echo "python3-cairo" ;;
                gobject-introspection) echo "gobject-introspection-devel" ;;
                gtk3)               echo "gtk3" ;;
                gdk3)               echo "gtk3" ;;          # bundled in gtk3 on fedora
                pango)              echo "pango" ;;
                python-tk)          echo "python3-tkinter" ;;
                inotify)            echo "inotify-tools" ;;
                bat)                echo "bat" ;;
                screenshot)         echo "scrot" ;;
                mpv)                echo "mpv" ;;
                terminator)         echo "terminator" ;;
                *)                  echo "$generic" ;;
            esac ;;
        arch)
            case "$generic" in
                portaudio)          echo "portaudio" ;;
                python-gobject)     echo "python-gobject" ;;
                python-gobject-cairo) echo "python-cairo" ;;
                gobject-introspection) echo "gobject-introspection" ;;
                gtk3)               echo "gtk3" ;;
                gdk3)               echo "gtk3" ;;
                pango)              echo "pango" ;;
                python-tk)          echo "tk" ;;
                inotify)            echo "inotify-tools" ;;
                bat)                echo "bat" ;;
                screenshot)         echo "scrot" ;;
                mpv)                echo "mpv" ;;
                terminator)         echo "terminator" ;;
                *)                  echo "$generic" ;;
            esac ;;
        opensuse)
            case "$generic" in
                portaudio)          echo "portaudio-devel" ;;
                python-gobject)     echo "python3-gobject" ;;
                python-gobject-cairo) echo "python3-cairo" ;;
                gobject-introspection) echo "gobject-introspection-devel" ;;
                gtk3)               echo "gtk3" ;;
                gdk3)               echo "gtk3" ;;
                pango)              echo "pango-devel" ;;
                python-tk)          echo "python3-tk" ;;
                inotify)            echo "inotify-tools" ;;
                bat)                echo "bat" ;;
                screenshot)         echo "scrot" ;;
                terminator)         echo "terminator" ;;
                *)                  echo "$generic" ;;
            esac ;;
        alpine)
            case "$generic" in
                portaudio)          echo "portaudio-dev" ;;
                python-gobject)     echo "py3-gobject3" ;;
                python-gobject-cairo) echo "py3-cairo" ;;
                gobject-introspection) echo "gobject-introspection-dev" ;;
                gtk3)               echo "gtk+3.0" ;;
                gdk3)               echo "gtk+3.0" ;;
                pango)              echo "pango-dev" ;;
                python-tk)          echo "py3-tkinter" ;;
                inotify)            echo "inotify-tools" ;;
                bat)                echo "bat" ;;
                screenshot)         echo "scrot" ;;
                terminator)         echo "" ;;             # not in alpine repos
                mpv)                echo "mpv" ;;
                *)                  echo "$generic" ;;
            esac ;;
        void)
            case "$generic" in
                portaudio)          echo "portaudio-devel" ;;
                python-gobject)     echo "python3-gobject" ;;
                python-gobject-cairo) echo "python3-cairo" ;;
                gobject-introspection) echo "gobject-introspection" ;;
                gtk3)               echo "gtk+3" ;;
                gdk3)               echo "gtk+3" ;;
                pango)              echo "pango" ;;
                python-tk)          echo "python3-tkinter" ;;
                inotify)            echo "inotify-tools" ;;
                bat)                echo "bat" ;;
                screenshot)         echo "scrot" ;;
                terminator)         echo "terminator" ;;
                mpv)                echo "mpv" ;;
                *)                  echo "$generic" ;;
            esac ;;
        *)  echo "$generic" ;;
    esac
}

# pip_install <pkg> [pkg...] — installs python packages, skips already-present ones
pip_install() {
    local missing=()
    for pkg in "$@"; do
        local import_name="${pkg//-/_}"
        import_name="${import_name%%[>=<!]*}"
        # Special import name mappings
        case "$pkg" in
            pdfminer.six)   import_name="pdfminer" ;;
            python-docx)    import_name="docx" ;;
            faster-whisper) import_name="faster_whisper" ;;
            Pillow|pillow)  import_name="PIL" ;;
        esac
        python3 -c "import ${import_name}" 2>/dev/null || missing+=("$pkg")
    done
    if [[ ${#missing[@]} -gt 0 ]]; then
        _info "pip installing: ${missing[*]}"
        pip3 install --break-system-packages "${missing[@]}" 2>/dev/null || \
        pip3 install "${missing[@]}" 2>/dev/null || \
        _warn "Some pip packages failed to install — Electra will still work for core features."
    else
        _ok "Python packages already present."
    fi
}

# download_bin <label> <url> <dest>
download_bin() {
    local label="$1" url="$2" dest="$3"
    echo -e "\n${CYAN}${BOLD}  ▸ Downloading ${label}…${RESET}"
    if command -v wget &>/dev/null; then
        wget -q --show-progress --progress=bar:force:noscroll \
             --tries=3 --waitretry=2 \
             -O "${dest}" "${url}" \
          || _err "Failed to download ${label}"
    else
        curl -fL --retry 3 --retry-delay 2 \
             --progress-bar \
             -o "${dest}" "${url}" \
          || _err "Failed to download ${label}"
    fi
    local size; size=$(du -h "${dest}" | cut -f1)
    _ok "${label} downloaded  (${size})"
}

# ═══════════════════════════════════════════════════════════════════════════════
_section "Step 0 — Detecting your Linux distribution"
# ═══════════════════════════════════════════════════════════════════════════════
detect_distro

# Architecture + libc sanity checks (non-fatal warnings)
ARCH=$(uname -m)
[[ "$ARCH" != "x86_64" ]] && _warn "Architecture: ${ARCH} — Electra binary targets x86_64. It may not run."
if ldd --version 2>&1 | head -1 | grep -qi musl; then
    _warn "musl libc detected. The Electra binary is built against glibc — it may not run on musl distros."
    _warn "Proceeding anyway. If it fails, try the source build."
fi

# ═══════════════════════════════════════════════════════════════════════════════
_section "Step 1 — Updating package lists"
# ═══════════════════════════════════════════════════════════════════════════════
$PKG_UPDATE || _warn "Package list update failed — continuing with cached data."

# ═══════════════════════════════════════════════════════════════════════════════
_section "Step 2 — Core runtime packages"
# ═══════════════════════════════════════════════════════════════════════════════
_info "Installing core runtime libraries…"
pkg_install \
    python3 \
    "$PIP_PKG" \
    curl \
    wget \
    git \
    ffmpeg \
    "$(pkg_name inotify)"

# python3-tk only needed on desktop — no-op on headless
$HAS_DISPLAY && pkg_install_optional "$(pkg_name python-tk)"

_ok "Core runtime ready."

# ═══════════════════════════════════════════════════════════════════════════════
_section "Step 3 — Desktop / GUI packages"
# ═══════════════════════════════════════════════════════════════════════════════
if $HAS_DISPLAY; then
    _info "Desktop detected — installing GTK3, audio, and bar dependencies…"

    # Audio (PortAudio — needed by pyaudio / voice input)
    pkg_install_optional "$(pkg_name portaudio)"

    # GTK3 runtime — required by electra_bar.bin and /gui mode
    pkg_install_optional \
        "$(pkg_name gtk3)" \
        "$(pkg_name gdk3)" \
        "$(pkg_name pango)" \
        "$(pkg_name gobject-introspection)" \
        "$(pkg_name python-gobject)" \
        "$(pkg_name python-gobject-cairo)"

    # Optional desktop tools
    _info "Installing optional desktop tools (mpv, bat, xdotool, scrot, terminator)…"
    pkg_install_optional \
        mpv \
        "$(pkg_name bat)" \
        xdotool \
        "$(pkg_name screenshot)" \
        terminator

    _ok "Desktop packages ready."
else
    _info "Headless mode — skipping GTK3, audio, and bar packages."

    # bat and tmux are useful on servers
    pkg_install_optional \
        "$(pkg_name bat)" \
        tmux \
        screen

    _ok "Server tools ready."
fi

# ═══════════════════════════════════════════════════════════════════════════════
_section "Step 4 — Python runtime dependencies"
# ═══════════════════════════════════════════════════════════════════════════════
# These are lazy imports NOT bundled in ai_terminal.bin — loaded at runtime.
#   chromadb        → MemPalace long-term memory (coder + chat)
#   qrcode          → /qr command
#   paramiko        → /ssh command
#   geocoder        → weather auto-location fallback
#   python-docx     → Word document read/write (writer mode)
#   markdown        → Markdown rendering / export
#   pdfminer.six    → read PDFs in coder/writer
#   pypdf           → PDF page manipulation
#   requests        → HTTP (most features)
#   feedparser      → /rss agent
#   rich            → terminal formatting
#   termcolor       → terminal colours
#   prompt_toolkit  → terminal input / history

_info "Installing core Python packages…"
pip_install \
    chromadb \
    qrcode \
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

# Voice input — only useful on desktop with a microphone
if $HAS_DISPLAY; then
    _info "Installing voice input packages (faster-whisper, pyaudio)…"
    pip_install \
        faster-whisper \
        pyaudio
else
    _skip "Voice input packages (headless — no microphone)"
fi

_ok "Python packages ready."

# ═══════════════════════════════════════════════════════════════════════════════
_section "Step 5 — Ollama (local AI model runner)"
# ═══════════════════════════════════════════════════════════════════════════════
# Ollama lets Electra run AI models completely offline (/offline mode).
# Non-fatal — Electra works with cloud models without it.
if command -v ollama &>/dev/null; then
    _ok "Ollama already installed — skipping."
else
    _info "Installing Ollama (enables offline AI models)…"
    if curl -fsSL https://ollama.com/install.sh | sh; then
        _ok "Ollama installed successfully."
        _grey "Pull a model later with:  ollama pull gemma3:4b"
    else
        _warn "Ollama installation failed — Electra still works with cloud models."
        _warn "Install manually later:   curl -fsSL https://ollama.com/install.sh | sh"
    fi
fi

# ═══════════════════════════════════════════════════════════════════════════════
_section "Step 6 — Downloading Electra AI Center binaries"
# ═══════════════════════════════════════════════════════════════════════════════
_info "Creating install directory: ${INSTALL_DIR}"
mkdir -p "${INSTALL_DIR}"

# Always download the terminal binary
download_bin "Electra AI Terminal" "${GITHUB_BASE}/ai_terminal.bin" "${BIN_TERMINAL}"

# Only download the bar on desktop installs
if $HAS_DISPLAY; then
    download_bin "Electra Bar" "${GITHUB_BASE}/electra_bar.bin" "${BIN_BAR}"
else
    _skip "Electra Bar (headless install — bar requires a desktop display)"
fi

# Download the AI Center icon (used for desktop shortcut and app menu entry)
AI_ICON_PATH="${INSTALL_DIR}/ai-icon.png"
AI_ICON_URL="https://makululinux.us/ai-icon.png"
_info "Downloading AI Center icon…"
if command -v wget &>/dev/null; then
    wget -q --tries=3 --waitretry=2 -O "${AI_ICON_PATH}" "${AI_ICON_URL}" 2>/dev/null \
        && _ok "Icon saved: ${AI_ICON_PATH}" \
        || { _warn "Icon download failed — using system fallback."; AI_ICON_PATH="utilities-terminal"; }
else
    curl -fsSL --retry 3 --retry-delay 2 -o "${AI_ICON_PATH}" "${AI_ICON_URL}" 2>/dev/null \
        && _ok "Icon saved: ${AI_ICON_PATH}" \
        || { _warn "Icon download failed — using system fallback."; AI_ICON_PATH="utilities-terminal"; }
fi
[[ -f "${AI_ICON_PATH}" ]] && chmod 644 "${AI_ICON_PATH}"

# ═══════════════════════════════════════════════════════════════════════════════
_section "Step 7 — Setting permissions"
# ═══════════════════════════════════════════════════════════════════════════════
chmod 755 "${INSTALL_DIR}"
chmod 755 "${BIN_TERMINAL}"
$HAS_DISPLAY && [[ -f "${BIN_BAR}" ]] && chmod 755 "${BIN_BAR}"

# Convenience symlink — lets users just type 'electra' from any shell
if [[ ! -L /usr/local/bin/electra ]]; then
    ln -sf "${BIN_TERMINAL}" /usr/local/bin/electra
    _ok "Symlink created: electra → ${BIN_TERMINAL}"
else
    _ok "Symlink already exists: /usr/local/bin/electra"
fi
_ok "Permissions set."

# ═══════════════════════════════════════════════════════════════════════════════
_section "Step 8 — Shell alias"
# ═══════════════════════════════════════════════════════════════════════════════
# Add 'electra' alias to the user's shell rc file as a fallback to the symlink
SHELL_RC="${REAL_HOME}/.bashrc"
[[ -f "${REAL_HOME}/.zshrc" ]]                         && SHELL_RC="${REAL_HOME}/.zshrc"
[[ -f "${REAL_HOME}/.config/fish/config.fish" ]]       && SHELL_RC="${REAL_HOME}/.config/fish/config.fish"

ALIAS_LINE="alias electra='${BIN_TERMINAL}'"
if ! grep -q "alias electra=" "${SHELL_RC}" 2>/dev/null; then
    { echo ""; echo "# Electra AI Center"; echo "${ALIAS_LINE}"; } >> "${SHELL_RC}"
    chown "${REAL_USER}:${REAL_USER}" "${SHELL_RC}" 2>/dev/null || true
    _ok "Alias added to ${SHELL_RC}"
else
    _ok "Alias already present in ${SHELL_RC}"
fi

# ═══════════════════════════════════════════════════════════════════════════════
_section "Step 9 — Desktop shortcuts (AI Center launcher)"
# ═══════════════════════════════════════════════════════════════════════════════
# Creates:
#   • /usr/share/applications/electra-ai-center.desktop  (app menu — all users)
#   • ~/Desktop/electra-ai-center.desktop                (desktop icon)
# Both open ai_terminal.bin in a terminal window.
# The system menu entry is owned by root; the desktop copy by the real user.

if $HAS_DISPLAY; then
    _info "Creating AI Center desktop shortcuts…"

    # Pick the best available terminal emulator for Terminal=true launch.
    # We need one that supports -e <cmd> so the binary stays in the foreground.
    pick_terminal() {
        # Prefer DE-native terminal, then common fallbacks
        case "$DESKTOP_ENV" in
            kde)      for t in konsole xterm; do command -v "$t" &>/dev/null && echo "$t" && return; done ;;
            cinnamon) for t in gnome-terminal xterm; do command -v "$t" &>/dev/null && echo "$t" && return; done ;;
            xfce)     for t in xfce4-terminal xterm; do command -v "$t" &>/dev/null && echo "$t" && return; done ;;
            mate)     for t in mate-terminal xterm; do command -v "$t" &>/dev/null && echo "$t" && return; done ;;
            lxqt)     for t in qterminal xterm; do command -v "$t" &>/dev/null && echo "$t" && return; done ;;
            lxde)     for t in lxterminal xterm; do command -v "$t" &>/dev/null && echo "$t" && return; done ;;
        esac
        # Generic fallback chain
        for t in gnome-terminal konsole xfce4-terminal mate-terminal lxterminal qterminal \
                 xterm uxterm rxvt-unicode rxvt tilix alacritty kitty terminator; do
            command -v "$t" &>/dev/null && echo "$t" && return
        done
        echo "xterm"  # last resort — almost always present
    }

    TERM_BIN="$(pick_terminal)"

    # Build the Exec lines — each terminal has its own flag to run a command
    case "$TERM_BIN" in
        gnome-terminal)
            EXEC_LINE="gnome-terminal -- ${BIN_TERMINAL}"
            EXEC_LINE_CODER="gnome-terminal -- ${BIN_TERMINAL} --gui"
            ;;
        konsole)
            EXEC_LINE="konsole -e ${BIN_TERMINAL}"
            EXEC_LINE_CODER="konsole -e ${BIN_TERMINAL} --gui"
            ;;
        xfce4-terminal)
            EXEC_LINE="xfce4-terminal -e ${BIN_TERMINAL}"
            EXEC_LINE_CODER="xfce4-terminal -e ${BIN_TERMINAL} --gui"
            ;;
        mate-terminal)
            EXEC_LINE="mate-terminal -e ${BIN_TERMINAL}"
            EXEC_LINE_CODER="mate-terminal -e ${BIN_TERMINAL} --gui"
            ;;
        lxterminal)
            EXEC_LINE="lxterminal -e ${BIN_TERMINAL}"
            EXEC_LINE_CODER="lxterminal -e ${BIN_TERMINAL} --gui"
            ;;
        qterminal)
            EXEC_LINE="qterminal -e ${BIN_TERMINAL}"
            EXEC_LINE_CODER="qterminal -e ${BIN_TERMINAL} --gui"
            ;;
        tilix)
            EXEC_LINE="tilix -e ${BIN_TERMINAL}"
            EXEC_LINE_CODER="tilix -e ${BIN_TERMINAL} --gui"
            ;;
        alacritty)
            EXEC_LINE="alacritty -e ${BIN_TERMINAL}"
            EXEC_LINE_CODER="alacritty -e ${BIN_TERMINAL} --gui"
            ;;
        kitty)
            EXEC_LINE="kitty ${BIN_TERMINAL}"
            EXEC_LINE_CODER="kitty ${BIN_TERMINAL} --gui"
            ;;
        terminator)
            EXEC_LINE="terminator -e ${BIN_TERMINAL}"
            EXEC_LINE_CODER="terminator -e ${BIN_TERMINAL} --gui"
            ;;
        *)
            EXEC_LINE="${TERM_BIN} -e ${BIN_TERMINAL}"
            EXEC_LINE_CODER="${TERM_BIN} -e ${BIN_TERMINAL} --gui"
            ;;
    esac

    # Icon: use the downloaded Electra icon, fall back to system icon name
    ICON="${AI_ICON_PATH}"

    DESKTOP_CONTENT="[Desktop Entry]
Version=1.0
Type=Application
Name=AI Center
GenericName=AI Terminal
Comment=Electra AI Center — Chat, Code, Write, Command
Exec=${EXEC_LINE}
Icon=${ICON}
Terminal=false
StartupNotify=true
Categories=Utility;Development;ArtificialIntelligence;
Keywords=AI;Electra;Chat;Code;Terminal;MakuluLinux;"

    CODER_DESKTOP_CONTENT="[Desktop Entry]
Version=1.0
Type=Application
Name=Ai Coder
GenericName=AI Terminal GUI
Comment=Electra AI Coder — Graphical Interface
Exec=${EXEC_LINE_CODER}
Icon=${ICON}
Terminal=false
StartupNotify=true
Categories=Utility;Development;ArtificialIntelligence;
Keywords=AI;Electra;Chat;Code;Terminal;MakuluLinux;"

    # ── System-wide app menu entries (owned by root) ──────────────────────────
    MENU_DIR="/usr/share/applications"
    MENU_FILE="${MENU_DIR}/electra-ai-center.desktop"
    CODER_MENU_FILE="${MENU_DIR}/electra-ai-coder.desktop"
    mkdir -p "${MENU_DIR}"
    echo "${DESKTOP_CONTENT}" > "${MENU_FILE}"
    chmod 644 "${MENU_FILE}"
    echo "${CODER_DESKTOP_CONTENT}" > "${CODER_MENU_FILE}"
    chmod 644 "${CODER_MENU_FILE}"
    _ok "App menu entries created: ${MENU_FILE} and ${CODER_MENU_FILE}"

    # ── Per-user desktop icons ────────────────────────────────────────────────
    DESKTOP_DIR="${REAL_HOME}/Desktop"
    DESK_FILE="${DESKTOP_DIR}/electra-ai-center.desktop"
    CODER_DESK_FILE="${DESKTOP_DIR}/electra-ai-coder.desktop"
    if [[ -d "${DESKTOP_DIR}" ]]; then
        echo "${DESKTOP_CONTENT}" > "${DESK_FILE}"
        chmod 755 "${DESK_FILE}"
        chown "${REAL_USER}:${REAL_USER}" "${DESK_FILE}"
        
        echo "${CODER_DESKTOP_CONTENT}" > "${CODER_DESK_FILE}"
        chmod 755 "${CODER_DESK_FILE}"
        chown "${REAL_USER}:${REAL_USER}" "${CODER_DESK_FILE}"
        
        # Mark as trusted so Cinnamon/GNOME/XFCE don't show "untrusted" warning
        sudo -u "${REAL_USER}" gio set "${DESK_FILE}" metadata::trusted true 2>/dev/null || true
        sudo -u "${REAL_USER}" gio set "${CODER_DESK_FILE}" metadata::trusted true 2>/dev/null || true
        # KDE marks trust differently
        if [[ "$DESKTOP_ENV" == "kde" ]]; then
            # KDE reads the X-KDE-Protocols field and checks executable bit
            # chmod 755 already done above — nothing else needed for KDE trust
            :
        fi
        _ok "Desktop icons  : ${DESK_FILE} and ${CODER_DESK_FILE}  (terminal: ${TERM_BIN})"
    else
        _warn "~/Desktop not found — skipping desktop icon (menu entries still created)"
    fi

    # Refresh app menu cache if update-desktop-database is available
    command -v update-desktop-database &>/dev/null && \
        update-desktop-database "${MENU_DIR}" 2>/dev/null || true
else
    _skip "Desktop shortcuts (headless — no display)"
fi

# ═══════════════════════════════════════════════════════════════════════════════
_section "Step 10 — Autostart: Electra Bar"
# ═══════════════════════════════════════════════════════════════════════════════
# Strategy by DE:
#   GNOME / Cinnamon / XFCE / MATE / Budgie / Pantheon / unknown:
#     → ~/.config/autostart/electra-bar.desktop   (XDG standard — works everywhere)
#   KDE Plasma:
#     → ~/.config/autostart/electra-bar.desktop   (KDE also honours XDG autostart)
#     → ~/.config/autostart-scripts/electra-bar.sh (legacy KDE4 path, belt-and-braces)
#     → qdbus org.kde.kded5 autostart (runtime registration if session is live)
#   LXDE / LXQt:
#     → ~/.config/autostart/electra-bar.desktop   (XDG) + lxsession entry

if $HAS_DISPLAY && [[ -f "${BIN_BAR}" ]]; then
    _info "Installing Electra Bar autostart for ${REAL_USER} (DE: ${DESKTOP_ENV})…"

    REAL_UID="$(id -u "${REAL_USER}")"

    # ── XDG autostart entry — works on ALL DEs ────────────────────────────────
    mkdir -p "${AUTOSTART_DIR}"
    cat > "${AUTOSTART_FILE}" << DESKTOP
[Desktop Entry]
Version=1.0
Type=Application
Name=Electra Bar
GenericName=AI Input Bar
Comment=Electra AI Center floating input bar
Exec=${BIN_BAR}
Icon=utilities-terminal
Terminal=false
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
X-GNOME-Autostart-Delay=5
X-KDE-autostart-after=panel
X-KDE-StartupNotify=false
StartupNotify=false
DESKTOP
    chown "${REAL_USER}:${REAL_USER}" "${AUTOSTART_FILE}"
    _ok "XDG autostart  : ${AUTOSTART_FILE}"

    # ── KDE-specific: belt-and-braces script autostart ────────────────────────
    if [[ "$DESKTOP_ENV" == "kde" ]]; then
        KDE_AUTOSTART_SCRIPTS="${REAL_HOME}/.config/autostart-scripts"
        KDE_BAR_SCRIPT="${KDE_AUTOSTART_SCRIPTS}/electra-bar.sh"
        mkdir -p "${KDE_AUTOSTART_SCRIPTS}"
        cat > "${KDE_BAR_SCRIPT}" << 'KDESCRIPT'
#!/bin/bash
# Electra Bar — KDE autostart script
sleep 5
exec /usr/share/MakuluSetup/tools/electra_bar.bin
KDESCRIPT
        # Patch in the real bin path (heredoc above uses literal string for safety)
        sed -i "s|/usr/share/MakuluSetup/tools/electra_bar.bin|${BIN_BAR}|g" "${KDE_BAR_SCRIPT}"
        chmod +x "${KDE_BAR_SCRIPT}"
        chown "${REAL_USER}:${REAL_USER}" "${KDE_BAR_SCRIPT}"
        _ok "KDE script     : ${KDE_BAR_SCRIPT}"
    fi

    # ── LXDE: also register with lxsession if present ────────────────────────
    if [[ "$DESKTOP_ENV" == "lxde" ]]; then
        LXSESSION_AUTOSTART="${REAL_HOME}/.config/lxsession/LXDE/autostart"
        mkdir -p "$(dirname "${LXSESSION_AUTOSTART}")"
        if ! grep -q "electra_bar" "${LXSESSION_AUTOSTART}" 2>/dev/null; then
            echo "@${BIN_BAR}" >> "${LXSESSION_AUTOSTART}"
            chown "${REAL_USER}:${REAL_USER}" "${LXSESSION_AUTOSTART}"
            _ok "LXDE autostart : ${LXSESSION_AUTOSTART}"
        fi
    fi

    _ok "Electra Bar will start automatically on next login."
else
    _skip "Autostart (headless or bar not installed)"
fi

# ═══════════════════════════════════════════════════════════════════════════════
_section "Step 11 — Launching Electra Bar now"
# ═══════════════════════════════════════════════════════════════════════════════
if $HAS_DISPLAY && [[ -f "${BIN_BAR}" ]]; then
    _info "Starting Electra Bar for ${REAL_USER}…"
    REAL_UID="$(id -u "${REAL_USER}")"
    sudo -u "${REAL_USER}" \
        DISPLAY="${DISPLAY:-:0}" \
        DBUS_SESSION_BUS_ADDRESS="${DBUS_SESSION_BUS_ADDRESS:-unix:path=/run/user/${REAL_UID}/bus}" \
        XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR:-/run/user/${REAL_UID}}" \
        nohup "${BIN_BAR}" >/dev/null 2>&1 &
    _ok "Electra Bar launched."
else
    _skip "Electra Bar launch (headless install)"
fi

# ═══════════════════════════════════════════════════════════════════════════════
#  DONE
# ═══════════════════════════════════════════════════════════════════════════════
echo ""
echo -e "${GREEN}${BOLD}  ════════════════════════════════════════════════════════${RESET}"
echo -e "${GREEN}${BOLD}  ✔  Electra AI Center installed successfully!${RESET}"
echo -e "${GREEN}${BOLD}  ════════════════════════════════════════════════════════${RESET}"
echo ""
echo -e "  ${BOLD}Start the AI terminal:${RESET}"
echo -e "  ${CYAN}    electra${RESET}                   (after re-login or:  source ~/.bashrc)"
echo -e "  ${CYAN}    ${BIN_TERMINAL}${RESET}"
echo ""

if $HAS_DISPLAY; then
    echo -e "  ${BOLD}Electra Bar:${RESET}"
    echo -e "  ${GREY}    Starts automatically on every login.${RESET}"
    echo -e "  ${GREY}    Or launch now:  ${BIN_BAR}${RESET}"
    echo ""
    echo -e "  ${BOLD}AI Center shortcut:${RESET}"
    echo -e "  ${GREY}    App menu → 'AI Center'  or  double-click the desktop icon.${RESET}"
    echo ""
    echo -e "  ${BOLD}Modes:${RESET}"
    echo -e "  ${GREY}    /chat      AI conversation${RESET}"
    echo -e "  ${GREY}    /coder     autonomous coding agent${RESET}"
    echo -e "  ${GREY}    /writer    content and document generation${RESET}"
    echo -e "  ${GREY}    /novel     full multi-chapter book generation${RESET}"
    echo -e "  ${GREY}    /command   natural-language system commands${RESET}"
    echo -e "  ${GREY}    /gui       full desktop IDE (GTK)${RESET}"
else
    echo -e "  ${BOLD}Modes available (headless):${RESET}"
    echo -e "  ${GREY}    /chat      /coder    /writer    /novel    /command${RESET}"
    echo ""
    echo -e "  ${GREY}  Not available without a display: electra_bar · /gui · voice input${RESET}"
fi

echo ""
echo -e "  ${GREY}Optional extras (install anytime):${RESET}"
echo -e "  ${GREY}    pip3 install playwright && playwright install chromium   # Finance bot${RESET}"
echo -e "  ${GREY}    ollama pull gemma3:4b                                    # Offline AI model${RESET}"
echo ""
