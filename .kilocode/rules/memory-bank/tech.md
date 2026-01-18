# RimWorld AI Colony Co-Play Technology Stack

## Technology Stack

### Primary Technologies
- **Python 3.10+** — Save file extraction and tooling
- **lxml** — Streaming XML parsing via iterparse for memory efficiency
- **JSON** — Output format for extracted state
- **Markdown** — Human-readable state summaries

### Data Infrastructure (Planned)
- **PostgreSQL 16** — Primary data storage on pgsql01 (10.25.20.8)
- **pgvector** — Semantic search over colony history
- **InfluxDB** — Time series for trend analysis (optional)
- **Neo4j** — Relationship graphs (optional)

### Future Technologies (Phase 2+)
- **C# / Unity** — RimWorld mod development
- **Harmony** — RimWorld mod patching library

## Dependencies

### Required Dependencies
```
lxml>=5.0.0  # Streaming XML parsing
```

### Development Dependencies
```
# None required for basic extraction
# pytest>=7.0.0    # Testing (if added)
```

### Future Dependencies
```
psycopg2>=2.9.0   # PostgreSQL connection
watchdog>=3.0.0   # File system monitoring
```

## Development Environment

### Prerequisites
- Python 3.10 or higher
- lxml installed (`pip install lxml`)
- Access to RimWorld saves directory
- FS MCP configured for Claude Desktop

### Setup Instructions

```powershell
# Navigate to repo
cd D:\development-repositories\rimworld-ai-colony-coplay

# Verify Python version
python --version  # Should be 3.10+

# Install dependencies
pip install lxml

# Run extractor
cd tools/extractor
python rimworld_extractor.py "..\..\game-saves\deserters-of-the-rim\Deserters of the Rim#§#Hoeaia.rws" -o ..\..\state\snapshots\
```

### Environment Variables / Configuration

```powershell
# No environment variables required for extraction
# Database credentials will come from /opt/global-env/research.env on cluster

# RimWorld saves location (default):
# C:\Users\{user}\AppData\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios\Saves\
```

## Infrastructure

### Current (Phase 1)
- **Platform:** Local Windows workstation
- **Resources:** Minimal — Python script runs on-demand
- **Output:** JSON/Markdown files in `state/snapshots/`

### Planned (Phase 1b+)
- **Database:** pgsql01 (10.25.20.8) — PostgreSQL with pgvector
- **MCP:** CrystalDB MCP for Claude queries
- **Watcher:** File system daemon for auto-extraction

## Technical Constraints

### Performance Requirements
- Process 25MB save file in <30 seconds ✅ (actual: ~2 seconds)
- Memory usage should not exceed 500MB during extraction ✅
- Graceful handling of malformed/unexpected XML ✅

### Compatibility Requirements
- Windows 10/11 (primary target)
- RimWorld 1.6+ save format (Odyssey expansion)
- Handles 267+ mod configurations

### File Format Constraints
- Input: .rws files (XML with CRLF line endings)
- Output: UTF-8 JSON and Markdown

## Development Workflow

### Version Control
- **Repository:** GitHub
- **Branching Strategy:** Feature branches (`feature/extractor-phase1-foundation`)
- **Commit Conventions:** Conventional commits (feat:, fix:, docs:, etc.)

### Testing

```powershell
# Run extraction against test save
cd tools/extractor
python rimworld_extractor.py "..\..\game-saves\deserters-of-the-rim\Deserters of the Rim#§#Hoeaia.rws" -o ..\..\state\snapshots\

# Check output
Get-Content ..\..\state\snapshots\colony_*.md | Select-Object -First 50
```

### Build and Deployment

```powershell
# No build step for Python
# Run extraction from tools/extractor/
python rimworld_extractor.py <save_file> [-o output_dir]
```

## File Locations

### Scripts
- `tools/extractor/rimworld_extractor.py` — Main extraction script
- `tools/extractor/parsers/meta.py` — Game/world info extraction
- `tools/extractor/parsers/factions.py` — Faction/relations extraction

### Data
- `game-saves/deserters-of-the-rim/` — Colony save files
- `state/snapshots/` — Extracted JSON/Markdown output
- `.internal-files/` — Development artifacts, GDR report

### Documentation
- `.kilocode/rules/memory-bank/` — Agent context files
- `work-logs/` — Phase completion records
- `docs/documentation-standards/` — Templates

## Troubleshooting

### Common Issues

#### lxml not installed
**Problem:** `ModuleNotFoundError: No module named 'lxml'`  
**Solution:** `pip install lxml`

#### Wrong element cleared
**Problem:** Data returns None/empty despite existing in XML  
**Solution:** Extract children before calling `elem.clear()` on parent

#### Wrong pawns extracted
**Problem:** World pawns captured instead of colonists  
**Solution:** Add `in_things`/`in_maps` section guards

### Debug Commands

```powershell
# Check save file size
(Get-Item "game-saves\deserters-of-the-rim\*.rws").Length / 1MB

# View extraction output
Get-Content state\snapshots\colony_*.json | ConvertFrom-Json | Select-Object -ExpandProperty colonists

# Check faction relations
Get-Content state\snapshots\colony_*.json | ConvertFrom-Json | Select-Object -ExpandProperty factions | Where-Object is_player
```

## Technical Documentation

- **GDR Report:** `.internal-files/rimworld-1_6-save-file-xml.md` — RimWorld 1.6 XML structure
- **Handoff Doc:** `.internal-files/rimworld-extractor-handoff.md` — Original spec (partially outdated)
- **lxml Docs:** https://lxml.de/parsing.html#iterparse-and-iterwalk
