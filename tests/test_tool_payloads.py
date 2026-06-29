import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lifecycle.config_loader import LifecycleConfig
from lifecycle.tool_payloads import build_deprovisioning_payloads, build_provisioning_payloads


def config_with_tools() -> LifecycleConfig:
    return LifecycleConfig(
        department_groups={},
        region_groups={},
        location_groups={},
        license_map={},
        tool_map={
            "Slack": {
                "enabled": True,
                "provisioning_action": "create_member",
                "deprovisioning_action": "deactivate_member",
                "access_by_department": {"Engineering": "engineering-workspace"},
            },
            "Legacy CRM": {
                "enabled": False,
                "provisioning_action": "create_user",
                "deprovisioning_action": "disable_user",
            },
        },
        settings={"simulation_mode": True, "tenant_domain": "example.invalid"},
    )


class ToolPayloadTests(unittest.TestCase):
    def test_build_provisioning_payloads_uses_department_access_profile(self) -> None:
        payloads = build_provisioning_payloads(
            {
                "work_email": "priya.shah@example.invalid",
                "display_name": "Priya Shah",
                "department": "Engineering",
                "job_title": "Cloud Automation Engineer",
                "manager": "Alex Morgan",
                "location": "Berlin",
            },
            "priya.shah@example.invalid",
            config_with_tools(),
        )

        self.assertEqual(len(payloads), 1)
        self.assertEqual(payloads[0]["tool"], "Slack")
        self.assertEqual(payloads[0]["action"], "create_member")
        self.assertEqual(payloads[0]["payload"]["accessProfile"], "engineering-workspace")

    def test_build_deprovisioning_payloads_includes_ticket_context(self) -> None:
        payloads = build_deprovisioning_payloads(
            {
                "work_email": "priya.shah@example.invalid",
                "last_working_day": "2026-12-31",
                "manager": "Alex Morgan",
                "offboarding_type": "Voluntary",
                "ticket_id": "ITSM-1001",
            },
            config_with_tools(),
        )

        self.assertEqual(len(payloads), 1)
        self.assertEqual(payloads[0]["action"], "deactivate_member")
        self.assertEqual(payloads[0]["payload"]["ticketId"], "ITSM-1001")


if __name__ == "__main__":
    unittest.main()
