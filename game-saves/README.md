<!--
---
title: "Game Saves"
description: "RimWorld save file archive for AI-assisted colony tracking"
author: "VintageDon"
date: "2026-01-17"
version: "1.0"
status: "Active"
tags:
  - type: directory-readme
  - domain: game-data
---
-->

# Game Saves

RimWorld save file archive. Contains complete colony history for AI advisory sessions.

**Status:** Currently gitignored. Will be exposed publicly once extraction pipeline is stable.

---

## 1. Structure

```
game-saves/
├── {colony-name}/              # One folder per colony
│   ├── *#§#Autosave-*.rws      # Rolling autosaves
│   ├── *#§#BadEvent.*.rws      # Event-triggered (negative)
│   ├── *#§#GoodEvent.*.rws     # Event-triggered (positive)
│   └── *#§#*.rws               # Manual saves
└── README.md                   # This file
```

---

## 2. Current Colonies

| Colony | Description |
|--------|-------------|
| [deserters-of-the-rim/](deserters-of-the-rim/) | Primary test colony, 300+ mods |

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
| Manual | Player-initiated | `Hoeaia.rws`, `New Arrivals1.rws` |

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
python tools/extractor/rimworld_extractor.py "game-saves/deserters-of-the-rim/Deserters of the Rim#§#Autosave-1.rws"

# Extract specific event
python tools/extractor/rimworld_extractor.py "game-saves/deserters-of-the-rim/Deserters of the Rim#§#BadEvent.Raid- Blue Moon Corporation.rws"
```

### For Claude Advisory

Claude reads extracted state from `state/snapshots/`, not directly from save files. The extraction pipeline transforms XML saves into queryable JSON.

---

## 6. Gitignore Status

Currently ignored to avoid committing large binary files during development. Will be tracked once:
- Extraction pipeline is stable
- Save file sizes are validated acceptable
- Public exposure aligns with open methodology goals

---

## 7. Related

| Document | Relationship |
|----------|--------------|
| [Repository Root](../README.md) | Parent directory |
| [tools/extractor/](../tools/extractor/README.md) | Processes these saves |
| [state/](../state/README.md) | Extraction output destination |
