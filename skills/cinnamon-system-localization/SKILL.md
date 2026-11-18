---
name: cinnamon-system-localization
description: Configures the system locale settings for language translation and generation on MakuluLinux Cinnamon.
triggers: ["change language to portuguese", "translate system", "pt-br locale setup", "set system language", "configure locales"]
---

# Cinnamon System Localization (PT-BR)

## Overview
This skill automates the process of generating and applying system-wide language locales, specifically for Portuguese (pt_BR), ensuring that the underlying system (Debian-based) and the Cinnamon desktop environment are properly localized.

## Proven Procedure
To translate the system environment to Portuguese (pt_BR):

1.  **Generate the Locale:**
    Ensure the Portuguese locale is enabled in the system configuration.
    ```bash
    # Enable the pt_BR locale
    sudo sed -i 's/# pt_BR.UTF-8 UTF-8/pt_BR.UTF-8 UTF-8/' /etc/locale.gen
    
    # Generate the locale files
    sudo locale-gen
    ```

2.  **Apply via Localectl:**
    Set the system-wide locale to match the newly generated one.
    ```bash
    sudo localectl set-locale LANG=pt_BR.UTF-8
    ```

3.  **Cinnamon Desktop Translation:**
    The user must also ensure the Language packs are installed. Most MakuluLinux installations handle this via the GUI, but the packages can be verified:
    ```bash
    # Install standard Portuguese language support for Cinnamon and common apps
    sudo apt update
    sudo apt install language-pack-pt-base language-pack-pt language-pack-gnome-pt
    ```

4.  **Restart Session:**
    The changes require a log out and log back in to take full effect.

## Pitfalls & Troubleshooting
*   **Partial Translation:** Sometimes applications (like browsers or specific CLI tools) will ignore the system-wide `LANG` variable if a local config file exists. If specific apps remain in English, ensure the user has set the locale correctly in their `~/.pam_environment` or `~/.bashrc`.
*   **Missing Packages:** If the menu and system settings remain in English despite `locale-gen` success, the `language-pack-gnome-pt` (which covers most Cinnamon/GTK components) is usually missing.
