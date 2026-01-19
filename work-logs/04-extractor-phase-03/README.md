<!--
---
title: "M04: Extractor Phase 3 — Kaggle Expansion"
description: "Deep pawn extraction, container scanning, world state tracking"
author: "VintageDon"
date: "2026-01-19"
version: "1.0"
status: "Complete"
tags:
  - type: worklog
  - domain: data-extraction
  - tech: [python, lxml, xml-parsing]
related_documents:
  - "[Previous Phase](../03-extractor-phase-02/README.md)"
  - "[Expansion Plan](../../scratch/extractor-v23-kaggle-expansion-plan.md)"
---
-->

# M04: Extractor Phase 3 — Kaggle Expansion

## Summary

| Attribute | Value |
|-----------|-------|
| Status | ✅ Complete |
| Sessions | 5 (m03-chat-01 through m03-chat-05) |
| Artifacts | rimworld_extractor_v2.py (v2.2 → v2.3) |

Objective: Expand extractor from advisory tool to comprehensive dataset generator capable of producing Kaggle-quality behavioral simulation data. Extract deep pawn psychology, genetics, social graphs, accurate inventories, and world population state.

Outcome: v2.3 extractor with 4 new extraction batches, ~1,800 lines (up from ~1,400), validated against 270-mod save files.

---

## 1. Contents

```
04-extractor-phase-03/
└── README.md               # This file
```

Related Files:

```
tools/extractor/
├── rimworld_extractor_v2.py    # v2.3 (Kaggle expansion)
└── schema_discovery.py         # Path validation tool

scratch/
└── extractor-v23-kaggle-expansion-plan.md  # Planning document

state/snapshots/
└── the-fringe-benefit/         # Production output
```

---

## 2. Work Completed

### Batch 1: Low-Hanging Fruit (m03-chat-02)

| Unit | Description | Result |
|------|-------------|--------|
| Apparel extraction | Worn items with def, stuff, quality, health | ✅ Working |
| Primary weapon | Equipped weapon from equipment container | ✅ Working |
| Immunity tracker | Disease immunity progress per hediff | ✅ Working |
| Lifetime records | `recordsDeflate` compressed blob | ⏸️ Deferred |

Path Corrections Discovered:

| Field | Plan (wrong) | Validated (correct) |
|-------|--------------|---------------------|
| Apparel | `apparel/wornApparel/li` | `apparel/wornApparel/innerList/li` |
| Weapon | `equipment/primaryEquip` | `equipment/equipment/innerList/li` |
| Immunity | `immunity/immunityList/li` | `immunity/imList/li` |

### Batch 2: Pawn Deep Dive (m03-chat-03)

| Unit | Description | Result |
|------|-------------|--------|
| Thought memories | Mood breakdown with def, age, stage, other_pawn | ✅ Working |
| Social opinions | `opinion_offset` from `directRelations` | ✅ Working |
| Genes (Biotech) | xenotype, endogenes, xenogenes extraction | ✅ Working |

### Batch 3: Inventory Accuracy (m03-chat-04)

| Unit | Description | Result |
|------|-------------|--------|
| `extract_container_contents()` | Recursive container scanning with depth guard | ✅ Working |
| `extract_resources_deep()` | Surface items + nested container contents | ✅ Working |
| `extract_resources_surface()` | Original function preserved for comparison | ✅ Renamed |

### Batch 4: World State & DLC (m03-chat-05)

| Unit | Description | Result |
|------|-------------|--------|
| Kidnapped pawns | Per-faction captive tracking | ✅ Working |
| World pawns | Dead, captured, left colony (357 NPCs in test save) | ✅ Working |
| Psycasts (Royalty) | Abilities, entropy, psyfocus extraction | ✅ Working |

---

## 3. Extraction Results

Final extraction from `the-fringe-benefit#§#Autosave-137.rws`:

| Category | Count/Value |
|----------|-------------|
| Game Version | 1.6 (Odyssey) |
| Mods | 270+ |
| Colonists | 7 |
| World Pawns | 357 (4 collections) |
| Kidnapped | 0 (no current captives) |
| Resources (deep) | Accurate with container contents |

### New Colonist Fields

| Field | Typical Values |
|-------|----------------|
| `apparel` | 4-8 items per colonist |
| `primary_weapon` | Weapon def + quality |
| `immunity` | Active disease immunities |
| `memories` | 10-25 thought memories |
| `opinion_offset` | Per-relation opinion modifier |
| `genes` | Xenotype + gene lists (Biotech pawns) |
| `psycasts` | Abilities + entropy/psyfocus (Royalty pawns) |

---

## 4. Key Decisions

| Decision | Rationale |
|----------|-----------|
| Deferred `recordsDeflate` | Requires Base64 + zlib decompression — separate implementation effort |
| Full world pawn extraction | Analytical value of complete population tracking outweighs minimal approach |
| Standalone `extract_psycasts()` | Easier to debug, cleaner separation of DLC-specific logic |
| Preserved `extract_resources_surface()` | Allows comparison and fallback if deep scanning has issues |
| KC work unit structure | Discrete prompts with prevalidation prevented agent context loss |

---

## 5. Technical Notes

### World Pawn Collections

Save file contains 4 separate world pawn collections:

| Collection | Purpose | Count |
|------------|---------|-------|
| `pawnsAlive` | Living off-map pawns | Variable |
| `pawnsDead` | Deceased pawns with history | Variable |
| `pawnsMothballed` | Performance-optimized storage | Variable |
| `pawnsForcefullyKeptAsWorldPawns` | Special tracking | Variable |

Total: 357 world pawns in test save.

### Container Recursion

Deep Storage and similar mods nest items inside buildings. The `extract_container_contents()` function:

- Handles arbitrary nesting depth (max_depth=5 guard)
- Tracks container_depth for analysis
- Avoids double-counting with surface scan separation

### Path Validation Methodology

Schema file too large for direct context loading (343KB, ~85K tokens). Validation performed via:

1. PowerShell `Select-String` queries against terminal element names
2. Targeted Python scripts for structure verification
3. Extraction test runs against live save files

---

## 6. Known Limitations

| Limitation | Notes |
|------------|-------|
| `recordsDeflate` not extracted | Compressed format needs separate decompression implementation |
| Version header | Still shows v2.2 in docstring, needs manual bump to v2.3 |
| Drug/outfit policies | Not yet extracted (medium priority) |
| Ideology precepts | Not yet extracted (low priority) |

---

## 7. Next Steps

Immediate:

1. Version bump to v2.3 in docstring
2. Dual-audience commenting pass
3. Update KC memory bank files
4. Update front page README

Future Milestones:

| Milestone | Focus |
|-----------|-------|
| M05 | Database schema (PostgreSQL + TimescaleDB) |
| M06 | Watcher daemon (auto-extract on save) |
| M07 | MCP integration (Claude queries) |

Deferred:

- `recordsDeflate` decompression (lifetime stats)
- Drug/food policy extraction
- Outfit policy parsing
- Ideology precept extraction

---

## 8. Session Log

| Chat | Date | Focus | Outcome |
|------|------|-------|---------|
| m03-chat-01 | 2026-01-18 | Planning, workflow setup | Batch strategy defined |
| m03-chat-02 | 2026-01-18 | Batch 1 implementation | Apparel, weapon, immunity |
| m03-chat-03 | 2026-01-18 | Batch 2 implementation | Memories, opinions, genes |
| m03-chat-04 | 2026-01-19 | Batch 3 implementation | Container scanning |
| m03-chat-05 | 2026-01-19 | Batch 4 implementation | World state, psycasts |
