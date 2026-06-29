"""Onboarding workflow planning."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any

from lifecycle.config_loader import LifecycleConfig
from lifecycle.graph_client_mock import MockGraphClient
from lifecycle.tool_payloads import build_provisioning_payloads
from lifecycle.validators import generate_standard_upn, validate_onboarding_record


def build_onboarding_plan(
    record: dict[str, Any],
    config: LifecycleConfig,
    graph_client: MockGraphClient | None = None,
) -> dict[str, Any]:
    """Build a complete, mock-safe onboarding plan for one user."""

    user = validate_onboarding_record(record)
    client = graph_client or MockGraphClient()
    user_principal_name = generate_standard_upn(
        user["first_name"],
        user["last_name"],
        config.tenant_domain,
    )
    license_assignment = config.license_for(user["employment_type"])
    groups = config.groups_for(user["department"], user["region"], user["location"])
    tool_payloads = build_provisioning_payloads(user, user_principal_name, config)

    graph_actions = [
        client.create_user(
            {
                "displayName": user["display_name"],
                "givenName": user["first_name"],
                "surname": user["last_name"],
                "userPrincipalName": user_principal_name,
                "mailNickname": user_principal_name.split("@", 1)[0],
                "accountEnabled": True,
                "department": user["department"],
                "jobTitle": user["job_title"],
                "usageLocation": user["region"],
            }
        ),
        client.assign_license(user_principal_name, str(license_assignment.get("sku", "UNMAPPED_LICENSE"))),
    ]
    graph_actions.extend(client.add_user_to_group(user_principal_name, group) for group in groups)

    return {
        "workflow": "onboarding",
        "generated_at": _utc_now(),
        "simulation_mode": config.simulation_mode,
        "subject": user,
        "account": {
            "user_principal_name": user_principal_name,
            "mail_nickname": user_principal_name.split("@", 1)[0],
        },
        "licenses": [license_assignment],
        "groups": groups,
        "tool_payloads": tool_payloads,
        "graph_actions": graph_actions,
        "summary": [
            "Validated onboarding record",
            "Generated standardized UPN",
            "Resolved license assignment",
            "Resolved Entra ID group assignments",
            "Generated SaaS provisioning payloads from configuration",
            "Prepared Microsoft Graph actions in simulation mode",
        ],
        "recommendations": [
            "Review generated groups and license selections before production execution.",
            "Store production Graph credentials in environment variables or managed identity.",
        ],
    }


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
