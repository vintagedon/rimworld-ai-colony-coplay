# RimWorld AI Colony Co-Play Technology Stack

## Technology Stack

### Primary Technologies
- **Python:** 3.10+ — Save file extraction and tooling
- **XML (stdlib):** ElementTree or streaming — Parse RimWorld .rws files
- **JSON:** Output format for extracted state

### Supporting Technologies
- **Markdown:** Human-readable state summaries
- **PowerShell:** Windows automation, file watching (future)
- **C# (Phase 2):** RimWorld mod development

### Future Technologies (Phase 2+)
- **Unity/.NET:** RimWorld modding framework
- **Harmony:** RimWorld mod patching library

## Dependencies

### Required Dependencies
```
# Python stdlib only for Phase 1
# No external packages required initially

# Optional for enhanced functionality:
# watchdog>=3.0.0  # File system monitoring (watcher)
```

### Development Dependencies
```
# None required for basic extraction
# pytest>=7.0.0    # Testing (if added)
# black>=23.0.0    # Formatting (if added)
```

## Development Environment

### Prerequisites
- Python 3.10 or higher
- Access to RimWorld saves directory
- FS MCP configured for Claude Desktop

### Setup Instructions

```powershell
# Navigate to repo
cd D:\development-repositories\rimworld-ai-colony-coplay

# Verify Python version
python --version  # Should be 3.10+

# No virtual environment needed for stdlib-only Phase 1
# If dependencies added later:
# python -m venv .venv
# .venv\Scripts\activate
# pip install -r requirements.txt

# Verify saves access
ls "$env:LOCALAPPDATA\..\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios\Saves"
```

### Environment Variables / Configuration

```powershell
# No environment variables required
# Paths configured via CLI arguments or config file (future)

# RimWorld saves location (default):
# C:\Users\{user}\AppData\LocalLow\Ludeon Studios\RimWorld by Ludeon Studios\Saves\
```

## Infrastructure

### Hosting / Runtime Environment
- **Platform:** Local Windows workstation
- **Resources:** Minimal — Python script runs on-demand
- **Access:** Local filesystem only

### External Services
- **None required for Phase 1**
- Future: May integrate with Claude API for automated advisory (not planned)

## Technical Constraints

### Performance Requirements
- Process 25MB save file in <30 seconds
- Memory usage should not exceed 500MB during extraction
- Graceful handling of malformed/unexpected XML

### Compatibility Requirements
- Windows 10/11 (primary target)
- RimWorld 1.5+ save format
- Handles 300+ mod configurations without crashing

### File Format Constraints
- Input: .rws files (XML with CRLF line endings)
- Output: UTF-8 JSON and Markdown

## Development Workflow

### Version Control
- **Repository:** Local Git, GitHub remote
- **Branching Strategy:** Feature branches for development work
- **Commit Conventions:** Conventional commits (feat:, fix:, docs:, etc.)

### Testing

```powershell
# Manual testing against test saves
python tools/extractor/rimworld_extractor.py ".ai-sandbox/Deserters of the Rim#§#Hoeaia.rws" -o state/snapshots/

# Validate JSON output
python -c "import json; json.load(open('state/snapshots/latest.json'))"
```

### Build and Deployment

```powershell
# No build step for Python
# "Deployment" is just running the script

# Run extraction
python tools/extractor/rimworld_extractor.py <save_file> [-o output_dir]
```

## Automation and Tooling

### Available Scripts
- `tools/extractor/rimworld_extractor.py` — Main extraction script (to be created)
- `shared/generate_tree.py` — Directory tree generation

### Future Automation
- File watcher daemon for automatic extraction
- Batch extraction for historical analysis

### Development Tools
- **VS Code:** Primary editor (workspace settings in `.vscode/`)
- **Claude Desktop:** Advisory interface, FS MCP access
- **KiloCode:** AI coding assistant for development work

## Troubleshooting

### Common Issues

#### Large file memory errors
**Problem:** Python runs out of memory parsing large saves  
**Solution:** Use streaming XML parsing (iterparse) instead of full DOM load

#### Encoding errors
**Problem:** Non-UTF8 characters in save file cause decode errors  
**Solution:** Read with `encoding='utf-8-sig'` or handle errors='replace'

#### Missing data sections
**Problem:** Expected XML structure not found (mod variations)  
**Solution:** Wrap section parsing in try/except, log warnings, continue

### Debug Commands

```powershell
# Check save file size
(Get-Item ".ai-sandbox\Deserters of the Rim#§#Hoeaia.rws").Length / 1MB

# Count lines in save
(Get-Content ".ai-sandbox\Deserters of the Rim#§#Hoeaia.rws" | Measure-Object -Line).Lines

# Quick XML structure peek
Select-String -Path ".ai-sandbox\*.rws" -Pattern "<colonists>" | Select-Object -First 5
```

## Technical Documentation

- **RimWorld Save Format:** Observed structure documented in `docs/rimworld-extractor-handoff.md`
- **RimAI Reference:** `.reference-data/Rimworld_AI_Core-main/docs/` for mod patterns
- **Python XML:** https://docs.python.org/3/library/xml.etree.elementtree.html
