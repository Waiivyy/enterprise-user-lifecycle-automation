#!/usr/bin/env python3
"""Validate onboarding or offboarding CSV/JSON files."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from lifecycle.validators import ValidationError, validate_offboarding_record, validate_onboarding_record
from lifecycle_cli import _load_records


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate lifecycle input data")
    parser.add_argument("workflow", choices=("onboarding", "offboarding"), help="Record type to validate")
    parser.add_argument("--input", required=True, help="CSV or JSON input file")
    args = parser.parse_args()

    validator = validate_onboarding_record if args.workflow == "onboarding" else validate_offboarding_record
    failed = False
    for index, record in enumerate(_load_records(Path(args.input)), start=1):
        try:
            validator(record)
            print(f"row {index}: valid")
        except ValidationError as exc:
            failed = True
            print(f"row {index}: invalid - {exc}", file=sys.stderr)

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
