# RimWorld AI Colony Co-Play Architecture

## Overview

RimWorld AI Colony Co-Play is architected as a loosely-coupled external system that reads RimWorld game state without modifying the game. The architecture separates concerns into three layers: data extraction (Python tooling), state storage (JSON snapshots), and advisory interface (Claude via FS MCP).

The system follows a pull-based model where extraction runs on-demand or triggered by file changes, producing point-in-time snapshots. Claude reads these snapshots during conversations, enabling stateful advisory without persistent server processes or game modifications.

## Core Components

### Save Extractor
**Purpose:** Parse RimWorld .rws XML save files into structured JSON  
**Location:** `tools/extractor/`  
**Key Characteristics:** Streaming XML parsing for memory efficiency, modular parsers for different data sections, handles 300+ mod configurations gracefully

### State Storage
**Purpose:** Store extracted snapshots and historical data  
**Location:** `state/`  
**Key Characteristics:** Timestamped JSON snapshots, Markdown summaries for human review, historical diffs for trend analysis (future)

### File Watcher (Future)
**Purpose:** Automatically trigger extraction on autosave file changes  
**Location:** `tools/watcher/`  
**Key Characteristics:** Monitors RimWorld saves directory, debounces rapid changes, invokes extractor

### Export Mod (Phase 2)
**Purpose:** Real-time state export from running game  
**Location:** `mod/`  
**Key Characteristics:** C# RimWorld mod, writes JSON on configurable tick intervals, no UI additions

## Structure

```
rimworld-ai-colony-coplay/
├── .ai-sandbox/              # Test saves, experiments (gitignored)
├── .reference-data/          # RimAI mod source for reference (gitignored)
├── .kilocode/rules/memory-bank/  # Agent context
│
├── tools/                    # Python tooling
│   ├── extractor/            # Save file parser
│   │   ├── rimworld_extractor.py
│   │   ├── parsers/          # Section-specific parsers
│   │   └── README.md
│   ├── watcher/              # File watcher (future)
│   └── README.md
│
├── state/                    # Extracted game state (gitignored)
│   ├── snapshots/            # Point-in-time JSON extracts
│   ├── history/              # Historical diffs/trends
│   └── README.md
│
├── mod/                      # C# mod source (Phase 2+)
│   └── README.md
│
├── docs/                     # Documentation
│   ├── documentation-standards/
│   └── rimworld-extractor-handoff.md
│
└── work-logs/                # Milestone worklogs
```

## Design Patterns and Principles

### Key Patterns

- **Streaming extraction:** Process large XML files without loading full DOM into memory
- **Modular parsers:** Separate parser modules for colonists, resources, factions, etc. — enables incremental development and testing
- **Snapshot-based state:** Point-in-time captures rather than live state — simpler, works with autosaves

### Design Principles

1. **No game modification (Phase 1):** Read-only external system, zero impact on game experience
2. **Graceful degradation:** Unknown mod data logged but doesn't crash extraction
3. **Efficient for large files:** 20-30MB saves must process in reasonable time (<30s)
4. **Human-readable output:** Markdown summaries alongside JSON for quick review

## Integration Points

### Internal Integrations
- **Extractor → State:** Extractor writes JSON/MD to `state/snapshots/`
- **Watcher → Extractor:** Watcher invokes extractor on file change detection

### External Integrations
- **RimWorld Saves:** Reads from `%LOCALAPPDATA%Low\Ludeon Studios\RimWorld by Ludeon Studios\Saves\`
- **Claude FS MCP:** Claude reads extracted state via filesystem access
- **Future: RimAI patterns:** May reference RimAI's WorldDataService patterns for mod development

## Data Flow

```
RimWorld Autosave (.rws)
        │
        ▼
   [Extractor]  ←── Manual CLI or Watcher trigger
        │
        ├──► state/snapshots/{timestamp}.json
        └──► state/snapshots/{timestamp}.md
                    │
                    ▼
              [Claude FS MCP]
                    │
                    ▼
             Advisory Conversation
```

## Architectural Decisions

### AD-001: External System vs. Game Mod
**Date:** 2026-01-17  
**Decision:** Phase 1 operates entirely outside the game, reading autosaves  
**Rationale:** Faster to implement, no mod development required, zero game impact, works with any mod configuration  
**Alternatives Considered:** Fork RimAI to add export-only mode — rejected due to complexity and maintenance burden  
**Implications:** Limited to save-time granularity, no real-time state

### AD-002: Python for Extraction
**Date:** 2026-01-17  
**Decision:** Use Python 3.10+ with stdlib XML parsing  
**Rationale:** Rapid development, good XML support, no compilation needed, easy to iterate  
**Alternatives Considered:** C# (consistency with eventual mod) — rejected for Phase 1 speed  
**Implications:** Extraction tooling separate from eventual mod codebase

### AD-003: Snapshot-Based State
**Date:** 2026-01-17  
**Decision:** Store point-in-time snapshots rather than maintain live state database  
**Rationale:** Simpler architecture, aligns with autosave cadence, no persistent daemon required  
**Alternatives Considered:** SQLite database with incremental updates — deferred to future if needed  
**Implications:** Each snapshot is self-contained, history via multiple snapshots

## Constraints and Limitations

- **Save-time granularity:** Only captures state when RimWorld writes autosave (1-5 min intervals)
- **No write capability (Phase 1):** Cannot modify game state, advisory only
- **Large file handling:** Must efficiently process 20-30MB XML without excessive memory
- **Mod variability:** 300+ mods means unpredictable XML structure variations

## Future Considerations

### Planned Improvements
- File watcher for automatic extraction
- Historical diff generation between snapshots
- Phase 2 export mod for real-time state

### Scalability Considerations
- May need incremental parsing if saves grow larger
- Historical storage may require pruning policy

### Known Technical Debt
- None yet (greenfield)
