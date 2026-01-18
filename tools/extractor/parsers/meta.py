"""
Meta Data Parser for RimWorld Save Files

Extracts game version, mod list, and other metadata from the <meta> section.
"""

import logging
from typing import Any, Dict

from lxml import etree

logger = logging.getLogger(__name__)


def extract_meta(save_file_path: str) -> Dict[str, Any]:
    """
    Extract metadata from RimWorld save file.

    Args:
        save_file_path: Path to .rws save file

    Returns:
        Dictionary with game version, mod list, and other metadata
    """
    meta_data = {
        'game_version': None,
        'mod_count': 0,
        'mods': []
    }

    try:
        # Use lxml iterparse for streaming
        for event, elem in etree.iterparse(
            save_file_path,
            events=('end',),
            tag='meta',
            remove_blank_text=True,
            remove_comments=True
        ):
            # Extract game version
            game_version = elem.find('gameVersion')
            if game_version is not None and game_version.text:
                meta_data['game_version'] = game_version.text.strip()

            # Extract mod IDs
            mod_ids_elem = elem.find('modIds')
            if mod_ids_elem is not None:
                mod_ids = [li.text.strip() for li in mod_ids_elem.findall('li') if li.text]

                # Extract mod names
                mod_names_elem = elem.find('modNames')
                mod_names = []
                if mod_names_elem is not None:
                    mod_names = [li.text.strip() for li in mod_names_elem.findall('li') if li.text]

                # Combine IDs and names
                for i, mod_id in enumerate(mod_ids):
                    mod_info = {
                        'id': mod_id,
                        'name': mod_names[i] if i < len(mod_names) else 'Unknown'
                    }
                    meta_data['mods'].append(mod_info)

                meta_data['mod_count'] = len(meta_data['mods'])

            # Clear element to free memory
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]

            # We only need the first meta element
            break

        logger.info(f"Extracted meta: {meta_data['game_version']}, {meta_data['mod_count']} mods")

    except Exception as e:
        logger.error(f"Error extracting meta data: {e}", exc_info=True)
        # Don't crash, return what we have

    return meta_data


def extract_game_info(save_file_path: str) -> Dict[str, Any]:
    """
    Extract basic game information from save file.

    Extracts from specific child elements as they fire, since clearing
    elements during iteration removes them before the parent can access them.

    Args:
        save_file_path: Path to .rws save file

    Returns:
        Dictionary with game time, storyteller, difficulty, etc.
    """
    game_info = {
        'ticks': None,
        'day': None,
        'year': None,
        'season': None,
        'quadrum': None,
        'storyteller': None,
        'difficulty': None
    }

    try:
        for event, elem in etree.iterparse(
            save_file_path,
            events=('end',),
            remove_blank_text=True,
            remove_comments=True
        ):
            tag = elem.tag

            # Extract game time when ticksGame fires
            if tag == 'ticksGame':
                if elem.text:
                    ticks = int(elem.text.strip())
                    game_info['ticks'] = ticks
                    # Calculate day, year, season, quadrum
                    # RimWorld: 60000 ticks = 1 day, 15 days = 1 quadrum, 4 quads = 1 year
                    game_info['day'] = ticks // 60000
                    game_info['year'] = 5500 + (ticks // (60000 * 60))  # Starting year 5500
                    quadrum_num = (ticks // (60000 * 15)) % 4
                    quads = ['Aprimay', 'Jugust', 'Septober', 'Decembary']
                    game_info['quadrum'] = quads[quadrum_num]
                    # Season is derived from quadrum
                    seasons = {'Aprimay': 'Spring', 'Jugust': 'Summer', 'Septober': 'Fall', 'Decembary': 'Winter'}
                    game_info['season'] = seasons.get(game_info['quadrum'], 'Unknown')

            # Extract storyteller when storyteller fires
            elif tag == 'storyteller':
                storyteller_def = elem.find('def')
                if storyteller_def is not None and storyteller_def.text:
                    game_info['storyteller'] = storyteller_def.text.strip()

            # Extract difficulty when difficulty fires
            elif tag == 'difficulty':
                difficulty_def = elem.find('def')
                if difficulty_def is not None and difficulty_def.text:
                    game_info['difficulty'] = difficulty_def.text.strip()

            # Stop after game element ends - we have all the data we need
            elif tag == 'game':
                elem.clear()
                break

            # Clear element to free memory
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]

        logger.info(f"Extracted game info: Year {game_info['year']}, Day {game_info['day']}, {game_info['season']}")

    except Exception as e:
        logger.error(f"Error extracting game info: {e}", exc_info=True)

    return game_info


def extract_world_info(save_file_path: str) -> Dict[str, Any]:
    """
    Extract world information from save file.

    The world info is nested inside <world><info>. We use the tag filter
    to only catch 'info' elements, then extract data when they fire.

    Args:
        save_file_path: Path to .rws save file

    Returns:
        Dictionary with world name, seed, etc.
    """
    world_info = {
        'name': None,
        'seed': None,
        'planet_coverage': None
    }

    try:
        # Use tag filter to catch 'info' elements
        # The world's info element contains name, seedString, etc.
        for event, elem in etree.iterparse(
            save_file_path,
            events=('end',),
            tag='info',
            remove_blank_text=True,
            remove_comments=True
        ):
            # Check if this info element has the world info children
            name_elem = elem.find('name')
            seed_elem = elem.find('seedString')

            # Only process if this looks like world info (has seedString)
            if seed_elem is not None:
                if name_elem is not None and name_elem.text:
                    world_info['name'] = name_elem.text.strip()

                if seed_elem.text:
                    world_info['seed'] = seed_elem.text.strip()

                coverage_elem = elem.find('planetCoverage')
                if coverage_elem is not None and coverage_elem.text:
                    try:
                        world_info['planet_coverage'] = float(coverage_elem.text.strip())
                    except ValueError:
                        pass

                # Clear and exit - we found the world info
                elem.clear()
                break

            # Clear element to free memory
            elem.clear()
            while elem.getprevious() is not None:
                del elem.getparent()[0]

        logger.info(f"Extracted world info: {world_info['name']}")

    except Exception as e:
        logger.error(f"Error extracting world info: {e}", exc_info=True)

    return world_info
