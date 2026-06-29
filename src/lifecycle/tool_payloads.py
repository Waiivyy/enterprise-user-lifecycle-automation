"""SaaS provisioning and deprovisioning payload builders."""

from __future__ import annotations

from typing import Any

from lifecycle.config_loader import LifecycleConfig


def build_provisioning_payloads(
    user: dict[str, str],
    user_principal_name: str,
    config: LifecycleConfig,
) -> list[dict[str, Any]]:
    """Build SaaS provisioning payloads from enabled tool configuration."""

    payloads: list[dict[str, Any]] = []
    for tool in config.tool_specs():
        payloads.append(
            {
                "tool": tool["name"],
                "action": str(tool.get("provisioning_action", "provision_user")),
                "payload": {
                    "email": user["work_email"],
                    "userPrincipalName": user_principal_name,
                    "displayName": user["display_name"],
                    "department": user["department"],
                    "jobTitle": user["job_title"],
                    "manager": user["manager"],
                    "location": user["location"],
                    "accessProfile": _access_profile_for_department(tool, user["department"]),
                },
            }
        )
    return payloads


def build_deprovisioning_payloads(
    user: dict[str, str],
    config: LifecycleConfig,
) -> list[dict[str, Any]]:
    """Build SaaS deprovisioning payloads from enabled tool configuration."""

    payloads: list[dict[str, Any]] = []
    for tool in config.tool_specs():
        payloads.append(
            {
                "tool": tool["name"],
                "action": str(tool.get("deprovisioning_action", "deprovision_user")),
                "payload": {
                    "email": user["work_email"],
                    "ticketId": user["ticket_id"],
                    "lastWorkingDay": user["last_working_day"],
                    "offboardingType": user["offboarding_type"],
                    "manager": user["manager"],
                },
            }
        )
    return payloads


def _access_profile_for_department(tool: dict[str, Any], department: str) -> str:
    access_profiles = tool.get("access_by_department", {})
    if isinstance(access_profiles, dict):
        return str(access_profiles.get(department, "standard"))
    return "standard"
