---
name: cinnamon-custom-desktop-launcher
description: Creates a standard .desktop file for custom applications or Python scripts to be used as desktop shortcuts in Cinnamon.
triggers: ["create a desktop shortcut for python script", "create .desktop file", "make script executable from desktop", "add application to cinnamon menu"]
---

# Cinnamon Custom Desktop Launcher

## Overview
This skill generates a valid `.desktop` file in the current directory, which can be moved to `~/Desktop` or `~/.local/share/applications` to launch custom scripts or applications. It specifically ensures the `Exec` line contains the full path to the executable, which is critical for desktop launchers to work correctly.

## Proven Procedure
To create a launcher for a custom script (e.g., `script.py`):

1.  Identify the absolute path to your script (use `pwd`).
2.  Create a file named `app_name.desktop` with the following template:

```bash
cat <<EOF > app_name.desktop
[Desktop Entry]
Type=Application
Name=Your App Name
Exec=python3 /path/to/your/script.py
Icon=applications-other
Terminal=false
Categories=Utility;
Comment=Description of your app
EOF
```

3.  Make the file executable (required for Cinnamon/Nemo to treat it as a launcher):
    ```bash
    chmod +x app_name.desktop
    ```

4.  (Optional) Move it to the desktop:
    ```bash
    mv app_name.desktop ~/Desktop/
    ```

## Pitfalls & Troubleshooting
*   **Permissions:** If the launcher icon looks like a text file, run `chmod +x` on the file. Cinnamon will not execute untrusted `.desktop` files.
*   **Pathing:** Always use the full absolute path in the `Exec` line. Relative paths often fail because the desktop environment launches the file with the user's home directory as the working directory, not the folder where the script resides.
*   **Icons:** If you want a custom icon, change `Icon=applications-other` to the absolute path of a `.png` or `.svg` file (e.g., `Icon=/home/user/images/logo.png`).
