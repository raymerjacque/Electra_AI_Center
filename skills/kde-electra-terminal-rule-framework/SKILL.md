---
name: kde-electra-terminal-rule-framework
description: A standardized Python framework for creating, testing, and running custom terminal commands ("Electra rules") with offline voice integration.
triggers: ["setup electra terminal rules", "create new electra rule", "initialize terminal automation framework", "configure electra offline voice command"]
---

# Electra Terminal Rule Framework

## Overview
This skill provides a standardized workflow for developing and managing custom "Electra Rules"—terminal-based automations triggered by voice or text. It includes a boilerplate `app.py` for continuous listening, transcription using `faster-whisper`, and a rule-execution engine that handles specific command sets (e.g., engineering tasks, file archiving, ROM management).

## Proven Procedure

1.  **Framework Initialization:**
    Ensure the core application structure exists in `~/workspace/`.
    ```bash
    mkdir -p ~/workspace/rules
    # Ensure app.py and test_app.py are present to manage logic and unit tests
    ```

2.  **Adding a New Rule:**
    To extend functionality, add a new rule function to the `app.py` logic engine. Example structure:
    ```python
    def rule_execute(command_name, params):
        if command_name == "new_rule":
            # Implementation here
            return "Rule executed successfully"
    ```

3.  **Dependencies:**
    The framework relies on specific audio and processing libraries. Ensure they are installed in your virtual environment:
    ```bash
    sudo apt install portaudio19-dev ffmpeg
    pip install faster-whisper sounddevice pytest
    ```

4.  **Execution:**
    Run the application to activate the command-listening loop:
    ```bash
    python3 ~/workspace/app.py
    ```

5.  **Archiving:**
    The system automatically logs interactions to `~/Desktop/ELEKTRA_SARUNAS`. Ensure this directory exists:
    ```bash
    mkdir -p ~/Desktop/ELEKTRA_SARUNAS
    ```

## Pitfalls & Troubleshooting
*   **Audio Drivers:** If voice commands are not detected, verify that `portaudio19-dev` is installed and the system recognizes your microphone (check `arecord -l`).
*   **Model Loading:** The initial startup may be slow as it loads the `faster-whisper` model into memory. This is expected.
*   **Permissions:** If the `app.py` cannot write to the archive directory, ensure the current user owns `~/Desktop/ELEKTRA_SARUNAS`.
