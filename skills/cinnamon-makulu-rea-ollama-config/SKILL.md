---
name: cinnamon-makulu-rea-ollama-config
description: Configure Makulu REA AI assistant to use a local Ollama model instead of the remote server.
triggers: ["makulu rea local ollama", "configure rea gui_settings.json", "change rea model ollama"]
---

# Makulu REA Local Ollama Configuration

## Overview
Makulu REA (Rapid Engineering Assistant) defaults to a remote server (`https://makululinux.us:2007`). This skill provides the procedure to configure REA to connect to a local Ollama instance running on `http://localhost:11434`.

## Proven Procedure
1. Locate the REA configuration file at:
   `/home/tommy/.config/rea/gui_settings.json` (or the equivalent user's home config directory).
2. Edit or write the JSON configuration to update `server_base` and `model`:
   ```json
   {
     "server_base": "http://localhost:11434",
     "api_key": "ollama",
     "model": "qwen3.8-coder",
     "temperature": 0.3
   }
   ```
3. Restart the REA application to apply changes.

## Pitfalls & Troubleshooting
- Ensure Ollama is running locally via `systemctl start ollama` or `ollama serve`.
- Ensure the model specified in `model` is actually downloaded locally via `ollama list`.
