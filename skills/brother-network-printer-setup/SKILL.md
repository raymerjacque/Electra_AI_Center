---
name: brother-network-printer-setup
description: Installs and configures network printers, specifically older Brother models like the DCP-7055W, using official Brother driver installation scripts and CUPS.
triggers: ["netzwerk drucker einrichten", "brother dcp-7055w", "brother printer linux", "cups printer setup"]
---

# Brother Network Printer Setup

## Overview
This skill outlines the process for installing and configuring a network printer (specifically Brother models like the DCP-7055W) on Linux using CUPS and the official Brother driver installation tool.

## Proven Procedure
1. Ensure CUPS and printing dependencies are installed:
   ```bash
   sudo apt update
   sudo apt install cups printer-driver-cups-pdf
   ```
2. Download and extract the official Brother driver installer script:
   ```bash
   cd ~/Downloads
   wget https://download.brother.com/welcome/dlf004939/linux-brpt-installer--2.2.1-1.tar.gz
   tar -zxvf linux-brpt-installer--2.2.1-1.tar.gz
   ```
3. Run the installer with root privileges, specifying the printer model name:
   ```bash
   sudo bash linux-brpt-installer-2.2.1 DCP-7055W
   ```
4. Follow the on-screen prompts provided by the Brother script to select network connection type (LPD/IPP/AppSocket) and provide the printer's IP address.

## Pitfalls & Troubleshooting
- Ensure the printer has a static IP address or DHCP reservation so the network path doesn't change.
- Make sure the CUPS service is running (`sudo systemctl enable --now cups`) before starting the installation script.
