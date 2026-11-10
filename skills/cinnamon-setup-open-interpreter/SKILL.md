---
name: cinnamon-setup-open-interpreter
description: Configures the Open Interpreter agent environment to allow an LLM to control the local system, file manager, and terminal operations directly.
triggers: ["setup personal AI agent", "install open interpreter", "how to make an AI control my pc", "set up coding assistant on cinnamon"]
---

# Cinnamon Setup: Open Interpreter Agent

## Overview
This skill facilitates the installation and environment preparation for "Open Interpreter," a tool that allows a Large Language Model to run code locally on your machine, perform web searches, and manipulate files. Because this agent operates at the system level, it requires specific Python environment isolation to prevent dependency conflicts with the Cinnamon system packages.

## Proven Procedure
1.  **Install Python requirements:** Open your terminal and ensure you have Python 3 and `pip` installed.
    ```bash
    sudo apt update
    sudo apt install python3-pip python3-venv
    ```

2.  **Create a dedicated directory and virtual environment:** It is crucial *not* to install this globally to avoid breaking Cinnamon/System components.
    ```bash
    mkdir ~/ai-agent && cd ~/ai-agent
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Open Interpreter:**
    ```bash
    pip install open-interpreter
    ```

4.  **Running the Agent:**
    To launch the agent, simply run the command:
    ```bash
    interpreter
    ```

5.  **Integration (Optional):** If you want to access this easily, create a `nemo` (File Manager) custom action or a desktop shortcut that runs:
    `gnome-terminal -- bash -c "cd ~/ai-agent && source venv/bin/activate && interpreter; exec bash"`

## Pitfalls & Troubleshooting
*   **System Permissions:** Open Interpreter will ask for permission before running code. **Always read the code it proposes** before saying "Yes." It has full access to delete files or run `sudo` commands if you allow it.
*   **Environment Conflicts:** If you get `apt` or `pip` errors, ensure you are *always* inside the `venv` (virtual environment) created in step 2. Never run `pip install open-interpreter` with `sudo`.
*   **Missing Dependencies:** If the agent fails to perform specific tasks (like image editing or web scraping), it may need system-level headers. Install common ones via `sudo apt install build-essential python3-dev`.
