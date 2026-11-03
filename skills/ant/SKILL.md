---
name: ant
description: Skill for ant Java build tool
---

# ant Skill

This skill provides functionality for the `ant` (Another NeTwork) build tool, which is a Java-based build tool similar to Make but more flexible and cross-platform.

**Overview:**
- Apache Ant is a Java library and command-line tool for building software projects
- Uses XML-based build files (build.xml) to define compilation, testing, and deployment tasks
- Part of the `ant` package on Debian/Ubuntu systems
- Requires Java (JDK/JRE) to run

**Commands:**
- `ant` - Run build using default build.xml
- `ant -buildfile <file.xml>` - Use a specific build file
- `ant -projecthelp` - Show project help targets
- `ant -version` - Show Ant version
- `ant -p` - Same as -projecthelp

**Build file structure:**
- `<project>` - Root element
- `<target>` - Group of tasks
- `<task>` - Individual operation (compile, jar, clean, etc.)
- Common targets: `clean`, `compile`, `jar`, `run`, `test`

**Usage examples:**
- Basic build: `ant`
- With specific build file: `ant -buildfile build.xml`
- Clean and compile: `ant clean compile`
