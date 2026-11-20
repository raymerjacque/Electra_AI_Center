---
name: kde-grub-kernel-rollback
description: Safely revert to a previous or stable kernel via the GRUB boot menu during system startup.
triggers: ["revert kernel", "swapback kernel", "boot old kernel", "grub advanced options", "kernel instability"]
---

# KDE GRUB Kernel Rollback

## Overview
This skill provides the procedure for reverting to a stable, non-optimized kernel (e.g., reverting from a CachyOS or testing kernel back to the stock Debian kernel) via the GRUB boot menu. This is a crucial troubleshooting step when dealing with graphical corruption, driver incompatibilities, or system instability introduced by kernel updates.

## Proven Procedure
1.  **Reboot the System:** Restart your computer via the start menu or `reboot` command.
2.  **Access GRUB:** Immediately after the BIOS/UEFI logo screen, press and hold the **Shift** key (or **Esc** if Shift fails). This will trigger the GRUB boot menu.
3.  **Navigate Advanced Options:** 
    *   Use the arrow keys to select **"Advanced options for Debian GNU/Linux"** (or the specific OS flavor if named differently).
    *   Press **Enter**.
4.  **Select Kernel:** You will see a list of available kernels. Identify the kernel that does not contain the conflicting version string (e.g., avoid "cachy" if troubleshooting CachyOS kernels).
5.  **Boot:** Press **Enter** on the chosen kernel to boot the system.
6.  **Verify:** Once logged into KDE Plasma, check system stability or hardware performance.

## Pitfalls & Troubleshooting
*   **Menu Not Showing:** If the GRUB menu doesn't appear, you may need to press the key repeatedly (tapped rhythmically) immediately upon power-on.
*   **Temporary vs. Permanent:** This method is temporary. If the system boots successfully into the stable kernel, the fix is active only until the next reboot unless you modify your GRUB configuration to make this kernel the permanent default (usually via `grub-customizer` or editing `/etc/default/grub`).
*   **Kernel Removal:** Do not immediately uninstall the problematic kernel until you are certain the stable kernel resolves all issues, otherwise, you may end up without a bootable OS.
