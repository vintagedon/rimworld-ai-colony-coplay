<!--
---
title: "M02b: Extractor Phase 2 — Schema-Driven v2"
description: "Schema discovery, DOM parsing, full extraction suite"
author: "VintageDon"
date: "2026-01-18"
version: "1.0"
status: "Complete"
tags:
  - type: worklog
  - domain: data-extraction
  - tech: [python, lxml, xml-parsing]
related_documents:
  - "[Previous Phase](../02-extractor-phase-01/README.md)"
---
-->

# M03: Extractor Phase 2 — Schema-Driven v2

## Summary

| Attribute | Value |
|-----------|-------|
| Status | ✅ Complete |
| Sessions | Multiple |
| Artifacts | schema_discovery.py, rimworld_extractor_v2.py (v2.2) |

**Objective:** Replace hardcoded path guessing with schema-driven extraction derived from actual save file analysis. Expand extraction to cover all meaningful game state.

**Outcome:** v2.2 extractor with 18+ extraction categories, dual-audience commenting, and validated output against 270-mod save files.

---

## 1. Contents

```
03-extractor-phase-02/
└── README.md               # This file
```

**Related Files:**
```
tools/extractor/
├── schema_discovery.py         # NEW: XML structure analysis tool
├── rimworld_extractor_v2.py    # NEW: Schema-driven extractor (v2.2)
├── rimworld_extractor.py       # Legacy v1 (reference only)
└── parsers/                    # Legacy modular parsers (reference)

state/snapshots/
├── the-fringe-benefit/         # Production output
└── milestone-03-extractor-phase-02/  # Validation captures
```

---

## 2. Work Completed

| Task | Description | Result |
|------|-------------|--------|
| Schema Discovery Tool | Walk full XML tree, map all paths | ✅ 4,854 unique paths |
| DOM Parsing | Replace streaming with full tree load | ✅ ~3s for 18MB |
| Faction Extraction | `Faction_` prefix handling | ✅ Working |
| Colonist Extraction | Player faction detection | ✅ 7 colonists |
| Building Extraction | Keyword categorization | ✅ 1,002 buildings |
| Zone Extraction | Growing + stockpile | ✅ 8 zones |
| Quest Extraction | Status derivation from parts | ✅ Working |
| World Objects | Settlements, Real Ruins, sites | ✅ 441 objects |
| Work Tab | Complex Jobs 0-9 priorities | ✅ 225 workgivers/pawn |
| Power Network | Batteries, generators, fuel | ✅ Working |
| Combat/Social Logs | Play log, battle log, tales | ✅ Working |
| Dual-Audience Comments | AI NOTEs + human context | ✅ Applied |

---

## 3. Extraction Results

Final extraction from `the-fringe-benefit#§#Autosave-129.rws`:

| Category | Count/Value |
|----------|-------------|
| Game Version | 1.6 (Odyssey) |
| Mods | 270 |
| Colonists | 7 |
| Animals | 2 |
| Buildings | 1,002 (428 walls, 256 conduits, 7 turrets) |
| Zones | 8 |
| Research Completed | 45 |
| World Locations | 441 (371 settlements, 50 Real Ruins) |
| Factions | 20+ |
| Work Tab Pawns | 12 |
| Workgivers per Pawn | 225 |

---

## 4. Key Decisions

| Decision | Rationale |
|----------|-----------|
| DOM over streaming | File sizes manageable, random access needed for cross-referencing |
| Schema-driven paths | v1 guessed wrong — discovery tool validates actual structure |
| Building categorization | Keyword heuristics cover vanilla + major mod packs |
| Work Tab extraction | Complex Jobs mod is common, 0-9 scale valuable for analysis |

---

## 5. Technical Notes

### Schema Discovery Results

| Metric | Value |
|--------|-------|
| Total XML Elements | 418,374 |
| Unique Tag Paths | 4,854 |
| Maximum Depth | 17 |

### Key XML Paths Discovered

- Factions: `savegame/game/world/factionManager/allFactions/li`
- Map pawns: `savegame/game/maps/li/things/thing` (Class="Pawn")
- Buildings: `savegame/game/maps/li/things/thing` (Class starts with "Building")
- Quests: `savegame/game/questManager/quests/li`
- World objects: `savegame/game/world/worldObjects/worldObjects/li`
- Work Tab: `savegame/game/components/li/Priorities`

### AI NOTEs Added

1. `extract_factions()` — Faction references use `Faction_<loadID>` format
2. `extract_work_tab_priorities()` — Work Tab mod-specific, won't exist without mod
3. `extract_pawn()` — Sub-elements use `IsNull="True"` attribute when empty
4. `extract_map_pawns()` — Must detect player faction first with `Faction_` prefix
5. Section header — Paths are 1.6-specific, re-run schema discovery if extraction breaks

---

## 6. Known Limitations

| Limitation | Notes |
|------------|-------|
| Work Tab names | Shows Thing_HumanXXXXX, not resolved to colonist names |
| Power rates | Production/consumption calculated at runtime, not in saves |
| Legacy v1 | Still in repo for reference, not recommended |

---

## 7. Next Phase

**Handoff:** Extractor v2.2 is complete with full extraction and dual-audience commenting. Ready for database integration or GitHub project frameout.

**Next Steps:**

1. **M04: GitHub Project Frameout** — Issues, milestones, project board
2. **M05: Database Schema** — PostgreSQL tables for pgsql01
3. **M06: Watcher Daemon** — Auto-extract on new saves
4. **M07: MCP Integration** — CrystalDB MCP for Claude queries

**Deferred:**
- Work Tab pawn name resolution
- Drug/outfit policy extraction
- Ideology/precept extraction
