# AGENTS.md

Entry point for AI coding agents working on this repository.

## Project Identity

**Domain:** Gaming / AI Integration / Save File Analysis
**Repository:** https://github.com/radioastronomyio/rimworld-ai-colony-coplay
**Purpose:** External AI advisor for RimWorld colony management via save file analysis. Claude reads autosave files, extracts colony state into structured data, maintains historical context, and provides strategic guidance through natural conversation. No game modification required.

**Status:** v2.3, M04 complete. Extractor handles 18MB+ modded save files in ~3 seconds with comprehensive extraction across colony state, pawn psychology, genetics, social graphs, and world population.

## Current State

**Phase:** M04 (Extractor Phase 3) complete. M05 (Database Storage) next.
**Date:** March 2026

### Completed Milestones

| Milestone | Delivered |
|-----------|----------|
| M01: Ideation & Setup | Repository scaffolding, documentation |
| M02: Extractor Phase 1 | Schema discovery, base extractor (v2.0) |
| M03: Extractor Phase 2 | Full extraction suite, Work Tab, dual-audience comments (v2.2) |
| M04: Extractor Phase 3 | Kaggle expansion: deep pawn, world state, containers (v2.3) |

### What's Next

| Milestone | Description |
|-----------|-------------|
| M05 | PostgreSQL with pgvector + TimescaleDB for state storage |
| M06 | File watcher for auto-extraction on new saves |
| M07 | CrystalDB MCP for Claude queries |
| Phase 2 | C# mod for real-time state export |

### Current Extraction Coverage

The extractor handles: meta/version/mods, game time, storyteller/difficulty, factions with bidirectional goodwill, 1000+ categorized buildings, zones, 45+ research projects, recursive container scanning for resources, quests, 441 world objects, Work Tab (225 workgivers/pawn), power network, play/battle logs, tales, and full pawn extraction (identity, skills, traits, health, needs, relations, apparel, weapons, immunity, memories, opinions, genes, psycasts). World state covers 357+ NPCs, kidnapped tracking, settlements, and Real Ruins POIs.

## Architecture

Read-only external observer, progressing toward Context Augmented Generation (CAG).

```
RimWorld Autosave (.rws)
    → Python Extractor (lxml, ~3s)
        → JSON/Markdown State Snapshots
            → [Planned] PostgreSQL + pgvector + TimescaleDB
                → [Planned] CrystalDB MCP → Claude
```

### Components

| Component | Technology | Status |
|-----------|------------|--------|
| Schema Discovery | Python / lxml | ✅ Working |
| Save Extractor v2.3 | Python / lxml | ✅ Working |
| State Storage | JSON/Markdown snapshots | ✅ Working |
| Database | PostgreSQL + pgvector + TimescaleDB | ⬜ Planned |
| Graph Database | Neo4j | ⬜ Planned |
| File Watcher | Python watchdog | ⬜ Planned |
| Claude Integration | CrystalDB MCP | ⬜ Planned |

## Key Constraints

- **Read-only.** The system never modifies game files; save files are parsed, not written.
- **External observer.** No in-game mod required for current functionality (Phase 2 adds optional C# mod).
- **Modded save support.** Must handle 270+ mod save files without breaking.
- **Extraction speed.** 18MB+ saves must extract in under 5 seconds.
- **State snapshots preserve history.** Timestamped outputs enable trend analysis across play sessions.

## Execution Environment

**Primary execution:** ML01 (`/opt/repos/rimworld-ai-colony-coplay/`)
**Agent runtime:** OpenCode (global config at `~/.config/opencode/opencode.json`)
**Session management:** aoe (Agent of Empires)
**Strategic work:** Claude.ai Projects
**Agentic coding:** Claude Code, OpenCode

## Repository Structure

```
rimworld-ai-colony-coplay/
├── assets/                         # Project images, diagrams
├── docs/
│   ├── documentation-standards/    # Templates, tagging strategy
│   ├── rimworld-save-schema-kb.md  # Schema documentation
│   └── schema_*.md                 # Schema discovery outputs
├── game-saves/                     # Colony save files
│   └── the-fringe-benefit/         # Current test colony (public)
├── internal-files/                 # Working documents
├── mod/                            # C# mod source (Phase 2+)
├── shared/                         # Cross-project utilities
├── spec/                           # Specifications
├── staging/                        # Staged work (gitignored)
├── state/                          # Extracted game state
│   └── snapshots/                  # JSON/Markdown output
├── tools/
│   ├── extractor/                  # Save file parser (v2.3)
│   └── watcher/                    # File watcher (planned)
├── work-logs/                      # Development milestones
├── AGENTS.md                       # This file
├── CLAUDE.md                       # Pointer to AGENTS.md
├── LICENSE                         # MIT
└── README.md
```

## Conventions

- **Documentation:** Use templates from `docs/documentation-standards/`
- **Commits:** Conventional commits (`feat:`, `fix:`, `docs:`)
- **Code comments:** Dual-audience style (human + AI agent)
- **Frontmatter:** YAML frontmatter with tags from `docs/documentation-standards/tagging-strategy.md`
- **Interior READMEs:** Every directory has one

## Related Repositories

| Repository | Relationship |
|-----------|-------------|
| `proxmox-astronomy-lab` | Infrastructure (PostgreSQL, Neo4j planned for state storage) |
