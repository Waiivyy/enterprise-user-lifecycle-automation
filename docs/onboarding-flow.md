# Onboarding Flow

The onboarding workflow accepts CSV or JSON records with these fields:

| Field | Purpose |
| --- | --- |
| `first_name` | Given name used for account generation. |
| `last_name` | Surname used for account generation. |
| `display_name` | Human-readable name for reports and payloads. |
| `work_email` | Mock work email used for SaaS payloads. |
| `department` | Used for group and SaaS access mapping. |
| `job_title` | Included in user and SaaS payloads. |
| `region` | Used for regional group mapping. |
| `location` | Used for office or remote group mapping. |
| `employment_type` | Used for Microsoft 365 license mapping. |
| `manager` | Included in reports and SaaS payloads. |
| `start_date` | Validated as `YYYY-MM-DD`. |

## Steps

1. Validate all required fields.
2. Normalize whitespace and email casing.
3. Generate a standardized UPN from first name, last name, and the mock tenant domain.
4. Resolve the Microsoft 365 license from `license-map.example.json`.
5. Resolve Entra ID groups from department, region, and location mappings.
6. Generate provisioning payloads for Slack, Box, Zoom, Notion, and Snipe-IT through `tool_payloads.py`.
7. Prepare Microsoft Graph-style actions in simulation mode.
8. Write Markdown and JSON reports.

## Example

```bash
python3 scripts/python/lifecycle_cli.py onboard --input data/sample-users.csv
```

The output report includes the generated UPN, selected license, group list, SaaS payloads, mock Graph actions, and review recommendations.
