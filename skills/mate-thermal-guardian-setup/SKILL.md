---
name: mate-thermal-guardian-setup
description: Automatically creates and installs a background service to monitor CPU temperature and adjust frequency governors dynamically.
triggers: ["setup thermal guardian", "cpu temperature management", "auto throttle cpu", "monitor thermal load"]
---

# Thermal Guardian Setup

## Overview
This skill implements a lightweight background daemon that monitors the CPU package temperature using `lm-sensors`. It automatically switches the CPU governor between `powersave` and `schedutil` based on thermal thresholds to prevent overheating while maintaining performance.

## Proven Procedure

1.  **Install dependencies** (if not present):
    ```bash
    sudo apt update && sudo apt install -y lm-sensors linux-cpupower
    sudo sensors-detect # Follow prompts to detect sensors
    ```

2.  **Deploy the thermal monitor script**:
    ```bash
    cat << 'EOF' | sudo tee /usr/local/bin/thermal_guardian.sh
    #!/bin/bash
    while true; do
        # Extract temp; assumes typical 'Package id 0' sensor output
        TEMP=$(sensors | grep -i 'Package id 0' | awk '{print $4}' | cut -c2-3)
        
        # Fallback if sensor read fails
        [[ -z "$TEMP" ]] && TEMP=50 

        if [ "$TEMP" -gt 85 ]; then
            sudo cpupower frequency-set -g powersave
            logger "Thermal Guardian: High Temp (${TEMP}°C). Switched to powersave."
        elif [ "$TEMP" -lt 60 ]; then
            sudo cpupower frequency-set -g schedutil
        fi
        sleep 10
    done
    EOF
    sudo chmod +x /usr/local/bin/thermal_guardian.sh
    ```

3.  **Create Systemd Service**:
    ```bash
    cat << 'EOF' | sudo tee /etc/systemd/system/thermal-guardian.service
    [Unit]
    Description=Thermal Guardian CPU Manager
    After=network.target

    [Service]
    ExecStart=/usr/local/bin/thermal_guardian.sh
    Restart=always
    User=root

    [Install]
    WantedBy=multi-user.target
    EOF
    ```

4.  **Enable and Start**:
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl enable --now thermal-guardian.service
    ```

## Pitfalls & Troubleshooting
*   **Sensor Name:** The command `grep 'Package id 0'` may need adjustment depending on your CPU architecture (e.g., `Core 0`, `Tdie`). Run `sensors` manually to verify your label.
*   **Permissions:** Always ensure `cpupower` is run as root or via a user with `sudo` privileges.
*   **Service Loops:** If the service fails, check logs using `journalctl -u thermal-guardian.service`.
