import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lifecycle.validators import (
    ValidationError,
    generate_standard_upn,
    validate_offboarding_record,
    validate_onboarding_record,
)


class ValidatorTests(unittest.TestCase):
    def test_validate_onboarding_record_normalizes_required_fields(self) -> None:
        record = validate_onboarding_record(
            {
                "first_name": "  Priya ",
                "last_name": " Shah ",
                "display_name": " Priya Shah ",
                "work_email": " priya.shah@example.invalid ",
                "department": "Engineering",
                "job_title": "Cloud Automation Engineer",
                "region": "Europe",
                "location": "Berlin",
                "employment_type": "Full-time",
                "manager": "Alex Morgan",
                "start_date": "2026-07-15",
            }
        )

        self.assertEqual(record["first_name"], "Priya")
        self.assertEqual(record["work_email"], "priya.shah@example.invalid")
        self.assertEqual(record["start_date"], "2026-07-15")

    def test_validate_onboarding_record_rejects_missing_and_invalid_fields(self) -> None:
        with self.assertRaises(ValidationError) as context:
            validate_onboarding_record(
                {
                    "first_name": "Priya",
                    "last_name": "",
                    "display_name": "Priya Shah",
                    "work_email": "not-an-email",
                    "department": "Engineering",
                    "job_title": "Cloud Automation Engineer",
                    "region": "Europe",
                    "location": "Berlin",
                    "employment_type": "Full-time",
                    "manager": "Alex Morgan",
                    "start_date": "07/15/2026",
                }
            )

        message = str(context.exception)
        self.assertIn("last_name is required", message)
        self.assertIn("work_email must be a valid email address", message)
        self.assertIn("start_date must use YYYY-MM-DD format", message)

    def test_validate_offboarding_record_requires_ticket_and_iso_date(self) -> None:
        record = validate_offboarding_record(
            {
                "work_email": "priya.shah@example.invalid",
                "last_working_day": "2026-12-31",
                "manager": "Alex Morgan",
                "offboarding_type": "Voluntary",
                "ticket_id": "ITSM-1001",
            }
        )

        self.assertEqual(record["ticket_id"], "ITSM-1001")

    def test_generate_standard_upn_sanitizes_names_and_domain(self) -> None:
        self.assertEqual(
            generate_standard_upn(" Élodie ", " O'Connor-Smith ", "Example.Invalid"),
            "elodie.oconnor-smith@example.invalid",
        )


if __name__ == "__main__":
    unittest.main()
