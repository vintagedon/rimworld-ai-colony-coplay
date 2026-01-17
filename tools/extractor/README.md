<!--
---
title: "RimWorld Save Extractor"
description: "Parses RimWorld .rws save files into structured JSON and Markdown"
author: "VintageDon"
date: "2026-01-17"
version: "1.0"
status: "Development"
tags:
  - type: directory-readme
  - domain: extraction
  - tech: python
  - tech: xml
---
-->

# RimWorld Save Extractor

Parses RimWorld .rws save files (XML format) into structured JSON for Claude advisory sessions.

---

## 1. Contents

```
extractor/
├── rimworld_extractor.py   # Main entry point
├── parsers/                # Section-specific parsing modules
│   ├── __init__.py
│   ├── colonists.py        # Pawn extraction
│   ├── resources.py        # Inventory/stockpiles
│   ├── factions.py         # Faction relations
│   ├── research.py         # Research progress
│   ├── world.py            # Map and environment
│   └── ...
└── README.md               # This file
```

---

## 2. Usage

```powershell
# Basic extraction
python rimworld_extractor.py "path/to/save.rws"

# Specify output directory
python rimworld_extractor.py "path/to/save.rws" -o ../../state/snapshots/

# Output formats (future)
python rimworld_extractor.py "path/to/save.rws" --format json
python rimworld_extractor.py "path/to/save.rws" --format markdown
python rimworld_extractor.py "path/to/save.rws" --format both
```

---

## 3. Output

### JSON Structure

```json
{
  "metadata": {
    "extracted_at": "2026-01-17T15:30:00Z",
    "save_file": "Colony.rws",
    "game_version": "1.5.xxxx",
    "mod_count": 312
  },
  "colonists": [...],
  "resources": {...},
  "research": {...},
  "factions": [...],
  "buildings": [...],
  "zones": [...],
  "environment": {...},
  "events": [...]
}
```

### Extraction Categories

| Category | Key Data Points |
|----------|-----------------|
| Colonists | Skills, traits, health, mood, needs, relationships, genes |
| Resources | Item counts, storage zones, nutrition levels |
| Research | Completed, current, available projects |
| Factions | Names, goodwill, recent interactions |
| Buildings | Structures, power grid, defenses |
| Zones | Stockpiles, growing zones, allowed areas |
| Environment | Weather, temperature, season, biome |
| Events | Recent incidents, scheduled events |

---

## 4. Development

### Adding a New Parser

1. Create `parsers/{section}_parser.py`
2. Implement extraction function following existing patterns
3. Register in `parsers/__init__.py`
4. Add integration in main extractor
5. Test against sample saves in `.ai-sandbox/`

### Testing

```powershell
# Test against sample save
python rimworld_extractor.py "../../game-saves/deserters-of-the-rim/Deserters of the Rim#§#Hoeaia.rws" -o ../../state/snapshots/

# Validate JSON output
python -c "import json; print(json.load(open('../../state/snapshots/latest.json'))['metadata'])"
```

---

## 5. Technical Notes

### Memory Efficiency

Save files can be 20-30MB. Use streaming XML parsing (`iterparse`) rather than loading the full DOM:

```python
for event, elem in ET.iterparse(save_file, events=('end',)):
    if elem.tag == 'colonist':
        process_colonist(elem)
        elem.clear()  # Free memory
```

### Mod Compatibility

Heavily modded saves contain unpredictable XML structures. Parsers should:
- Wrap section parsing in try/except
- Log warnings for missing expected elements
- Continue extraction even if one section fails
- Never crash on unknown mod data

---

## 6. Related

| Document | Relationship |
|----------|--------------|
| [tools/](../README.md) | Parent directory |
| [Extractor Handoff](../../docs/rimworld-extractor-handoff.md) | Full specification and requirements |
| [state/snapshots/](../../state/README.md) | Output destination |
| [game-saves/](../../game-saves/) | Colony save files |
