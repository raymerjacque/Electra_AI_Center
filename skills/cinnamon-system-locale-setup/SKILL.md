---
name: cinnamon-system-locale-setup
description: Configures system-wide locale settings and generates language locales for the Cinnamon desktop environment.
triggers: ["change language to german", "set system locale", "configure locale", "set system language", "locale generation"]
---

# Cinnamon System Locale Configuration

## Overview
This skill handles the process of changing the system-wide locale (language, region settings) on MakuluLinux running the Cinnamon desktop environment. It ensures the necessary locale definitions are generated and that the system configuration is updated to apply these changes.

## Proven Procedure
To change the system language (e.g., to German), follow these steps:

1.  **Check Available Locales:**
    Verify if the desired locale is supported by the system:
    ```bash
    localectl list-locales | grep de_DE
    ```

2.  **Generate the Locale (If missing):**
    Edit the locale generation file:
    ```bash
    sudo nano /etc/locale.gen
    ```
    Uncomment the line: `de_DE.UTF-8 UTF-8`
    
    Then generate:
    ```bash
    sudo locale-gen
    ```

3.  **Set System-Wide Locale:**
    Apply the locale setting:
    ```bash
    sudo localectl set-locale LANG=de_DE.UTF-8
    ```

4.  **Refresh:**
    Log out of the Cinnamon desktop session and log back in for the changes to take effect across the GUI.

## Pitfalls & Troubleshooting
*   **Partial Translation:** Simply changing the locale does not always translate every installed application. You may need to install language packs specific to your desktop environment (e.g., `language-pack-de` or `cinnamon-l10n`).
*   **Terminal vs. GUI:** `localectl` affects the system-wide environment variables. If some apps remain in English, ensure your user profile `~/.bashrc` or `~/.profile` does not have conflicting `LANG` overrides.
*   **Session Persistence:** You *must* re-login to the desktop environment. Changes will not apply to already-running processes immediately.
