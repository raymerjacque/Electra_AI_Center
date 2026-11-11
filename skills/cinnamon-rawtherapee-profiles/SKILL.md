---
name: cinnamon-rawtherapee-profiles
description: Guide on where to find processing profiles (.pp3 files) for RawTherapee and how to install them in user configurations.
triggers: ["rawtherapee profiles", "install rawtherapee pp3", "raw therapy processing profiles"]
---

# RawTherapee Profiles Installation

## Overview
This skill outlines how to acquire and install custom processing profiles (`.pp3` files) for RawTherapee on Linux.

## Proven Procedure
1. **Locate User Configuration Directory**:
   RawTherapee stores user profiles and configurations in `~/.config/RawTherapee/` (or `~/.config/rawtherapee/`).
   If the `profiles` directory does not exist inside it, create it:
   ```bash
   mkdir -p ~/.config/RawTherapee/profiles
   ```

2. **Acquire Profiles**:
   - Download community `.pp3` profiles from GitHub repositories, photography forums (like Pixls.us), or official RawTherapee documentation/contrib packages.
   - System-wide profiles are typically installed at `/usr/share/rawtherapee/profiles/`.

3. **Install Profiles**:
   Copy the downloaded `.pp3` files into the user profiles directory:
   ```bash
   cp *.pp3 ~/.config/RawTherapee/profiles/
   ```

4. **Verify in RawTherapee**:
   Launch RawTherapee, open the File Browser or Editor, and access the Processing Profiles panel to apply the newly added profiles.

## Pitfalls & Troubleshooting
- **Case Sensitivity**: Directory names (`RawTherapee` vs `rawtherapee`) can be case-sensitive depending on the build and file system. Ensure you check both or match the exact folder created by the application on first run.
- **File Extension**: Ensure profiles end with the `.pp3` extension.
