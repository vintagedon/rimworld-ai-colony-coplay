# KC Structured Prompt: RimWorld Complete Save Extractor

## Task: RimWorld Save File Complete Data Extraction
Branch: `feature/rimworld-extractor`
Mode: Code

---

### Objective

Build a Python extractor that parses RimWorld `.rws` save files and outputs **complete** structured data (JSON + Markdown). The extractor handles heavily modded saves (300+ mods, 20-30MB XML files) and captures every extractable data point for AI advisor consumption.

When complete: Running `python rimworld_extractor.py <save.rws>` produces comprehensive JSON containing all game state, and a human-readable Markdown summary.

---

### Scope

**Modify:**
- `rimworld_extractor.py` — main extraction script

**Reference:**
- Sample save file: `Deserters_of_the_Rim___Hoeaia.rws` (23MB, 665k lines, 300+ mods)
- Existing MVP script (provided below) — working colonist/skill/resource extraction
- RimWorld save XML structure documentation (below)

**Output Location:**
- JSON and MD files to specified output directory

---

### Context: RimWorld Save Structure

Save files are XML with this hierarchy:

```
<savegame>
  <meta>                           # Lines 1-30
    <gameVersion>
    <modIds><li>...</li></modIds>
    <modNames><li>...</li></modNames>
  </meta>
  
  <game>                           # Lines ~1400-352000
    <currentMapIndex>
    <ticksGame>                    # Game time in ticks (60000 = 1 day)
    <playSettings>                 # Auto-home, auto-rebuild, etc.
    <storyteller>
    <difficulty>
    
    <researchManager>              # Lines ~2000-2800
      <currentProj>
      <progress><keys><li>...</li></keys><values><li>...</li></values></progress>
    </researchManager>
    
    <history>                      # Lines ~2900-14000 (historical records)
    <taleManager>                  # Lines ~14500-28000 (story events)
    
    <world>                        # Lines ~72000-226000
      <info>
        <name>                     # World name
        <seedString>               # World seed
        <planetCoverage>
      </info>
      <grid>                       # World map tiles
      <factionManager>             # Lines ~91000-101000
        <allFactions>
          <li>
            <def>PlayerColony|Empire|TribeCivil|...</def>
            <name>
            <loadID>               # Faction_XX reference
            <leader>               # Thing_HumanXXXX reference
            <relationSettings>     # Relations to other factions
              <li>
                <other>Faction_XX</other>
                <kind>Hostile|Neutral|Ally</kind>
                <goodwill>-100 to 100</goodwill>
              </li>
            </relationSettings>
          </li>
        </allFactions>
      </factionManager>
      <worldObjects>               # Settlements, sites on world map
    </world>
    
    <maps>                         # Lines ~226000-352000
      <li>                         # Each map
        <uniqueID>
        <mapInfo><Size>(X, Y, Z)</Size></mapInfo>
        <weatherManager>
          <curWeather>             # Current weather def
          <curWeatherAge>
        </weatherManager>
        <mapTemperature>
        <zoneManager>              # Stockpile zones, growing zones
        <areaManager>              # Home area, allowed areas
        <things>                   # Lines ~233000+ THE MAIN DATA
          <thing Class="Building_...">   # Buildings
          <thing Class="Pawn">           # Colonists, animals, enemies
          <thing Class="ThingWithComps"> # Items with components
          <thing Class="Filth">          # Dirt, blood, etc.
        </things>
        <roofGrid>
        <terrainGrid>
        <fogGrid>
      </li>
    </maps>
  </game>
</savegame>
```

### Pawn Structure (Colonists/Animals) — ~1700 lines each

