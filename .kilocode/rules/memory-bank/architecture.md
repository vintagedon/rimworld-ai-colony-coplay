# RimWorld AI Colony Co-Play Architecture

## Overview

RimWorld AI Colony Co-Play is architected as a Context Augmented Generation (CAG) system where Claude provides gameplay advice based on actual extracted game state, not generic knowledge. The architecture separates concerns into three layers: data extraction (Python/lxml tooling), state storage (PostgreSQL with pgvector), and advisory interface (Claude via database MCP).

The system follows a pull-based model where extraction runs on-demand or triggered by file changes, producing point-in-time snapshots stored in PostgreSQL. Claude queries this database during conversations, enabling stateful advisory grounded in real colony data.

## Core Components

### Save Extractor
**Purpose:** Parse RimWorld .rws XML save files into structured JSON  
**Location:** `tools/extractor/`  
**Status:** ✅ Implemented  
**Key Characteristics:** 
- lxml iterparse for memory-efficient streaming
- Modular parsers for meta, factions, colonists
- Handles 267+ mod configurations
- ~2 second extraction for 22MB files

### State Storage
**Purpose:** Store extracted snapshots and enable historical queries  
**Current:** `state/snapshots/` (JSON/Markdown files)  
**Planned:** PostgreSQL on pgsql01 (10.25.20.8) with pgvector  
**Key Characteristics:** Timestamped snapshots, semantic search via embeddings, trend analysis

### File Watcher (Planned)
**Purpose:** Automatically trigger extraction on autosave file changes  
**Location:** `tools/watcher/`  
**Key Characteristics:** Monitors RimWorld saves directory, debounces rapid changes, invokes extractor, writes to PostgreSQL

### MCP Integration (Planned)
**Purpose:** Enable Claude to query colony data directly  
**Component:** CrystalDB MCP connected to pgsql01  
**Key Characteristics:** SQL queries over snapshots, colonists, resources, factions

## Structure

```
rimworld-ai-colony-coplay/
├── .internal-files/          # Development artifacts (gitignored)
│   ├── rimworld-1_6-save-file-xml.md  # GDR research report
│   └── rimworld-extractor-handoff.md  # Original spec
│
├── .kilocode/rules/memory-bank/  # Agent context
│
├── tools/                    # Python tooling
│   ├── extractor/            # Save file parser ✅
│   │   ├── rimworld_extractor.py
│   │   ├── parsers/
│   │   │   ├── __init__.py
│   │   │   ├── meta.py
│   │   │   └── factions.py
│   │   └── README.md
│   ├── watcher/              # File watcher (planned)
│   └── README.md
│
├── state/                    # Extracted game state (gitignored)
│   ├── snapshots/            # JSON/Markdown extracts
│   └── README.md
│
├── game-saves/               # Colony saves (gitignored)
│   └── deserters-of-the-rim/ # Test colony
│
├── docs/                     # Documentation
│   ├── documentation-standards/
│   └── data-science-infrastructure.md
│
└── work-logs/                # Milestone worklogs
```

## CAG Data Flow

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│ RimWorld        │     │ pgsql01          │     │ Claude          │
│ (autosaves)     │     │ 10.25.20.8       │     │                 │
│                 │────▶│ ┌──────────────┐ │◀────│ CrystalDB MCP   │
│ Saves folder    │     │ │ rimworld_db  │ │     │                 │
│ watched by      │     │ │ + pgvector   │ │     │ "How's morale   │
│ Python daemon   │     │ └──────────────┘ │     │  trending?"     │
└─────────────────┘     └──────────────────┘     └─────────────────┘
        │                        ▲
        │                        │
        └────────────────────────┘
              Extractor writes
              to database
```

## Current Data Flow (Phase 1)

```
RimWorld Autosave (.rws)
        │
        ▼
   [Extractor]  ←── Manual CLI
        │
        ├──► state/snapshots/colony_{timestamp}.json
        └──► state/snapshots/colony_{timestamp}.md
                    │
                    ▼
              [Claude FS MCP]
                    │
                    ▼
             Advisory Conversation
