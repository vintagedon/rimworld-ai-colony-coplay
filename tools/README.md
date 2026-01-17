<!--
---
title: "Tools"
description: "Python tooling for RimWorld save file processing"
author: "VintageDon"
date: "2026-01-17"
version: "1.0"
status: "Active"
tags:
  - type: directory-readme
  - domain: tooling
  - tech: python
---
-->

# Tools

Python tooling for RimWorld save file extraction and processing.

---

## 1. Contents

```
tools/
├── extractor/          # Save file parser
│   ├── parsers/        # Section-specific parsing modules
│   └── README.md
├── watcher/            # File watcher daemon (future)
│   └── README.md
└── README.md           # This file
```

---

## 2. Subdirectories

| Directory | Description | Status |
|-----------|-------------|--------|
| [extractor/](extractor/README.md) | Parses .rws save files into JSON/Markdown | 🔄 In Progress |
| [watcher/](watcher/README.md) | Monitors saves folder, triggers extraction | ⬜ Planned |

---

## 3. Usage

```powershell
# Run extraction manually
python tools/extractor/rimworld_extractor.py "<save_file>.rws" -o state/snapshots/

# Future: Start file watcher
python tools/watcher/watch.py --saves-dir "path/to/saves"
```

---

## 4. Related

| Document | Relationship |
|----------|--------------|
| [Repository Root](../README.md) | Parent directory |
| [state/](../state/README.md) | Output destination for extracted data |
| [Extractor Handoff](../docs/rimworld-extractor-handoff.md) | Development specification |
