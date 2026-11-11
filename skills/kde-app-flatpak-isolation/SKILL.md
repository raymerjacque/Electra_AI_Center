---
name: kde-app-flatpak-isolation
description: How to install and run KDE applications (like Kdenlive) on non-KDE desktop environments without installing the full KDE Plasma desktop suite.
triggers: ["install kde apps without kde", "run kdenlive on cinnamon", "install kdenlive without plasma", "flatpak kde apps"]
---

# KDE App Flatpak Isolation

## Overview
This skill addresses the common misconception that KDE-based applications (like Kdenlive, Krita, or Okular) require the full KDE Plasma Desktop Environment to function on other environments like Cinnamon, XFCE, or GNOME. By using Flatpak, you can install these applications in a self-contained environment, avoiding the dependency bloat of the full KDE suite.

## Proven Procedure
To install KDE applications on non-KDE desktops, prioritize the Flatpak distribution method:

1.  **Search for the Flatpak package:**
    ```bash
    flatpak search <app-name>
    ```

2.  **Install the application:**
    ```bash
    flatpak install flathub <app-id> -y
    ```
    *Example for Kdenlive:*
    ```bash
    flatpak install flathub org.kde.kdenlive -y
    ```

3.  **Run the application:**
    The application will appear in your standard desktop application menu automatically, or you can launch it via terminal:
    ```bash
    flatpak run <app-id>
    ```

## Pitfalls & Troubleshooting
*   **Dependency Bloat:** Do NOT attempt `sudo apt install kdenlive` if you want to avoid installing massive amounts of KDE Plasma desktop dependencies. APT packages often pull in the full desktop environment, whereas Flatpaks bring only the necessary runtime libraries.
*   **Theming/Styling:** KDE applications running via Flatpak on non-KDE desktops might not perfectly match your system's GTK theme. They will use the default KDE "Breeze" theme by default. This is expected behavior for containerized apps and does not affect functionality.
*   **Permissions:** If a KDE app (like Kdenlive) cannot access your files, use `flatpak permission-set` or a tool like **Flatseal** (available on Flathub) to grant the application access to specific folders (e.g., `/home/user/Videos`).
