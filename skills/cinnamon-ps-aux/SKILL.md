---
name: cinnamon-ps-aux
description: Display running processes on Cinnamon desktop environment using ps aux command
triggers: ["ps aux", "list processes", "system monitoring"]
---

# Display Running Processes (ps aux)

## Overview
Shows all running processes on the system with detailed information including user, CPU usage, memory usage, and command. This is a standard Linux system monitoring command that works on Cinnamon desktop environments.

## Proven Procedure
Run the command directly in the terminal:
```bash
ps aux
```

Or to filter and show only relevant processes:
```bash
ps aux | grep -i [process_name]
```

## Pitfalls & Troubleshooting
- The output can be very large; use `less` or `head` to paginate: `ps aux | less`
- To find a specific process, use grep with the process name
- On Cinnamon systems, you can also use the system monitor applet for a graphical interface
- The `aux` flags mean: `a` = show all processes (except session leaders), `u` = show user-oriented format, `x` = show processes without controlling terminal
