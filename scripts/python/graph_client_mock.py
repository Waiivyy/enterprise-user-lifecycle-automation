#!/usr/bin/env python3
"""Small utility showing the mock Graph client response shape."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from lifecycle.graph_client_mock import MockGraphClient


def main() -> int:
    client = MockGraphClient()
    response = client.disable_sign_in("sample.user@example.invalid")
    print(json.dumps(response, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