```xml
<thing Class="Pawn">
  <def>Human</def>                      # Or animal def
  <id>Human290935</id>
  <pos>(182, 0, 147)</pos>
  <faction>Faction_19</faction>         # Player faction reference
  
  <name Class="NameTriple">             # +226 lines from start
    <first>Viktor</first>
    <nick>Vik</nick>                    # Optional
    <last>Valentine</last>
  </name>
  
  <gender>Male|Female</gender>
  
  <ageTracker>
    <ageBiologicalTicks>XXXXXXXXX</ageBiologicalTicks>
    <ageChronologicalTicks>XXXXXXXXX</ageChronologicalTicks>
    <birthAbsTicks>XXXXXXXXX</birthAbsTicks>
  </ageTracker>
  
  <story>                               # +499 lines
    <childhood>Backstory_Def</childhood>
    <adulthood>Backstory_Def</adulthood>
    <headType>                          # Appearance
    <bodyType>
    <traits>
      <allTraits>
        <li>
          <def>TraitDef</def>
          <degree>-2 to 2</degree>      # For spectrum traits
        </li>
      </allTraits>
    </traits>
  </story>
  
  <healthTracker>                       # +598 lines
    <hediffSet>
      <hediffs>
        <li Class="Hediff_Injury|Hediff_AddedPart|Hediff_...">
          <def>Gunshot|BionicArm|...</def>
          <severity>0.0-1.0</severity>
          <part>Torso|LeftArm|...</part>    # Body part
          <ageTicks>
        </li>
      </hediffs>
    </hediffSet>
  </healthTracker>
  
  <needs>                               # +741 lines
    <needs>
      <li Class="Need_Mood">
        <def>Mood</def>
        <curLevel>0.0-1.0</curLevel>
        <thoughts>
          <memories>
            <li Class="Thought_Memory">
              <def>ThoughtDef</def>
              <moodPowerFactor>
              <age>                      # Ticks since thought
            </li>
          </memories>
        </thoughts>
      </li>
      <li Class="Need_Food">
        <curLevel>0.0-1.0</curLevel>
      </li>
      <li Class="Need_Rest">...</li>
      <li Class="Need_Joy">...</li>
      <li Class="Need_Comfort">...</li>
      <li Class="Need_Outdoors">...</li>
      <li Class="Need_Beauty">...</li>
    </needs>
  </needs>
  
  <skills>                              # +1423 lines
    <skills>
      <li>
        <def>Shooting|Melee|Construction|Mining|Cooking|Plants|Animals|Crafting|Artistic|Medicine|Social|Intellectual</def>
        <level>0-20</level>
        <passion>None|Minor|Major</passion>
        <xpSinceLastLevel>XXXX.XX</xpSinceLastLevel>
      </li>
    </skills>
    <lastXpSinceMidnightResetTimestamp>
  </skills>
  
  <workSettings>                        # +1500 lines
    <priorities>
      <!-- Indexed by WorkTypeDef order -->
    </priorities>
  </workSettings>
  
  <relations>                           # Social relationships
    <directRelations>
      <li>
        <def>Spouse|Lover|Friend|Rival|...</def>
        <otherPawn>Thing_HumanXXXX</otherPawn>
      </li>
    </directRelations>
  </relations>
  
  <ideo>                                # +1490 lines (Ideology DLC)
    <ideo>Ideo_XX</ideo>
    <certainty>0.0-1.0</certainty>
  </ideo>
  
  <genes>                               # +1640 lines (Biotech DLC)
    <xenotypeDef>Baseliner|Hussar|...</xenotypeDef>
    <endogenes><li>GeneDef</li></endogenes>
    <xenogenes><li>GeneDef</li></xenogenes>
  </genes>
  
  <apparel>
    <wornApparel>
      <innerList>
        <li>
          <def>Apparel_Pants</def>
          <stuff>Synthread</stuff>
          <quality>Normal|Good|Excellent|...</quality>
          <health>0-100</health>
        </li>
      </innerList>
    </wornApparel>
  </apparel>
  
  <equipment>
    <primary>                           # Weapon
      <def>Gun_AssaultRifle</def>
      <quality>
      <health>
    </primary>
  </equipment>
  
  <inventory>
    <innerContainer>
      <innerList>...</innerList>
    </innerContainer>
  </inventory>
  
  <!-- MOD-SPECIFIC SECTIONS -->
  <psyche>                              # Psychology mod
    <upbringing>
    <personalityNodes>
      <li>
        <def>PersonalityNodeDef</def>
        <rawRating>0.0-1.0</rawRating>
      </li>
    </personalityNodes>
  </psyche>
  
  <SimpleSidearms_...>                  # Simple Sidearms mod
  <VEF_...>                             # Vanilla Expanded Framework
  <RRPawnBadge_...>                     # Pawn Badge mod
</thing>
```

---

### Deliverables & Validation

#### 1. **Complete Meta Extraction**
   - [ ] Game version string extracted
   - [ ] Full mod list with IDs and names (expect 300+)
   - [ ] Storyteller def extracted
   - [ ] Difficulty settings extracted
   - [ ] World name and seed extracted
   - [ ] JSON output: `meta.game_version`, `meta.mods[]`, `meta.storyteller`, `meta.difficulty`, `meta.world_name`, `meta.world_seed`

#### 2. **Complete Game Time Extraction**
   - [ ] Ticks, calculated day, year, season, quadrum
   - [ ] Current weather
   - [ ] Map temperature (outdoor)
   - [ ] JSON output: `game_time.ticks`, `game_time.day`, `game_time.year`, `game_time.season`, `game_time.quadrum`, `game_time.weather`, `game_time.temperature`

#### 3. **Complete Research Extraction**
   - [ ] Current research project
   - [ ] All completed research (list of defs)
   - [ ] Progress values for in-progress research
   - [ ] JSON output: `research.current`, `research.completed[]`, `research.progress{}`

#### 4. **Complete Faction Extraction**
   - [ ] All factions with def, name, loadID
   - [ ] Player faction identified (def=PlayerColony)
   - [ ] Relations between player and each faction (kind + goodwill)
   - [ ] Faction leaders (pawn references)
   - [ ] JSON output: `factions[]` with `id`, `name`, `type`, `is_player`, `leader`, `relations[]`

