"""
Faction Parser for RimWorld Save Files

Extracts faction information with single-pass index resolution for accurate
faction relations mapping.
"""

import logging
from typing import Any, Dict, List, Optional

from lxml import etree

logger = logging.getLogger(__name__)


def extract_factions(save_file_path: str) -> List[Dict[str, Any]]:
    """
    Extract faction data using single-pass index resolution.

    Single pass: Build faction index map and extract all factions
    Then resolve relations after all factions are indexed

    Args:
        save_file_path: Path to .rws save file

    Returns:
        List of faction dictionaries with resolved relations
    """
    factions = []
    faction_index_map = {}  # Index (0, 1, 2...) -> faction info

    try:
        # Single pass: Build faction index map and extract all factions
        logger.info("Building faction index map and extracting factions...")
        faction_index = 0
        for event, elem in etree.iterparse(
            save_file_path,
            events=('end',),
            tag='li',
            remove_blank_text=True,
            remove_comments=True
        ):
            # Check if this is a faction element (direct child of allFactions)
            parent = elem.getparent()
            if parent is not None and parent.tag == 'allFactions':
                faction_data = _extract_faction_basic(elem)
                if faction_data:
                    # Store with index position
                    faction_data['index'] = faction_index
                    faction_index_map[faction_index] = faction_data
                    faction_index += 1

                # Only clear faction-level elements after extraction
                # (not inner li elements like relations/li which would be cleared
                # before parent faction li gets processed)
                elem.clear()
                while elem.getprevious() is not None:
                    del parent[0]

        logger.info(f"Built index map with {len(faction_index_map)} factions")

        # Convert map to list
        factions = list(faction_index_map.values())

        # Now resolve relations for all factions (use same list from first pass)
        logger.info("Resolving faction relations...")
        for faction in factions:
            relations = _resolve_faction_relations(faction, faction_index_map)
            faction['relations'] = relations

        logger.info(f"Extracted {len(factions)} factions with resolved relations")

    except Exception as e:
        logger.error(f"Error extracting factions: {e}", exc_info=True)

    return factions


def _extract_faction_basic(elem: etree._Element) -> Optional[Dict[str, Any]]:
    """
    Extract basic faction information including relations.

    Args:
        elem: XML element for a faction

    Returns:
        Dictionary with basic faction data or None
    """
    try:
        def_elem = elem.find('def')
        load_id_elem = elem.find('loadID')
        name_elem = elem.find('name')

        if def_elem is None or load_id_elem is None:
            return None

        load_id = load_id_elem.text.strip() if load_id_elem.text else None
        faction_data = {
            'def': def_elem.text.strip() if def_elem.text else None,
            'load_id': load_id,
            # Keep 'id' as an alias for downstream code expecting this key.
            'id': load_id,
            'name': name_elem.text.strip() if name_elem is not None and name_elem.text else 'Unknown',
            'is_player': False,
            'relations': []
        }

        # Identify player faction
        if faction_data['def'] == 'PlayerColony':
            faction_data['is_player'] = True

        # Extract relations while we have the element
        relations_elem = elem.find('relations')
        if relations_elem is not None:
            for rel_li in relations_elem.findall('li'):
                other_elem = rel_li.find('other')
                goodwill_elem = rel_li.find('goodwill')
                kind_elem = rel_li.find('kind')

                if other_elem is not None and other_elem.text:
                    relation = {
                        'other_ref': other_elem.text.strip(),
                        'goodwill': None,
                        'kind': None
                    }

                    if goodwill_elem is not None and goodwill_elem.text:
                        try:
                            relation['goodwill'] = int(goodwill_elem.text.strip())
                        except ValueError:
                            pass

                    if kind_elem is not None and kind_elem.text:
                        relation['kind'] = kind_elem.text.strip()

                    faction_data['relations'].append(relation)

        return faction_data

    except Exception as e:
        logger.warning(f"Error extracting basic faction data: {e}")
        return None


