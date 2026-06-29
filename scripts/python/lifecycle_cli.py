#!/usr/bin/env python3
"""CLI entry point for onboarding and offboarding demo workflows."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from lifecycle.config_loader import ConfigError, load_lifecycle_config
from lifecycle.graph_client_mock import MockGraphClient
from lifecycle.offboarding import build_offboarding_plan
from lifecycle.onboarding import build_onboarding_plan
from lifecycle.report_builder import write_report_bundle
from lifecycle.validators import ValidationError


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise user lifecycle automation demo CLI")
    _add_shared_options(parser)

    subparsers = parser.add_subparsers(dest="workflow", required=True)
    onboarding = subparsers.add_parser("onboard", help="Generate onboarding reports")
    _add_shared_options(onboarding, after_subcommand=True)
    onboarding.add_argument("--input", required=True, help="CSV or JSON onboarding input file")

    offboarding = subparsers.add_parser("offboard", help="Generate offboarding reports")
    _add_shared_options(offboarding, after_subcommand=True)
    offboarding.add_argument("--input", required=True, help="CSV or JSON offboarding input file")

    args = parser.parse_args()

    try:
        config = load_lifecycle_config(args.config_dir)
        mock_data = _load_json(Path(args.mock_graph_data)) if Path(args.mock_graph_data).exists() else {}
        graph_client = MockGraphClient(mock_data)
        records = _load_records(Path(args.input))

        for index, record in enumerate(records, start=1):
            if args.workflow == "onboard":
                report = build_onboarding_plan(record, config, graph_client)
                base_name = _safe_report_name("onboarding-report", report["subject"]["work_email"], index)
            else:
                report = build_offboarding_plan(record, config, graph_client)
                base_name = _safe_report_name("offboarding-report", report["subject"]["work_email"], index)

            paths = write_report_bundle(report, args.output_dir, base_name)
            _print_summary(report, paths)

    except (ConfigError, ValidationError, FileNotFoundError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


def _add_shared_options(parser: argparse.ArgumentParser, after_subcommand: bool = False) -> None:
    default = argparse.SUPPRESS if after_subcommand else None
    parser.add_argument(
        "--config-dir",
        default=default or str(ROOT / "config"),
        help="Path to example config directory",
    )
    parser.add_argument(
        "--output-dir",
        default=default or str(ROOT / "reports"),
        help="Directory for generated reports",
    )
    parser.add_argument(
        "--mock-graph-data",
        default=default or str(ROOT / "data" / "mock-graph-responses.json"),
        help="Mock Graph response JSON file",
    )


def _load_records(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")
    if path.suffix.lower() == ".csv":
        with path.open(newline="", encoding="utf-8") as handle:
            return list(csv.DictReader(handle))
    if path.suffix.lower() == ".json":
        payload = _load_json(path)
        if isinstance(payload, list):
            return [dict(item) for item in payload]
        if isinstance(payload, dict):
            return [payload]
    raise ValueError("Input file must be CSV, a JSON object, or a JSON array")


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _safe_report_name(prefix: str, work_email: str, index: int) -> str:
    safe_email = work_email.lower().replace("@", "-at-").replace(".", "-")
    return f"{prefix}-{index:02d}-{safe_email}"


def _print_summary(report: dict[str, Any], paths: dict[str, Path]) -> None:
    subject = report["subject"]
    mode = "simulation" if report.get("simulation_mode", True) else "production"
    subject_label = subject.get("display_name") or subject["work_email"]
    print("")
    print(f"Workflow: {report['workflow']}")
    print(f"Subject: {subject_label} <{subject['work_email']}>")
    print(f"Mode: {mode}")
    print(f"Groups: {len(report.get('groups', []))}")
    print(f"SaaS payloads: {len(report.get('tool_payloads', []))}")
    print(f"Markdown report: {paths['markdown']}")
    print(f"JSON report: {paths['json']}")


if __name__ == "__main__":
    raise SystemExit(main())
