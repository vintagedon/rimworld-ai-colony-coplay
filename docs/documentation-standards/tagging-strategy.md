<!--
---
title: "Tagging Strategy"
description: "Controlled vocabulary for document classification in rimworld-ai-colony-coplay"
author: "VintageDon (https://github.com/vintagedon/)"
date: "2026-03-29"
version: "2.0"
tags:
  - type: guide
  - domain: documentation
related_documents:
  - "[Interior README Template](interior-readme-template.md)"
  - "[General KB Template](general-kb-template.md)"
  - "[Worklog README Template](worklog-readme-template.md)"
---
-->

# Tagging Strategy

## 1. Purpose

Controlled tag vocabulary for the rimworld-ai-colony-coplay repository. Consistent tagging enables human navigation and RAG system retrieval.

---

## 2. Why Controlled Vocabulary

Uncontrolled tagging leads to synonyms fragmenting search, inconsistent granularity, and tag proliferation that reduces signal. A controlled vocabulary defines allowed values upfront, ensuring consistency across contributors and time.

---

## 3. Tag Categories

| Category | Question Answered | Required |
|----------|-------------------|----------|
| `type` | What kind of document is this? | Yes |
| `domain` | What subject area? | Yes |
| `status` | What's the lifecycle state? | Recommended |
| `tech` | What technologies involved? | When applicable |

---

## 4. Domain Tags

| Tag | Use For | Boundary |
|-----|---------|----------|
| `extraction` | Save file parsing, XML traversal, lxml, schema discovery, extractor versions | Getting data out of .rws files, not storing or querying it |
| `state` | Extracted snapshots, JSON/Markdown outputs, colony state representation | The data after extraction, not the extraction process |
| `pawn` | Colonist data: skills, traits, health, needs, relations, genes, psycasts | Individual pawn-level extraction and analysis |
| `colony` | Buildings, zones, research, resources, power, factions, quests, work tab | Colony-level systems and aggregate state |
| `world` | World pawns, settlements, Real Ruins, kidnapped tracking, faction bases | World-level state beyond the player colony |
| `database` | PostgreSQL, pgvector, TimescaleDB, Neo4j, storage architecture | Planned persistent storage layer |
| `integration` | MCP, CrystalDB, Claude Desktop, file watcher, CAG architecture | Connecting extracted state to Claude |
| `mod` | C# mod source, real-time export, in-game hooks | Phase 2 game modification (future) |
| `schema` | Save file XML schema documentation, field discovery | Understanding the .rws structure |
| `documentation` | Templates, standards, meta-content about the repo itself | Docs about docs |

---

## 5. Type Tags

| Tag | Use For |
|-----|---------|
| `project-root` | Repository root README |
| `directory-readme` | Interior README for any directory |
| `worklog` | Work log entries and milestone documentation |
| `guide` | Step-by-step procedures and how-to documents |
| `reference` | Schema docs, field inventories, extraction coverage tables |
| `specification` | Milestone specs, architecture specs |
| `report` | Extraction results, Kaggle dataset documentation |

---

## 6. Status Tags

| Tag | Description |
|-----|-------------|
| `draft` | In development, not yet complete |
| `active` | Current, maintained |
| `under-review` | Review in progress |
| `deprecated` | Superseded, avoid for new work |
| `archived` | Historical reference only |

---

## 7. Tech Tags

| Tag | Technology |
|-----|-----------|
| `python` | Python scripts and modules |
| `lxml` | XML parsing library |
| `xml` | RimWorld save file format |
| `postgresql` | Planned state storage |
| `pgvector` | Planned vector embeddings |
| `timescaledb` | Planned time-series state |
| `neo4j` | Planned social graph storage |
| `csharp` | Phase 2 mod development |
| `powershell` | Windows automation scripts |

---

## 8. Implementation

### Standard Frontmatter

```yaml
<!--
---
title: "Document Title"
description: "What this document covers"
author: "VintageDon (https://github.com/vintagedon/)"
date: "YYYY-MM-DD"
version: "1.0"
status: "Active"
tags:
  - type: reference
  - domain: extraction
  - tech: [python, lxml]
related_documents:
  - "[Related Doc](path/to/doc.md)"
---
-->
```

### Conventions

- Use lowercase, hyphenated values
- Tech tags use canonical names
- One value per line for readability, or array syntax for multi-value
- `related_documents` links use relative paths within the repo

---

## 9. Maintaining the Vocabulary

- This document is the authoritative source for allowed tag values
- Prefer broader tags over proliferating specific ones
- Check for existing coverage before adding new tags
- Backfill existing documents when adding new tags

---

## 10. References

| Resource | Description |
|----------|-------------|
| [Interior README Template](interior-readme-template.md) | Shows tag usage in directory READMEs |
| [General KB Template](general-kb-template.md) | Shows tag usage for standalone docs |
| [Worklog README Template](worklog-readme-template.md) | Shows tag usage for work log entries |
