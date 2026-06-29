"""Offboarding workflow planning."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from lifecycle.config_loader import LifecycleConfig
from lifecycle.graph_client_mock import MockGraphClient
from lifecycle.tool_payloads import build_deprovisioning_payloads
from lifecycle.validators import validate_offboarding_record


def build_offboarding_plan(
    record: dict[str, Any],
    config: LifecycleConfig,
    graph_client: MockGraphClient | None = None,
) -> dict[str, Any]:
    """Build a complete, mock-safe offboarding plan for one user."""

    user = validate_offboarding_record(record)
    client = graph_client or MockGraphClient()
    snapshot = client.get_user_snapshot(user["work_email"])
    licenses = list(snapshot.get("assignedLicenses", ["M365_BUSINESS_PREMIUM"]))
    groups = list(snapshot.get("memberOf", ["group-start2-engineering", "group-start2-europe"]))
    tool_payloads = build_deprovisioning_payloads(user, config)

    graph_actions = [
        client.disable_sign_in(user["work_email"]),
        client.revoke_sessions(user["work_email"]),
    ]
    graph_actions.extend(client.remove_license(user["work_email"], str(license_sku)) for license_sku in licenses)
    graph_actions.extend(client.remove_from_group(user["work_email"], str(group_id)) for group_id in groups)

    return {
        "workflow": "offboarding",
        "generated_at": _utc_now(),
        "simulation_mode": config.simulation_mode,
        "subject": user,
        "licenses": [{"sku": license_sku, "action": "remove"} for license_sku in licenses],
        "groups": groups,
        "tool_payloads": tool_payloads,
        "graph_actions": graph_actions,
        "summary": [
            "Validated offboarding record",
            "Prepared sign-in disablement",
            "Prepared session revocation",
            "Listed licenses and groups for removal",
            "Generated SaaS deprovisioning payloads from configuration",
            "Prepared Microsoft Graph actions in simulation mode",
        ],
        "recommendations": [
            f"Confirm mailbox delegation or forwarding with manager {user['manager']}.",
            "Export required audit metadata before deleting or purging any account data.",
            "Review offboarding actions with the ticket owner before production execution.",
        ],
        "mailbox": {
            "recommended_delegate": user["manager"],
            "forwarding": "Review business requirement before enabling forwarding.",
            "retention": "Apply legal hold or retention policy only when approved.",
        },
    }


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
