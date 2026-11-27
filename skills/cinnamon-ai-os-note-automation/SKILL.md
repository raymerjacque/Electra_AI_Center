---
name: cinnamon-ai-os-note-automation
description: Enables a standardized note-taking workflow where the system captures input via the "Copy this" keyword and saves it to a structured text file.
triggers: ["save note", "copy this", "automation note taking", "note system"]
---

# AI-OS Note Automation (Copy This)

## Overview
This skill provides a persistent mechanism for the AI to save arbitrary information snippets, ideas, or commands into a local `my_notes.txt` file with automatic timestamps and categories. It is designed to be triggered by the user phrase "Copy this".

## Proven Procedure
The system utilizes a Python handler script to format and append data.

1.  **Trigger Mechanism**: When the user says "Copy this", the AI parses the following text as `[Name]` and `[Content]`.
2.  **Execution**: The AI invokes the `save_note.py` script located in the workspace.
3.  **File Format**: Notes are stored in `~/my_notes.txt` using the following schema:
    ```
    [YYYY-MM-DD HH:MM:SS] [Name]
    Content: 
    [Content body]
    --------------------------------------------------
    ```

### Implementation Logic (`/home/merrill/workspace/Practice/src/save_note.py`)
This script should be kept available in the workspace path for the AI to call:
```python
import datetime
import sys

def save_note(name, content):
    filepath = "/home/merrill/workspace/Practice/my_notes.txt"
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filepath, "a") as f:
        f.write(f"[{timestamp}] [{name}]\n")
        f.write(f"Content: \n{content}\n")
        f.write("-" * 50 + "\n\n")

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        save_note(sys.argv[1], sys.argv[2])
```

## Pitfalls & Troubleshooting
*   **File Path Consistency**: If `my_notes.txt` is moved or the workspace structure changes, the script must be updated with the new absolute path.
*   **Permissions**: Ensure the AI process has write permissions to the `/home/merrill/workspace/Practice/` directory.
*   **Trigger Misidentification**: If the user accidentally uses the phrase "Copy this" in casual conversation, the system may attempt to create a note. If this happens, verify the note content and delete the unwanted entry from `my_notes.txt` manually.
