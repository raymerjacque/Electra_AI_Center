---
name: cups-network-printer-setup
description: Configure and add a network printer in CUPS via command line using lpadmin and LPD/IPP protocol with a PPD file.
triggers: ["add network printer", "cups lpadmin printer setup", "configure printer via ip", "printer lpd uri"]
---

# CUPS Network Printer Setup

## Overview
This skill provides the procedure for setting up a network printer (such as a Brother laser printer) directly through the CUPS command-line interface using `lpadmin`, an IP address, and an appropriate PPD driver file.

## Proven Procedure
1. Ensure the printer driver and PPD file are installed on the system.
2. Register the printer in CUPS using `lpadmin`:
   ```bash
   sudo lpadmin -p "<Printer_Name>" -E -v lpd://<IP_Address>/binary_p1 -m "<driver.ppd>"
   ```
   *Example:*
   ```bash
   sudo lpadmin -p "Brother_DCP-7055W" -E -v lpd://192.168.178.29/binary_p1 -m "brother_dcp7055w_printer_en.ppd"
   ```
3. Enable and accept jobs for the printer if necessary:
   ```bash
   sudo cupsenable <Printer_Name>
   sudo cupsaccept <Printer_Name>
   ```

## Pitfalls & Troubleshooting
- **PPD Not Found:** If `lpadmin` fails with an error that the PPD file cannot be found, specify the absolute path to the PPD file or use the CUPS web interface at `http://localhost:631/admin`.
- **Incorrect URI Scheme:** Depending on the printer model, the URI queue (e.g., `/binary_p1`, `/queue`, or raw socket `socket://IP:9100`) may vary. Check manufacturer specifications if `lpd` fails to transmit jobs.
