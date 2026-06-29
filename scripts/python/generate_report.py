#!/usr/bin/env python3
"""Generate sample onboarding and offboarding reports from bundled demo data."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(ROOT / "src"))

from lifecycle.config_loader import load_lifecycle_config
from lifecycle.graph_client_mock import MockGraphClient
from lifecycle.offboarding import build_offboarding_plan
from lifecycle.onboarding import build_onboarding_plan
from lifecycle.report_builder import write_report_bundle
from lifecycle_cli import _load_json, _load_records


def main() -> int:
    config = load_lifecycle_config(ROOT / "config")
    graph_client = MockGraphClient(_load_json(ROOT / "data" / "mock-graph-responses.json"))

    onboarding_record = _load_records(ROOT / "data" / "sample-users.csv")[0]
    onboarding_report = build_onboarding_plan(onboarding_record, config, graph_client)
    onboarding_paths = write_report_bundle(onboarding_report, ROOT / "reports", "onboarding-report-sample")

    offboarding_record = _load_records(ROOT / "data" / "sample-offboarding.csv")[0]
    offboarding_report = build_offboarding_plan(offboarding_record, config, graph_client)
    offboarding_paths = write_report_bundle(offboarding_report, ROOT / "reports", "offboarding-report-sample")

    print(f"Wrote {onboarding_paths['markdown']}")
    print(f"Wrote {onboarding_paths['json']}")
    print(f"Wrote {offboarding_paths['markdown']}")
    print(f"Wrote {offboarding_paths['json']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
