<!--
---
title: "Tools"
description: "Python tooling for RimWorld save file processing"
author: "VintageDon"
date: "2026-01-18"
version: "1.1"
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
├── extractor/              # Save file parser
│   ├── rimworld_extractor_v2.py   # Main extractor (v2.2)
│   ├── schema_discovery.py        # XML structure analysis
│   ├── rimworld_extractor.py      # Legacy v1 (reference)
│   ├── parsers/                   # Legacy modular parsers
│   └── README.md
├── watcher/                # File watcher daemon (planned)
│   └── README.md
└── README.md               # This file
```

---

## 2. Subdirectories

| Directory | Description | Status |
|-----------|-------------|--------|
| [extractor/](extractor/README.md) | Parses .rws save files into JSON/Markdown | ✅ Complete |
| [watcher/](watcher/README.md) | Monitors saves folder, triggers extraction | ⬜ Planned |

---

## 3. Usage

```powershell
# Discover XML schema structure
python tools/extractor/schema_discovery.py "<save_file>.rws"

# Run extraction (JSON + Markdown)
python tools/extractor/rimworld_extractor_v2.py "<save_file>.rws" -o state/snapshots/

# JSON only (for downstream processing)
python tools/extractor/rimworld_extractor_v2.py "<save_file>.rws" --json-only

# Future: Start file watcher
python tools/watcher/watch.py --saves-dir "path/to/saves"
```

---

## 4. Related

| Document | Relationship |
|----------|--------------|
| [Repository Root](../README.md) | Parent directory |
| [state/](../state/README.md) | Output destination for extracted data |
| [game-saves/](../game-saves/README.md) | Source save files |
