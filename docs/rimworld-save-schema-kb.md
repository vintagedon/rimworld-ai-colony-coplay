<!--
---
title: "RimWorld Save File Schema Knowledge Base"
description: "Guide to navigating RimWorld save XML structure and using schema discovery files"
author: "Claude + CrainBramp"
date: "2026-01-19"
version: "1.0"
status: "Active"
tags:
  - type: knowledge-base
  - domain: data-extraction
  - tech: xml
related_documents:
  - "[Extractor](../tools/extractor/rimworld_extractor_v2.py)"
  - "[Schema Discovery](../tools/extractor/schema_discovery.py)"
  - "[Expansion Plan](../scratch/extractor-v23-kaggle-expansion-plan.md)"
---
-->

# RimWorld Save File Schema Knowledge Base

This document explains the structure of RimWorld save files and how to use the schema discovery outputs for developing extraction logic.

---

## 1. Schema Files Overview

Two schema discovery outputs are available in `docs/`:

| File | Depth | Size | Use Case |
|------|-------|------|----------|
| `schema_*-depth-6.md` | 6 levels | ~50KB | Quick navigation, common paths |
| `schema_*-full-depth.md` | 17 levels | ~350KB | Complete structure, deep paths |

### Reading Schema Output

The schema uses tree notation with metadata:

```
└── tag_name (count) — attrs: [attr1, attr2] — [text]
```

- **count**: Number of occurrences in the save file
- **attrs**: XML attributes present on the element
- **[text]**: Indicates the element contains text content (not just children)

Example interpretation:
```
├── li (322) — attrs: [Class]
```
This means 322 `<li>` elements exist at this path, each with a `Class` attribute.

---

## 2. Top-Level Structure

RimWorld saves follow this root structure:

```xml
<savegame>
    <meta>          <!-- Save metadata, mod list -->
    <game>          <!-- All game state -->
        <maps>      <!-- Colony maps (usually 1) -->
        <world>     <!-- World state, factions, world pawns -->
        <components><!-- Mod data storage -->
        ...
    </game>
</savegame>
```

Key insight: Most data lives under `game/`. The `meta` section contains mod load order which determines available XML extensions.

---

## 3. Major Path Categories

### 3.1 Game State

| Data | Path | Notes |
|------|------|-------|
| Tick counter | `game/tickManager/ticksGame` | Current game time in ticks |
| Storyteller | `game/components/li/currentStoryteller` | Active storyteller def |
| Difficulty | `game/components/li/currentDifficulty` | Current difficulty setting |
| Research | `game/researchManager/progress` | Keys/values dict format |

### 3.2 Factions

| Data | Path | Notes |
|------|------|-------|
| All factions | `game/world/factionManager/allFactions/li` | Each `li` is one faction |
| Faction name | `faction/name` | Display name |
| Faction def | `faction/def` | `PlayerColony` for player faction |
| Faction ID | `faction/loadID` | Referenced as `Faction_{loadID}` elsewhere |
| Relations | `faction/relations/li` | Goodwill, relation kind |
| Kidnapped | `faction/kidnapped/li` | Pawn IDs held captive |

**AI NOTE**: Faction references throughout the save use `Faction_<loadID>` format. When resolving pawn faction membership, strip the `Faction_` prefix to match against `loadID` values.

### 3.3 Maps and Things

| Data | Path | Notes |
|------|------|-------|
| Map list | `game/maps/li` | Usually single map |
| Map size | `map/mapInfo/size` | Format: `(x, y, z)` |
| All things | `map/things/thing` | Buildings, items, pawns |
| Zones | `map/zoneManager/allZones/li` | Stockpiles, growing zones |
| Weather | `map/weatherManager/curWeather` | Current weather def |

Thing elements use `Class` attribute to identify type:
- `Class="Pawn"` — Colonists, animals, NPCs
- `Class="Building_*"` — Structures
- `Class="ThingWithComps"` — Stackable items
- `Class="MinifiedThing"` — Uninstalled buildings

### 3.4 Pawns (Map)

Pawns on the player's map are in `map/things/thing[@Class='Pawn']`.

| Data | Path (relative to pawn) | Notes |
|------|-------------------------|-------|
| Pawn ID | `id` | Unique identifier |
| Definition | `def` | `Human` for colonists |
| Faction | `faction` | `Faction_<loadID>` format |
| Name | `name/*` | Class determines structure |
| Age | `ageTracker/ageBiologicalTicks` | Convert to years ÷ 3600000 |
| Skills | `skills/skills/li` | Def, level, passion |
| Traits | `story/traits/allTraits/li` | Def, degree |
| Health | `healthTracker/hediffSet/hediffs/li` | Injuries, diseases, implants |
| Needs | `needs/needs/li` | Mood, food, rest levels |
| Memories | `needs/needs/li[def='Mood']/thoughts/memories/memories/li` | Mood modifiers |
| Relations | `social/directRelations/li` | Family, friends, opinion |
| Apparel | `apparel/wornApparel/innerList/li` | Worn items |
| Equipment | `equipment/equipment/innerList/li` | Weapons |
| Genes | `genes/*` | Biotech DLC |
| Abilities | `abilities/abilities/li` | Psycasts, mod abilities |
| Immunity | `healthTracker/immunity/imList/li` | Disease immunity progress |

