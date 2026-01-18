#!/usr/bin/env python3
"""
RimWorld Save File Extractor v2.2

Schema-driven extractor using XML paths discovered from actual save file analysis.
This replaces the original hardcoded-path approach that produced "Unknown" values.

Key insight: RimWorld save files are deeply nested XML (~17 levels deep) with
mod-specific extensions. Rather than guess paths, we ran schema_discovery.py
against real saves to map the actual structure. All paths in this file were
validated against 18MB saves with 270+ mods.

The extractor uses DOM parsing (lxml) rather than streaming because:
- File sizes (~18MB) fit comfortably in memory
- Random access simplifies cross-referencing (e.g., faction ID → name lookups)
- Streaming would require multiple passes for the same data

Output: JSON (for downstream CAG queries) and Markdown (for human review).

Usage:
    python rimworld_extractor_v2.py <save_file.rws> [-o output_dir]
    python rimworld_extractor_v2.py <save_file.rws> --json-only
    python rimworld_extractor_v2.py <save_file.rws> --md-only
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

from lxml import etree


# =============================================================================
# UTILITY FUNCTIONS
# =============================================================================
# These handle the quirks of RimWorld's XML serialization: missing elements,
# empty text nodes, and type coercion. Every extraction function uses these
# to avoid repetitive null-checking.

def get_text(elem: Optional[etree._Element], default: str = '') -> str:
    """Safely get text content from an element."""
    if elem is None:
        return default
    return (elem.text or '').strip() or default


def get_int(elem: Optional[etree._Element], default: int = 0) -> int:
    """Safely get integer from element text."""
    text = get_text(elem)
    try:
        return int(text) if text else default
    except ValueError:
        return default


def get_float(elem: Optional[etree._Element], default: float = 0.0) -> float:
    """Safely get float from element text."""
    text = get_text(elem)
    try:
        return float(text) if text else default
    except ValueError:
        return default


def ticks_to_years(ticks: int) -> float:
    """Convert RimWorld ticks to years.
    
    RimWorld runs at 60 ticks/second, 2500 ticks/hour, 60000 ticks/day,
    900000 ticks/quadrum (15 days), 3600000 ticks/year (4 quadrums).
    """
    return ticks / 3600000.0


def ticks_to_days(ticks: int) -> int:
    """Convert RimWorld ticks to days (60000 ticks per day)."""
    return ticks // 60000


def parse_position(pos_str: str) -> tuple:
    """Parse position string like '(45, 67, 0)' into tuple.
    
    RimWorld uses (x, y, z) where y is always 0 for ground-level objects.
    The z coordinate is the "vertical" axis on the 2D map view.
    """
    if not pos_str:
        return None
    match = re.match(r'\((\d+),\s*(\d+),\s*(\d+)\)', pos_str)
    if match:
        return (int(match.group(1)), int(match.group(2)), int(match.group(3)))
    return None


# =============================================================================
# EXTRACTION FUNCTIONS
# =============================================================================
# Each function targets a specific section of the save file. Paths were
# discovered via schema_discovery.py analysis of actual save files.
#
# AI NOTE: These paths are specific to RimWorld 1.6. Major version updates
# may change structure. If extraction suddenly returns empty data, re-run
# schema_discovery.py to verify paths haven't shifted.

def extract_meta(root: etree._Element) -> dict:
    """Extract save file metadata from savegame/meta.
    
    This section is always present and contains the mod load order,
    which is critical for understanding which XML extensions are active.
    """
    meta = root.find('meta')
    if meta is None:
        return {}

    # Mod IDs and names are parallel arrays - zip them for useful output
    mod_ids = [get_text(li) for li in meta.findall('modIds/li')]
    mod_names = [get_text(li) for li in meta.findall('modNames/li')]

    return {
        'game_version': get_text(meta.find('gameVersion')),
        'mod_count': len(mod_ids),
        'mods': list(zip(mod_ids, mod_names))
    }


def extract_game_time(root: etree._Element) -> dict:
    """Extract game time and storyteller info.
    
    Time is stored as raw ticks in tickManager. We convert to human-readable
    year/quadrum/day format. Storyteller and difficulty are in components/li,
    not at the top level - a quirk of RimWorld's component system.
    """
    game = root.find('game')
    if game is None:
        return {}

    result = {
        'ticks': 0,
        'year': 5500,  # RimWorld's epoch year
        'quadrum': 'Unknown',
        'day': 1,
        'hour': 0,
        'storyteller': None,
        'difficulty': None
    }

    # Time calculation: 60 days/year, 15 days/quadrum, 4 quadrums
    tick_manager = game.find('tickManager')
    if tick_manager is not None:
        result['ticks'] = get_int(tick_manager.find('ticksGame'))
        total_days = ticks_to_days(result['ticks'])
        result['year'] = 5500 + (total_days // 60)
        day_of_year = total_days % 60
        result['quadrum'] = ['Aprimay', 'Jugust', 'Septober', 'Decembary'][day_of_year // 15]
        result['day'] = (day_of_year % 15) + 1
        result['hour'] = (result['ticks'] % 60000) // 2500

    # Storyteller lives in game/components, not a dedicated element
    for component in game.findall('components/li'):
        storyteller = component.find('currentStoryteller')
        if storyteller is not None:
            result['storyteller'] = get_text(storyteller)
        difficulty = component.find('currentDifficulty')
        if difficulty is not None:
            result['difficulty'] = get_text(difficulty)

    return result


def extract_colony_stats(root: etree._Element) -> dict:
    """Extract colony-level statistics from storyWatcher.
    
    The storyWatcher tracks metrics used by storytellers to scale difficulty:
    adaptation days, population history, raid counts. Useful for understanding
    why the game is sending certain threats.
    """
    stats = {
        'greatest_population': 0,
        'num_raids_enemy': 0,
        'num_threats_queued': 0,
        'adaptation_days': 0.0,
        'pop_adaptation_days': 0.0
    }

    story_watcher = root.find('game/storyWatcher')
    if story_watcher is None:
        return stats

    stats_record = story_watcher.find('statsRecord')
    if stats_record is not None:
        stats['greatest_population'] = get_int(stats_record.find('greatestPopulation'))
        stats['num_raids_enemy'] = get_int(stats_record.find('numRaidsEnemy'))
        stats['num_threats_queued'] = get_int(stats_record.find('numThreatsQueued'))

    # Adaptation affects storyteller pacing - higher = harder events
    watcher_adapt = story_watcher.find('watcherAdaptation')
    if watcher_adapt is not None:
        stats['adaptation_days'] = get_float(watcher_adapt.find('adaptDays'))

    pop_adapt = story_watcher.find('watcherPopAdaptation')
    if pop_adapt is not None:
        stats['pop_adaptation_days'] = get_float(pop_adapt.find('adaptDays'))

    return stats


def extract_weather(root: etree._Element) -> dict:
    """Extract current weather conditions from the first map."""
    weather = {
        'current': None,
        'current_age_ticks': 0,
        'last': None
    }

    # Multi-map colonies exist but are rare; we extract from first map only
    for map_elem in root.findall('game/maps/li'):
        weather_manager = map_elem.find('weatherManager')
        if weather_manager is not None:
            weather['current'] = get_text(weather_manager.find('curWeather'))
            weather['current_age_ticks'] = get_int(weather_manager.find('curWeatherAge'))
            weather['last'] = get_text(weather_manager.find('lastWeather'))
            break

    return weather


def extract_factions(root: etree._Element) -> list:
    """Extract all factions with relations.
    
    AI NOTE: Faction references throughout the save use "Faction_<loadID>" format.
    When resolving references elsewhere, strip the "Faction_" prefix to match
    against loadID values in the faction_map. This is a common source of
    "Unknown faction" bugs if not handled correctly.
    """
    factions = []
    faction_map = {}  # loadID -> name, for resolving references

    faction_manager = root.find('game/world/factionManager')
    if faction_manager is None:
        return factions

    # First pass: build the faction lookup map
    for faction_elem in faction_manager.findall('allFactions/li'):
        load_id = get_text(faction_elem.find('loadID'))
        name = get_text(faction_elem.find('name'), 'Unknown')
        faction_map[load_id] = name

        faction = {
            'load_id': load_id,
            'name': name,
            'def': get_text(faction_elem.find('def')),
            'leader': get_text(faction_elem.find('leader')),
            'is_player': get_text(faction_elem.find('def')) == 'PlayerColony',
            'hidden': get_text(faction_elem.find('hidden')) == 'True',
            'relations': []
        }

        # Relations store goodwill (-100 to +100) and diplomatic status
        for rel in faction_elem.findall('relations/li'):
            other_id = get_text(rel.find('other'))
            # Strip "Faction_" prefix for lookup compatibility
            other_id_clean = other_id.replace('Faction_', '') if other_id else ''
            faction['relations'].append({
                'other_id': other_id_clean,
                'goodwill': get_int(rel.find('goodwill')),
                'kind': get_text(rel.find('kind'), 'Neutral')
            })

        factions.append(faction)

    # Second pass: resolve faction names in relations
    for faction in factions:
        for rel in faction['relations']:
            rel['other_name'] = faction_map.get(rel['other_id'], 'Unknown')

    return factions


def extract_research(root: etree._Element) -> dict:
    """Extract research progress from researchManager.
    
    Progress is stored as a key-value map where keys are research def names
    and values are accumulated research points. A project is "complete" when
    its value exceeds the required cost (stored in game defs, not the save).
    """
    research = {
        'current_project': None,
        'completed_count': 0,
        'completed': [],
        'in_progress': {}
    }

    research_manager = root.find('game/researchManager')
    if research_manager is None:
        return research

    research['current_project'] = get_text(research_manager.find('currentProj'))

    # Progress uses parallel keys/values arrays (RimWorld's dict serialization)
    progress = research_manager.find('progress')
    if progress is not None:
        keys = [get_text(li) for li in progress.findall('keys/li')]
        values = [get_float(li) for li in progress.findall('values/li')]
        for key, value in zip(keys, values):
            if value > 0:
                research['completed'].append(key)
                research['in_progress'][key] = value
        research['completed_count'] = len(research['completed'])

    return research


def extract_quests(root: etree._Element) -> list:
    """Extract active and completed quests from questManager.
    
    Quest structure is complex: each quest has multiple "parts" representing
    different objectives or conditions. We aggregate part states to determine
    overall quest status.
    """
    quests = []

    quest_manager = root.find('game/questManager')
    if quest_manager is None:
        return quests

    for quest_elem in quest_manager.findall('quests/li'):
        quest = {
            'name': get_text(quest_elem.find('name')),
            'accepted_by': get_text(quest_elem.find('acceptedBy')),
            'appearance_tick': get_int(quest_elem.find('appearanceTick')),
            'challenge_rating': get_int(quest_elem.find('challengeRating')),
            'parent': get_text(quest_elem.find('parent')),
        }

        # Quest parts contain the actual objectives and their states
        parts = []
        for part_elem in quest_elem.findall('parts/li'):
            part = {
                'class': part_elem.get('Class', ''),
                'state': get_text(part_elem.find('state')),
                'outcome': get_text(part_elem.find('outcome')),
            }

            # World object reference (for site-based quests like item stash)
            world_obj = get_text(part_elem.find('worldObject'))
            if world_obj:
                part['world_object'] = world_obj

            # Map parent (for map-based objectives)
            map_parent = get_text(part_elem.find('mapParent'))
            if map_parent:
                part['map_parent'] = map_parent

            # Delay info - how long until quest expires or triggers
            delay_ticks = get_int(part_elem.find('delayTicks'))
            if delay_ticks > 0:
                part['delay_ticks'] = delay_ticks
                part['delay_days'] = round(delay_ticks / 60000, 1)

            if part.get('state') or part.get('outcome') or part.get('world_object'):
                parts.append(part)

        if parts:
            quest['parts'] = parts

        # Derive overall status from individual part states
        states = [p.get('state', '') for p in parts if p.get('state')]
        outcomes = [p.get('outcome', '') for p in parts if p.get('outcome')]

        if 'Failed' in outcomes or 'Failed' in states:
            quest['status'] = 'Failed'
        elif 'Completed' in outcomes or all(s == 'Completed' for s in states if s):
            quest['status'] = 'Completed'
        elif any(s == 'Active' for s in states):
            quest['status'] = 'Active'
        else:
            quest['status'] = 'Unknown'

        quests.append(quest)

    return quests


def extract_world_objects(root: etree._Element) -> dict:
    """Extract world objects (settlements, sites, ruins, etc.).
    
    World objects are everything on the world map: faction settlements,
    quest sites, ruins, caravans. We categorize them for easier querying.
    
    Real Ruins mod adds special fields: blueprintName (the uploaded base ID),
    originX/originZ (original coordinates), and wealthOnEnter (loot value).
    These are extracted when present for raid target prioritization.
    """
    world_data = {
        'settlements': [],
        'sites': [],
        'ruins': [],
        'other': [],
        'summary': {}
    }

    # Build faction lookup with "Faction_" prefix for direct matching
    faction_map = {}
    for faction_elem in root.findall('game/world/factionManager/allFactions/li'):
        load_id = get_text(faction_elem.find('loadID'))
        name = get_text(faction_elem.find('name'), 'Unknown')
        faction_map[f"Faction_{load_id}"] = name

    world_objects = root.find('game/world/worldObjects')
    if world_objects is None:
        return world_data

    for obj_elem in world_objects.findall('worldObjects/li'):
        obj_class = obj_elem.get('Class', '')
        obj_def = get_text(obj_elem.find('def'))

        world_obj = {
            'id': get_int(obj_elem.find('ID')),
            'def': obj_def,
            'class': obj_class,
            'tile': get_int(obj_elem.find('tile')),
            'faction': get_text(obj_elem.find('faction')),
            'faction_name': faction_map.get(get_text(obj_elem.find('faction')), ''),
        }

        name = get_text(obj_elem.find('nameInt'))
        if name:
            world_obj['name'] = name

        # Temporary sites have expiration ticks
        expiration = get_int(obj_elem.find('expiration'))
        if expiration > 0:
            world_obj['expiration_tick'] = expiration

        # Real Ruins mod data - GUIDs identify uploaded player bases
        blueprint_name = get_text(obj_elem.find('blueprintName'))
        if blueprint_name:
            world_obj['blueprint_name'] = blueprint_name
            world_obj['origin_x'] = get_int(obj_elem.find('originX'))
            world_obj['origin_z'] = get_int(obj_elem.find('originZ'))
            world_obj['wealth_on_enter'] = get_float(obj_elem.find('wealthOnEnter'))

        poi_type = get_text(obj_elem.find('poiType'))
        if poi_type:
            world_obj['poi_type'] = poi_type

        # Military power for assessing settlement raid difficulty
        military_power = get_float(obj_elem.find('militaryPower'))
        if military_power > 0:
            world_obj['military_power'] = military_power

        # Categorize by def/class keywords
        def_lower = obj_def.lower()
        class_lower = obj_class.lower()

        if 'settlement' in def_lower or 'settlement' in class_lower:
            world_data['settlements'].append(world_obj)
        elif 'ruins' in def_lower or 'realruins' in class_lower or blueprint_name:
            world_data['ruins'].append(world_obj)
        elif 'site' in def_lower or 'site' in class_lower:
            world_data['sites'].append(world_obj)
        else:
            world_data['other'].append(world_obj)

        key = obj_def or obj_class
        world_data['summary'][key] = world_data['summary'].get(key, 0) + 1

    world_data['total'] = (
        len(world_data['settlements']) +
        len(world_data['sites']) +
        len(world_data['ruins']) +
        len(world_data['other'])
    )

    return world_data


def extract_work_tab_priorities(root: etree._Element) -> dict:
    """Extract Work Tab mod priorities (detailed per-workgiver priorities).
    
    The Work Tab mod (Fluffy) replaces vanilla's 4-level priority system with
    a 0-9 scale and per-workgiver granularity. With Complex Jobs enabled,
    each pawn can have ~225 individual workgiver priorities.
    
    Priority values: 0 = disabled, 1 = highest priority, 9 = lowest priority.
    This inverts typical intuition (lower number = higher priority).
    
    Time-based scheduling stores comma-separated values for each hour.
    We extract the mode (most common value) to get the "usual" priority.
    
    AI NOTE: This data only exists if Work Tab mod is active. The vanilla
    workSettings/priorities path is separate and uses a different schema.
    Check has_work_tab_mod before assuming this data exists.
    """
    work_data = {
        'has_work_tab_mod': False,
        'pawns': {},
        'workgiver_list': [],
        'summary': {}
    }

    # Work Tab stores data in game/components, not with the pawn
    for component in root.findall('game/components/li'):
        priorities_elem = component.find('Priorities')
        if priorities_elem is None:
            continue

        work_data['has_work_tab_mod'] = True

        for idx, pawn_li in enumerate(priorities_elem.findall('values/li')):
            pawn_ref = get_text(pawn_li.find('Pawn'))
            load_id = get_text(pawn_li.find('loadId'))

            pawn_priorities = {
                'pawn_ref': pawn_ref,
                'load_id': load_id,
                'priorities': {}
            }

            for priority_li in pawn_li.findall('Priorities/li'):
                workgiver = get_text(priority_li.find('Workgiver'))
                priority_val = get_text(priority_li.find('Priorities'))

                if workgiver and priority_val:
                    # Handle time-scheduled priorities (comma-separated hourly values)
                    if ',' in priority_val:
                        vals = [int(v) for v in priority_val.split(',') if v.strip().isdigit()]
                        if vals:
                            # Mode = most common value = "usual" priority
                            pawn_priorities['priorities'][workgiver] = max(set(vals), key=vals.count)
                    else:
                        try:
                            pawn_priorities['priorities'][workgiver] = int(priority_val)
                        except ValueError:
                            # Malformed priority value (non-integer); skip this workgiver
                            # to allow extraction to continue robustly
                            pass

                    if workgiver not in work_data['workgiver_list']:
                        work_data['workgiver_list'].append(workgiver)

            pawn_key = pawn_ref or load_id or f"pawn_{idx}"
            work_data['pawns'][pawn_key] = pawn_priorities

            # Summary stats for quick overview
            priorities = pawn_priorities['priorities']
            if priorities:
                enabled = [wg for wg, p in priorities.items() if p > 0]
                high_priority = [wg for wg, p in priorities.items() if p == 1]
                pawn_priorities['enabled_count'] = len(enabled)
                pawn_priorities['high_priority_count'] = len(high_priority)

        break  # Only need first matching component

    if work_data['has_work_tab_mod']:
        work_data['summary'] = {
            'total_pawns': len(work_data['pawns']),
            'total_workgivers': len(work_data['workgiver_list']),
        }

    return work_data


def extract_pawn(pawn_elem: etree._Element) -> dict:
    """Extract full pawn data from a thing element.
    
    Pawns are the most complex entities in the save, with ~1700 lines each
    in heavily modded games. This extracts the core data needed for AI
    advisory: skills, traits, health, needs, relations.
    
    AI NOTE: Many pawn sub-elements use IsNull="True" attribute when empty
    rather than being absent. Always check for this attribute before
    iterating children, or you'll get empty results.
    """
    pawn = {
        'id': get_text(pawn_elem.find('id')),
        'def': get_text(pawn_elem.find('def')),
        'kind_def': get_text(pawn_elem.find('kindDef')),
        'faction': get_text(pawn_elem.find('faction')),
        'gender': get_text(pawn_elem.find('gender')),
        'pos': get_text(pawn_elem.find('pos')),
    }

    # Names use Class attribute to distinguish NameTriple (humans) vs NameSingle (animals)
    name_elem = pawn_elem.find('name')
    if name_elem is not None:
        name_class = name_elem.get('Class', '')
        if name_class == 'NameTriple':
            pawn['name'] = {
                'first': get_text(name_elem.find('first')),
                'nick': get_text(name_elem.find('nick')),
                'last': get_text(name_elem.find('last')),
                'full': f"{get_text(name_elem.find('first'))} '{get_text(name_elem.find('nick'))}' {get_text(name_elem.find('last'))}"
            }
        elif name_class == 'NameSingle':
            name_val = get_text(name_elem.find('name'))
            pawn['name'] = {'single': name_val, 'full': name_val}
        else:
            pawn['name'] = {'full': 'Unnamed'}

    # Age: biological (actual age) vs chronological (includes cryptosleep)
    age_tracker = pawn_elem.find('ageTracker')
    if age_tracker is not None:
        bio_ticks = get_int(age_tracker.find('ageBiologicalTicks'))
        chrono_ticks = get_int(age_tracker.find('ageChronologicalTicks'))
        pawn['age'] = {
            'biological': round(ticks_to_years(bio_ticks), 1),
            'chronological': round(ticks_to_years(chrono_ticks), 1)
        }

    # Skills with passion levels (None/Minor/Major)
    skills_container = pawn_elem.find('skills')
    if skills_container is not None and skills_container.get('IsNull') != 'True':
        pawn['skills'] = []
        for skill_li in skills_container.findall('skills/li'):
            pawn['skills'].append({
                'def': get_text(skill_li.find('def')),
                'level': get_int(skill_li.find('level')),
                'passion': get_text(skill_li.find('passion'), 'None'),
                'xp': get_float(skill_li.find('xpSinceLastLevel'))
            })

    # Backstory and traits define pawn capabilities and mood modifiers
    story = pawn_elem.find('story')
    if story is not None and story.get('IsNull') != 'True':
        pawn['story'] = {
            'childhood': get_text(story.find('childhood')),
            'adulthood': get_text(story.find('adulthood')),
            'body_type': get_text(story.find('bodyType')),
            'hair_def': get_text(story.find('hairDef')),
            'head_type': get_text(story.find('headType')),
        }

        pawn['traits'] = []
        for trait_li in story.findall('traits/allTraits/li'):
            trait = {
                'def': get_text(trait_li.find('def')),
                'degree': get_int(trait_li.find('degree')),
            }
            # Biotech: some traits come from genes
            source_gene = get_text(trait_li.find('sourceGene'))
            if source_gene:
                trait['source_gene'] = source_gene
            pawn['traits'].append(trait)

    # Health: hediffs are injuries, diseases, implants, etc.
    health_tracker = pawn_elem.find('healthTracker')
    if health_tracker is not None:
        pawn['health'] = {
            'state': get_text(health_tracker.find('healthState'), 'Mobile'),
            'hediffs': []
        }

        for hediff in health_tracker.findall('hediffSet/hediffs/li'):
            hediff_data = {
                'def': get_text(hediff.find('def')),
                'severity': get_float(hediff.find('severity')),
                'is_permanent': get_text(hediff.find('isPermanent')) == 'True',
            }
            part = hediff.find('part')
            if part is not None:
                hediff_data['part'] = {
                    'body': get_text(part.find('body')),
                    'index': get_int(part.find('index'))
                }
            pawn['health']['hediffs'].append(hediff_data)

    # Needs: food, rest, mood, etc. - values 0.0 to 1.0
    needs_elem = pawn_elem.find('needs')
    if needs_elem is not None and needs_elem.get('IsNull') != 'True':
        pawn['needs'] = {}
        for need in needs_elem.findall('needs/li'):
            need_def = get_text(need.find('def'))
            need_level = get_float(need.find('curLevel'))
            if need_def:
                pawn['needs'][need_def] = round(need_level, 3)

    # Social relations (family, friends, rivals)
    social = pawn_elem.find('social')
    if social is not None and social.get('IsNull') != 'True':
        pawn['relations'] = []
        for rel in social.findall('directRelations/li'):
            pawn['relations'].append({
                'def': get_text(rel.find('def')),
                'other_pawn': get_text(rel.find('otherPawn'))
            })

    # Training (for animals) - what commands they've learned
    training = pawn_elem.find('training')
    if training is not None and training.get('IsNull') != 'True':
        pawn['training'] = {
            'learned': [],
            'master': get_text(pawn_elem.find('.//master'))
        }
        learned_vals = training.find('learned/vals')
        if learned_vals is not None:
            pawn['training']['learned'] = [get_text(li) for li in learned_vals.findall('li')]

    # Vanilla work priorities (if Work Tab mod not present)
    work_settings = pawn_elem.find('workSettings')
    if work_settings is not None and work_settings.get('IsNull') != 'True':
        priorities_elem = work_settings.find('priorities/vals')
        if priorities_elem is not None:
            pawn['work_priorities'] = [get_int(li) for li in priorities_elem.findall('li')]

    return pawn


def extract_map_pawns(root: etree._Element) -> tuple[list, list]:
    """Extract colonists and animals from map things.
    
    Pawns are mixed in with all other map things (buildings, items, plants).
    We filter by Class="Pawn" then separate colonists from animals by
    checking def (Human vs animal types) and faction membership.
    
    AI NOTE: The player faction ID must be detected first by finding the
    faction with def="PlayerColony", then prefixed with "Faction_" to match
    the format used in pawn faction references. Getting this wrong results
    in zero colonists extracted.
    """
    colonists = []
    animals = []

    # Find player faction ID for filtering
    player_faction_id = None
    for faction in root.findall('game/world/factionManager/allFactions/li'):
        if get_text(faction.find('def')) == 'PlayerColony':
            player_faction_id = f"Faction_{get_text(faction.find('loadID'))}"
            break

    for map_elem in root.findall('game/maps/li'):
        things = map_elem.find('things')
        if things is None:
            continue

        for thing in things.findall('thing'):
            if thing.get('Class') != 'Pawn':
                continue

            pawn = extract_pawn(thing)
            pawn_def = pawn.get('def', '')
            faction = pawn.get('faction', '')

            # Humans belonging to player faction are colonists
            if pawn_def == 'Human':
                if faction == player_faction_id:
                    pawn['type'] = 'colonist'
                    colonists.append(pawn)
            else:
                # Animals: either player-faction or have a master (tamed)
                has_master = pawn.get('training', {}).get('master')
                if faction == player_faction_id or has_master:
                    pawn['type'] = 'animal'
                    animals.append(pawn)

    return colonists, animals


def extract_resources(root: etree._Element) -> dict:
    """Extract stockpiled resources from map things.
    
    Resources are ThingWithComps (stackable items) and MinifiedThing
    (uninstalled furniture/buildings). We sum stackCount by def name.
    """
    resources = {}

    for map_elem in root.findall('game/maps/li'):
        things = map_elem.find('things')
        if things is None:
            continue

        for thing in things.findall('thing'):
            thing_class = thing.get('Class', '')
            if thing_class in ('ThingWithComps', 'MinifiedThing'):
                def_name = get_text(thing.find('def'))
                stack_count = get_int(thing.find('stackCount'), 1)
                if def_name:
                    resources[def_name] = resources.get(def_name, 0) + stack_count

    return resources


def extract_building(thing_elem: etree._Element) -> dict:
    """Extract building data from a thing element.
    
    Buildings have optional fields depending on type: power consumers have
    powerOn, generators have fuel, temperature controls have targetTemperature.
    We extract all fields when present.
    """
    building = {
        'id': get_text(thing_elem.find('id')),
        'def': get_text(thing_elem.find('def')),
        'class': thing_elem.get('Class', ''),
        'pos': get_text(thing_elem.find('pos')),
        'faction': get_text(thing_elem.find('faction')),
    }

    # Material used (stone type, metal, wood)
    stuff = get_text(thing_elem.find('stuff'))
    if stuff:
        building['stuff'] = stuff

    quality = get_text(thing_elem.find('quality'))
    if quality:
        building['quality'] = quality

    health = get_int(thing_elem.find('health'))
    if health > 0:
        building['health'] = health

    rot = get_text(thing_elem.find('rot'))
    if rot:
        building['rotation'] = int(rot) if rot.isdigit() else rot

    # Power state (for electrical buildings)
    power_on = get_text(thing_elem.find('powerOn'))
    if power_on:
        building['power_on'] = power_on == 'True'

    stored_power = get_float(thing_elem.find('storedPower'))
    if stored_power > 0:
        building['stored_power'] = stored_power

    # Fuel (for generators, torches, campfires)
    fuel = get_float(thing_elem.find('fuel'))
    if fuel > 0:
        building['fuel'] = fuel

    allow_auto_refuel = get_text(thing_elem.find('allowAutoRefuel'))
    if allow_auto_refuel:
        building['auto_refuel'] = allow_auto_refuel == 'True'

    target_fuel = get_float(thing_elem.find('configuredTargetFuelLevel'))
    if target_fuel > 0:
        building['target_fuel_level'] = target_fuel

    # Temperature controls (coolers, heaters)
    target_temp = get_float(thing_elem.find('targetTemperature'))
    if target_temp != 0:
        building['target_temperature'] = target_temp

    return building


def categorize_building(def_name: str, class_name: str) -> str:
    """Categorize a building by its def name and class.
    
    This uses keyword matching as a heuristic. It's not exhaustive - mods
    add buildings with unpredictable naming. Unknown buildings fall through
    to 'other'. The keyword lists cover vanilla and major mod packs
    (Vanilla Expanded, LWM Deep Storage, etc.).
    
    AI NOTE: If adding new keywords, maintain alphabetical order within
    each list for readability. The order doesn't affect matching logic.
    """
    def_lower = def_name.lower()
    class_lower = class_name.lower()

    # Production: workbenches, crafting stations, research
    production_keywords = [
        'bench', 'table', 'fabricator', 'refinery', 'smelter', 'smithy',
        'stove', 'butcher', 'brewery', 'loom', 'tailor', 'machining',
        'biofuel', 'crematorium', 'stonecutter', 'sculptor', 'research',
        'druglab', 'component', 'assembler', 'mill', 'kitchen', 'workbench'
    ]
    if any(kw in def_lower for kw in production_keywords) or 'worktable' in class_lower:
        return 'production'

    # Defense: walls, turrets, traps
    defense_keywords = [
        'turret', 'wall', 'embrasure', 'sandbag', 'trap', 'barricade',
        'shield', 'mortar', 'autocannon', 'bunker', 'fortification'
    ]
    if any(kw in def_lower for kw in defense_keywords) or 'turret' in class_lower:
        return 'defense'

    # Power: generators, batteries, conduits
    power_keywords = [
        'generator', 'battery', 'conduit', 'solar', 'wind', 'geothermal',
        'chemfuel', 'watermill', 'power', 'vanometric'
    ]
    if any(kw in def_lower for kw in power_keywords):
        return 'power'

    # Storage: shelves, crates, hoppers
    storage_keywords = [
        'shelf', 'hopper', 'stockpile', 'crate', 'cabinet', 'locker',
        'storage', 'container'
    ]
    if any(kw in def_lower for kw in storage_keywords) or 'storage' in class_lower:
        return 'storage'

    # Furniture: beds, chairs, decorations
    furniture_keywords = [
        'bed', 'chair', 'stool', 'throne', 'lamp', 'light', 'torch',
        'dresser', 'endtable', 'nightstand', 'rug', 'carpet',
        'plant_pot', 'column', 'brazier', 'fireplace', 'television', 'chess',
        'diningtable', 'standingdesk'
    ]
    if any(kw in def_lower for kw in furniture_keywords):
        return 'furniture'

    if 'door' in def_lower or 'door' in class_lower:
        return 'doors'

    # Temperature: coolers, heaters, vents
    temp_keywords = ['cooler', 'heater', 'vent', 'campfire', 'passive_cooler']
    if any(kw in def_lower for kw in temp_keywords):
        return 'temperature'

    # Medical: hospital beds, vitals monitors
    medical_keywords = ['medical', 'hospital', 'vitals', 'biosculpter', 'sleepaccelerator']
    if any(kw in def_lower for kw in medical_keywords):
        return 'medical'

    if 'floor' in def_lower or 'tile' in def_lower:
        return 'floors'

    return 'other'


def extract_buildings(root: etree._Element) -> dict:
    """Extract all buildings from map things.
    
    We filter to player-faction buildings only (or unowned structures like
    ancient ruins that have no faction). Enemy buildings on the map are
    excluded to focus on what the player controls.
    """
    buildings = {
        'production': [],
        'defense': [],
        'power': [],
        'storage': [],
        'furniture': [],
        'doors': [],
        'temperature': [],
        'medical': [],
        'floors': [],
        'other': []
    }

    summary = {}
    building_prefixes = ('Building',)

    # Get player faction for filtering
    player_faction_id = None
    for faction in root.findall('game/world/factionManager/allFactions/li'):
        if get_text(faction.find('def')) == 'PlayerColony':
            player_faction_id = f"Faction_{get_text(faction.find('loadID'))}"
            break

    for map_elem in root.findall('game/maps/li'):
        things = map_elem.find('things')
        if things is None:
            continue

        for thing in things.findall('thing'):
            thing_class = thing.get('Class', '')
            if not thing_class.startswith(building_prefixes):
                continue

            def_name = get_text(thing.find('def'))
            building = extract_building(thing)

            # Skip enemy buildings
            faction = building.get('faction', '')
            if faction and faction != player_faction_id:
                continue

            category = categorize_building(def_name, thing_class)
            buildings[category].append(building)

            key = f"{category}:{def_name}"
            summary[key] = summary.get(key, 0) + 1

    return {
        'by_category': buildings,
        'summary': summary,
        'total_count': sum(len(v) for v in buildings.values())
    }


def extract_zones(root: etree._Element) -> list:
    """Extract all zones from the map.
    
    Zones are player-defined areas: stockpiles (with filter settings),
    growing zones (with plant type), and custom zones. Each zone tracks
    its member cells for area calculation.
    """
    zones = []

    for map_elem in root.findall('game/maps/li'):
        zone_manager = map_elem.find('zoneManager')
        if zone_manager is None:
            continue

        for zone_elem in zone_manager.findall('allZones/li'):
            zone = {
                'id': get_text(zone_elem.find('ID')),
                'label': get_text(zone_elem.find('label')),
                'base_label': get_text(zone_elem.find('baseLabel')),
                'class': zone_elem.get('Class', ''),
                'color': get_text(zone_elem.find('color')),
                'cell_count': len(zone_elem.findall('cells/li')),
            }

            zone['cells'] = [get_text(li) for li in zone_elem.findall('cells/li')]

            # Growing zone specifics
            plant_def = get_text(zone_elem.find('plantDefToGrow'))
            if plant_def:
                zone['plant_to_grow'] = plant_def
                zone['type'] = 'growing'

            # Stockpile specifics
            settings = zone_elem.find('settings')
            if settings is not None:
                zone['type'] = 'stockpile'
                zone['priority'] = get_text(settings.find('priority'))

            if 'type' not in zone:
                zone['type'] = 'other'

            zones.append(zone)

    return zones


def extract_play_log(root: etree._Element, limit: int = 500) -> list:
    """Extract social interaction log.
    
    The playLog records social interactions: chitchat, insults, deep talks.
    We extract recent entries for relationship analysis.
    """
    interactions = []

    play_log = root.find('game/playLog')
    if play_log is None:
        return interactions

    for entry in play_log.findall('entries/li')[-limit:]:
        interaction = {
            'log_id': get_text(entry.find('logID')),
            'tick': get_int(entry.find('ticksAbs')),
            'type': get_text(entry.find('intDef')),
            'initiator': get_text(entry.find('initiator')),
            'recipient': get_text(entry.find('recipient')),
            'initiator_faction': get_text(entry.find('initiatorFaction')),
        }

        extras = [get_text(li) for li in entry.findall('extras/li')]
        if extras:
            interaction['extras'] = extras

        interactions.append(interaction)

    return interactions


def extract_battle_log(root: etree._Element, limit: int = 50) -> list:
    """Extract combat log.
    
    Battles are grouped combat events with individual entries for each
    attack, hit, miss, and wound. Useful for post-battle analysis.
    """
    battles = []

    battle_log = root.find('game/battleLog')
    if battle_log is None:
        return battles

    for battle_elem in battle_log.findall('battles/li')[-limit:]:
        battle = {
            'timestamp': get_int(battle_elem.find('creationTimestamp')),
            'entries': []
        }

        for entry in battle_elem.findall('entries/li'):
            combat_entry = {
                'log_id': get_text(entry.find('logID')),
                'tick': get_int(entry.find('ticksAbs')),
                'class': entry.get('Class', ''),
                'initiator': get_text(entry.find('initiatorPawn')),
                'recipient': get_text(entry.find('recipientPawn')),
                'weapon': get_text(entry.find('weaponDef')),
                'projectile': get_text(entry.find('projectileDef')),
            }

            damaged = []
            for part in entry.findall('damagedParts/li'):
                damaged.append({
                    'body': get_text(part.find('body')),
                    'index': get_int(part.find('index'))
                })
            if damaged:
                combat_entry['damaged_parts'] = damaged

            battle['entries'].append(combat_entry)

        battles.append(battle)

    return battles


def extract_tales(root: etree._Element, limit: int = 100) -> list:
    """Extract significant colony events (tales).
    
    Tales are memorable events used by the art system to generate
    descriptions for sculptures and other artworks. They capture
    moments like kills, research completions, and social events.
    """
    tales = []

    tale_manager = root.find('game/taleManager')
    if tale_manager is None:
        return tales

    for tale_elem in tale_manager.findall('tales/li')[-limit:]:
        tale = {
            'id': get_text(tale_elem.find('id')),
            'def': get_text(tale_elem.find('def')),
            'date': get_int(tale_elem.find('date')),
        }

        # Environmental context when event occurred
        surroundings = tale_elem.find('surroundings')
        if surroundings is not None and surroundings.get('IsNull') != 'True':
            tale['surroundings'] = {
                'biome': get_text(surroundings.find('biome')),
                'weather': get_text(surroundings.find('weather')),
                'temperature': get_float(surroundings.find('temperature')),
                'room_role': get_text(surroundings.find('roomRole')),
                'room_beauty': get_float(surroundings.find('roomBeauty')),
                'room_impressiveness': get_float(surroundings.find('roomImpressiveness')),
            }

        # Pawn involved in the event
        pawn_data = tale_elem.find('pawnData')
        if pawn_data is not None:
            name_elem = pawn_data.find('name')
            if name_elem is not None:
                tale['pawn'] = {
                    'name': f"{get_text(name_elem.find('first'))} '{get_text(name_elem.find('nick'))}' {get_text(name_elem.find('last'))}".strip(),
                    'faction': get_text(pawn_data.find('faction')),
                    'kind': get_text(pawn_data.find('kind')),
                }

        tales.append(tale)

    return tales


def extract_power_network(root: etree._Element) -> dict:
    """Extract power network summary.
    
    We aggregate battery storage and generator fuel levels. Note that
    actual power production/consumption rates aren't in saves - they're
    calculated at runtime from ThingDef XMLs in the game data.
    """
    power = {
        'generators': [],
        'batteries': [],
        'total_stored': 0,
        'total_fuel': 0
    }

    for map_elem in root.findall('game/maps/li'):
        things = map_elem.find('things')
        if things is None:
            continue

        for thing in things.findall('thing'):
            thing_class = thing.get('Class', '')
            if not thing_class.startswith('Building'):
                continue

            def_name = get_text(thing.find('def'))
            def_lower = def_name.lower()

            stored = get_float(thing.find('storedPower'))
            fuel = get_float(thing.find('fuel'))

            if stored > 0:
                power['batteries'].append({
                    'def': def_name,
                    'stored': stored,
                    'pos': get_text(thing.find('pos'))
                })
                power['total_stored'] += stored

            if fuel > 0:
                power['generators'].append({
                    'def': def_name,
                    'fuel': fuel,
                    'auto_refuel': get_text(thing.find('allowAutoRefuel')) == 'True',
                    'pos': get_text(thing.find('pos'))
                })
                power['total_fuel'] += fuel

            # Passive generators (solar, wind, geothermal) have no fuel
            if any(kw in def_lower for kw in ['solar', 'wind', 'geothermal', 'vanometric']):
                if not any(g['def'] == def_name and g.get('pos') == get_text(thing.find('pos')) for g in power['generators']):
                    power['generators'].append({
                        'def': def_name,
                        'power_on': get_text(thing.find('powerOn')) == 'True',
                        'pos': get_text(thing.find('pos'))
                    })

    return power


def build_map_grid(root: etree._Element) -> dict:
    """Build a 2D grid representation of the map.
    
    Extracts positions of all buildings, pawns, and zones for potential
    map visualization. The coordinate system is (x, y, z) where y is
    always 0 for ground-level and z is the vertical axis on screen.
    """
    grid_data = {
        'size': {'x': 0, 'z': 0},
        'buildings': [],
        'zones': {},
        'pawns': [],
    }

    for map_elem in root.findall('game/maps/li'):
        # Map size from mapInfo
        size = map_elem.find('mapInfo/size')
        if size is not None:
            size_text = get_text(size)
            match = re.match(r'\((\d+),\s*(\d+),\s*(\d+)\)', size_text)
            if match:
                grid_data['size']['x'] = int(match.group(1))
                grid_data['size']['z'] = int(match.group(3))

        things = map_elem.find('things')
        if things is not None:
            for thing in things.findall('thing'):
                thing_class = thing.get('Class', '')
                pos = parse_position(get_text(thing.find('pos')))

                if pos and thing_class.startswith('Building'):
                    def_name = get_text(thing.find('def'))
                    category = categorize_building(def_name, thing_class)
                    grid_data['buildings'].append({
                        'x': pos[0],
                        'z': pos[2],
                        'def': def_name,
                        'category': category
                    })

                elif pos and thing_class == 'Pawn':
                    name_elem = thing.find('name')
                    name = 'Unknown'
                    if name_elem is not None:
                        nick = get_text(name_elem.find('nick'))
                        if nick:
                            name = nick
                        else:
                            name = get_text(name_elem.find('name'), 'Unknown')

                    pawn_def = get_text(thing.find('def'))
                    grid_data['pawns'].append({
                        'x': pos[0],
                        'z': pos[2],
                        'name': name,
                        'type': 'human' if pawn_def == 'Human' else 'animal'
                    })

        # Zone cells for area mapping
        zone_manager = map_elem.find('zoneManager')
        if zone_manager is not None:
            for zone_elem in zone_manager.findall('allZones/li'):
                zone_id = get_text(zone_elem.find('ID'))
                zone_label = get_text(zone_elem.find('label'))
                cells = []
                for cell in zone_elem.findall('cells/li'):
                    pos = parse_position(get_text(cell))
                    if pos:
                        cells.append({'x': pos[0], 'z': pos[2]})

                grid_data['zones'][zone_id] = {
                    'label': zone_label,
                    'cells': cells
                }

    return grid_data


# =============================================================================
# MAIN EXTRACTOR
# =============================================================================

class RimWorldExtractorV2:
    """Schema-driven RimWorld save file extractor.
    
    Orchestrates all extraction functions and manages the DOM tree lifecycle.
    Designed for single-use: instantiate, call extract_all(), discard.
    """

    def __init__(self, save_path: str):
        self.save_path = Path(save_path)
        self.root = None

    def load(self):
        """Load and parse the save file."""
        print(f"Loading: {self.save_path.name}")
        print(f"File size: {self.save_path.stat().st_size / 1024 / 1024:.1f} MB")
        self.root = etree.parse(str(self.save_path)).getroot()
        print("Parse complete")

    def extract_all(self) -> dict:
        """Extract all data from the save file.
        
        Calls each extraction function in dependency order (factions must
        be extracted before pawns for faction name resolution).
        """
        if self.root is None:
            self.load()

        data = {}

        print("Extracting meta...")
        data['meta'] = extract_meta(self.root)

        print("Extracting game time...")
        data['game_time'] = extract_game_time(self.root)

        print("Extracting colony stats...")
        data['colony_stats'] = extract_colony_stats(self.root)

        print("Extracting weather...")
        data['weather'] = extract_weather(self.root)

        # Factions first - needed for name resolution in later extractions
        print("Extracting factions...")
        data['factions'] = extract_factions(self.root)

        print("Extracting research...")
        data['research'] = extract_research(self.root)

        print("Extracting pawns...")
        colonists, animals = extract_map_pawns(self.root)
        data['colonists'] = colonists
        data['animals'] = animals

        print("Extracting resources...")
        data['resources'] = extract_resources(self.root)

        print("Extracting buildings...")
        data['buildings'] = extract_buildings(self.root)

        print("Extracting zones...")
        data['zones'] = extract_zones(self.root)

        print("Extracting power network...")
        data['power'] = extract_power_network(self.root)

        print("Extracting play log (social)...")
        data['play_log'] = extract_play_log(self.root)

        print("Extracting battle log...")
        data['battle_log'] = extract_battle_log(self.root)

        print("Extracting tales (events)...")
        data['tales'] = extract_tales(self.root)

        print("Extracting quests...")
        data['quests'] = extract_quests(self.root)

        print("Extracting world objects...")
        data['world'] = extract_world_objects(self.root)

        print("Extracting Work Tab priorities...")
        data['work_tab'] = extract_work_tab_priorities(self.root)

        print("Building map grid...")
        data['map_grid'] = build_map_grid(self.root)

        total_items = (
            len(colonists) + len(animals) +
            data['buildings']['total_count'] +
            len(data['zones']) +
            len(data['play_log']) +
            sum(len(b['entries']) for b in data['battle_log']) +
            len(data['tales']) +
            len(data['quests']) +
            data['world']['total']
        )
        print(f"Extraction complete: {total_items} items extracted")

        return data


# =============================================================================
# REPORT GENERATION
# =============================================================================

def generate_markdown(data: dict) -> str:
    """Generate a comprehensive markdown report for human review.
    
    This is a presentation layer - it doesn't extract new data, just
    formats what extract_all() produced. The report is organized by
    decision-relevance: summary first, then actionable sections (quests,
    threats), then reference data (colonists, buildings).
    """
    lines = []

    meta = data.get('meta', {})
    game_time = data.get('game_time', {})
    colony_stats = data.get('colony_stats', {})
    weather = data.get('weather', {})

    lines.append("# RimWorld Colony Report")
    lines.append("")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append(f"**Game Version:** {meta.get('game_version', 'Unknown')}")
    lines.append(f"**Mod Count:** {meta.get('mod_count', 0)}")
    lines.append("")

    # Summary
    lines.append("## Summary")
    lines.append("")
    lines.append("| Category | Count |")
    lines.append("|----------|-------|")
    lines.append(f"| Colonists | {len(data.get('colonists', []))} |")
    lines.append(f"| Animals | {len(data.get('animals', []))} |")
    lines.append(f"| Buildings | {data.get('buildings', {}).get('total_count', 0)} |")
    lines.append(f"| Zones | {len(data.get('zones', []))} |")
    lines.append(f"| Research Completed | {data.get('research', {}).get('completed_count', 0)} |")
    lines.append(f"| Active Quests | {len([q for q in data.get('quests', []) if q.get('status') == 'Active'])} |")
    lines.append(f"| World Locations | {data.get('world', {}).get('total', 0)} |")
    lines.append(f"| Enemy Raids Survived | {colony_stats.get('num_raids_enemy', 0)} |")
    lines.append(f"| Greatest Population | {colony_stats.get('greatest_population', 0)} |")
    lines.append("")

    # Game Time & Conditions
    lines.append("## Game Time & Conditions")
    lines.append("")
    lines.append(f"**Year {game_time.get('year', 5500)}, {game_time.get('quadrum', '?')}, Day {game_time.get('day', 1)}, Hour {game_time.get('hour', 0)}**")
    lines.append("")
    if game_time.get('storyteller'):
        lines.append(f"- Storyteller: {game_time['storyteller']}")
    if game_time.get('difficulty'):
        lines.append(f"- Difficulty: {game_time['difficulty']}")
    if weather.get('current'):
        lines.append(f"- Weather: {weather['current']}")
    lines.append(f"- Adaptation: {colony_stats.get('adaptation_days', 0):.1f} days")
    lines.append("")

    # Quests
    quests = data.get('quests', [])
    active_quests = [q for q in quests if q.get('status') == 'Active']
    if active_quests:
        lines.append("## Active Quests")
        lines.append("")
        for quest in active_quests:
            challenge = quest.get('challenge_rating', 0)
            stars = '★' * challenge if challenge > 0 else '-'
            lines.append(f"- **{quest['name']}** (Challenge: {stars})")

            for part in quest.get('parts', []):
                if part.get('delay_days'):
                    lines.append(f"  - Time remaining: ~{part['delay_days']} days")
                    break
        lines.append("")

    # World Overview
    world = data.get('world', {})
    if world.get('total', 0) > 0:
        lines.append("## World Overview")
        lines.append("")
        lines.append(f"**Total Locations:** {world['total']}")
        lines.append("")

        if world.get('settlements'):
            lines.append(f"### Settlements ({len(world['settlements'])})")
            lines.append("")
            by_faction = {}
            for s in world['settlements']:
                fname = s.get('faction_name') or s.get('faction') or 'Unknown'
                by_faction.setdefault(fname, []).append(s)
            for fname, settlements in sorted(by_faction.items(), key=lambda x: -len(x[1])):
                lines.append(f"- {fname}: {len(settlements)} settlements")
            lines.append("")

        if world.get('ruins'):
            lines.append(f"### Ruins/POIs ({len(world['ruins'])})")
            lines.append("")
            for ruin in world['ruins'][:10]:
                name = ruin.get('blueprint_name') or ruin.get('name') or ruin.get('def')
                wealth = ruin.get('wealth_on_enter', 0)
                if wealth > 0:
                    lines.append(f"- {name} (wealth: {wealth:,.0f})")
                else:
                    lines.append(f"- {name}")
            if len(world['ruins']) > 10:
                lines.append(f"- ... and {len(world['ruins']) - 10} more")
            lines.append("")

    # Factions
    lines.append("## Factions")
    lines.append("")

    player_faction = None
    for faction in data.get('factions', []):
        if faction.get('is_player'):
            player_faction = faction
            lines.append(f"### {faction['name']} (Player)")
            break

    if player_faction:
        lines.append("")
        lines.append("| Faction | Goodwill | Status |")
        lines.append("|---------|----------|--------|")
        for rel in sorted(player_faction.get('relations', []), key=lambda r: r.get('goodwill', 0), reverse=True):
            if rel.get('other_name') and rel['other_name'] != 'Unknown':
                lines.append(f"| {rel['other_name']} | {rel.get('goodwill', 'N/A')} | {rel.get('kind', 'Neutral')} |")
        lines.append("")

    # Work Tab (if present)
    work_tab = data.get('work_tab', {})
    if work_tab.get('has_work_tab_mod'):
        lines.append("## Work Assignments (Work Tab)")
        lines.append("")
        lines.append(f"**Total Workgivers:** {work_tab['summary'].get('total_workgivers', 0)}")
        lines.append("")

        for pawn_key, pawn_data in work_tab.get('pawns', {}).items():
            pawn_ref = pawn_data.get('pawn_ref', pawn_key).replace('Thing_', '')
            enabled = pawn_data.get('enabled_count', 0)
            high_pri = pawn_data.get('high_priority_count', 0)

            top_jobs = [wg for wg, p in pawn_data.get('priorities', {}).items() if p == 1][:5]
            top_str = ', '.join(top_jobs) if top_jobs else 'None'

            lines.append(f"**{pawn_ref}**: {enabled} jobs enabled, {high_pri} high priority")
            lines.append(f"  - Top priorities: {top_str}")
        lines.append("")

    # Colonists
    lines.append("## Colonists")
    lines.append("")

    for colonist in data.get('colonists', []):
        name = colonist.get('name', {}).get('full', 'Unknown')
        age = colonist.get('age', {})
        pos = colonist.get('pos', '')

        lines.append(f"### {name}")
        lines.append("")
        lines.append(f"**{colonist.get('gender', 'Unknown')}**, {age.get('biological', '?')} years old")
        if pos:
            lines.append(f"Location: {pos}")
        lines.append("")

        story = colonist.get('story', {})
        if story.get('childhood') or story.get('adulthood'):
            lines.append(f"*{story.get('childhood', '?')} → {story.get('adulthood', '?')}*")
            lines.append("")

        traits = colonist.get('traits', [])
        if traits:
            trait_str = ", ".join(t['def'] for t in traits)
            lines.append(f"**Traits:** {trait_str}")
            lines.append("")

        skills = colonist.get('skills', [])
        if skills:
            lines.append("**Skills:**")
            lines.append("")
            for skill in sorted(skills, key=lambda s: s.get('level', 0), reverse=True):
                passion_mark = ''
                if skill.get('passion') == 'Major':
                    passion_mark = ' ★★'
                elif skill.get('passion') == 'Minor':
                    passion_mark = ' ★'
                lines.append(f"- {skill['def']}: {skill.get('level', 0)}{passion_mark}")
            lines.append("")

        hediffs = colonist.get('health', {}).get('hediffs', [])
        notable_hediffs = [h for h in hediffs if h.get('severity', 0) > 0 or h.get('is_permanent')]
        if notable_hediffs:
            lines.append("**Health:**")
            lines.append("")
            for h in notable_hediffs:
                lines.append(f"- {h['def']} (severity: {h.get('severity', 0):.2f})")
            lines.append("")

    # Animals
    animals = data.get('animals', [])
    if animals:
        lines.append("## Colony Animals")
        lines.append("")
        animal_counts = {}
        for animal in animals:
            animal_def = animal.get('def', 'Unknown')
            animal_counts[animal_def] = animal_counts.get(animal_def, 0) + 1
        for animal_def, count in sorted(animal_counts.items(), key=lambda x: -x[1]):
            lines.append(f"- {animal_def}: {count}")
        lines.append("")

    # Zones
    zones = data.get('zones', [])
    if zones:
        lines.append("## Zones")
        lines.append("")
        lines.append("| Zone | Type | Cells | Details |")
        lines.append("|------|------|-------|---------|")
        for zone in zones:
            details = ""
            if zone.get('plant_to_grow'):
                details = f"Growing: {zone['plant_to_grow']}"
            elif zone.get('priority'):
                details = f"Priority: {zone['priority']}"
            lines.append(f"| {zone['label']} | {zone['type']} | {zone['cell_count']} | {details} |")
        lines.append("")

    # Buildings
    buildings_data = data.get('buildings', {})
    if buildings_data.get('total_count', 0) > 0:
        lines.append("## Buildings")
        lines.append("")
        lines.append(f"**Total:** {buildings_data['total_count']} structures")
        lines.append("")

        summary = buildings_data.get('summary', {})
        categories_order = ['production', 'defense', 'power', 'storage', 'furniture', 'doors', 'temperature', 'medical', 'other']

        for category in categories_order:
            category_items = {k.split(':', 1)[1]: v for k, v in summary.items() if k.startswith(f"{category}:")}
            if category_items:
                lines.append(f"### {category.capitalize()}")
                lines.append("")
                for def_name, count in sorted(category_items.items(), key=lambda x: -x[1])[:15]:
                    lines.append(f"- {def_name}: {count}")
                lines.append("")

    # Power
    power = data.get('power', {})
    if power.get('total_stored', 0) > 0 or power.get('generators'):
        lines.append("## Power Network")
        lines.append("")
        lines.append(f"**Total Stored:** {power.get('total_stored', 0):.0f} Wd")
        lines.append(f"**Total Fuel:** {power.get('total_fuel', 0):.1f}")
        lines.append(f"**Batteries:** {len(power.get('batteries', []))}")
        lines.append(f"**Generators:** {len(power.get('generators', []))}")

        for gen in power.get('generators', []):
            if gen.get('fuel'):
                lines.append(f"- {gen['def']}: {gen['fuel']:.1f} fuel {'(auto)' if gen.get('auto_refuel') else ''}")
        lines.append("")

    # Resources
    lines.append("## Resources")
    lines.append("")
    resources = data.get('resources', {})
    categories = {
        'Materials': ['Steel', 'Plasteel', 'Component', 'Gold', 'Silver', 'Uranium', 'Jade', 'WoodLog', 'Stone', 'Blocks'],
        'Food': ['Meal', 'Raw', 'Meat', 'Vegetable', 'Berries', 'Corn', 'Rice', 'Potato', 'Hops'],
        'Medicine': ['Medicine', 'Herbal', 'Glitterworld'],
    }
    for category, keywords in categories.items():
        category_items = {k: v for k, v in resources.items()
                         if any(kw.lower() in k.lower() for kw in keywords)}
        if category_items:
            lines.append(f"### {category}")
            lines.append("")
            for item, count in sorted(category_items.items(), key=lambda x: -x[1])[:15]:
                lines.append(f"- {item}: {count:,}")
            lines.append("")

    # Research
    research = data.get('research', {})
    lines.append("## Research")
    lines.append("")
    lines.append(f"**Current Project:** {research.get('current_project', 'None')}")
    lines.append(f"**Completed:** {research.get('completed_count', 0)} projects")
    lines.append("")

    # Recent Interactions
    play_log = data.get('play_log', [])
    if play_log:
        lines.append("## Recent Social Interactions")
        lines.append("")
        lines.append(f"*Showing last {min(20, len(play_log))} of {len(play_log)} logged interactions*")
        lines.append("")
        for entry in play_log[-20:]:
            initiator = entry.get('initiator', '').replace('Thing_', '')
            recipient = entry.get('recipient', '').replace('Thing_', '')
            int_type = entry.get('type', 'Unknown')
            lines.append(f"- {initiator} → {recipient}: {int_type}")
        lines.append("")

    # Recent Combat
    battle_log = data.get('battle_log', [])
    if battle_log:
        lines.append("## Recent Combat")
        lines.append("")
        total_entries = sum(len(b['entries']) for b in battle_log)
        lines.append(f"*{len(battle_log)} battles, {total_entries} combat events*")
        lines.append("")

    # Recent Tales
    tales = data.get('tales', [])
    if tales:
        lines.append("## Recent Events (Tales)")
        lines.append("")
        lines.append(f"*Last {min(15, len(tales))} of {len(tales)} recorded events*")
        lines.append("")
        for tale in tales[-15:]:
            pawn_info = tale.get('pawn', {})
            pawn_name = pawn_info.get('name', '').strip() if pawn_info else ''
            tale_def = tale.get('def', 'Unknown')
            if pawn_name:
                lines.append(f"- {tale_def}: {pawn_name}")
            else:
                lines.append(f"- {tale_def}")
        lines.append("")

    # Map Grid Summary
    map_grid = data.get('map_grid', {})
    if map_grid.get('size', {}).get('x', 0) > 0:
        lines.append("## Map")
        lines.append("")
        lines.append(f"**Size:** {map_grid['size']['x']} x {map_grid['size']['z']}")
        lines.append(f"**Buildings Placed:** {len(map_grid.get('buildings', []))}")
        lines.append(f"**Pawns on Map:** {len(map_grid.get('pawns', []))}")
        lines.append(f"**Zones Defined:** {len(map_grid.get('zones', {}))}")
        lines.append("")

    return "\n".join(lines)


# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(
        description='Extract data from RimWorld save files (v2.2 - schema-driven)'
    )
    parser.add_argument('save_file', help='Path to .rws save file')
    parser.add_argument('-o', '--output', help='Output directory (default: same as save file)')
    parser.add_argument('--json-only', action='store_true', help='Only output JSON, skip markdown')
    parser.add_argument('--md-only', action='store_true', help='Only output markdown, skip JSON')

    args = parser.parse_args()

    save_path = Path(args.save_file)
    if not save_path.exists():
        print(f"Error: File not found: {save_path}")
        sys.exit(1)

    if args.output:
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
    else:
        output_dir = save_path.parent

    extractor = RimWorldExtractorV2(str(save_path))
    data = extractor.extract_all()

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    base_name = f"colony_{timestamp}"

    if not args.md_only:
        json_path = output_dir / f"{base_name}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"JSON: {json_path}")

    if not args.json_only:
        md_path = output_dir / f"{base_name}.md"
        md_content = generate_markdown(data)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"Markdown: {md_path}")


if __name__ == '__main__':
    main()
