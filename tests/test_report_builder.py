import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lifecycle.report_builder import build_markdown_report, write_report_bundle


def sample_report() -> dict:
    return {
        "workflow": "onboarding",
        "simulation_mode": True,
        "subject": {
            "display_name": "Priya Shah",
            "work_email": "priya.shah@example.invalid",
            "department": "Engineering",
        },
        "summary": [
            "Validated onboarding record",
            "Prepared Microsoft 365 license assignment",
        ],
        "licenses": [{"sku": "M365_BUSINESS_PREMIUM", "display_name": "Microsoft 365 Business Premium"}],
        "groups": ["group-start2-engineering", "group-start2-europe"],
        "tool_payloads": [
            {"tool": "Slack", "action": "create_member", "payload": {"email": "priya.shah@example.invalid"}}
        ],
        "recommendations": ["Review all simulated actions before production enablement."],
    }


class ReportBuilderTests(unittest.TestCase):
    def test_build_markdown_report_includes_simulation_status_and_actions(self) -> None:
        markdown = build_markdown_report(sample_report())

        self.assertIn("# Onboarding Report - Priya Shah", markdown)
        self.assertIn("**Execution mode:** Simulation", markdown)
        self.assertIn("group-start2-engineering", markdown)
        self.assertIn("Slack", markdown)
        self.assertIn("Microsoft 365 Business Premium", markdown)

    def test_write_report_bundle_creates_markdown_and_json(self) -> None:
        with TemporaryDirectory() as directory:
            paths = write_report_bundle(sample_report(), Path(directory), "onboarding-report-test")

            self.assertTrue(paths["markdown"].exists())
            self.assertTrue(paths["json"].exists())
            self.assertTrue(paths["markdown"].read_text(encoding="utf-8").startswith("# Onboarding Report"))
            written_json = json.loads(paths["json"].read_text(encoding="utf-8"))
            self.assertEqual(written_json["subject"]["work_email"], "priya.shah@example.invalid")


if __name__ == "__main__":
    unittest.main()
