---
name: ai-os-config-management
description: Manages the standardized YAML configuration file used to categorize and track system software, tools, and development environments.
triggers: ["organize system software", "update ai-os-config.yaml", "add new category to system config", "configure system inventory"]
---

# AI-OS Configuration Management

## Overview
This skill provides the structure and maintenance procedure for the `/home/guy/ai-os-config.yaml` file. This central registry allows the AI to inventory installed software categories, track development environment dependencies, and map CLI tools, ensuring consistent system state management.

## Proven Procedure
To update or view the system configuration structure, adhere to the following schema stored in `/home/guy/ai-os-config.yaml`:

1.  **Structure:** Use the following YAML template for all system organization:
    ```yaml
    system_config:
      cli_tools:
        - name: <name>
          package_manager: <apt|pip|npm|etc>
          description: <purpose>
      development_environments:
        - name: <lang_or_framework>
          version: <v>
          path: <dir>
      system_utilities:
        - name: <util_name>
          config_path: <path_to_conf>
    ```

2.  **Implementation:**
    *   When installing new tools, always append to the relevant category in this file.
    *   Use `yq` (if available) or standard text editors for batch updates.
    *   To verify the integrity of the file, run a syntax check: `python3 -c "import yaml, sys; yaml.safe_load(sys.stdin)" < /home/guy/ai-os-config.yaml`.

## Pitfalls & Troubleshooting
*   **YAML Syntax:** YAML is indentation-sensitive. Always use 2 spaces (never tabs).
*   **Validation:** If the AI fails to parse the file, it is likely due to an unescaped special character in the `description` or `path` fields. Always wrap values containing colons or slashes in quotes.
*   **Sync:** This file is the "source of truth." Do not manually modify installed software without updating this file, or the AI's internal state model will drift.
