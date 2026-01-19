# RimWorld AI Colony Co-Play Context

## Current State
**Last Updated:** 2026-01-19

### Recent Accomplishments
- ✅ **M01: Ideation and Setup** — Complete
- ✅ **M02: Extractor Phase 1** — Complete (v2.0)
- ✅ **M03: Extractor Phase 2** — Complete (v2.2)
  - Schema discovery tool created (`schema_discovery.py`)
  - DOM parsing with lxml, ~3s for 18MB saves
  - 18+ extraction categories validated
  - Work Tab mod priorities (0-9 scale, ~225 workgivers/pawn)
  - Dual-audience commenting applied
- ✅ **M04: Extractor Phase 3 — Kaggle Expansion** — Complete (v2.3)
  - Batch 1: apparel, primary_weapon, immunity extraction
  - Batch 2: thought memories, social opinions (opinion_offset), genes (Biotech)
  - Batch 3: recursive container scanning (`extract_resources_deep`)
  - Batch 4: world pawns (357 NPCs), kidnapped tracking, psycasts (Royalty)
  - ~1,800 lines (up from ~1,400)

### Current Phase

**M04 Complete.** Ready for milestone wrap-up and commit.

### Active Work

Milestone wrap-up tasks:
1. ✓ Dual commenting pass on extractor
2. ⏸️ Schema KB document (deferred — large files)
3. ✓ Interior READMEs check (gitignored dirs skipped)
4. ✓ Work-log 04 written
5. ✓ KC memory bank update (this file)
6. ◻️ Front page README update
7. ◻️ Feature commit

## Next Steps

### Immediate
1. Update main README.md with v2.3 capabilities
2. Commit and push M04 work

### Near-Term (Next Sessions)
- **M05: Database Schema** — PostgreSQL + pgvector + TimescaleDB on pgsql01
- **M06: Watcher Daemon** — Auto-extract on new saves
- **M07: MCP Integration** — Database MCP for Claude queries

### Future / Backlog
- `recordsDeflate` decompression (lifetime stats — Base64 + zlib)
- Drug/food policy extraction
- Outfit policy extraction
- Ideology/precept extraction
- Work Tab pawn name resolution (currently shows Thing_HumanXXXXX)
- TimescaleDB time series for trend analysis
- Neo4j for relationship graphs

## Active Decisions

### Pending Decisions
- **Database schema:** Exact table structure for snapshots, colonists, skills, resources
- **Neo4j use case:** Colonist social networks, faction relationship graphs, or both
- **Watcher trigger:** Polling interval vs. filesystem events

### Recent Decisions
- **2026-01-19 — Full world pawn extraction:** Analytical value of complete population tracking outweighs minimal approach
- **2026-01-19 — Standalone psycasts function:** Easier to debug, cleaner DLC separation
- **2026-01-19 — Deferred recordsDeflate:** Requires Base64 + zlib — separate implementation effort
- **2026-01-18 — KC work unit structure:** Discrete prompts with prevalidation prevent agent context loss
- **2026-01-18 — DOM over streaming:** File sizes manageable, random access simplifies cross-referencing

## Blockers and Dependencies

### Current Blockers
- None

### External Dependencies
- **pgsql01:** PostgreSQL with pgvector + TimescaleDB for CAG system
- **Neo4j:** For relationship graph queries
- **Database MCP:** For Claude to query extracted data

## Technical Notes

### Extraction Performance
- 18MB save file processed in ~3 seconds with DOM parsing
- lxml etree.parse() loads full tree
- 270+ mods handled without issues
- World pawn extraction adds 357 NPCs across 4 collections

### Path Corrections (M04)
| Field | Planned Path | Validated Path |
|-------|--------------|----------------|
| Apparel | `apparel/wornApparel/li` | `apparel/wornApparel/innerList/li` |
| Weapon | `equipment/primaryEquip` | `equipment/equipment/innerList/li` |
| Immunity | `immunity/immunityList/li` | `immunity/imList/li` |
| Opinions | `social/opinions` | `social/directRelations` + `opinionOffset` |
| World pawns | `worldPawnsAlive` | `worldPawns` (4 sub-collections) |

### File Locations
- Extractor: `tools/extractor/rimworld_extractor_v2.py` (v2.3)
- Schema discovery: `tools/extractor/schema_discovery.py`
- Test colony: `game-saves/the-fringe-benefit/`
- Output: `state/snapshots/colony_*.json` and `colony_*.md`
- Expansion plan: `scratch/extractor-v23-kaggle-expansion-plan.md`

### Current Colony Stats (The Fringe Benefit)
- 7 colonists, 2 animals
- 357 world pawns (dead, captured, left)
- 1,002 buildings
- 270+ mods active

## Context for Next Session
- Extractor v2.3 complete with Kaggle expansion
- Deep extraction: memories, genes, opinions, psycasts, world pawns
- Accurate resource counts with container recursion
- Ready for database schema design on pgsql01
