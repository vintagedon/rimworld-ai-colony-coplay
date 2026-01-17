<!--
---
title: "State"
description: "Extracted game state snapshots and historical data"
author: "VintageDon"
date: "2026-01-17"
version: "1.0"
status: "Active"
tags:
  - type: directory-readme
  - domain: data-storage
---
-->

# State

Extracted RimWorld game state. This directory contains output from the extractor and is **gitignored** (regenerated from saves).

---

## 1. Contents

```
state/
├── snapshots/          # Point-in-time extractions
│   ├── {timestamp}.json
│   ├── {timestamp}.md
│   └── latest.json     # Symlink/copy of most recent
├── history/            # Historical analysis (future)
│   ├── diffs/          # Changes between snapshots
│   └── trends/         # Aggregated trend data
└── README.md           # This file
```

---

## 2. Subdirectories

| Directory | Description | Status |
|-----------|-------------|--------|
| [snapshots/](snapshots/) | Point-in-time JSON/MD extractions | 🔄 Active |
| [history/](history/) | Diffs and trend analysis | ⬜ Planned |

---

## 3. Usage

### For Claude Advisory

Claude reads from this directory via FS MCP during conversations:

```
"How is Viktor doing?"
→ Claude reads state/snapshots/latest.json
→ Returns mood, health, recent events for Viktor
```

### Manual Inspection

```powershell
# View latest extraction metadata
cat state/snapshots/latest.json | jq '.metadata'

# View colonist summary
cat state/snapshots/latest.md
```

---

## 4. File Naming

### Snapshots

```
{colony_name}_{timestamp}.json
{colony_name}_{timestamp}.md

Example:
deserters-of-the-rim_2026-01-17T15-30-00.json
deserters-of-the-rim_2026-01-17T15-30-00.md
```

### Latest

`latest.json` and `latest.md` are copies of the most recent extraction for easy access.

---

## 5. Gitignore

This directory's contents are gitignored because:
- Output is regenerated from save files
- JSON files can be large (1-5MB per snapshot)
- Personal game data shouldn't be in version control

The directory structure and README are tracked; contents are not.

---

## 6. Related

| Document | Relationship |
|----------|--------------|
| [Repository Root](../README.md) | Parent directory |
| [tools/extractor/](../tools/extractor/README.md) | Produces this output |
| [game-saves/](../game-saves/) | Source save files |
