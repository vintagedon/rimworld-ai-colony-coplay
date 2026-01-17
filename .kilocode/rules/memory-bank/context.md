# RimWorld AI Colony Co-Play Context

## Current State
**Last Updated:** 2026-01-17

### Recent Accomplishments
- Repository scaffolded with standard template structure
- Directory structure finalized (tools/, state/, mod/, game-saves/)
- Memory bank populated with all 7 context files
- Primary README and all interior READMEs written
- Handoff document created for KC extractor work (`docs/rimworld-extractor-handoff.md`)
- Colony saves organized in `game-saves/deserters-of-the-rim/` with event-triggered saves enabled
- Reference materials added (RimAI Framework/Core source in `.reference-data/`)
- M01 worklog completed

### Current Phase

**M01: Ideation and Setup** is complete. Ready for initial commit and M02.

### Active Work

Completed:
1. ✓ Memory bank population
2. ✓ Primary README.md
3. ✓ Interior READMEs for all directories
4. ✓ M01 worklog documentation

## Next Steps

### Immediate
1. Initial commit: "Initial commit: repository scaffolding and documentation"
2. Delete empty `README-pending.md` file
3. Push to GitHub

### Near-Term (Next Sessions)
- M02: GitHub Project Frameout (labels, milestones, tasks, sub-tasks)
- Run KC extractor prompt to build initial Python script
- Test extraction against Deserters of the Rim saves
- Iterate on extraction completeness

### Future / Backlog
- File watcher for automatic extraction on autosave
- Historical diff tracking between snapshots
- Un-gitignore `game-saves/` once tooling is stable
- Phase 2 scoping: export mod architecture
- Integration patterns for Claude advisory sessions

## Active Decisions

### Pending Decisions
- **Extraction trigger:** Manual CLI vs. file watcher daemon — deferred until basic extraction works
- **History granularity:** How many snapshots to retain, diff format — decide after initial extraction validates

### Recent Decisions
- **2026-01-17 - Save location:** `game-saves/` replaces `.ai-sandbox/` as canonical save location
- **2026-01-17 - Directory structure:** Chose `tools/` over `src/` for Python tooling, `state/` for extracted output, `mod/` as future placeholder
- **2026-01-17 - State location:** Extracted JSON lives in repo (gitignored) rather than external location
- **2026-01-17 - Colony focus:** Deserters of the Rim is active test colony

## Blockers and Dependencies

### Current Blockers
- None

### External Dependencies
- **RimWorld autosaves:** User has configured extended autosave (18 slots) with event-triggered saves
- **FS MCP access:** Claude needs filesystem access to saves and extracted state

## Notes and Observations

### Recent Insights
- RimAI mod source in `.reference-data/` provides useful reference for what's queryable (WorldDataService, Tooling patterns)
- Save files are 11-29MB depending on colony age/size — streaming/targeted extraction preferred over full DOM load
- Event-triggered saves (BadEvent/GoodEvent) provide excellent snapshots at critical game moments

### Context for Next Session
- Handoff doc at `docs/rimworld-extractor-handoff.md` is ready for KC execution
- Test saves are in `game-saves/deserters-of-the-rim/` — use `Hoeaia.rws` as primary test file
- Extractor script location: `tools/extractor/rimworld_extractor.py` (to be created)
