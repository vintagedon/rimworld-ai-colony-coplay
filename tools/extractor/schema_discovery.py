#!/usr/bin/env python3
"""
RimWorld Save Schema Discovery

Parses a RimWorld .rws save file and outputs a hierarchical schema
showing all XML tag paths with occurrence counts. Used to understand
save file structure before building targeted extractors.

Usage:
    python schema_discovery.py <save_file.rws> [-o output.md] [-d max_depth]
"""

import argparse
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

from lxml import etree


class SchemaNode:
    """Represents a node in the schema tree."""

    def __init__(self, name: str):
        self.name = name
        self.count = 0
        self.children: Dict[str, 'SchemaNode'] = {}
        self.has_text = False
        self.has_attributes = False
        self.attribute_names: set = set()

    def get_or_create_child(self, name: str) -> 'SchemaNode':
        """Get existing child or create new one."""
        if name not in self.children:
            self.children[name] = SchemaNode(name)
        return self.children[name]

    def increment(self):
        """Increment occurrence count."""
        self.count += 1


class SchemaDiscovery:
    """Discovers XML schema from RimWorld save files."""

    def __init__(self, save_path: str, max_depth: Optional[int] = None):
        """
        Initialize schema discovery.

        Args:
            save_path: Path to .rws save file
            max_depth: Maximum depth to traverse (None for unlimited)
        """
        self.save_path = Path(save_path)
        self.max_depth = max_depth
        self.root_node = SchemaNode("(root)")
        self.total_elements = 0
        self.max_depth_reached = 0

    def discover(self) -> 'SchemaNode':
        """
        Parse save file and build schema tree.

        Returns:
            Root SchemaNode containing full schema
        """
        print(f"Parsing: {self.save_path.name}")
        print(f"File size: {self.save_path.stat().st_size / 1024 / 1024:.1f} MB")

        tree = etree.parse(str(self.save_path))
        root = tree.getroot()

        self._walk_element(root, self.root_node, depth=0)

        print(f"Total elements: {self.total_elements:,}")
        print(f"Max depth reached: {self.max_depth_reached}")

        return self.root_node

    def _walk_element(self, element: etree._Element, parent_node: SchemaNode, depth: int):
        """Recursively walk XML tree and build schema."""
        self.total_elements += 1
        self.max_depth_reached = max(self.max_depth_reached, depth)

        # Get or create node for this tag
        node = parent_node.get_or_create_child(element.tag)
        node.increment()

        # Track if element has text content
        if element.text and element.text.strip():
            node.has_text = True

        # Track attributes
        if element.attrib:
            node.has_attributes = True
            node.attribute_names.update(element.attrib.keys())

        # Recurse into children (respect max_depth)
        if self.max_depth is None or depth < self.max_depth:
            for child in element:
                self._walk_element(child, node, depth + 1)

    def count_unique_paths(self, node: Optional[SchemaNode] = None) -> int:
        """Count total unique tag paths in schema."""
        if node is None:
            node = self.root_node
        count = len(node.children)
        for child in node.children.values():
            count += self.count_unique_paths(child)
        return count


def generate_markdown(
    schema: SchemaNode,
    save_path: Path,
    total_elements: int,
    max_depth_reached: int,
    unique_paths: int
) -> str:
    """Generate hierarchical markdown from schema tree."""
    lines = [
        "# RimWorld Save Schema Discovery",
        "",
        f"**Source:** `{save_path.name}`",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**File Size:** {save_path.stat().st_size / 1024 / 1024:.1f} MB",
        "",
        "## Summary",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Total XML Elements | {total_elements:,} |",
        f"| Unique Tag Paths | {unique_paths:,} |",
        f"| Maximum Depth | {max_depth_reached} |",
        "",
        "## Schema Tree",
        "",
        "Format: `tag_name (count)` — attributes: [attr1, attr2] — has text content",
        "",
    ]

    def write_node(node: SchemaNode, depth: int, prefix: str = ""):
        """Recursively write node and children."""
        # Sort children: high-count items first, then alphabetically
        sorted_children = sorted(
            node.children.items(),
            key=lambda x: (-x[1].count, x[0])
        )

        for i, (name, child) in enumerate(sorted_children):
            is_last = i == len(sorted_children) - 1
            connector = "└── " if is_last else "├── "
            child_prefix = prefix + ("    " if is_last else "│   ")

            # Build node description
            desc = f"{name} ({child.count:,})"

            if child.has_attributes:
                attrs = ", ".join(sorted(child.attribute_names))
                desc += f" — attrs: [{attrs}]"

            if child.has_text and not child.children:
                desc += " — [text]"

            lines.append(f"{prefix}{connector}{desc}")

            # Recurse
            write_node(child, depth + 1, child_prefix)

    write_node(schema, 0)

    return "\n".join(lines)


