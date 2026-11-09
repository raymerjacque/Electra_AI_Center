---
name: cinnamon-android-broken-screen-scrcpy
description: Access and control Android devices with broken displays, touchscreens, or lock screens on Linux using scrcpy and ADB.
triggers: ["android broken screen linux", "scrcpy broken display", "access locked android via pc", "adb control phone without screen"]
---

# Android Broken Screen Access via Scrcpy & ADB on Linux

## Overview
When an Android device has a broken display, non-functional touch screen, or is locked without screen visibility, Linux users can regain full control, mirror the screen, and extract data using **scrcpy** combined with **ADB (Android Debug Bridge)** and physical adapters (OTG).

## Proven Procedure

1. **Install ADB and Scrcpy**:
   ```bash
   sudo apt update
   sudo apt install adb scrcpy
   ```

2. **Connect the Device via USB**:
   Ensure USB debugging is enabled (if previously configured). If USB debugging is *not* enabled and the screen is completely dead, a USB OTG hub is required to connect a physical mouse and keyboard directly to the phone.

3. **Verify Connection**:
   ```bash
   adb devices
   ```

4. **Launch Scrcpy to Mirror and Control**:
   ```bash
   scrcpy
   ```
   * Useful flags for broken screens:
     * Turn off device screen while mirroring: `scrcpy --turn-screen-off`
     * Stay awake: `scrcpy --stay-awake`
     * Limit resolution if laggy: `scrcpy -m 1024`

## Pitfalls & Troubleshooting
* **Unauthorized Device**: If `adb devices` shows `unauthorized`, you must accept the RSA prompt on the phone screen. If the screen is dead, use an OTG mouse to click "Allow" blindly or use a USB-to-HDMI / capture card adapter if the phone supports video output (DisplayPort over USB-C).
* **USB Debugging Disabled**: Standard ADB commands will fail with `device unauthorized` or no device listed if USB debugging was never enabled in Developer Options.
