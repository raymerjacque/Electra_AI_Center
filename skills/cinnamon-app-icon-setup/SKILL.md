---
name: cinnamon-app-icon-setup
description: Handles the manual registration and cache updates required to make custom application icons appear in the Cinnamon application menu.
triggers: ["add icon to application", "fix missing desktop icon", "cinnamon icon cache update", "refresh application icons"]
---

# Cinnamon Application Icon Registration

## Overview
This skill automates the registration of custom application icons (.svg or .png) within the Cinnamon desktop environment. Simply placing an icon file is often insufficient; the system's icon cache must be updated to reflect the changes in the `hicolor` theme directory for the Cinnamon menu to recognize the new file.

## Proven Procedure
To register a new icon for a desktop application:

1.  **Place the Icon:** Ensure your icon file (e.g., `appname.svg`) is located in `~/.local/share/icons/hicolor/scalable/apps/` or similar resolution-specific directories.
2.  **Verify/Create Index:** Ensure the base theme directory has an `index.theme` file.
3.  **Update Cache:** Execute the following command to force Cinnamon (and GTK-based apps) to reload the icon cache:
    ```bash
    touch ~/.local/share/icons/hicolor/index.theme
    gtk-update-icon-cache -f ~/.local/share/icons/hicolor/
    ```

## Pitfalls & Troubleshooting
*   **Permissions:** If the command fails, ensure the directory structure exists recursively.
*   **Caching:** If the icon does not appear immediately in the menu, you may need to restart the Cinnamon panel: `cinnamon --replace &` (though usually not necessary for simple icon updates).
*   **Naming:** The icon filename must match the `Icon=` field inside your `.desktop` file exactly (excluding the extension).
