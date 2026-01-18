#!/usr/bin/env python3
"""
RimWorld Save File Extractor

Extracts comprehensive game state from RimWorld .rws save files using
lxml streaming for memory efficiency. Outputs JSON and Markdown reports.

Usage:
    python rimworld_extractor.py <save_file.rws> [-o output_dir]
"""

import argparse
import json
import logging
import os
import sys
from datetime import datetime
from typing import Any, Dict, List

from lxml import etree

# Import parsers
from parsers import extract_factions, extract_meta
from parsers.meta import extract_game_info, extract_world_info

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class RimWorldExtractor:
    """Main extractor class for RimWorld save files."""

    def __init__(self, save_file_path: str):
        """
        Initialize extractor.

        Args:
            save_file_path: Path to .rws save file
        """
        self.save_file_path = save_file_path
        self.data = {
            'meta': {},
            'game_time': {},
            'world': {},
            'factions': [],
            'colonists': [],
            'animals': [],
            'resources': {},
            'research': {},
            'buildings': {},
            'zones': []
        }

    def extract_all(self) -> Dict[str, Any]:
        """
        Extract all data from save file.

        Returns:
            Complete extracted data dictionary
        """
        logger.info(f"Starting extraction from: {self.save_file_path}")

        # Extract metadata
        logger.info("Extracting metadata...")
        self.data['meta'] = extract_meta(self.save_file_path)

        # Extract game info
        logger.info("Extracting game info...")
        self.data['game_time'] = extract_game_info(self.save_file_path)

        # Extract world info
        logger.info("Extracting world info...")
        self.data['world'] = extract_world_info(self.save_file_path)

        # Extract factions
        logger.info("Extracting factions...")
        self.data['factions'] = extract_factions(self.save_file_path)

        # Extract research
        logger.info("Extracting research...")
        self.data['research'] = self._extract_research()

        # Extract colonists
        logger.info("Extracting colonists...")
        self.data['colonists'] = self._extract_colonists()

        # Extract resources
        logger.info("Extracting resources...")
        self.data['resources'] = self._extract_resources()

        # Extract animals
        logger.info("Extracting animals...")
        self.data['animals'] = self._extract_animals()

        logger.info("Extraction complete!")
        return self.data

    def _extract_research(self) -> Dict[str, Any]:
        """
        Extract research data.

        Uses tag filter to get the complete researchManager element with all
        children intact, then extracts data from it.

        Returns:
            Dictionary with current project, completed research, and progress
        """
        research_data = {
            'current': None,
            'completed': [],
            'progress': {}
        }

        try:
            # Use tag filter to get the complete researchManager element
            for event, elem in etree.iterparse(
                self.save_file_path,
                events=('end',),
                tag='researchManager',
                remove_blank_text=True,
                remove_comments=True
            ):
                # Extract current project
                current_elem = elem.find('currentProj')
                if current_elem is not None and current_elem.text:
                    research_data['current'] = current_elem.text.strip()

                # Extract completed research from progress element
                progress_elem = elem.find('progress')
                if progress_elem is not None:
                    keys_elem = progress_elem.find('keys')
                    values_elem = progress_elem.find('values')

                    if keys_elem is not None:
                        for key_li in keys_elem.findall('li'):
                            if key_li.text:
                                research_def = key_li.text.strip()
                                research_data['completed'].append(research_def)

                    # Extract progress values (for in-progress research)
                    if values_elem is not None:
                        for i, val_li in enumerate(values_elem.findall('li')):
                            if val_li.text:
                                try:
                                    progress = float(val_li.text.strip())
                                    if i < len(research_data['completed']):
                                        research_def = research_data['completed'][i]
                                        research_data['progress'][research_def] = progress
                                except ValueError:
                                    pass

                # Clear and exit (only one researchManager)
                elem.clear()
                break

            logger.info(f"Extracted {len(research_data['completed'])} completed research projects")

        except Exception as e:
            logger.error(f"Error extracting research: {e}", exc_info=True)

        return research_data

    def _extract_colonists(self) -> List[Dict[str, Any]]:
        """
        Extract colonist data from pawns.

        Only extracts pawns from within <things> section inside <maps> (map objects).
        World pawns and quest things stored elsewhere are ignored.

        Identifies colonists by:
        - Human pawns in the player faction within the map's things section

        Returns:
            List of colonist dictionaries
        """
        colonists = []
        player_faction_id = self._get_player_faction_id()
        in_maps = False
        in_things = False

        try:
            # Use both start and end events to track when we're inside <maps><things>
            for event, elem in etree.iterparse(
                self.save_file_path,
                events=('start', 'end'),
                remove_blank_text=True,
                remove_comments=True
            ):
                # Track entry into <maps> and <things> sections
                if event == 'start':
                    if elem.tag == 'maps':
                        in_maps = True
                    elif elem.tag == 'things' and in_maps:
                        in_things = True
                    continue

                # Handle end events
                tag = elem.tag

                # Exit <things> section (only the one inside maps)
                if tag == 'things' and in_things:
                    in_things = False
                    elem.clear()
                    break  # Exit after processing map things

                # Exit <maps> section
                if tag == 'maps' and in_maps:
                    in_maps = False
                    elem.clear()
                    break

                # Only process Pawn thing elements inside <maps><things>
                # RimWorld uses <thing Class="Pawn"> for map pawns
                if not in_things:
                    # Clear elements outside the section we care about
                    elem.clear()
                    continue

                # Don't clear inside <things> - children need their text intact when
                # the parent thing element fires. Clearing child elements makes their
                # text None before we can read them.
                if tag != 'thing' or elem.get('Class') != 'Pawn':
                    continue  # Don't clear - children need to be accessible

                # Extract pawn data directly from the complete element
                current_pawn = {'skills': [], 'traits': [], 'health': [], 'needs': {}}

                def_elem = elem.find('def')
                if def_elem is not None and def_elem.text:
                    current_pawn['def'] = def_elem.text.strip()

                # Skip non-human pawns early
                if current_pawn.get('def') != 'Human':
                    elem.clear()
                    continue

                faction_elem = elem.find('faction')
                if faction_elem is not None and faction_elem.text:
                    current_pawn['faction'] = faction_elem.text.strip()

                # Only include pawns in player faction
                if current_pawn.get('faction') != player_faction_id:
                    elem.clear()
                    continue

                id_elem = elem.find('id')
                if id_elem is not None and id_elem.text:
                    current_pawn['id'] = id_elem.text.strip()

                # Extract name (NameTriple)
                name_elem = elem.find('.//name[@Class="NameTriple"]')
                if name_elem is not None:
                    first = name_elem.find('first')
                    nick = name_elem.find('nick')
                    last = name_elem.find('last')
                    current_pawn['name'] = {
                        'first': first.text.strip() if first is not None and first.text else '',
                        'nick': nick.text.strip() if nick is not None and nick.text else '',
                        'last': last.text.strip() if last is not None and last.text else ''
                    }

                gender_elem = elem.find('gender')
                if gender_elem is not None and gender_elem.text:
                    current_pawn['gender'] = gender_elem.text.strip()

                age_elem = elem.find('.//ageBiologicalTicks')
                if age_elem is not None and age_elem.text:
                    try:
                        ticks = int(age_elem.text.strip())
                        current_pawn['age_biological'] = ticks / 3600000.0  # Ticks to years
                    except ValueError:
                        pass

                # Extract skills (nested under skills/skills in RimWorld save format)
                inner_skills = elem.find('.//skills/skills')
                if inner_skills is not None:
                    for skill_li in inner_skills.findall('li'):
                        skill_def = skill_li.find('def')
                        skill_level = skill_li.find('level')
                        skill_passion = skill_li.find('passion')

                        if skill_def is not None and skill_def.text:
                            skill_data = {
                                'def': skill_def.text.strip(),
                                'level': int(skill_level.text.strip()) if skill_level is not None and skill_level.text else 0,
                                'passion': skill_passion.text.strip() if skill_passion is not None and skill_passion.text else 'None'
                            }
                            current_pawn['skills'].append(skill_data)

                # Extract traits
                traits_elem = elem.find('.//allTraits')
                if traits_elem is not None:
                    for trait_li in traits_elem.findall('li'):
                        trait_def = trait_li.find('def')
                        trait_degree = trait_li.find('degree')

                        if trait_def is not None and trait_def.text:
                            trait_data = {
                                'def': trait_def.text.strip(),
                                'degree': int(trait_degree.text.strip()) if trait_degree is not None and trait_degree.text else 0
                            }
                            current_pawn['traits'].append(trait_data)

                # Extract needs
                needs_elem = elem.find('.//needs')
                if needs_elem is not None:
                    for need_li in needs_elem.findall('li'):
                        need_def = need_li.find('def')
                        need_level = need_li.find('curLevel')
                        if need_def is not None and need_def.text and need_level is not None and need_level.text:
                            try:
                                current_pawn['needs'][need_def.text.strip()] = float(need_level.text.strip())
                            except ValueError:
                                pass

                colonists.append(current_pawn)

                # Clear element to free memory
                elem.clear()

            logger.info(f"Extracted {len(colonists)} colonists")

        except Exception as e:
            logger.error(f"Error extracting colonists: {e}", exc_info=True)

        return colonists

    def _extract_resources(self) -> Dict[str, Any]:
        """
        Extract resource data from things inside maps.

        Returns:
            Dictionary of resources grouped by category
        """
        resources = {
            'materials': {},
            'food': {},
            'medicine': {},
            'apparel': {},
            'weapons': {},
            'other': {}
        }

        try:
            in_maps = False
            in_things = False

            for event, elem in etree.iterparse(
                self.save_file_path,
                events=('start', 'end'),
                remove_blank_text=True,
                remove_comments=True
            ):
                # Track entry into <maps> and <things> sections
                if event == 'start':
                    if elem.tag == 'maps':
                        in_maps = True
                    elif elem.tag == 'things' and in_maps:
                        in_things = True
                    continue

                # Handle end events
                tag = elem.tag

                # Exit <things> section
                if tag == 'things' and in_things:
                    in_things = False
                    elem.clear()
                    break

                # Exit <maps> section
                if tag == 'maps' and in_maps:
                    in_maps = False
                    elem.clear()
                    break

                # Only process inside map things
                if not in_things:
                    elem.clear()
                    continue

                # Don't clear inside <things> - children need their text intact
                # Extract stackable items
                # RimWorld uses <thing Class="ThingWithComps"> for items
                if tag == 'thing':
                    class_attr = elem.get('Class')
                    if class_attr == 'ThingWithComps':
                        def_elem = elem.find('def')
                        stack_count_elem = elem.find('stackCount')

                        if def_elem is not None and def_elem.text and stack_count_elem is not None and stack_count_elem.text:
                            item_def = def_elem.text.strip()
                            try:
                                count = int(stack_count_elem.text.strip())

                                # Categorize item
                                category = self._categorize_item(item_def)
                                resources[category][item_def] = resources[category].get(item_def, 0) + count
                            except ValueError:
                                pass
                # Don't clear - children need to be accessible for other elements

            logger.info(f"Extracted resources from {sum(len(v) for v in resources.values())} item types")

        except Exception as e:
            logger.error(f"Error extracting resources: {e}", exc_info=True)

        return resources

    def _extract_animals(self) -> List[Dict[str, Any]]:
        """
        Extract animal data from pawns.

        Only extracts animals from within <things> section inside <maps>.
        World pawns and quest things stored elsewhere are ignored.

        Identifies colony animals by:
        - Non-Human pawns in player faction within the map's things section
        - Non-Human pawns with a master (tamed animals)

        Returns:
            List of animal dictionaries
        """
        animals = []
        player_faction_id = self._get_player_faction_id()
        in_maps = False
        in_things = False

        try:
            # Use both start and end events to track when we're inside <maps><things>
            for event, elem in etree.iterparse(
                self.save_file_path,
                events=('start', 'end'),
                remove_blank_text=True,
                remove_comments=True
            ):
                # Track entry into <maps> and <things> sections
                if event == 'start':
                    if elem.tag == 'maps':
                        in_maps = True
                    elif elem.tag == 'things' and in_maps:
                        in_things = True
                    continue

                # Handle end events
                tag = elem.tag

                # Exit <things> section
                if tag == 'things' and in_things:
                    in_things = False
                    elem.clear()
                    break

                # Exit <maps> section
                if tag == 'maps' and in_maps:
                    in_maps = False
                    elem.clear()
                    break

                # Only process Pawn thing elements inside <maps><things>
                # RimWorld uses <thing Class="Pawn"> for map pawns
                if not in_things:
                    elem.clear()
                    continue

                # Don't clear inside <things> - children need their text intact
                if tag != 'thing' or elem.get('Class') != 'Pawn':
                    continue  # Don't clear

                def_elem = elem.find('def')
                if def_elem is None or not def_elem.text:
                    elem.clear()
                    continue

                pawn_def = def_elem.text.strip()

                # Skip humans
                if pawn_def == 'Human':
                    elem.clear()
                    continue

                faction_elem = elem.find('faction')
                master_elem = elem.find('.//master')

                faction = faction_elem.text.strip() if faction_elem is not None and faction_elem.text else None
                has_master = master_elem is not None and master_elem.text

                # Check if this is a colony animal
                in_player_faction = faction == player_faction_id

                if in_player_faction or has_master:
                    animal = {
                        'def': pawn_def,
                        'faction': faction
                    }
                    if has_master:
                        animal['master'] = master_elem.text.strip()
                    animals.append(animal)

                # Clear element to free memory
                elem.clear()

            logger.info(f"Extracted {len(animals)} animals")

        except Exception as e:
            logger.error(f"Error extracting animals: {e}", exc_info=True)

        return animals

    def _get_player_faction_id(self) -> str:
        """
        Get player faction loadID from extracted factions.

        Returns:
            Player faction loadID in "Faction_N" format or empty string
        """
        for faction in self.data.get('factions', []):
            if faction.get('is_player'):
                load_id = faction.get('load_id', '')
                return f"Faction_{load_id}" if load_id else ''
        return ''

    def _categorize_item(self, item_def: str) -> str:
        """
        Categorize an item by its def name.

        Args:
            item_def: Item definition name

        Returns:
            Category name
        """
        # Materials
        materials = ['Steel', 'WoodLog', 'StoneBlocks', 'Component', 'Plasteel', 'Gold', 'Silver', 'Chemfuel']
        if any(m in item_def for m in materials):
            return 'materials'

        # Food
        food = ['Meal', 'RawPotatoes', 'RawRice', 'Meat', 'Kibble', 'Berries']
        if any(f in item_def for f in food):
            return 'food'

        # Medicine
        medicine = ['Medicine', 'HerbalMedicine', 'GlitterworldMedicine']
        if any(m in item_def for m in medicine):
            return 'medicine'

        # Apparel
        apparel = ['Apparel_', 'Pants', 'Jacket', 'Hat', 'Shirt']
        if any(a in item_def for a in apparel):
            return 'apparel'

        # Weapons
        weapons = ['Gun_', 'MeleeWeapon_', 'Bow_', 'Spear_']
        if any(w in item_def for w in weapons):
            return 'weapons'

        return 'other'


