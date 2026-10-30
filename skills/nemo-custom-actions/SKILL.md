---
name: nemo-custom-actions
description: Create custom right-click context menu actions in the Nemo file manager using .nemo_action configuration files.
triggers: ["nemo custom action", "right click menu nemo", "add context menu nemo", "nemo action webp", "nemo file manager extension"]
---

# Nemo Custom Actions

## Overview
This skill provides the procedure for adding custom right-click context menu items in the Nemo file manager (used in Cinnamon and other Linux environments) using `.nemo_action` configuration files.

## Proven Procedure
1. Create a custom action file inside the user actions directory:
   `~/.local/share/nemo/actions/<action_name>.nemo_action`

2. Populate the file with the required configuration parameters. For example, converting images to WebP:
   ```ini
   [Nemo Action]
   Name=Convert to WebP
   Comment=Convert selected image to WebP
   Exec=cwebp -q 80 %F -o %F.webp
   Icon-Name=image-x-generic
   Selection=s
   Extensions=jpg;jpeg;png;
   Quote=double
   ```

3. Restart the Nemo file manager to load the new action:
   ```bash
   nemo -q
   ```

## Pitfalls & Troubleshooting
- **Selection Types:** Ensure `Selection` matches your use case (`s` for single selection, `m` for multiple, `any` for any).
- **Reloading:** Changes will not appear until Nemo is fully restarted using `nemo -q`.
