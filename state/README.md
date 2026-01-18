<!--
---
title: "State"
description: "Extracted game state snapshots and historical data"
author: "VintageDon"
date: "2026-01-18"
version: "1.1"
status: "Active"
tags:
  - type: directory-readme
  - domain: data-storage
---
-->

# State

Extracted RimWorld game state. This directory contains output from the extractor.

---

## 1. Contents

```
state/
├── snapshots/                          # Point-in-time extractions
│   ├── the-fringe-benefit/             # Current test colony output
│   │   ├── colony_{timestamp}.json
│   │   └── colony_{timestamp}.md
│   └── milestone-03-extractor-phase-02/ # Milestone captures
├── history/                            # Historical analysis (planned)
│   ├── diffs/                          # Changes between snapshots
│   └── trends/                         # Aggregated trend data
└── README.md                           # This file
```

---

## 2. Subdirectories

| Directory | Description | Status |
|-----------|-------------|--------|
| [snapshots/](snapshots/README.md) | Point-in-time JSON/MD extractions | ✅ Active |
| [history/](history/README.md) | Diffs and trend analysis | ⬜ Planned |

---

## 3. Usage

### For Claude Advisory

Claude reads from this directory via FS MCP during conversations:

```
"How is Viktor doing?"
→ Claude reads state/snapshots/the-fringe-benefit/colony_*.json
→ Returns mood, health, recent events for Viktor
```

### Manual Inspection

```powershell
# View latest extraction summary
Get-Content state/snapshots/the-fringe-benefit/colony_*.md | Select-Object -First 100

# Parse JSON for specific data
Get-Content state/snapshots/the-fringe-benefit/colony_*.json | ConvertFrom-Json | Select-Object -ExpandProperty colonists
```

---

## 4. File Naming

### Snapshots

```
colony_{timestamp}.json
colony_{timestamp}.md

Example:
colony_20260118_153000.json
colony_20260118_153000.md
```

---

## 5. Gitignore Status

Snapshot contents are typically gitignored because:
- Output is regenerated from save files
- JSON files can be large (1-5MB per snapshot)
- Personal game data shouldn't be in version control

The directory structure and READMEs are tracked; contents may not be.

---

## 6. Related

| Document | Relationship |
|----------|--------------|
| [Repository Root](../README.md) | Parent directory |
| [tools/extractor/](../tools/extractor/README.md) | Produces this output |
| [game-saves/](../game-saves/README.md) | Source save files |