def generate_markdown_report(data: Dict[str, Any]) -> str:
    """
    Generate human-readable Markdown report from extracted data.

    Args:
        data: Extracted data dictionary

    Returns:
        Markdown report string
    """
    lines = []

    # Header
    lines.append("# RimWorld Colony Report")
    lines.append("")
    lines.append(f"**Colony:** {data['world'].get('name', 'Unknown')}")
    lines.append(f"**World Seed:** {data['world'].get('seed', 'Unknown')}")
    lines.append("")

    # Game time
    game_time = data.get('game_time', {})
    lines.append("## Game Time")
    lines.append(f"- **Year:** {game_time.get('year', 'Unknown')}")
    lines.append(f"- **Quadrum:** {game_time.get('quadrum', 'Unknown')}")
    lines.append(f"- **Day:** {game_time.get('day', 'Unknown')}")
    lines.append(f"- **Season:** {game_time.get('season', 'Unknown')}")
    lines.append(f"- **Storyteller:** {game_time.get('storyteller', 'Unknown')}")
    lines.append(f"- **Difficulty:** {game_time.get('difficulty', 'Unknown')}")
    lines.append("")

    # Meta
    meta = data.get('meta', {})
    lines.append("## Meta")
    lines.append(f"- **Game Version:** {meta.get('game_version', 'Unknown')}")
    lines.append(f"- **Mod Count:** {meta.get('mod_count', 0)}")
    lines.append("")

    # Factions
    lines.append("## Factions")
    player_faction = None
    for faction in data.get('factions', []):
        if faction.get('is_player'):
            player_faction = faction
            lines.append(f"### Player Faction: {faction.get('name', 'Unknown')}")
            lines.append(f"- **Def:** {faction.get('def', 'Unknown')}")
            lines.append(f"- **Relations:** {len(faction.get('relations', []))} factions")
            lines.append("")
            break

    if player_faction:
        lines.append("#### Player Relations:")
        for rel in player_faction.get('relations', [])[:10]:  # Show first 10
            lines.append(f"- **{rel.get('other_name', 'Unknown')}:** {rel.get('kind', 'Unknown')} (Goodwill: {rel.get('goodwill', 'N/A')})")
        lines.append("")

    # Colonists
    lines.append("## Colonists")
    for colonist in data.get('colonists', []):
        name = colonist.get('name', {})
        full_name = f"{name.get('first', '')} '{name.get('nick', '')}' {name.get('last', '')}".strip()
        lines.append(f"### {full_name}")
        lines.append(f"- **Gender:** {colonist.get('gender', 'Unknown')}")
        lines.append(f"- **Age:** {colonist.get('age_biological', 0):.1f} years")
        lines.append(f"- **Skills:** {len(colonist.get('skills', []))} skills")
        lines.append(f"- **Traits:** {len(colonist.get('traits', []))} traits")
        lines.append("")

    # Resources
    lines.append("## Resources")
    for category, items in data.get('resources', {}).items():
        if items:
            lines.append(f"### {category.capitalize()}")
            for item_def, count in sorted(items.items(), key=lambda x: x[1], reverse=True)[:10]:
                lines.append(f"- **{item_def}:** {count}")
            lines.append("")

    # Research
    lines.append("## Research")
    research = data.get('research', {})
    lines.append(f"- **Current Project:** {research.get('current', 'None')}")
    lines.append(f"- **Completed:** {len(research.get('completed', []))} projects")
    lines.append("")

    # Animals
    animals = data.get('animals', [])
    if animals:
        lines.append("## Animals")
        lines.append(f"- **Count:** {len(animals)}")
        lines.append("")

    return "\n".join(lines)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Extract data from RimWorld save files',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('save_file', help='Path to .rws save file')
    parser.add_argument('-o', '--output', default='state/snapshots/',
                        help='Output directory (default: state/snapshots/)')
    args = parser.parse_args()

    # Validate save file exists
    if not os.path.exists(args.save_file):
        logger.error(f"Save file not found: {args.save_file}")
        sys.exit(1)

    # Create output directory if needed
    os.makedirs(args.output, exist_ok=True)

    # Extract data
    extractor = RimWorldExtractor(args.save_file)
    data = extractor.extract_all()

    # Generate output filenames
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    json_filename = os.path.join(args.output, f'colony_{timestamp}.json')
    md_filename = os.path.join(args.output, f'colony_{timestamp}.md')

    # Write JSON output
    try:
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info(f"JSON output written to: {json_filename}")
        logger.debug(f"Final data structure: factions count = {len(data.get('factions', []))}")
    except Exception as e:
        logger.error(f"Error writing JSON output: {e}", exc_info=True)
        sys.exit(1)

    # Write Markdown output
    try:
        md_content = generate_markdown_report(data)
        with open(md_filename, 'w', encoding='utf-8') as f:
            f.write(md_content)
        logger.info(f"Markdown report written to: {md_filename}")
    except Exception as e:
        logger.error(f"Error writing Markdown output: {e}", exc_info=True)
        sys.exit(1)

    logger.info("Extraction complete!")


if __name__ == '__main__':
    main()
