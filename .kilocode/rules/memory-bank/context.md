# RimWorld AI Colony Co-Play Context

## Current State
**Last Updated:** 2026-01-18

### Recent Accomplishments
- ✅ **M01: Ideation and Setup** — Complete
- ✅ **M02: Extractor Phase 1** — Complete
  - lxml streaming architecture implemented
  - Meta extraction: 267 mods, game version
  - Faction extraction: 20 factions with LoadID resolution
  - Relations extraction: Goodwill values populated
  - Colonist extraction: 11 colonists with skills, traits, needs
  - Resource extraction: 65 item types categorized
  - Research extraction: 310 completed projects
  - Animal extraction: 34 animals
  - Game time: Year, day, quadrum, season
  - World info: Colony name, seed

### Current Phase

**M02: Extractor Phase 1** is complete. Ready for commit and M03 planning.

### Active Work

Phase 1 Extraction — Complete:
1. ✓ GDR research on RimWorld 1.6 XML structure
2. ✓ lxml streaming parser implementation
3. ✓ Faction relations with LoadID resolution
4. ✓ Colonist/animal extraction with section guards
5. ✓ Resource/research extraction
6. ✓ JSON + Markdown output formats
7. ✓ M02 worklog documentation

## Next Steps

### Immediate
1. Update main README.md with Phase 1 completion
2. Commit feature branch: `feature/extractor-phase1-foundation`
3. Merge to main

### Near-Term (Next Sessions)
- **M03: Database Schema** — Design PostgreSQL tables for pgsql01
- **M04: Watcher Daemon** — Auto-extract on new saves
- **M05: MCP Integration** — CrystalDB MCP for Claude queries

### Future / Backlog
- Storyteller/difficulty extraction (nested deeper in save)
- Gender extraction for modded saves (stored in genes)
- InfluxDB time series for trend analysis
- Neo4j for relationship graphs
- Progress Renderer correlation (visual + data)

## Active Decisions

### Pending Decisions
- **Database schema:** Exact table structure for snapshots, colonists, skills, resources
- **Watcher trigger:** Polling interval vs. filesystem events

### Recent Decisions
- **2026-01-18 — lxml over stdlib:** Memory-efficient streaming for 22MB files
- **2026-01-18 — Two-pass LoadID:** Build faction index, then resolve references
- **2026-01-18 — Section guards:** Only extract pawns from `<things>` inside `<maps>`
- **2026-01-18 — Database target:** pgsql01 with pgvector, not local Docker

## Blockers and Dependencies

### Current Blockers
- None

### External Dependencies
- **pgsql01 (10.25.20.8):** PostgreSQL with pgvector for CAG system
- **CrystalDB MCP:** For Claude to query extracted data
- **RimWorld autosaves:** 18-slot autosave with event-triggered saves configured

## Technical Notes

### Extraction Performance
- 22MB save file processed in ~2 seconds
- lxml iterparse keeps memory constant
- 267 mods handled without issues

### Known XML Quirks (RimWorld 1.6)
- Pawns use `<thing Class="Pawn">` not `<li Class="Pawn">`
- Faction references use `Faction_N` format
- Skills nested under `<skills><skills><li>`
- Gender stored in genes/body type for modded pawns
- Compressed world data in `*Deflate` tags (ignored)

### File Locations
- Extractor: `tools/extractor/rimworld_extractor.py`
- Parsers: `tools/extractor/parsers/`
- Test save: `game-saves/deserters-of-the-rim/Deserters of the Rim#§#Hoeaia.rws`
- Output: `state/snapshots/colony_*.json` and `colony_*.md`
- GDR report: `.internal-files/rimworld-1_6-save-file-xml.md`

## Context for Next Session
- Extractor is functional — run from `tools/extractor/`
- Output validates against actual colony (11 colonists, 310 research, etc.)
- Ready to design database schema for historical storage
- CAG architecture: Save → Extractor → PostgreSQL → MCP → Claude
