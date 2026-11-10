---
name: ollama-troubleshooting
description: Troubleshooting steps to verify service status, port availability, and network binding for the local Ollama AI model.
triggers: ["ollama not working", "cannot connect to local ollama", "ollama service status", "ollama bind address"]
---

# Ollama Troubleshooting & Configuration

## Overview
This skill provides a systematic approach to debugging common Ollama connectivity issues, specifically when the local LLM server fails to respond or needs to be accessible across different network interfaces (e.g., for frontend applications or Docker containers).

## Proven Procedure
To diagnose and resolve local Ollama connectivity issues:

1.  **Check Service Status**: Ensure the Ollama service is running.
    ```bash
    systemctl status ollama
    ```
    If stopped, start and enable it:
    ```bash
    sudo systemctl enable --now ollama
    ```

2.  **Verify Port Listening**: Confirm Ollama is listening on the default port `11434`.
    ```bash
    ss -tuln | grep 11434
    ```

3.  **Configure Network Binding**: By default, Ollama binds to `127.0.0.1` (loopback). If you need to access it from other services (Docker, network apps), you must set the `OLLAMA_HOST` environment variable to `0.0.0.0`.
    *   **Temporary Session**: `export OLLAMA_HOST=0.0.0.0`
    *   **Persistent Configuration**: Edit the systemd service file:
        ```bash
        sudo systemctl edit ollama.service
        ```
        Add the following lines:
        ```ini
        [Service]
        Environment="OLLAMA_HOST=0.0.0.0"
        ```
        Then reload and restart:
        ```bash
        sudo systemctl daemon-reload
        sudo systemctl restart ollama
        ```

## Pitfalls & Troubleshooting
*   **Permissions**: Ensure your user is in the correct group if you are managing the service files.
*   **Firewall**: If using `ufw`, ensure port `11434` is allowed if you change the host binding to `0.0.0.0`.
*   **Conflicting Services**: If `ss -tuln` shows something else on 11434, another service may be squatting on the port.
