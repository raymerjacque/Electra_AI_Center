---
name: acl
description: Skill for acl (Access Control Lists) utility
---

# acl Skill

This skill provides functionality for managing Access Control Lists (ACLs) on Linux systems using the `setfacl` and `getfacl` commands.

**Overview:**
- ACLs allow fine-grained permission control beyond the standard owner/group/other permission model
- Part of the util-linux package on most Linux distributions

**Commands:**
- `setfacl -m u:username:rwx <file>` - Add ACL entry for user
- `setfacl -x u:username <file>` - Remove ACL entry for user
- `getfacl <file>` - Show ACL entries for a file
- `chmod <file>` - Standard permission changes (base model)

**Usage examples:**
- Set user read-write: `setfacl -m u:john:rw file.txt`
- Get current ACLs: `getfacl file.txt`
- Remove all ACLs: `setfacl -b file.txt` (clear base and named entries)
