import json
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from lifecycle.config_loader import ConfigError, load_lifecycle_config


def write_json(path: Path, payload: dict) -> None:
    path.write_text(json.dumps(payload), encoding="utf-8")


class ConfigLoaderTests(unittest.TestCase):
    def test_load_lifecycle_config_loads_all_expected_maps(self) -> None:
        with TemporaryDirectory() as directory:
            config_dir = Path(directory)
            write_json(
                config_dir / "department-group-map.example.json",
                {
                    "departments": {"Engineering": ["group-start2-engineering"]},
                    "regions": {"Europe": ["group-start2-europe"]},
                    "locations": {"Berlin": ["group-start2-berlin"]},
                },
            )
            write_json(
                config_dir / "license-map.example.json",
                {
                    "employment_types": {
                        "Full-time": {
                            "sku": "M365_BUSINESS_PREMIUM",
                            "display_name": "Microsoft 365 Business Premium",
                        }
                    }
                },
            )
            write_json(
                config_dir / "tool-access-map.example.json",
                {
                    "tools": {
                        "Slack": {
                            "enabled": True,
                            "provisioning_action": "create_member",
                            "groups": ["Engineering"],
                        }
                    }
                },
            )
            write_json(
                config_dir / "settings.example.json",
                {
                    "simulation_mode": True,
                    "tenant_domain": "example.invalid",
                    "report_timezone": "UTC",
                },
            )

            config = load_lifecycle_config(config_dir)

            self.assertTrue(config.simulation_mode)
            self.assertEqual(config.tenant_domain, "example.invalid")
            self.assertEqual(config.department_groups["Engineering"], ["group-start2-engineering"])
            self.assertEqual(config.region_groups["Europe"], ["group-start2-europe"])
            self.assertEqual(config.location_groups["Berlin"], ["group-start2-berlin"])
            self.assertEqual(
                config.license_for("Full-time")["display_name"],
                "Microsoft 365 Business Premium",
            )
            self.assertEqual(config.tool_specs()[0]["name"], "Slack")
            self.assertEqual(config.enabled_tools()[0]["name"], "Slack")

    def test_load_lifecycle_config_rejects_missing_required_file(self) -> None:
        with TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ConfigError, "department-group-map.example.json"):
                load_lifecycle_config(Path(directory))


if __name__ == "__main__":
    unittest.main()