```

## Database Schema (Planned)

```sql
-- Core snapshot tracking
snapshots (
  id SERIAL PRIMARY KEY,
  extracted_at TIMESTAMP,
  game_ticks BIGINT,
  game_year INT,
  game_day INT,
  quadrum VARCHAR(20),
  colony_name VARCHAR(100)
)

-- Colonist state per snapshot
colonists (
  id SERIAL PRIMARY KEY,
  snapshot_id INT REFERENCES snapshots(id),
  pawn_id VARCHAR(50),
  name VARCHAR(100),
  mood FLOAT,
  age FLOAT
)

-- Skills per colonist
skills (
  id SERIAL PRIMARY KEY,
  colonist_id INT REFERENCES colonists(id),
  skill_def VARCHAR(50),
  level INT,
  passion VARCHAR(20)
)

-- Resources per snapshot
resources (
  id SERIAL PRIMARY KEY,
  snapshot_id INT REFERENCES snapshots(id),
  item_def VARCHAR(100),
  category VARCHAR(50),
  count INT
)

-- Faction relations per snapshot
faction_relations (
  id SERIAL PRIMARY KEY,
  snapshot_id INT REFERENCES snapshots(id),
  faction_name VARCHAR(100),
  faction_def VARCHAR(100),
  goodwill INT,
  relation_kind VARCHAR(20)
)
```

## Architectural Decisions

### AD-001: External System vs. Game Mod
**Date:** 2026-01-17  
**Decision:** Phase 1 operates entirely outside the game, reading autosaves  
**Rationale:** Faster to implement, no mod development required, zero game impact  
**Status:** Implemented ✅

### AD-002: lxml for Extraction
**Date:** 2026-01-18  
**Decision:** Use lxml iterparse for streaming XML parsing  
**Rationale:** Memory-efficient for 22MB files, ~2 second extraction  
**Status:** Implemented ✅

### AD-003: PostgreSQL over Local Storage
**Date:** 2026-01-18  
**Decision:** Use pgsql01 cluster database instead of local SQLite/JSON  
**Rationale:** Existing infrastructure, pgvector for semantic search, proper backups  
**Status:** Planned

### AD-004: CAG over RAG
**Date:** 2026-01-18  
**Decision:** Context Augmented Generation using live game data, not document retrieval  
**Rationale:** Real colony state enables specific advice, not generic RimWorld knowledge  
**Status:** Architecture defined

## Extraction Capabilities

| Category | Status | Notes |
|----------|--------|-------|
| Meta (version, mods) | ✅ | 267 mods |
| Game Time | ✅ | Year, day, quadrum |
| World Info | ✅ | Name, seed |
| Factions | ✅ | 20 with LoadID resolution |
| Relations | ✅ | Goodwill integers |
| Colonists | ✅ | 11 with skills, traits |
| Animals | ✅ | 34 |
| Resources | ✅ | 65 item types |
| Research | ✅ | 310 completed |
| Storyteller | ⚠️ | Needs deeper XML path |
| Buildings | 🔲 | Planned |
| Zones | 🔲 | Planned |

## Constraints and Limitations

- **Save-time granularity:** Only captures state when RimWorld writes autosave
- **No write capability (Phase 1):** Cannot modify game state, advisory only
- **Gender extraction:** Modded saves store gender in genes/body type
- **Compressed world data:** `*Deflate` tags not parsed (not needed for advisor)

## Future Considerations

### Planned Improvements
- PostgreSQL storage with pgvector
- File watcher for automatic extraction
- CrystalDB MCP for Claude queries
- InfluxDB for time series trends
- Progress Renderer correlation

### Scalability Considerations
- May need incremental parsing if saves grow larger
- Historical storage may require pruning policy
- Consider event-triggered saves for higher resolution

### Technical Debt
- Storyteller/difficulty extraction incomplete
- Gender extraction fails on modded pawns
