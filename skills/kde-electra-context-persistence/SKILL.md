---
name: kde-electra-context-persistence
description: Automates the persistent injection of user preference profiles into Electra AI sessions to avoid re-explaining context.
triggers: ["electra context persistence", "save electra preferences", "configure electra startup profile", "load persistent AI context"]
---

# Electra AI Context Persistence

## Overview
This skill implements a "Context Injection" mechanism for the Electra AI interface. It creates a centralized profile file (`~/.electra_profile.txt`) that stores user preferences, project constraints, and persona settings. By automatically prepending this content to the initial prompt, users can save daily conversation limits by avoiding redundant explanations.

## Proven Procedure
1.  **Create the Profile File:**
    Create a hidden text file in your home directory to hold your preferences.
    ```bash
    touch ~/.electra_profile.txt
    ```

2.  **Edit the Profile:**
    Open this file in a text editor (e.g., KWrite or Kate) and list your preferences, coding style, or system requirements clearly.
    ```bash
    kate ~/.electra_profile.txt
    ```
    *Example content:*
    > I am Elcis. I prefer concise explanations, terminal-first workflows, and I primarily work on AI-Center projects. Never use long pleasantries.

3.  **Implement Injection Workflow:**
    To utilize this, whenever starting a new task, use the following prompt pattern to "bootstrap" the AI session:
    > "Read my profile at ~/.electra_profile.txt and adopt these settings for this session: [Paste relevant context or confirm you have read the file]."

4.  **Optional Automation (Bash Alias):**
    You can add an alias to your `.bashrc` or `.zshrc` to cat the file to your clipboard, making it easier to paste into the terminal prompt.
    ```bash
    echo "alias get-electra-profile='cat ~/.electra_profile.txt | xclip -selection clipboard'" >> ~/.bashrc
    source ~/.bashrc
    ```

## Pitfalls & Troubleshooting
*   **File Permissions:** Ensure the file is readable by your user (standard home directory permissions apply).
*   **Token Limits:** While this saves *human* effort, remember that pasting a massive context file consumes tokens on the AI side. Keep the `~/.electra_profile.txt` file concise—focus on critical constraints rather than narrative history.
*   **Updates:** Remember to update `~/.electra_profile.txt` whenever your project scope changes, as the AI will rely on the stale file if it isn't updated.
