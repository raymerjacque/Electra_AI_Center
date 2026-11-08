---
name: ai-os-offline-config
description: Configures Electra/Makulu AI to operate in offline mode using local GGUF/Ollama model backends.
triggers: ["activate offline ai", "set up local llm", "enable local offline mode for electra", "configure offline model backend"]
---

# AI/OS Offline Model Configuration

## Overview
This skill provides the necessary procedure to switch the Electra AI interface from cloud-based API endpoints to a local, offline backend. This is useful for privacy-focused workflows, air-gapped environments, or simply avoiding API usage limits.

## Proven Procedure

1. **Modify Configuration:**
   Edit the local configuration file located at `~/.config/makulu/ai/config.json`.
   Locate the `backend` or `endpoint` parameter and ensure it points to your local runner (e.g., `http://localhost:11434` for Ollama).

2. **Set Environment Variables:**
   For a persistent offline state, append the following to your `~/.bashrc` or `~/.zshrc`:
   ```bash
   export MAKULU_OFFLINE_MODE=true
   export ELECTRA_LOCAL_WEIGHTS="/path/to/your/local/models/"
   ```
   *Note: Ensure the directory specified in `ELECTRA_LOCAL_WEIGHTS` contains your valid model files (e.g., .gguf).*

3. **Restart Service:**
   Apply the changes by restarting the AI service daemon:
   ```bash
   systemctl --user restart makulu-ai-service
   ```

## Pitfalls & Troubleshooting
* **Missing Models:** If the AI refuses to start in offline mode, verify that the `ELECTRA_LOCAL_WEIGHTS` directory actually contains valid model weight files and that the system has read permissions.
* **Socket Errors:** If the backend is set to `localhost:11434` (Ollama), ensure the Ollama service is running (`systemctl status ollama`) before attempting to connect the frontend.
* **Permissions:** If the `config.json` file is immutable or owned by root, use `sudo` to edit, but ensure your user owns the resulting file to prevent service startup failures.