**AI NOTE**: Name elements use `Class` attribute:
- `Class="NameTriple"` → `first`, `nick`, `last` children
- `Class="NameSingle"` → `name` child only

### 3.5 World Pawns

Pawns not on the map (dead, captured, traveling) are in `game/world/worldPawns/`:

| Collection | Path | Contents |
|------------|------|----------|
| Alive | `worldPawns/pawnsAlive/li` | Off-map living pawns |
| Mothballed | `worldPawns/pawnsMothballed/li` | Memory-optimized storage |
| Dead | `worldPawns/pawnsDead/li` | Deceased pawns with history |
| Forcefully kept | `worldPawns/pawnsForcefullyKeptAsWorldPawns/li` | References only |

Each pawn has `becameWorldPawnTickAbs` indicating when they left the map.

### 3.6 World Objects

World map locations are in `game/world/worldObjects/worldObjects/li`:

| Data | Path | Notes |
|------|------|-------|
| Definition | `def` | Settlement, Site, etc. |
| Tile | `tile` | World map tile ID |
| Faction | `faction` | Owner faction |
| Name | `nameInt` | Display name |

**Real Ruins mod** adds:
- `blueprintName` — Uploaded base GUID
- `wealthOnEnter` — Loot value
- `originX/originZ` — Original map coordinates

### 3.7 Containers and Resources

Storage mods nest items inside buildings:

```
building/innerContainer/innerList/li
                       └── item/innerContainer/innerList/li  (nested)
```

Each item has:
- `def` — Item definition
- `stackCount` — Quantity (default 1)
- `stuff` — Material for stuffable items
- `quality` — Quality level

**AI NOTE**: Always check `IsNull="True"` attribute before iterating containers. Missing items from resource counts usually means containers weren't scanned.

### 3.8 Work Tab (Mod-Specific)

Work Tab mod stores priorities in `game/components/li/Priorities`:

| Data | Path | Notes |
|------|------|-------|
| Pawn reference | `values/li/Pawn` | Thing_HumanXXXX format |
| Priorities | `values/li/Priorities/li` | Workgiver + priority value |

Priority values: 0 = disabled, 1 = highest, 9 = lowest.

---

## 4. Common Patterns

### 4.1 Null Attributes

RimWorld uses `IsNull="True"` attribute on empty containers instead of omitting them:

```xml
<apparel IsNull="True" />       <!-- No apparel -->
<apparel>                        <!-- Has apparel -->
    <wornApparel>...</wornApparel>
</apparel>
```

Always check: `elem.get('IsNull') != 'True'` before iterating children.

### 4.2 Dictionary Serialization

Key-value maps serialize as parallel arrays:

```xml
<progress>
    <keys>
        <li>Research_Machining</li>
        <li>Research_Smithing</li>
    </keys>
    <values>
        <li>1200.0</li>
        <li>600.0</li>
    </values>
</progress>
```

Reconstruct with: `zip(keys.findall('li'), values.findall('li'))`

### 4.3 Position Format

Coordinates use `(x, y, z)` string format:
- `x` — Horizontal axis
- `y` — Always 0 for ground level
- `z` — Vertical axis on 2D map view

Parse with regex: `\((\d+),\s*(\d+),\s*(\d+)\)`

### 4.4 Tick Conversions

| Unit | Ticks |
|------|-------|
| Second | 60 |
| Hour | 2,500 |
| Day | 60,000 |
| Quadrum | 900,000 |
| Year | 3,600,000 |

---

## 5. Using Schema Discovery

Run the discovery tool to analyze new save files:

```powershell
cd tools/extractor
python schema_discovery.py "path/to/save.rws" -d 8  # depth 8
python schema_discovery.py "path/to/save.rws"       # full depth
```

### Validating Paths

Before implementing new extraction, validate paths exist:

```powershell
# Quick check for element existence
Select-String -Path "schema_*.md" -Pattern "kidnapped"

# Check path depth and structure
Select-String -Path "schema_*.md" -Pattern "worldPawns"
```

### When to Re-run Discovery

- After RimWorld major version updates
- When extraction returns unexpected empty results
- When adding support for new mods
- When debugging path assumptions

---

## 6. Mod Extensions

Common mods that extend save structure:

| Mod | Extension Location | Data |
|-----|-------------------|------|
| Work Tab | `game/components/li/Priorities` | Per-workgiver priorities |
| Real Ruins | `world/worldObjects/li/*` | Blueprint data |
| Biotech DLC | `pawn/genes/*` | Genetic modifications |
| Royalty DLC | `pawn/abilities/*`, `pawn/psychicEntropy/*` | Psycasts |
| Ideology DLC | `pawn/ideo/*` | Beliefs, roles |

**AI NOTE**: Check mod list in `meta/modIds/li` to determine which extensions are active before assuming paths exist.

---

## 7. Troubleshooting

| Symptom | Likely Cause | Solution |
|---------|--------------|----------|
| Empty colonist list | Wrong player faction ID | Check `Faction_` prefix handling |
| Zero resources | Missing container scan | Add innerContainer traversal |
| Missing pawn data | `IsNull="True"` not checked | Add null attribute guard |
| Path not found | RimWorld version change | Re-run schema discovery |
| Wrong faction names | ID resolution failure | Build faction lookup map first |

---

## Document Info

| | |
|---|---|
| Created | 2026-01-19 |
| Updated | 2026-01-19 |
| Version | 1.0 |
| Status | Active |
