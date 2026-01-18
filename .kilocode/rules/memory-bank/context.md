# RimWorld AI Colony Co-Play Context

## Current State
**Last Updated:** 2026-01-18

### Recent Accomplishments
- ✅ **M01: Ideation and Setup** — Complete
- ✅ **M02: Extractor Phase 1** — Complete
  - Schema discovery tool created (`schema_discovery.py`)
  - v2.2 schema-driven extractor with DOM parsing
  - Full extraction: 18+ categories validated
  - Dual-audience commenting applied to extractor
  - Work Tab mod priorities extraction (0-9 scale, ~225 workgivers/pawn)
  - Quest extraction with status derivation
  - World objects: settlements, ruins (Real Ruins), sites
  - Buildings categorized: production, defense, power, storage, furniture, etc.
  - Power network summary (batteries, generators, fuel levels)
  - Play log, battle log, tales extraction
  - Map grid data for potential visualization
- ✅ **Interior READMEs** — All directories documented with interior READMEs

### Current Phase

**M02 Complete.** Ready for database integration (M03).

### Active Work

Phase 1 Extraction — Complete:
1. ✓ Schema discovery via `schema_discovery.py`
2. ✓ DOM-based extractor using actual XML paths
3. ✓ Faction relations with `Faction_` prefix handling
4. ✓ Colonist/animal extraction with player faction filtering
5. ✓ Buildings, zones, power network
6. ✓ Quests, world objects, Work Tab priorities
7. ✓ JSON + Markdown output formats
8. ✓ Dual-audience commenting throughout extractor

## Next Steps

### Immediate
1. Commit and push current work
2. ✓ Update main README.md with current status

### Near-Term (Next Sessions)
- **M03: Database Storage** — PostgreSQL + pgvector + TimescaleDB + Neo4j on pgsql01
- **M04: Watcher Daemon** — Auto-extract on new saves
- **M05: MCP Integration** — Database MCP for Claude queries

### Future / Backlog
- TimescaleDB time series for trend analysis (mood, resources over time)
- Neo4j for relationship graphs (colonist social networks, faction webs)
- Progress Renderer correlation (visual + data)
- Resolve pawn names in Work Tab output (currently shows Thing_HumanXXXXX)
- Drug/outfit policy extraction
- Ideology/precept extraction

## Active Decisions

### Pending Decisions
- **Database schema:** Exact table structure for snapshots, colonists, skills, resources
- **Neo4j use case:** Colonist social networks, faction relationship graphs, or both
- **Watcher trigger:** Polling interval vs. filesystem events
- **Work Tab name resolution:** Cross-reference pawn IDs to colonist names

### Recent Decisions
- **2026-01-18 — Multi-database architecture:** PostgreSQL (relational) + TimescaleDB (time series) + Neo4j (graph)
- **2026-01-18 — DOM over streaming:** File sizes (~18MB) manageable, random access simplifies cross-referencing
- **2026-01-18 — Schema-driven paths:** Run discovery tool, extract actual paths, not hardcoded guesses
- **2026-01-18 — Building categorization:** Keyword heuristics for production/defense/power/etc.
- **2026-01-18 — Work Tab extraction:** Handle Complex Jobs mod's 0-9 priority scale
- **2026-01-18 — Real Ruins support:** Extract blueprintName, wealthOnEnter for raid targeting

## Blockers and Dependencies

### Current Blockers
- None

### External Dependencies
- **pgsql01:** PostgreSQL with pgvector + TimescaleDB extension for CAG system
- **Neo4j:** For relationship graph queries
- **Database MCP:** For Claude to query extracted data
- **RimWorld autosaves:** 18-slot autosave with event-triggered saves configured

## Technical Notes

### Extraction Performance
- 18MB save file processed in ~3 seconds with DOM parsing
- lxml etree.parse() loads full tree (manageable for current file sizes)
- 270 mods handled without issues

### Known XML Quirks (RimWorld 1.6)
- Pawns use `Class="Pawn"` attribute on `<thing>` elements
- Faction references use `Faction_<loadID>` format — strip prefix for lookup
- Skills nested under `<skills><skills><li>` (double nesting)
- Many pawn sub-elements use `IsNull="True"` attribute when empty
- Work Tab stores priorities in `game/components/li/Priorities`, not with pawn
- Real Ruins adds `blueprintName`, `originX/Z`, `wealthOnEnter` to world objects

### File Locations
- Extractor: `tools/extractor/rimworld_extractor_v2.py`
- Schema discovery: `tools/extractor/schema_discovery.py`
- Test colony: `game-saves/the-fringe-benefit/`
- Output: `state/snapshots/colony_*.json` and `colony_*.md`

### Current Colony Stats (The Fringe Benefit)
- 7 colonists, 2 animals
- 1,002 buildings (428 walls, 256 conduits, 7 turrets)
- 8 zones (growing + stockpile)
- 45 research completed
- 441 world locations (371 settlements, 50 Real Ruins)
- 270 mods active

## Context for Next Session
- Extractor v2.2 is functional and fully commented
- Schema discovery tool available for future XML analysis
- Output validates against actual colony
- Ready for database schema design on pgsql01
- CAG architecture: Save → Extractor → (PostgreSQL + TimescaleDB + Neo4j) → MCP → Claude
