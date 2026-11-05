---
name: nemo-documents-maxs-menu-rework-inspection
description: Inspects the maxs-menu-rework project in the Documents directory to understand its structure, admin interface capabilities, and deployment status. Useful for determining where features like slideshow uploads are located and what administrative controls exist.
triggers: ["inspect maxs-menu-rework", "check maxs-menu-rework files", "maxs-menu-rework directory structure"]
---

# maxs-menu-rework Project Inspection

## Overview
Investigated the `maxs-menu-rework` project located in the user's Documents directory to catalog its structure, admin interface features, and current deployment status. This skill determines where specific features (such as slideshow uploads) are located and what administrative controls are available.

## Proven Procedure
1. Navigate to the project directory:
   ```bash
   cd ~/Documents/maxs-menu-rework
   ```
2. List all files and directories to understand the project structure:
   ```bash
   ls -la
   ```
3. Read key configuration and source files to understand the admin interface and feature set. In this session, the following was confirmed:
   - The admin area (`/admin`) includes: Edit Menus (screen selector, save/publish, import menu JSON, add items/headers), History, My Account, and admin-only sections: Schedule, Theme, System, Users.
   - The slideshow upload feature is **not** integrated into the admin navigation. It exists on a separate page at `http://<pi-ip>:8080/slideshow-upload/screen<N>` (screen 1–10).
   - The slideshow upload page supports JPG, PNG, GIF, and SVG uploads (maximum 20 images, 5MB each) with configurable interval, shuffle, and repeat settings.
   - The feature is not linked from the admin navigation and would require modifying `base.html` and adding an admin route to integrate it.

4. Check for active services and environment configuration:
   ```bash
   ls -la .menu.env  # confirms MENU_PORT=8080 is set
   ls -la venv/      # virtual environment exists but systemd service is not active
   ```

## Pitfalls & Troubleshooting
- The slideshow upload is **not** accessible from the admin menu; it must be reached via direct URL.
- If the system is not running, start the development environment with `source venv/bin/activate` and ensure the service is configured to run on port 8080.
- No systemd service is currently active; manual startup may be required for testing.
- Integrating the slideshow upload into the admin interface would require template modifications and route additions, which are beyond the scope of a simple inspection.

---

**Note:** This task was a file/structure inspection and does not require a desktop-specific prefix, as it involves examining project files in the Documents directory rather than configuring a desktop environment, theme, panel, or file manager.
