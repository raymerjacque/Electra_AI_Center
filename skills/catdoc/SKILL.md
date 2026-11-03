---
name: catdoc
description: Skill for catdoc
---

# catdoc Skill

This skill provides functionality for `catdoc`, a utility that converts Microsoft Word files to plain text.

**Overview:**
- `catdoc` converts Microsoft Word (.doc, .docx) files to plain text format
- Useful for reading Word documents in environments without Microsoft Word
- Part of the `catdoc` package on Debian/Ubuntu systems
- Also converts Excel and PowerPoint files

**Commands:**
- `catdoc <file>` - Convert Word file to plain text
- `catdoc -o <output> <file>` - Specify output file
- `catdoc --version` - Show version information

**Usage examples:**
- Convert Word to text: `catdoc document.doc > document.txt`
- Convert with options: `catdoc -o output.txt file.doc`
- Batch convert: `for f in *.doc; do catdoc "$f" > "${f%.doc}.txt"; done`

**Package purpose:**
- Provides command-line conversion of Microsoft Office documents to plain text
- Useful for scripting and processing Office files on Linux systems
