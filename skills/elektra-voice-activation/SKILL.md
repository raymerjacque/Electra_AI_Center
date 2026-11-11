---
name: elektra-voice-activation
description: Automates the startup sequence for the Elektra voice recognition system using a dedicated execution script.
triggers: ["start elektra voice", "aktivizēt elektra audio režīmu", "elektra voice mode startup"]
---

# Elektra Voice Activation Skill

## Overview
This skill manages the activation of the custom Elektra voice recognition environment. It encapsulates the execution of the `start_elektra_voice.sh` script, which handles the loading of dependencies and initialization of the listening session.

## Proven Procedure
To activate the voice mode, execute the startup script located in the project root:

1. Navigate to the project directory:
   ```bash
   cd ~/ELEKTRA_PROJEKTI/
   ```
2. Execute the startup script:
   ```bash
   ./start_elektra_voice.sh
   ```

*Note: If the script is not executable, run `chmod +x start_elektra_voice.sh` first.*

## Pitfalls & Troubleshooting
*   **Permissions:** If you receive "Permission denied," ensure the script has execution rights using `chmod +x start_elektra_voice.sh`.
*   **Environment:** Ensure your Python environment or virtual environment is correctly referenced inside the `start_elektra_voice.sh` script. If the script fails to find dependencies, verify the `PATH` variables within the script.
*   **Audio Access:** If the mic is not detected, ensure the user has appropriate permissions for audio devices (check `groups` to confirm inclusion in the `audio` group).