#### 5. **Complete Colonist Extraction (all fields)**
   - [ ] Identity: id, name (first/nick/last), gender
   - [ ] Age: biological, chronological (calculated from ticks)
   - [ ] Backstories: childhood, adulthood defs
   - [ ] Appearance: head type, body type, hair, skin/hair color
   - [ ] All 12 skills with level, passion, XP
   - [ ] All traits with degrees
   - [ ] Current mood (0-1 scale)
   - [ ] All needs: food, rest, joy, comfort, outdoors, beauty, etc.
   - [ ] All health conditions (hediffs) with severity, body part, age
   - [ ] All thoughts/memories with mood impact and age
   - [ ] Social relations (spouse, friends, rivals, etc.)
   - [ ] Ideology: ideo reference, certainty
   - [ ] Genes: xenotype, endogenes, xenogenes
   - [ ] Apparel: all worn items with def, stuff, quality, health
   - [ ] Equipment: primary weapon with stats
   - [ ] Inventory contents
   - [ ] Work priorities
   - [ ] Current position (x, y, z)
   - [ ] Current job (if any)
   - [ ] JSON output: comprehensive `colonists[]` array

#### 6. **Complete Animal Extraction**
   - [ ] All tamed animals (faction = player)
   - [ ] Species, name, gender, age
   - [ ] Training status
   - [ ] Bonded pawn (if any)
   - [ ] Health conditions
   - [ ] JSON output: `animals[]`

#### 7. **Complete Resource Extraction**
   - [ ] All stackable items with counts (not just predefined list)
   - [ ] Quality items tracked separately
   - [ ] Group by category (materials, food, medicine, apparel, weapons, etc.)
   - [ ] JSON output: `resources{}` grouped by category

#### 8. **Building/Structure Extraction**
   - [ ] Count of each building type
   - [ ] Power grid status (if extractable)
   - [ ] Defensive structures (turrets, traps)
   - [ ] Production buildings (benches, refineries)
   - [ ] JSON output: `buildings{}` with counts by type

#### 9. **Zone Extraction**
   - [ ] Stockpile zones with settings
   - [ ] Growing zones with plant type
   - [ ] Other zones (dumping, etc.)
   - [ ] JSON output: `zones[]`

#### 10. **World State Extraction**
   - [ ] Known settlements/sites on world map
   - [ ] Active caravans (if any)
   - [ ] Pending events/quests (if extractable)
   - [ ] JSON output: `world.settlements[]`, `world.caravans[]`

#### 11. **Mod-Specific Data (graceful handling)**
   - [ ] Psychology mod: personality nodes if present
   - [ ] Vanilla Expanded: honors, powers if present
   - [ ] Other mod data: capture in `colonist.mod_data{}` dict
   - [ ] Unknown mod fields: log but don't crash
   - [ ] JSON output: mod data nested under relevant entities

#### 12. **Markdown Report Generation**
   - [ ] Colony summary header (name, day, season)
   - [ ] Colonist roster with mood indicators, top skills, health alerts
   - [ ] Resource summary grouped by category
   - [ ] Faction relations summary
   - [ ] Alerts section (low mood, injuries, critical needs)
   - [ ] Output: readable `.md` file

#### 13. **Performance & Robustness**
   - [ ] Handles 20-30MB save files without memory issues
   - [ ] Completes extraction in <30 seconds
   - [ ] Graceful handling of missing/malformed data
   - [ ] CRLF line endings handled (Windows saves)
   - [ ] No crashes on unexpected XML structure

---

### Constraints

- **Pure Python 3.10+** — no external XML libraries beyond stdlib (ElementTree acceptable but regex preferred for streaming large files)
- **No full DOM load** — file is 20-30MB; use streaming/targeted extraction
- **Preserve existing CLI interface** — `python rimworld_extractor.py <save.rws> [-o output_dir]`
- **JSON must be machine-parseable** — valid JSON, consistent schema
- **Markdown must be human-readable** — suitable for quick reference during gameplay
- **Fail gracefully** — missing mod data should log warning, not crash

---

### Existing MVP Code

The current working script extracts: colonists (11 found), skills (12 per colonist), traits, health conditions, mood, resources (20 types), research (310 completed). 

**Known issues to fix:**
1. Faction relations returning empty (XML structure mismatch)
2. Regex escape warning on line 246
3. Only tracks predefined resource list (should discover all)
4. Missing: meta, weather, animals, buildings, zones, world state, mod data

**File location:** `rimworld_extractor.py` (provided separately)

---

### Test Validation Commands

```bash
# Run extraction
python rimworld_extractor.py "Deserters_of_the_Rim___Hoeaia.rws" -o ./output/

# Validate JSON structure
python -c "import json; d=json.load(open('output/*.json')); print(f'Colonists: {len(d[\"colonists\"])}, Factions: {len(d[\"factions\"])}')"

# Check colonist completeness
python -c "import json; d=json.load(open('output/*.json')); c=d['colonists'][0]; required=['skills','traits','health','mood','needs','relations','apparel','equipment']; missing=[k for k in required if k not in c or not c[k]]; print(f'Missing fields: {missing or \"None\"}')"

# Verify no crashes on full extraction
python rimworld_extractor.py "Deserters_of_the_Rim___Hoeaia.rws" -o ./output/ && echo "SUCCESS"
```

---

**Environment:**
- Python 3.10+
- Windows paths with CRLF line endings in save files
- Large files (20-30MB XML)
- Heavily modded saves (300+ mods, non-standard fields)