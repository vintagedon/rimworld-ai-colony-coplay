# RimWorld AI Colony Co-Play Tasks and Workflows

## Common Workflows

### Extraction: Manual Save Processing

**When to use:** When you want to extract current colony state for Claude advisory  
**Frequency:** On-demand, typically before advisory sessions

**Steps:**
1. Ensure RimWorld has autosaved recently (or manual save)
2. Run extractor against target save file
3. Verify JSON output is valid
4. Review Markdown summary for obvious issues

**Command:**
```powershell
python tools/extractor/rimworld_extractor.py "<save_file>.rws" -o state/snapshots/
```

**Expected Outcome:** JSON and MD files in `state/snapshots/` with current timestamp  
**Common Issues:** Large files may take 20-30 seconds; watch for memory warnings

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

**Quality check:** Does context.md accurately reflect current state?

---

### Updating architecture.md

**When:** When architectural patterns emerge or change  
**What to update:**
1. Add new components as they're created
2. Document architectural decisions with rationale
3. Update structure diagram if directories change
4. Record integration points as they're established

**Quality check:** Can someone understand the system structure from this file alone?

---

## Session Management

### Session Start Procedure

**Objective:** Load context and confirm understanding

1. **Load memory bank files** — Read brief.md, context.md, scan others as needed
2. **Confirm context** — Verify current phase and immediate next steps
3. **Check for stale data** — If "Last Updated" is old, flag for review
4. **Ready state** — Proceed with work

---

### Session End Procedure

**Objective:** Update memory bank with session outcomes

1. **Update context.md** — Accomplishments, next steps, decisions
2. **Update other files if needed** — architecture.md, tech.md if changed
3. **Commit changes** if appropriate

```powershell
git add .kilocode/rules/memory-bank/
git commit -m "Update memory bank: [what changed]"
```

---

## Development Workflows

### Adding a New Parser Module

**When to use:** When extraction needs to handle a new data section  
**Location:** `tools/extractor/parsers/`

**Steps:**
1. Create new parser file: `parsers/{section}_parser.py`
2. Implement extraction function following existing patterns
3. Add import and integration in main extractor
4. Test against sample save
5. Update handoff doc if deliverables change

**Expected Outcome:** New data section appears in JSON output

---

### Testing Extraction Changes

**When to use:** After modifying extractor code

**Steps:**
1. Run extraction against test save
2. Validate JSON is parseable
3. Spot-check values against in-game data
4. Check for new warnings/errors in output

**Commands:**
```powershell
# Run extraction
python tools/extractor/rimworld_extractor.py ".ai-sandbox/Deserters of the Rim#§#Hoeaia.rws" -o state/snapshots/

# Validate JSON
python -c "import json; d=json.load(open('state/snapshots/latest.json')); print(f'Colonists: {len(d.get(\"colonists\", []))}')"
```

---

## Quality Checklists

### Extraction Output Checklist
- [ ] JSON is valid (parseable)
- [ ] Colonist count matches in-game
- [ ] Resource counts are reasonable
- [ ] No Python exceptions during run
- [ ] Markdown summary is readable

### Code Change Checklist
- [ ] Follows existing patterns
- [ ] Handles missing/malformed data gracefully
- [ ] Tested against sample save
- [ ] No new warnings in extraction run
