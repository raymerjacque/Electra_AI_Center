---
name: pipewire-audio-routing-fix
description: Troubleshoots and fixes audio output routing issues where sound is directed to the wrong device using PipeWire's command-line tools.
triggers: ["pipewire audio routing", "no sound output but microphone works", "wpctl set-default", "audio sink switching", "force audio output device"]
---

# PipeWire Audio Routing Fix

## Overview
This skill addresses the common issue where PipeWire routes audio output to an incorrect device (e.g., a Bluetooth headset or incorrect sink) while ignoring the primary sound card, despite `pavucontrol` showing activity. It uses `wpctl` to identify and switch the default audio sink.

## Proven Procedure

1.  **Check the current audio status:**
    Execute the following command to list all audio devices (Sinks and Sources):
    ```bash
    wpctl status
    ```

2.  **Identify the Target Device:**
    Look under the **Audio -> Sinks** section. Find your primary sound card (e.g., "Built-in Audio" or similar) and note its ID number (e.g., `45`).

3.  **Set the Default Output:**
    Force the system to use the desired device as the default output:
    ```bash
    wpctl set-default <ID_NUMBER>
    ```
    *(Replace `<ID_NUMBER>` with the ID found in step 2)*.

4.  **Verify:**
    Play a sound to confirm the routing has updated immediately.

## Pitfalls & Troubleshooting
*   **Persistent Switching:** If the device keeps switching back to a Bluetooth device, check if that device is still connected and marked as a priority. You may need to disconnect or temporarily disable Bluetooth if it keeps hijacking the audio output.
*   **Service Restart:** If `wpctl` commands are unresponsive, PipeWire might be hung. Try restarting the user-space services:
    ```bash
    systemctl --user restart pipewire pipewire-pulse wireplumber
    ```