def generate_dense_markdown(
    schema: SchemaNode,
    save_path: Path,
    total_elements: int,
    max_depth_reached: int,
    unique_paths: int
) -> str:
    """Generate denser markdown using headers for top levels, lists for deeper."""
    lines = [
        "# RimWorld Save Schema Discovery",
        "",
        f"**Source:** `{save_path.name}`",
        f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"**File Size:** {save_path.stat().st_size / 1024 / 1024:.1f} MB",
        "",
        "## Summary",
        "",
        f"| Metric | Value |",
        f"|--------|-------|",
        f"| Total XML Elements | {total_elements:,} |",
        f"| Unique Tag Paths | {unique_paths:,} |",
        f"| Maximum Depth | {max_depth_reached} |",
        "",
        "---",
        "",
    ]

    def format_node_info(child: SchemaNode) -> str:
        """Format node count and metadata."""
        info = f"({child.count:,})"
        if child.has_attributes:
            attrs = ", ".join(sorted(child.attribute_names))
            info += f" attrs:[{attrs}]"
        if child.has_text and not child.children:
            info += " [text]"
        return info

    def write_node(node: SchemaNode, depth: int):
        """Recursively write node using headers then indented lists."""
        sorted_children = sorted(
            node.children.items(),
            key=lambda x: (-x[1].count, x[0])
        )

        for name, child in sorted_children:
            info = format_node_info(child)

            if depth <= 3:
                # Use headers for top 4 levels
                header_level = "#" * (depth + 2)
                lines.append(f"{header_level} {name} {info}")
                lines.append("")
            else:
                # Use indented list for deeper levels
                indent = "  " * (depth - 4)
                lines.append(f"{indent}- **{name}** {info}")

            write_node(child, depth + 1)

        # Add spacing after header sections
        if depth <= 3 and sorted_children:
            lines.append("")

    write_node(schema, 0)

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Discover XML schema from RimWorld save files"
    )
    parser.add_argument(
        "save_file",
        help="Path to .rws save file"
    )
    parser.add_argument(
        "-o", "--output",
        help="Output markdown file (default: schema_<savename>.md)"
    )
    parser.add_argument(
        "-d", "--max-depth",
        type=int,
        default=None,
        help="Maximum depth to traverse (default: unlimited)"
    )
    parser.add_argument(
        "--dense",
        action="store_true",
        help="Use dense markdown format with headers"
    )

    args = parser.parse_args()

    # Validate input
    save_path = Path(args.save_file)
    if not save_path.exists():
        print(f"Error: File not found: {save_path}")
        sys.exit(1)

    # Run discovery
    discovery = SchemaDiscovery(str(save_path), args.max_depth)
    schema = discovery.discover()
    unique_paths = discovery.count_unique_paths()

    # Generate output
    if args.dense:
        markdown = generate_dense_markdown(
            schema,
            save_path,
            discovery.total_elements,
            discovery.max_depth_reached,
            unique_paths
        )
    else:
        markdown = generate_markdown(
            schema,
            save_path,
            discovery.total_elements,
            discovery.max_depth_reached,
            unique_paths
        )

    # Determine output path
    if args.output:
        output_path = Path(args.output)
    else:
        output_path = save_path.parent / f"schema_{save_path.stem}.md"

    # Write output
    output_path.write_text(markdown, encoding="utf-8")
    print(f"\nSchema written to: {output_path}")
    print(f"Unique paths discovered: {unique_paths:,}")


if __name__ == "__main__":
    main()
