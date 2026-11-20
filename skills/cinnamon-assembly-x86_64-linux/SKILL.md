---
name: cinnamon-assembly-x86_64-linux
description: Provides a standard template and compilation workflow for x86_64 assembly programs on Linux using NASM and ld.
triggers: ["write assembly program", "x86_64 assembly hello world", "nasm assembly linux", "assembly system call linux"]
---

# x86_64 Assembly Hello World & Compilation for Linux

## Overview
This skill provides a reusable template, system call register mapping, and compilation/linking commands for writing raw x86_64 assembly programs on Linux without standard C library (`libc`) dependencies.

## Proven Procedure

1. **Create the source file (`hello.asm`)**:
```assembly
section .data
    hello db "Hello, World!", 0x0a      ; message with a newline
    hello_len equ $ - hello             ; calculate length automatically

section .text
    global _start

_start:
    ; 1. Write system call (sys_write)
    mov rax, 1          ; system call 1 is write
    mov rdi, 1          ; file descriptor 1 is stdout
    mov rsi, hello      ; pointer to string
    mov rdx, hello_len  ; length of string
    syscall             ; trigger kernel

    ; 2. Exit system call (sys_exit)
    mov rax, 60         ; system call 60 is exit
    xor rdi, rdi        ; exit code 0
    syscall             ; trigger kernel
```

2. **Assemble, Link, and Execute**:
```bash
# Install NASM if not present
sudo apt-get update && sudo apt-get install -y nasm

# Assemble to 64-bit ELF object file
nasm -f elf64 hello.asm -o hello.o

# Link the object file into an executable
ld hello.o -o hello

# Run the binary
./hello
```

## Pitfalls & Troubleshooting
- **Missing exit syscall**: Forgetting `sys_exit` (rax=60) will cause the program to continue executing arbitrary memory after the text section, resulting in a `Segmentation fault`.
- **
