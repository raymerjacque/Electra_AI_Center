---
name: cinnamon-rea-ollama-config
description: Configures the Makulu REA application to connect to a local Ollama instance for AI processing instead of the default remote server.
triggers: ["configure REA ollama", "connect REA to local LLM", "REA server settings", "Makulu REA local model"]
---

# REA Ollama Configuration

## Overview
This skill allows switching the Makulu REA AI assistant from its default remote server configuration to a local Ollama instance. This is useful for privacy, offline usage, or faster inference using local hardware.

## Proven Procedure
To configure REA to use a local Ollama server, modify the configuration file located in the user's home directory.

1.  Open the configuration file:
    ```bash
    nano ~/.config/rea/gui_settings.json
    ```

2.  Update the `server_base` and `model` keys within the JSON object to match your local Ollama setup:
    ```json
    {
      "server_base": "http://localhost:11434",
      "model": "llama3.1:latest"
    }
    ```
    *Note: Ensure the model name defined in the config actually exists in your local Ollama instance (verify via `ollama list`).*

3.  Restart the REA application for changes to take effect.

## Pitfalls & Troubleshooting
*   **Model Availability:** If REA fails to generate a response, ensure the model specified in `gui_settings.json` is pulled locally by running `ollama pull <model_name>` in your terminal.
*   **Permissions:** If the `gui_settings.json` file is read-only, ensure your user owns the file using `chown $USER:$USER ~/.config/rea/gui_settings.json`.
*   **Service Status:** Verify Ollama is actually running in the background before launching REA by checking `systemctl status ollama` or looking for the process.
