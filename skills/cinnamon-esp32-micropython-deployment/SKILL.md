---
name: cinnamon-esp32-micropython-deployment
description: Procedures for flashing MicroPython firmware and deploying robust, non-blocking scripts with I2C and Wi-Fi reconnection logic to ESP32 devices.
triggers: ["esp32", "micropython", "esp32-s3", "firmware flash", "ampy", "rshell", "esp32 wifi reconnection"]
---

# ESP32 MicroPython Firmware Deployment & Robustness

## Overview
This skill covers flashing MicroPython firmware to ESP32 / ESP32-S3 microcontrollers and deploying robust Python scripts featuring non-blocking execution loops, fault-tolerant I2C sensor reading, and automated Wi-Fi reconnection handling.

## Proven Procedure
1. **Flash MicroPython Firmware**:
   ```bash
   esptool.py --chip esp32s3 --port /dev/ttyACM0 erase_flash
   esptool.py --chip esp32s3 --port /dev/ttyACM0 --baud 460800 write_flash -z 0x0 firmware.bin
   ```
2. **Structure Non-Blocking Main Script (`main.py`)**:
   - Use `time.ticks_ms()` and `time.ticks_diff()` for non-blocking timing intervals instead of `time.sleep()`.
   - Wrap I2C sensor calls in `try...except OSError` blocks to gracefully handle disconnections without crashing the main loop.
   - Implement periodic Wi-Fi status checks and non-blocking reconnection routines.

## Pitfalls & Troubleshooting
- **Serial Permission Errors**: Ensure user is in the `dialout` or `plugdev` group (`sudo usermod -aG dialout $USER`).
- **Blocking Delays**: Avoid long `time.sleep()` calls in the main application loop, as they prevent timely Wi-Fi keep-alive handling and event processing.
