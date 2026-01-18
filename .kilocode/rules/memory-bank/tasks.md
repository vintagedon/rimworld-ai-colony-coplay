# RimWorld AI Colony Co-Play Tasks and Workflows

## Common Workflows

### Extraction: Manual Save Processing

**When to use:** When you want to extract current colony state for Claude advisory  
**Frequency:** On-demand, typically before advisory sessions

**Steps:**
1. Ensure RimWorld has autosaved recently (or manual save)
2. Navigate to extractor directory
3. Run extractor against target save file
4. Verify JSON output is valid
5. Review Markdown summary for obvious issues

**Commands:**
```powershell
cd D:\development-repositories\rimworld-ai-colony-coplay\tools\extractor
python rimworld_extractor_v2.py "..\..\game-saves\the-fringe-benefit\the-fringe-benefit#§#Autosave-129.rws" -o ..\..\state\snapshots\
```

**Expected Outcome:** JSON and MD files in `state/snapshots/` with current timestamp  
**Expected Output:** ~7 colonists, ~20 factions, ~1000 buildings, ~45 research projects

---

### Schema Discovery: Analyzing Save Structure

**When to use:** When extraction returns unexpected results or after RimWorld updates  
**Frequency:** As needed for debugging or path verification

**Steps:**
1. Run schema discovery against a save file
2. Review output for path structure
3. Compare against extractor assumptions
4. Update extractor paths if needed

**Commands:**
```powershell
cd D:\development-repositories\rimworld-ai-colony-coplay\tools\extractor

# Full depth discovery (large output)
python schema_discovery.py "..\..\game-saves\the-fringe-benefit\the-fringe-benefit#§#Autosave-129.rws"

# Limited depth for overview
python schema_discovery.py "..\..\game-saves\the-fringe-benefit\the-fringe-benefit#§#Autosave-129.rws" -d 6
```

**Expected Outcome:** Markdown file with full XML tree structure, depths, sample values

---

### Advisory Session: Colony Review with Claude

**When to use:** When playing RimWorld and wanting strategic advice  
**Frequency:** During or after play sessions

**Steps:**
1. Run extraction on latest autosave
2. Start Claude conversation in this project context
3. Ask Claude to review colony state (it will read from `state/snapshots/`)
4. Discuss specific concerns, optimization opportunities, or strategic questions

**Expected Outcome:** Data-backed advisory based on actual colony state  
**Common Issues:** If extraction hasn't run recently, data will be stale

---

## Development Workflows

### Testing Extraction Changes

**When to use:** After modifying extractor code

**Steps:**
1. Navigate to extractor directory
2. Run extraction against test save
3. Validate JSON is parseable
4. Spot-check values against in-game data
5. Check for new warnings/errors in output

**Commands:**
```powershell
cd D:\development-repositories\rimworld-ai-colony-coplay\tools\extractor

# Run extraction
python rimworld_extractor_v2.py "..\..\game-saves\the-fringe-benefit\the-fringe-benefit#§#Autosave-129.rws" -o ..\..\state\snapshots\

# Validate JSON
python -c "import json; d=json.load(open('..\..\state\snapshots\colony_*.json')); print(f'Colonists: {len(d[\"colonists\"])}, Buildings: {d[\"buildings\"][\"total_count\"]}')"

# JSON only (faster for testing)
python rimworld_extractor_v2.py "..\..\game-saves\the-fringe-benefit\the-fringe-benefit#§#Autosave-129.rws" --json-only
```

---

### Adding New Extraction Category

**When to use:** When a new data section needs to be extracted  
**Location:** `tools/extractor/rimworld_extractor_v2.py`

**Steps:**
1. Run schema_discovery.py to find the XML path
2. Add extraction function following existing patterns
3. Wire into `extract_all()` method
4. Add to markdown report in `generate_markdown()`
5. Test against sample save
6. Add dual-audience comments
7. Update memory bank if deliverables change

**Pattern to follow:**
```python
def extract_{section}(root: etree._Element) -> dict:
    """Extract {section} data from {path}.
    
    {Context for humans about what this data represents.}
    
    AI NOTE: {Any hidden constraints or cross-references to watch for.}
    """
    data = {}
    
    section_elem = root.find('game/path/to/section')
    if section_elem is None:
        return data
    
    for item in section_elem.findall('items/li'):
        # Extract with safe getters
        data[get_text(item.find('key'))] = get_text(item.find('value'))
    
    return data
```

---

### Committing Feature Work

**When to use:** After completing a feature or milestone

**Steps:**
1. Update worklog README in `work-logs/{milestone}/`
2. Update memory bank files (context.md at minimum)
3. Update main README if capabilities changed
4. Stage and commit with conventional commit message

**Commands:**
```powershell
cd D:\development-repositories\rimworld-ai-colony-coplay
git add .
git status  # Review changes
git commit -m "feat(extractor): add quest extraction with status derivation"
```

---

## Memory Bank Maintenance

### Updating context.md

**When:** After every significant work session  
**What to update:**
1. Move completed items from "Next Steps" to "Recent Accomplishments"
2. Update "Current Phase" if phase changed
3. Update "Next Steps" with new actionable items
4. Document any new decisions in "Active Decisions"
5. Add/resolve blockers as appropriate
6. Update "Last Updated" date

---

### Updating architecture.md

**When:** When architectural patterns emerge or change  
**What to update:**
1. Add new components as they're created
2. Document architectural decisions with rationale
3. Update structure diagram if directories change
4. Update extraction capabilities table

---

## Session Management

### Session Start Procedure

1. **Load memory bank files** — Read brief.md, context.md
2. **Confirm context** — Verify current phase and immediate next steps
3. **Check for stale data** — If "Last Updated" is old, flag for review
4. **Ready state** — Proceed with work

### Session End Procedure

1. **Update context.md** — Accomplishments, next steps, decisions
2. **Update other files if needed** — architecture.md, tech.md
3. **Update worklog** if milestone work completed
4. **Commit changes** if appropriate

---

## Future Workflows (Planned)

### Database Population

**When to use:** After PostgreSQL schema is created on pgsql01

**Steps:**
1. Run extraction to JSON
2. Load JSON into PostgreSQL tables
3. Verify data integrity
4. Query via CrystalDB MCP

### Watcher Daemon

**When to use:** During active play sessions for automatic extraction

**Steps:**
1. Start watcher daemon pointing at saves directory
2. Play RimWorld normally
3. Watcher auto-extracts on autosave
4. Data available in PostgreSQL for queries

---

## Quality Checklists

### Extraction Output Checklist
- [ ] JSON is valid (parseable)
- [ ] Colonist count matches expected (~7 for The Fringe Benefit)
- [ ] Factions have relations populated (not empty arrays)
- [ ] Buildings total is reasonable (~1000)
- [ ] Resource counts are reasonable
- [ ] No Python exceptions during run
- [ ] Markdown summary is readable

### Code Change Checklist
- [ ] Uses safe getters (get_text, get_int, get_float)
- [ ] Handles missing/malformed data gracefully
- [ ] Checks for IsNull="True" attributes before iterating
- [ ] Player faction detection uses correct prefix handling
- [ ] Tested against sample save
- [ ] No new warnings in extraction run
- [ ] Dual-audience comments added where appropriate

### Dual-Audience Comment Checklist
- [ ] Intent comments explain what/why, not what the code says
- [ ] AI NOTEs added for hidden constraints (cross-references, required formats)
- [ ] No commenting theatre (obvious code left uncommented)
- [ ] Docstrings on all extraction functions
