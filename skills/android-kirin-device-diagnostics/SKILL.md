---
name: android-kirin-device-diagnostics
description: A Python-based workflow for automating connectivity and diagnostics for Huawei/Kirin chipset Android devices using ADB and Fastboot protocols.
triggers: ["kirin device connection", "huawei fastboot diagnostics", "python kirin automation", "extract hw-chipset info"]
---

# Android Kirin Device Diagnostics

## Overview
This skill provides a standardized Python framework for interacting with Huawei/Kirin chipset devices. It automates the verification of ADB connections and facilitates the retrieval of hardware-specific Fastboot variables (such as `hw-chipset` and `hw-build-id`), which are essential for device identification and flashing workflows.

## Proven Procedure

To automate the connection and diagnostic check for Kirin devices, use the following Python logic:

1.  **Dependencies:** Ensure `adb` and `fastboot` are installed and accessible in the system PATH.
2.  **Implementation:**
    Create a management script (e.g., `kirin_manager.py`) that utilizes `subprocess` to interface with the device.

```python
import subprocess

def get_fastboot_variable(variable_name):
    """Executes fastboot getvar command and parses the output."""
    try:
        result = subprocess.run(
            ['fastboot', 'getvar', variable_name],
            capture_output=True, text=True, stderr=subprocess.STDOUT
        )
        # Fastboot outputs are often on stderr
        output = result.stderr if result.stderr else result.stdout
        for line in output.splitlines():
            if variable_name in line:
                return line.split(':', 1)[1].strip()
    except Exception as e:
        return f"Error: {e}"
    return None

def run_diagnostics():
    chipset = get_fastboot_variable('hw-chipset')
    build_id = get_fastboot_variable('hw-build-id')
    print(f"Device Chipset: {chipset}")
    print(f"Build ID: {build_id}")

if __name__ == "__main__":
    run_diagnostics()
```

## Pitfalls & Troubleshooting
*   **Permissions:** Huawei devices in Fastboot mode often require root/sudo privileges to read proprietary variables. Run your script with elevated permissions if access is denied.
*   **Protocol:** Ensure the device is in `Fastboot` mode, not `Recovery` or `Normal` boot, as `fastboot getvar` will fail otherwise.
*   **Output Stream:** Fastboot commands frequently return results via `stderr` rather than `stdout`, which can cause simple `subprocess` calls to return empty strings if not handled correctly.
