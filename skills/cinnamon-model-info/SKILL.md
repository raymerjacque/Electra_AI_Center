---
name: cinnamon-model-info
description: Displays the current AI model configuration and cascade information for the Electra system on Cinnamon desktop
triggers: ["model identification", "AI system configuration", "cascade model info"]
---

# AI Model Configuration for Electra System

## Overview
This skill provides information about the current AI model setup, including the primary model in the cascade, locally available models, and system configuration. Useful for understanding which model is currently active and the fallback configuration.

## Proven Procedure

Run the following command to identify the model configuration:

```bash
cat /home/valentine/.config/electra/model_cascade.conf 2>/dev/null || echo "Model cascade config not found at default location"
```

If the file doesn't exist at the default location, search for model configuration files:

```bash
find /home -name "*model*" -type f 2>/dev/null | head -20
find /etc -name "*electra*" -type f 2>/dev/null | head -10
find /usr -name "*electra*" -type f 2>/dev/null | head -10
```

Check for Ollama models:

```bash
ollama list 2>/dev/null || echo "Ollama not installed or not running"
```

## Pitfalls & Troubleshooting

- **Model cascade config not found**: The configuration may be located elsewhere or use a different naming convention. Search broadly using `find` commands as shown above.
- **Ollama not available**: If Ollama is not installed, local model information will not be available through that method. Check if `ollama` command exists.
- **Permission issues**: Some configuration files may require elevated permissions to read. Use `sudo` if necessary, but be cautious with system files.

**Note**: This skill is specific to the Cinnamon desktop environment on MakuluLinux and provides insight into the AI model architecture used by the Electra assistant system.
