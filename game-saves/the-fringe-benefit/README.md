<!--
---
title: "The Fringe Benefit Colony"
description: "Primary test colony for RimWorld AI Colony Co-Play development"
author: "VintageDon"
date: "2026-01-18"
version: "1.0"
status: "Active"
tags:
  - type: directory-readme
  - domain: game-data
  - colony: the-fringe-benefit
---
-->

# The Fringe Benefit Colony

Primary test colony for RimWorld AI Colony Co-Play development. This is a heavily modded colony used to validate extraction capabilities.

---

## 1. Colony Overview

| Attribute | Value |
|-----------|-------|
| Colony Name | The Fringe Benefit |
| Storyteller | Ariadne Archduchess (VFE) |
| Difficulty | Custom |
| Game Time | Year 5501, Aprimay |
| Colonists | 7 |
| Mods | 270 active |

---

## 2. Contents

```
the-fringe-benefit/
├── the-fringe-benefit#§#Autosave-*.rws   # Rolling autosaves (18 slots)
├── BadEvent/                              # Event-triggered saves (negative)
│   └── *.rws
├── GoodEvent/                             # Event-triggered saves (positive)
│   └── *.rws
└── README.md                              # This file
```

---

## 3. Save Configuration

| Setting | Value |
|---------|-------|
| Autosave Slots | 18 |
| Autosave Interval | ~2 minutes |
| Event Saves | Enabled (BadEvent/GoodEvent) |

---

## 4. Mod Highlights

Key mods affecting save file structure:
- Vanilla Expanded Framework
- VFE Deserters
- Work Tab (Complex Jobs enabled)
- Real Ruins
- Progress Renderer

---

## 5. Usage

```powershell
# Extract latest autosave
python tools/extractor/rimworld_extractor_v2.py "game-saves/the-fringe-benefit/the-fringe-benefit#§#Autosave-129.rws" -o state/snapshots/the-fringe-benefit/

# List available saves
Get-ChildItem "game-saves/the-fringe-benefit/*.rws" | Select-Object Name, Length, LastWriteTime
```

---

## 6. Related

| Document | Relationship |
|----------|--------------|
| [game-saves/](../README.md) | Parent directory |
| [state/snapshots/the-fringe-benefit/](../../state/snapshots/the-fringe-benefit/README.md) | Extraction output |
