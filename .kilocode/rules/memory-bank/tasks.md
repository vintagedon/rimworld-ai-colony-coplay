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
python rimworld_extractor.py "..\..\game-saves\deserters-of-the-rim\Deserters of the Rim#§#Hoeaia.rws" -o ..\..\state\snapshots\
```

**Expected Outcome:** JSON and MD files in `state/snapshots/` with current timestamp  
**Expected Output:** ~11 colonists, ~20 factions, ~65 resource types, ~310 research projects

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

### Adding a New Parser Module

**When to use:** When extraction needs to handle a new data section  
**Location:** `tools/extractor/parsers/`

**Steps:**
1. Create new parser file: `parsers/{section}.py`
2. Implement extraction function following lxml iterparse patterns
3. Add import in `parsers/__init__.py`
4. Integrate in `rimworld_extractor.py`
5. Test against sample save
6. Update memory bank if deliverables change

**Pattern to follow:**
```python
from lxml import etree

def extract_{section}(save_file_path: str) -> dict:
    for event, elem in etree.iterparse(save_file_path, events=('end',)):
        if elem.tag == 'target_tag':
            # Extract data before clearing
            data = elem.findtext('child')
            elem.clear()
            break
    return data
```

---

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
python rimworld_extractor.py "..\..\game-saves\deserters-of-the-rim\Deserters of the Rim#§#Hoeaia.rws" -o ..\..\state\snapshots\

# Validate JSON
python -c "import json; d=json.load(open('..\..\state\snapshots\colony_*.json')); print(f'Colonists: {len(d[\"colonists\"])}')"
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
git commit -m "feat(extractor): add faction relations with LoadID resolution"
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
- [ ] Colonist count matches expected (~11 for Hoeaia)
- [ ] Factions have relations populated (not empty arrays)
- [ ] Resource counts are reasonable
- [ ] No Python exceptions during run
- [ ] Markdown summary is readable

### Code Change Checklist
- [ ] Follows lxml iterparse patterns
- [ ] Handles missing/malformed data gracefully
- [ ] Uses section guards (in_things, in_maps) for pawns
- [ ] Extracts children before calling elem.clear()
- [ ] Tested against sample save
- [ ] No new warnings in extraction run
