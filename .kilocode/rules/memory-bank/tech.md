# RimWorld AI Colony Co-Play Technology Stack

## Technology Stack

### Primary Technologies
- **Python 3.10+** — Save file extraction and tooling
- **lxml** — DOM-based XML parsing for schema discovery and extraction
- **JSON** — Output format for extracted state
- **Markdown** — Human-readable state summaries

### Data Infrastructure (Planned)
- **PostgreSQL 16** — Primary data storage on pgsql01
- **pgvector** — Semantic search over colony history
- **TimescaleDB** — Time series extension for trend analysis (mood, resources over time)
- **Neo4j** — Relationship graphs (colonist social networks, faction webs)

### Future Technologies (Phase 2+)
- **C# / Unity** — RimWorld mod development
- **Harmony** — RimWorld mod patching library

## Dependencies

### Required Dependencies
```
lxml>=5.0.0  # DOM-based XML parsing
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
neo4j>=5.0.0      # Neo4j driver
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
python rimworld_extractor_v2.py "..\..\game-saves\the-fringe-benefit\the-fringe-benefit#§#Autosave-129.rws" -o ..\..\state\snapshots\
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
- **Database:** pgsql01 — PostgreSQL with pgvector + TimescaleDB extension
- **Graph DB:** Neo4j for relationship queries
- **MCP:** CrystalDB MCP for Claude queries
- **Watcher:** File system daemon for auto-extraction

## Technical Constraints

### Performance Requirements
- Process 25MB save file in <30 seconds ✅ (actual: ~3 seconds)
- Memory usage should not exceed 500MB during extraction ✅
- Graceful handling of malformed/unexpected XML ✅

### Compatibility Requirements
- Windows 10/11 (primary target)
- RimWorld 1.6+ save format (Odyssey expansion)
- Handles 270+ mod configurations

### File Format Constraints
- Input: .rws files (XML with CRLF line endings)
- Output: UTF-8 JSON and Markdown

## Development Workflow

### Version Control
- **Repository:** GitHub
- **Branching Strategy:** Feature branches
- **Commit Conventions:** Conventional commits (feat:, fix:, docs:, etc.)

### Testing

```powershell
# Run schema discovery (to understand save structure)
cd tools/extractor
python schema_discovery.py "..\..\game-saves\the-fringe-benefit\the-fringe-benefit#§#Autosave-129.rws"

# Run extraction against test save
python rimworld_extractor_v2.py "..\..\game-saves\the-fringe-benefit\the-fringe-benefit#§#Autosave-129.rws" -o ..\..\state\snapshots\

# Check output
Get-Content ..\..\state\snapshots\colony_*.md | Select-Object -First 100
```

### Build and Deployment

```powershell
# No build step for Python
# Run extraction from tools/extractor/
python rimworld_extractor_v2.py <save_file> [-o output_dir] [--json-only] [--md-only]
```

## File Locations

### Scripts
- `tools/extractor/rimworld_extractor_v2.py` — Main extraction script (v2.2, schema-driven)
- `tools/extractor/schema_discovery.py` — XML structure analysis tool
- `tools/extractor/rimworld_extractor.py` — Legacy v1 extractor (reference only)
- `tools/extractor/parsers/` — Legacy modular parsers (reference only)

### Data
- `game-saves/the-fringe-benefit/` — Current colony save files
- `state/snapshots/` — Extracted JSON/Markdown output
- `.internal-files/` — Development artifacts, schema outputs

### Documentation
- `.kilocode/rules/memory-bank/` — Agent context files
- `work-logs/` — Phase completion records
- `docs/documentation-standards/` — Templates

## Troubleshooting

### Common Issues

#### lxml not installed
**Problem:** `ModuleNotFoundError: No module named 'lxml'`  
**Solution:** `pip install lxml`

#### "Unknown" values in output
**Problem:** Faction names, genders, or other fields show as "Unknown"  
**Solution:** Run schema_discovery.py to verify XML paths, update extractor if paths changed

#### Zero colonists extracted
**Problem:** Colonist array is empty despite having colonists in-game  
**Solution:** Player faction detection may have failed — check that `def="PlayerColony"` faction exists and ID prefix handling is correct

#### Work Tab shows Thing_HumanXXXXX
**Problem:** Work Tab priorities use pawn references, not names  
**Solution:** Known limitation — cross-reference resolution planned for future version

### Debug Commands

```powershell
# Check save file size
(Get-Item "game-saves\the-fringe-benefit\*.rws").Length / 1MB

# View extraction output summary
Get-Content state\snapshots\colony_*.json | ConvertFrom-Json | Select-Object -ExpandProperty colonists | Select-Object -ExpandProperty name

# Check faction relations
Get-Content state\snapshots\colony_*.json | ConvertFrom-Json | Select-Object -ExpandProperty factions | Where-Object is_player

# Run schema discovery for debugging
python tools\extractor\schema_discovery.py "game-saves\the-fringe-benefit\*.rws" -d 8
```

## Technical Documentation

- **Schema Discovery Output:** `.internal-files/schema_*.md` — Actual XML structure from saves
- **lxml Docs:** https://lxml.de/parsing.html
- **RimWorld Wiki:** Save file format documentation (1.2-era, mostly still valid)

## Extractor CLI Reference

```
usage: rimworld_extractor_v2.py [-h] [-o OUTPUT] [--json-only] [--md-only] save_file

Extract data from RimWorld save files (v2.2 - schema-driven)

positional arguments:
  save_file             Path to .rws save file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output directory (default: same as save file)
  --json-only           Only output JSON, skip markdown
  --md-only             Only output markdown, skip JSON
```

## Schema Discovery CLI Reference

```
usage: schema_discovery.py [-h] [-o OUTPUT] [-d DEPTH] save_file

Discover XML schema structure from RimWorld save files

positional arguments:
  save_file             Path to .rws save file

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output file (default: schema_{save_name}.md)
  -d DEPTH, --depth DEPTH
                        Maximum depth to traverse (default: unlimited)
```
