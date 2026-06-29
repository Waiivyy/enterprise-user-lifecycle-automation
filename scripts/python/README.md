# Python Scripts

These scripts provide local orchestration and reporting for the demo lifecycle workflows.

## Commands

```bash
python3 scripts/python/validate_user_data.py onboarding --input data/sample-users.csv
python3 scripts/python/validate_user_data.py offboarding --input data/sample-offboarding.csv
python3 scripts/python/lifecycle_cli.py onboard --input data/sample-users.csv
python3 scripts/python/lifecycle_cli.py offboard --input data/sample-offboarding.csv
python3 scripts/python/generate_report.py
```

All commands use mock data and simulation mode by default. No Microsoft Graph calls are made.

## Notes

- `lifecycle_cli.py` is the main operator-facing entry point.
- `generate_report.py` refreshes the committed sample reports.
- `graph_client_mock.py` prints an example Graph-style simulation response for quick inspection.
