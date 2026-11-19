---
name: kde-python-libtorrent-setup
description: Handles the installation of libtorrent Python bindings and system dependencies on Debian/Ubuntu-based systems.
triggers: ["ModuleNotFoundError: No module named 'libtorrent'", "install libtorrent python", "setup python libtorrent"]
---

# Python libtorrent Setup

## Overview
This skill resolves the common `ModuleNotFoundError: No module named 'libtorrent'` error in Python scripts. It ensures that both the underlying C++ system library (`libtorrent-rasterbar`) and the Python bindings are installed correctly, as `pip install libtorrent` often fails without the system-level C++ headers present.

## Proven Procedure
To resolve missing `libtorrent` dependencies, follow these steps in your terminal:

1.  **Update your package list and install the system-level development library:**
    ```bash
    sudo apt update
    sudo apt install -y libtorrent-rasterbar-dev python3-libtorrent
    ```

2.  **Verify or install the Python bindings via pip (if needed):**
    If the system package `python3-libtorrent` does not fully satisfy your specific environment or if you are working within a virtual environment, use:
    ```bash
    pip install libtorrent
    ```

## Pitfalls & Troubleshooting
*   **Version Mismatch:** Sometimes `pip` installs a different version than the system `libtorrent-rasterbar`. Always prioritize the system package (`sudo apt install python3-libtorrent`) first, as it is compiled to match your OS libraries.
*   **Virtual Environments:** If you are inside a `venv`, ensure you have installed the necessary build-essential packages (`sudo apt install build-essential`) before running `pip install libtorrent`, as it may attempt to compile C++ extensions locally.
