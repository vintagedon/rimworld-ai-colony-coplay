# RimWorld AI Colony Co-Play Product Overview

## Problems Solved

This project addresses:

- **No external AI advisor for RimWorld:** There's no solution for using Claude Desktop as an external companion that reads game state without modifying the game experience. This project enables that workflow.

- **Loss of context across play sessions:** RimWorld colonies develop over many real-world hours. Without persistent tracking, an AI advisor cannot reference colony history, identify trends, or understand the narrative arc of a playthrough.

- **Information overload in complex colonies:** Heavily modded RimWorld with 10+ colonists generates enormous amounts of data. Players miss critical issues (colonist mood spirals, resource depletion trends, skill gaps) buried in the complexity.

- **Manual state explanation:** Without automated extraction, getting AI advice requires manually describing colony state — tedious and incomplete.

## How It Works

The system operates in a read-only capacity, extracting game state from RimWorld's autosave files (.rws XML format) and transforming it into structured data Claude can analyze.

A Python extractor using lxml DOM parsing reads save files on demand, pulling comprehensive colony data: colonists (skills, traits, health, needs, relationships), resources, research progress, faction relations, buildings, zones, quests, world objects, and mod-specific data like Work Tab priorities. This data is output as JSON for programmatic access and Markdown for human readability.

Claude accesses extracted state via filesystem MCP or database queries during conversations, enabling queries like "how is Viktor's mood trending?" or "are we at risk of food shortage?" with answers grounded in actual game data rather than speculation.

Key components:
- **Schema Discovery:** Python/lxml tool to map actual XML structure from saves
- **Save Extractor:** Schema-driven Python/lxml script parsing .rws XML files into structured JSON
- **State Storage:** Timestamped snapshots enabling historical analysis (moving to PostgreSQL + TimescaleDB + Neo4j)
- **Claude Integration:** CAG (Context Augmented Generation) via database queries

## Goals and Outcomes

### Primary Goals
1. **Complete state extraction:** Parse all meaningful data from heavily modded saves ✅
2. **Historical tracking:** Maintain timestamped snapshots enabling trend analysis and change detection
3. **Efficient processing:** Handle 18-25MB save files in under 30 seconds ✅ (actual: ~3 seconds)

### User Experience Goals
- Ask Claude about colony state and receive accurate, data-backed answers
- Identify risks and optimization opportunities through trend analysis
- Maintain narrative continuity across play sessions with persistent colony memory

### Success Metrics
- **Extraction completeness:** 18+ categories validated ✅
- **Performance:** Sub-5-second extraction for 18MB saves ✅
- **Accuracy:** Extracted data matches in-game values when spot-checked ✅

## Phased Roadmap

| Phase | Focus | Status |
|-------|-------|--------|
| M01 | Repository setup, documentation | ✅ Complete |
| M02 | Extractor v2, schema discovery, full extraction | ✅ Complete |
| M03 | Database storage (PostgreSQL + TimescaleDB + Neo4j) | 🔄 Next |
| M04 | File watcher for automatic extraction | Planned |
| M05 | MCP integration for Claude queries | Planned |
| P2 | Lightweight export mod (real-time state) | Future |
| P3 | Limited game interaction (draft orders, priorities) | Future |

## Current Extraction Capabilities

| Category | Status | Notes |
|----------|--------|-------|
| Meta (version, mods) | ✅ | 270 mods extracted |
| Game Time | ✅ | Year, day, quadrum, hour |
| Storyteller | ✅ | From game/components |
| Difficulty | ✅ | From game/components |
| Weather | ✅ | Current + last |
| Colony Stats | ✅ | Adaptation, raids, population |
| Factions | ✅ | 20+ factions with relations |
| Relations | ✅ | Goodwill integers populated |
| Research | ✅ | 45+ completed, current project |
| Colonists | ✅ | 7 with full profiles (skills, traits, health, needs) |
| Animals | ✅ | 2 colony animals with training |
| Resources | ✅ | Dynamic discovery, all stockpiled items |
| Buildings | ✅ | 1,002 categorized (production, defense, power, etc.) |
| Zones | ✅ | 8 zones with details |
| Power Network | ✅ | Batteries, generators, fuel levels |
| Play Log | ✅ | Social interactions |
| Battle Log | ✅ | Combat events |
| Tales | ✅ | Colony events for narrative |
| Quests | ✅ | 23 quests with status derivation |
| World Objects | ✅ | 441 (settlements, Real Ruins, sites) |
| Work Tab | ✅ | 225 workgivers per pawn (0-9 scale) |
| Map Grid | ✅ | Building/pawn positions for visualization |

## Current Colony: The Fringe Benefit

The active test colony for extraction validation:

- **Storyteller:** Ariadne Archduchess (VFE)
- **Year:** 5501, Aprimay, Day 5
- **Colonists:** 7
- **Buildings:** 1,002 (428 walls, 256 conduits, 7 turrets)
- **Wealth:** 100K+
- **World:** 441 locations (371 settlements, 50 Real Ruins)
- **Mods:** 270 active
