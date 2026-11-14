---
name: ai-local-network-exposure
description: Configures local AI services or backends to be accessible over a local network by adjusting bind interfaces and firewall rules.
triggers: ["access ai from another computer", "make local llm network accessible", "ollama expose on network", "allow lan access to ai server"]
---

# AI Local Network Exposure

## Overview
This skill provides the standard procedure for exposing a local AI backend (like Ollama or a custom Python FastAPI wrapper) to other devices on the same local network. By default, most AI services bind to `127.0.0.1` (localhost) for security; this process modifies those binds and ensures the firewall permits traffic.

## Proven Procedure

### 1. Identify the Bind Interface
Most AI services default to loopback. To expose them, you must change the binding host to `0.0.0.0` (all interfaces).

*   **For Ollama:**
    Set the environment variable before starting the service:
    ```bash
    export OLLAMA_HOST=0.0.0.0
    ollama serve
    ```
    *Note: To make this permanent, edit your systemd service file via `sudo systemctl edit ollama.service` and add `Environment="OLLAMA_HOST=0.0.0.0"`.*

*   **For Python/FastAPI:**
    In your server launch script or Python code, ensure the `run` command looks like this:
    ```python
    uvicorn.run(app, host="0.0.0.0", port=8000)
    ```

### 2. Configure Firewall (UFW)
Ensure your firewall allows incoming traffic on the specific port you are using (e.g., 11434 for Ollama).

```bash
# Example for Ollama
sudo ufw allow 11434/tcp
# Reload to apply changes
sudo ufw reload
```

## Pitfalls & Troubleshooting
*   **Security Warning:** Exposing services on `0.0.0.0` makes them accessible to *anyone* on your local network. Do not do this on public or untrusted Wi-Fi.
*   **Double-check IP:** On your client machine, access the service via the host machine's local IP address (e.g., `http://192.168.1.5:11434`), not `localhost`.
*   **Firewall Conflicts:** If you are using a GUI-based firewall (like `gufw`), ensure the rule is toggled "Allow" and the profile is active.
