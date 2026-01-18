<!--
---
title: "Legacy Parsers"
description: "Modular parsers from v1 extractor (reference only)"
author: "VintageDon"
date: "2026-01-18"
version: "1.0"
status: "Deprecated"
tags:
  - type: directory-readme
  - domain: tooling
  - tech: python
  - status: deprecated
---
-->

# Legacy Parsers

Modular parsers from the v1 streaming extractor. **Reference only** — not used by v2.

---

## 1. Contents

```
parsers/
├── __init__.py         # Package init
├── meta.py             # Game version, mods, world info
├── factions.py         # Faction extraction
└── README.md           # This file
```

---

## 2. Status

**Deprecated.** The v2 extractor (`rimworld_extractor_v2.py`) uses a monolithic approach with all extraction logic in a single file. This simplifies maintenance and allows cross-referencing between extraction functions.

These parsers are kept for reference in case modular extraction is revisited in the future.

---

## 3. Why Deprecated

| v1 Approach | v2 Approach |
|-------------|-------------|
| Streaming (iterparse) | DOM (full tree load) |
| Modular parsers | Monolithic file |
| Memory-efficient | Random access needed |
| Complex state tracking | Simple tree navigation |

The v2 approach was chosen because:
- File sizes (~18MB) are manageable for DOM parsing
- Cross-referencing (e.g., faction ID → name) requires random access
- Single file is easier to maintain and comment

---

## 4. Related

| Document | Relationship |
|----------|--------------|
| [extractor/](../README.md) | Parent directory |
| [rimworld_extractor_v2.py](../rimworld_extractor_v2.py) | Current extractor |
