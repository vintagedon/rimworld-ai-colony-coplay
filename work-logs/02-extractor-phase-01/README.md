<!--
---
title: "M02: Extractor Phase 1 — Foundation"
description: "lxml streaming architecture, faction relations, meta/colonist/resource extraction"
author: "VintageDon"
date: "2026-01-18"
version: "1.0"
status: "Complete"
tags:
  - type: worklog
  - domain: data-extraction
  - tech: [python, lxml, xml-parsing]
related_documents:
  - "[Previous Phase](../01-ideation-and-setup/README.md)"
  - "[GDR Report](../../.internal-files/rimworld-1_6-save-file-xml.md)"
---
-->

# M02: Extractor Phase 1 — Foundation

## Summary

| Attribute | Value |
|-----------|-------|
| Status | ✅ Complete |
| Sessions | 1 |
| Artifacts | 1 GDR report, 4 Python files, 2 output formats |

**Objective:** Build a working RimWorld save file extractor using lxml streaming, fix broken faction relations, and extract core game state data.

**Outcome:** Functional extractor producing JSON + Markdown reports with colonists, factions, resources, research, animals, and game time from 22MB modded save files.

---

## 1. Contents

```
02-extractor-phase-01/
└── README.md               # This file
```

**Related Files:**
```
tools/extractor/
├── rimworld_extractor.py   # Main extractor script
├── parsers/
│   ├── __init__.py
│   ├── meta.py             # Game version, mods, world info
│   └── factions.py         # Faction extraction with LoadID resolution
└── README.md

.internal-files/
├── rimworld-1_6-save-file-xml.md    # GDR research report
├── rimworld-extractor-handoff.md    # Original KC prompt (outdated)
└── rimworld_extractor.py            # Original MVP (superseded)
```

---

## 2. Work Completed

| Task | Description | Result |
|------|-------------|--------|
| GDR Research | RimWorld 1.6 XML structure analysis via Gemini Deep Research | ✅ Comprehensive report |
| Version Discovery | Identified save as 1.6.4633 (Odyssey), not 1.5 as assumed | ✅ Corrected assumptions |
| lxml Architecture | Streaming iterparse for memory-efficient 22MB file processing | ✅ Working |
| Meta Extraction | Game version, 267 mods, storyteller, difficulty | ✅ Working |
| Faction Extraction | 20 factions with LoadID resolution | ✅ Working |
| Relations Extraction | Goodwill values and relation kinds populated | ✅ Working |
| Colonist Extraction | 11 colony members with skills, traits, needs | ✅ Working |
| Resource Extraction | 65 item types categorized | ✅ Working |
| Research Extraction | 310 completed projects, current project | ✅ Working |
| Animal Extraction | 34 colony animals | ✅ Working |
| Game Time | Year 5501, Day 113, Quadrum, Season | ✅ Working |
| World Info | Colony name (Algenib), seed (intestines) | ✅ Working |

---

## 3. Extraction Results

Final extraction from `Deserters of the Rim#§#Hoeaia.rws`:

| Component | Count/Value |
|-----------|-------------|
| Game Version | 1.6.4633 rev1261 |
| Mods | 267 |
| Factions | 20 |
| Player Relations | 20 (with goodwill integers) |
| Colonists | 11 |
| Animals | 34 |
| Resource Types | 65 |
| Completed Research | 310 |
| Current Research | OrbitalTech |

---

## 4. Issues Encountered

| Issue | Resolution |
|-------|------------|
| Faction relations empty | XML structure changed in 1.6 — `<relations>` not `<relationSettings>` |
| Faction ID format mismatch | Pawns use `Faction_19`, index used `19` — added `Faction_` prefix |
| Relations extraction disabled | Code was commented out — restored |
| iterparse clearing children | Elements cleared before children read — extract before clear |
| Wrong element tag | RimWorld uses `<thing Class="Pawn">` not `<li Class="Pawn">` |
| World pawns captured | Missing `in_things`/`in_maps` guards — added section tracking |
| Gender showing Unknown | Modded saves store gender in genes/body type, not direct element |

---

## 5. Agent Collaboration

| Agent | Role | Contribution |
|-------|------|--------------|
| GDR (Gemini) | Research | RimWorld 1.6 XML structure documentation |
| KiloCode/GLM | Implementation | Initial lxml architecture, parser modules |
| Codex | Bug fix | Faction ID alias fix |
| Claude Code | Bug fix | Section guards, iterparse pattern fixes |
| Claude (Opus) | Orchestration | Diagnosis, prompt crafting, review |

---

## 6. Known Limitations

| Limitation | Notes |
|------------|-------|
| Storyteller/Difficulty | Not extracted — nested deeper in save structure |
| Gender for humans | Returns "Unknown" — stored in genes/body type in modded saves |
| Compressed world data | `*Deflate` tags not parsed — out of scope for advisor use case |
| PawnRenderTree | Visual-only data ignored — not needed for gameplay advice |

---

## 7. Next Phase

**Handoff:** Extractor produces valid JSON/Markdown output. Ready for database schema design and watcher daemon.

**Next Steps:**

1. **Schema Design** — PostgreSQL tables for snapshots, colonists, skills, resources, factions
2. **Database Setup** — Create `rimworld_coplay` database on pgsql01
3. **Watcher Daemon** — File watcher to auto-extract on new saves
4. **MCP Integration** — CrystalDB MCP for Claude queries

**Deferred:**
- Storyteller/difficulty extraction
- Gender extraction for modded saves
- Needs data extraction refinement
