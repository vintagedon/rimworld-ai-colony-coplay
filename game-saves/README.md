<!--
---
title: "Game Saves"
description: "RimWorld save file archive for AI-assisted colony tracking"
author: "VintageDon"
date: "2026-01-18"
version: "1.1"
status: "Active"
tags:
  - type: directory-readme
  - domain: game-data
---
-->

# Game Saves

RimWorld save file archive. Contains complete colony history for AI advisory sessions.

**Status:** Public — save files are tracked for open methodology demonstration.

---

## 1. Structure

```
game-saves/
├── the-fringe-benefit/         # Current test colony
│   ├── *#§#Autosave-*.rws      # Rolling autosaves (18 slots)
│   ├── BadEvent/               # Event-triggered saves (negative)
│   ├── GoodEvent/              # Event-triggered saves (positive)
│   └── README.md
└── README.md                   # This file
```

---

## 2. Current Colonies

| Colony | Description | Status |
|--------|-------------|--------|
| [the-fringe-benefit/](the-fringe-benefit/README.md) | Primary test colony, 270 mods | ✅ Active |

---

## 3. Save Naming Convention

RimWorld (with mods) generates saves with this pattern:

```
{Colony Name}#§#{Save Type}.{Details}.rws
```

| Type | Trigger | Example |
|------|---------|---------|
| Autosave-N | Timed interval | `Autosave-1.rws` through `Autosave-18.rws` |
| BadEvent | Negative event | `BadEvent.Raid- Blue Moon Corporation.rws` |
| GoodEvent | Positive event | `GoodEvent.Cargo pods (apparel).rws` |
| Manual | Player-initiated | `Colony Name.rws` |

---

## 4. RimWorld Save Settings

Recommended settings for maximum history:

| Setting | Value | Rationale |
|---------|-------|-----------|
| Autosave interval | 1-2 minutes | Granular state tracking |
| Autosave slots | 15-20 | Extended rolling history |
| Event saves | Enabled | Capture significant moments |

---

## 5. Usage

### For Extraction

```powershell
# Extract latest autosave
python tools/extractor/rimworld_extractor_v2.py "game-saves/the-fringe-benefit/the-fringe-benefit#§#Autosave-129.rws" -o state/snapshots/the-fringe-benefit/

# Extract specific event save
python tools/extractor/rimworld_extractor_v2.py "game-saves/the-fringe-benefit/BadEvent/the-fringe-benefit#§#BadEvent.Raid.rws"
```

### For Claude Advisory

Claude reads extracted state from `state/snapshots/`, not directly from save files. The extraction pipeline transforms XML saves into queryable JSON.

---

## 6. Related

| Document | Relationship |
|----------|--------------|
| [Repository Root](../README.md) | Parent directory |
| [tools/extractor/](../tools/extractor/README.md) | Processes these saves |
| [state/](../state/README.md) | Extraction output destination |
