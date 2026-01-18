<!--
---
title: "RimWorld Save File Extractor"
description: "Schema-driven extraction tools for RimWorld save files"
author: "VintageDon"
date: "2026-01-18"
version: "2.2"
status: "Active"
tags:
  - type: directory-readme
  - domain: tooling
  - tech: python
  - tech: lxml
---
-->

# RimWorld Save File Extractor

Tools for extracting game state from RimWorld `.rws` save files.

---

## 1. Contents

```
extractor/
├── rimworld_extractor_v2.py    # Main extractor (v2.2, recommended)
├── schema_discovery.py         # XML structure analysis tool
├── rimworld_extractor.py       # Legacy v1 (reference only)
├── parsers/                    # Legacy modular parsers (reference only)
└── README.md                   # This file
```

---

## 2. Tools

### `rimworld_extractor_v2.py` — Extract Colony Data (Recommended)

Schema-driven extractor using paths discovered from actual save file analysis. Uses DOM parsing for full tree access.

```powershell
# Basic usage - outputs JSON and Markdown
python rimworld_extractor_v2.py <save_file.rws>

# Custom output directory
python rimworld_extractor_v2.py <save_file.rws> -o ../../state/snapshots/the-fringe-benefit/

# JSON only (for downstream processing)
python rimworld_extractor_v2.py <save_file.rws> --json-only

# Markdown only (for human review)
python rimworld_extractor_v2.py <save_file.rws> --md-only
```

**Extracts (18+ categories):**

| Category | Description |
|----------|-------------|
| Meta | Game version, mod list (270+ supported) |
| Game Time | Year, quadrum, day, hour, ticks |
| Storyteller | Active storyteller and difficulty |
| Weather | Current and previous weather |
| Colony Stats | Adaptation days, raid count, population history |
| Factions | All factions with relations and goodwill |
| Colonists | Full profiles (skills, traits, health, needs, story) |
| Animals | Colony animals with training status |
| Resources | All stockpiled items |
| Buildings | Categorized (production, defense, power, storage, etc.) |
| Zones | Growing zones, stockpiles with settings |
| Research | Current project and completed list |
| Quests | Active/completed with status derivation |
| World Objects | Settlements, Real Ruins, sites |
| Work Tab | Complex Jobs priorities (0-9 scale) |
| Power Network | Batteries, generators, fuel levels |
| Play Log | Social interactions |
| Battle Log | Combat events |
| Tales | Colony events for narrative |
| Map Grid | Building/pawn positions |

### `schema_discovery.py` — Discover XML Structure

Analyzes a save file and outputs a hierarchical schema showing all XML paths with occurrence counts. Use this to understand what data is available or debug extraction issues.

```powershell
# Basic usage - outputs schema next to save file
python schema_discovery.py <save_file.rws>

# Limit depth for quick overview
python schema_discovery.py <save_file.rws> -d 6

# Custom output location
python schema_discovery.py <save_file.rws> -o schema.md
```

### `rimworld_extractor.py` — Legacy Extractor

Original streaming extractor using iterparse. Kept for reference but **v2 is recommended**.

---

## 3. Output Format

### JSON Structure

```json
{
  "meta": { "game_version": "1.6.4633", "mod_count": 270, "mods": [...] },
  "game_time": { "year": 5501, "quadrum": "Aprimay", "day": 5, "hour": 12 },
  "storyteller": "Ariadne Archduchess",
  "difficulty": "Custom",
  "colony_stats": { "greatest_population": 7, "num_raids_enemy": 3 },
  "factions": [...],
  "colonists": [...],
  "animals": [...],
  "buildings": { "by_category": {...}, "total_count": 1002 },
  "zones": [...],
  "resources": {...},
  "research": { "current_project": "...", "completed": [...] },
  "quests": [...],
  "world": { "settlements": [...], "ruins": [...], "sites": [...] },
  "work_tab": { "pawns": {...} },
  "power": { "batteries": [...], "generators": [...] },
  "play_log": [...],
  "battle_log": [...],
  "tales": [...],
  "map_grid": {...}
}
```

### Markdown Report

Human-readable summary organized by decision-relevance:
- Colony overview (quick status)
- Active quests with deadlines
- Faction relations
- Colonist profiles
- Resource inventory
- Recent events

---

## 4. Requirements

```powershell
pip install lxml
```

- Python 3.10+
- lxml (DOM parsing)

---

## 5. Schema Discovery Results

From analysis of `the-fringe-benefit#§#Autosave-129.rws` (18MB, 270 mods):

| Metric | Value |
|--------|-------|
| Total XML Elements | 418,374 |
| Unique Tag Paths | 4,854 |
| Maximum Depth | 17 |

Key paths discovered:
- Factions: `savegame/game/world/factionManager/allFactions/li`
- Map pawns: `savegame/game/maps/li/things/thing` (Class="Pawn")
- Buildings: `savegame/game/maps/li/things/thing` (Class starts with "Building")
- Quests: `savegame/game/questManager/quests/li`
- World objects: `savegame/game/world/worldObjects/worldObjects/li`
- Work Tab: `savegame/game/components/li/Priorities`

---

## 6. Related

| Document | Relationship |
|----------|--------------|
| [tools/](../README.md) | Parent directory |
| [state/snapshots/](../../state/snapshots/README.md) | Output destination |
| [game-saves/](../../game-saves/README.md) | Source save files |
| [parsers/](parsers/README.md) | Legacy modular parsers |