def _resolve_faction_relations(faction_data: Dict[str, Any], ref_map: Dict[int, Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Resolve faction relations from stored unresolved relations.

    Args:
        faction_data: Faction dictionary with basic info and unresolved relations
        ref_map: Faction index map

    Returns:
        List of resolved relation dictionaries
    """
    resolved_relations = []
    
    for relation in faction_data.get('relations', []):
        other_ref = relation.get('other_ref', '')
        if not other_ref:
            continue
        
        # Parse "Faction_N" format to extract index number
        if other_ref.startswith('Faction_'):
            try:
                other_index = int(other_ref.replace('Faction_', ''))
            except ValueError:
                logger.warning(f"Invalid faction reference format: {other_ref}")
                continue
        else:
            # Direct index number
            try:
                other_index = int(other_ref)
            except ValueError:
                logger.warning(f"Invalid faction reference: {other_ref}")
                continue
        
        # Resolve other faction from index map
        other_faction = ref_map.get(other_index, {})
        other_name = other_faction.get('name', 'Unknown')
        other_def = other_faction.get('def', 'Unknown')
        
        resolved_relation = {
            'other_id': other_ref,
            'other_name': other_name,
            'other_def': other_def,
            'goodwill': relation.get('goodwill'),
            'kind': relation.get('kind')
        }
        
        resolved_relations.append(resolved_relation)
        logger.debug(f"  Appended relation: {resolved_relation['other_name']} -> {resolved_relation.get('goodwill', 'N/A')}, {resolved_relation.get('kind', 'N/A')}")
    
    return resolved_relations


def _extract_relation(elem: etree._Element, ref_map: Dict[int, Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    Extract a single faction relation and resolve the other faction.

    Args:
        elem: XML element for a relation
        ref_map: Faction index map for resolving references

    Returns:
        Dictionary with relation data or None
    """
    try:
        other_elem = elem.find('other')
        goodwill_elem = elem.find('goodwill')
        kind_elem = elem.find('kind')

        if other_elem is None:
            return None

        other_ref = other_elem.text.strip() if other_elem.text else None
        if not other_ref:
            return None

        # Parse "Faction_N" format to extract index number
        # Format: "Faction_0", "Faction_1", etc.
        if other_ref.startswith('Faction_'):
            try:
                other_index = int(other_ref.replace('Faction_', ''))
            except ValueError:
                logger.warning(f"Invalid faction reference format: {other_ref}")
                other_index = -1
        else:
            # Direct index number
            try:
                other_index = int(other_ref)
            except ValueError:
                logger.warning(f"Invalid faction reference: {other_ref}")
                other_index = -1

        # Resolve other faction from index map
        other_faction = ref_map.get(other_index, {})
        other_name = other_faction.get('name', 'Unknown')
        other_def = other_faction.get('def', 'Unknown')

        relation = {
            'other_id': other_ref,
            'other_name': other_name,
            'other_def': other_def,
            'goodwill': None,
            'kind': None
        }

        # Extract goodwill
        if goodwill_elem is not None and goodwill_elem.text:
            try:
                relation['goodwill'] = int(goodwill_elem.text.strip())
            except ValueError:
                logger.warning(f"Invalid goodwill value: {goodwill_elem.text}")

        # Extract kind
        if kind_elem is not None and kind_elem.text:
            relation['kind'] = kind_elem.text.strip()

        return relation

    except Exception as e:
        logger.warning(f"Error extracting relation: {e}")
        return None


def get_player_faction(factions: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    Get player faction from factions list.

    Args:
        factions: List of faction dictionaries

    Returns:
        Player faction dictionary or None
    """
    for faction in factions:
        if faction.get('is_player'):
            return faction
    return None


def get_hostile_factions(factions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Get all factions hostile to the player.

    Args:
        factions: List of faction dictionaries

    Returns:
        List of hostile faction dictionaries
    """
    player_faction = get_player_faction(factions)
    if not player_faction:
        return []

    hostile_factions = []
    for faction in factions:
        if faction.get('is_player'):
            continue

        # Check if player has hostile relation to this faction
        for relation in player_faction.get('relations', []):
            if relation.get('other_id') == faction.get('id'):
                if relation.get('kind') == 'Hostile':
                    hostile_factions.append(faction)
                break

    return hostile_factions
