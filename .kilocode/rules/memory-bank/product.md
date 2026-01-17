# RimWorld AI Colony Co-Play Product Overview

## Problems Solved

This project addresses:

- **No external AI advisor for RimWorld:** Existing AI mods (RimAI Framework/Core) add in-game UI elements and terminals. There's no solution for using Claude Desktop as an external companion that reads game state without modifying the game experience.

- **Loss of context across play sessions:** RimWorld colonies develop over many real-world hours. Without persistent tracking, an AI advisor cannot reference colony history, identify trends, or understand the narrative arc of a playthrough.

- **Information overload in complex colonies:** Heavily modded RimWorld with 10+ colonists generates enormous amounts of data. Players miss critical issues (colonist mood spirals, resource depletion trends, skill gaps) buried in the complexity.

- **Manual state explanation:** Without automated extraction, getting AI advice requires manually describing colony state — tedious and incomplete.

## How It Works

The system operates in a read-only capacity during Phase 1, extracting game state from RimWorld's autosave files (.rws XML format) and transforming it into structured data Claude can analyze.

A Python extractor parses save files on demand or via file watcher, pulling colonist details (skills, mood, health, relationships), resources, research progress, faction relations, and environmental state. This data is output as JSON for programmatic access and Markdown for human readability.

Claude accesses extracted state via filesystem MCP during conversations, enabling queries like "how is Viktor's mood trending?" or "are we at risk of food shortage?" with answers grounded in actual game data rather than speculation.

Key components:
- **Save Extractor:** Python script parsing .rws XML files into structured JSON
- **State Storage:** Timestamped snapshots enabling historical analysis
- **Claude Integration:** FS MCP access to extracted state during advisory conversations

## Goals and Outcomes

### Primary Goals
1. **Complete state extraction:** Parse all meaningful data from heavily modded saves (colonists, resources, research, factions, buildings, zones)
2. **Historical tracking:** Maintain timestamped snapshots enabling trend analysis and change detection
3. **Efficient processing:** Handle 20-30MB save files in under 30 seconds without memory issues

### User Experience Goals
- Ask Claude about colony state and receive accurate, data-backed answers
- Identify risks and optimization opportunities through trend analysis
- Maintain narrative continuity across play sessions with persistent colony memory

### Success Metrics
- **Extraction completeness:** All 13 deliverable categories from handoff spec validated
- **Performance:** Sub-30-second extraction for 25MB saves
- **Accuracy:** Extracted data matches in-game values when spot-checked

## Phased Roadmap

| Phase | Focus | Status |
|-------|-------|--------|
| P1 | Save file extraction + Claude advisory | Active |
| P2 | Lightweight export mod (real-time state) | Future |
| P3 | Limited game interaction (draft orders, priorities) | Future |
