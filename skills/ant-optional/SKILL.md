---
name: ant-optional
description: Skill for ant-optional (optional Ant tasks)
---

# ant-optional Skill

This skill provides functionality for `ant-optional`, which contains optional tasks for the Apache Ant build tool that require additional Java libraries.

**Overview:**
- `ant-optional` provides optional Ant tasks that depend on external Java libraries
- These tasks are not included in the core Ant distribution due to licensing or size considerations
- Part of the `ant-optional` package on Debian/Ubuntu systems
- Tasks include those for JUnit testing, CVS, SVN, and other optional functionality

**Commands:**
- `ant -listtasks` - List available Ant tasks
- Tasks are automatically available when the corresponding library is installed
- Common optional tasks: `junit`, `cvschangelog`, `s3`, `ssh`

**Usage:**
- JUnit testing: `ant -Dtest=MyTest test`
- Requires corresponding Java libraries to be installed
- Tasks are loaded dynamically by Ant based on available classpath

**Dependencies:**
- `ant-optional` package itself
- Additional Java libraries for specific tasks (e.g., junit4 for junit task)
