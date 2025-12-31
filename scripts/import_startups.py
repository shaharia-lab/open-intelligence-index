#!/usr/bin/env python3
"""
Import startups from a JSON file into individual YAML files.

Usage:
    python scripts/import_startups.py <input.json>

This script:
1. Reads a JSON file containing startup entries
2. Validates each entry against schemas/startup.schema.json
3. Creates individual YAML files in index/startups/{country_code}/{startup_id}.yaml
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import jsonschema
    from yaml import dump
except ImportError as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install jsonschema pyyaml")
    sys.exit(1)


def load_schema(schema_path: Path) -> dict:
    """Load the JSON schema for validation."""
    with open(schema_path) as f:
        return json.load(f)


def validate_startup(startup: dict, schema: dict, index: int) -> list[str]:
    """Validate a single startup entry against the schema.

    Returns a list of validation errors (empty if valid).
    """
    errors = []

    try:
        jsonschema.validate(instance=startup, schema=schema)
    except jsonschema.ValidationError as e:
        errors.append(f"Entry #{index} ({startup.get('id', 'UNKNOWN')}): {e.message}")

    return errors


def format_yaml(startup: dict) -> str:
    """Format a startup dict as YAML with proper styling."""
    # Remove None values
    cleaned = {k: v for k, v in startup.items() if v is not None}

    # YAML configuration to match existing style
    yaml_str = dump(
        cleaned,
        default_flow_style=False,
        sort_keys=False,
        allow_unicode=True,
        indent=2,
        width=80,
        line_break="\n"
    )

    # Add schema comment at the top
    schema_comment = "# yaml-language-server: $schema=https://raw.githubusercontent.com/shaharia-lab/open-intelligence-index/main/schemas/startup.schema.json\n"

    # Remove trailing whitespace from each line
    lines = yaml_str.split('\n')
    lines = [line.rstrip() for line in lines]
    yaml_str = '\n'.join(lines)

    return schema_comment + yaml_str


def get_country_dir(country_code: str) -> str:
    """Return lowercase ISO country code as directory name."""
    return country_code.lower()


def import_startups(input_path: Path, schema_path: Path, output_base: Path, dry_run: bool = False) -> None:
    """Import startups from JSON file to individual YAML files."""

    # Load schema
    schema = load_schema(schema_path)

    # Load input JSON
    with open(input_path) as f:
        startups = json.load(f)

    if not isinstance(startups, list):
        print(f"Error: Input JSON must be an array of startup objects")
        sys.exit(1)

    print(f"Found {len(startups)} startup entries in {input_path}")

    # Validate all entries first
    all_errors = []
    for i, startup in enumerate(startups):
        errors = validate_startup(startup, schema, i)
        all_errors.extend(errors)

    if all_errors:
        print("\nValidation errors found:")
        for error in all_errors:
            print(f"  - {error}")
        sys.exit(1)

    print("All entries validated successfully!")

    # Create YAML files
    created = 0
    skipped = 0

    for startup in startups:
        startup_id = startup['id']
        country_code = startup['headquarters']['country_code']
        country_dir = get_country_dir(country_code)

        # Determine output path
        output_dir = output_base / country_dir
        output_file = output_dir / f"{startup_id}.yaml"

        if output_file.exists():
            print(f"  Skipping {startup_id}: {output_file} already exists")
            skipped += 1
            continue

        if dry_run:
            print(f"  Would create: {output_file}")
            created += 1
            continue

        # Create directory if needed
        output_dir.mkdir(parents=True, exist_ok=True)

        # Write YAML file
        yaml_content = format_yaml(startup)
        output_file.write_text(yaml_content)

        print(f"  Created: {output_file}")
        created += 1

    print(f"\nSummary: {created} files created, {skipped} skipped")


def main():
    parser = argparse.ArgumentParser(
        description="Import startups from JSON to individual YAML files"
    )
    parser.add_argument(
        "input",
        type=Path,
        help="Path to input JSON file containing startup entries"
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path("schemas/startup.schema.json"),
        help="Path to JSON schema file (default: schemas/startup.schema.json)"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("index/startups"),
        help="Base output directory (default: index/startups)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be created without writing files"
    )

    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)

    if not args.schema.exists():
        print(f"Error: Schema file not found: {args.schema}")
        sys.exit(1)

    import_startups(args.input, args.schema, args.output_dir, args.dry_run)


if __name__ == "__main__":
    main()
