---
name: cinnamon-jarvis-automation-framework
description: A template and methodology for creating Python-based desktop automation scripts and unit tests for Linux system integration.
triggers: ["create python automation script", "setup jarvis helper", "python automation framework", "test python automation code"]
---

# Jarvis Automation Framework

## Overview
This skill provides a foundational structure for building Python-based desktop automation ("Jarvis" style helpers). It leverages a modular approach for the core script and a `unittest` suite to ensure robustness before deploying logic that interacts with system commands. Use this when starting new automation projects on Linux to ensure consistent structure and testing.

## Proven Procedure

### 1. Initialize the Script (`jarvis_helper.py`)
Create a robust, extensible Python script that handles system interactions via the `subprocess` module.

```python
import subprocess
import logging

logging.basicConfig(level=logging.INFO)

class JarvisHelper:
    def execute_command(self, cmd):
        try:
            result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            logging.error(f"Command failed: {e.stderr}")
            return None

# Add project specific methods here
```

### 2. Implement Unit Tests (`test_jarvis.py`)
Always pair your helper with a test suite to verify commands without executing them directly on the system.

```python
import unittest
from jarvis_helper import JarvisHelper

class TestJarvisHelper(unittest.TestCase):
    def setUp(self):
        self.jarvis = JarvisHelper()

    def test_command_execution(self):
        # Example test
        output = self.jarvis.execute_command("echo hello")
        self.assertEqual(output, "hello")

if __name__ == '__main__':
    unittest.main()
```

### 3. Execution
Run your tests before running your main helper:
```bash
python3 -m unittest test_jarvis.py
```

## Pitfalls & Troubleshooting
*   **Shell Injection:** Never pass raw user input directly to `shell=True` in `subprocess.run()`. Always sanitize input.
*   **Pathing:** Use absolute paths for commands (e.g., `/usr/bin/python3`) if the script is intended to run via `cron` or systemd services.
*   **Permissions:** If your script interacts with system files or services, ensure the user executing the script has the necessary permissions (or `sudo` rights specifically configured for that command in `/etc/sudoers`).
