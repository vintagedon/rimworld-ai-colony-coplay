<!--
---
title: "Save File Watcher"
description: "Monitors RimWorld saves directory and triggers extraction on changes"
author: "VintageDon"
date: "2026-01-17"
version: "1.0"
status: "Planned"
tags:
  - type: directory-readme
  - domain: automation
  - tech: python
---
-->

# Save File Watcher

Monitors the RimWorld saves directory and automatically triggers extraction when autosaves occur.

**Status:** ⬜ Planned — Not yet implemented.

---

## 1. Planned Contents

```
watcher/
├── watch.py            # Main watcher daemon
├── config.py           # Configuration handling
└── README.md           # This file
```

---

## 2. Planned Usage

```powershell
# Start watcher with default settings
python watch.py

# Specify saves directory
python watch.py --saves-dir "C:\Users\...\Saves"

# Specify output directory
python watch.py --output ../../state/snapshots/

# Run as background process
pythonw watch.py --daemon
```

---

## 3. Design Notes

### Behavior

- Monitor RimWorld saves directory for .rws file changes
- Debounce rapid changes (RimWorld writes incrementally)
- Invoke extractor after file write stabilizes
- Log extraction results
- Handle errors gracefully (don't crash on bad saves)

### Configuration

```yaml
# config.yaml (planned)
saves_directory: "C:/Users/.../RimWorld/Saves"
output_directory: "../state/snapshots"
debounce_seconds: 5
extract_on_startup: true
log_level: INFO
```

### Dependencies

```
watchdog>=3.0.0  # File system monitoring
```

---

## 4. Related

| Document | Relationship |
|----------|--------------|
| [tools/](../README.md) | Parent directory |
| [extractor/](../extractor/README.md) | Invoked by watcher |
| [state/](../../state/README.md) | Output destination |
