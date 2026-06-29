import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


class LifecycleCliTests(unittest.TestCase):
    def test_onboarding_cli_accepts_output_dir_after_subcommand(self) -> None:
        root = Path(__file__).resolve().parents[1]
        with TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    sys.executable,
                    str(root / "scripts" / "python" / "lifecycle_cli.py"),
                    "onboard",
                    "--input",
                    str(root / "data" / "sample-users.csv"),
                    "--output-dir",
                    directory,
                ],
                cwd=root,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(list(Path(directory).glob("onboarding-report-*.md")))

    def test_offboarding_cli_uses_subject_label_in_summary(self) -> None:
        root = Path(__file__).resolve().parents[1]
        with TemporaryDirectory() as directory:
            result = subprocess.run(
                [
                    sys.executable,
                    str(root / "scripts" / "python" / "lifecycle_cli.py"),
                    "offboard",
                    "--input",
                    str(root / "data" / "sample-offboarding.csv"),
                    "--output-dir",
                    directory,
                ],
                cwd=root,
                capture_output=True,
                text=True,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Subject: priya.shah@example.invalid", result.stdout)
            self.assertNotIn("User: priya.shah@example.invalid", result.stdout)


if __name__ == "__main__":
    unittest.main()
