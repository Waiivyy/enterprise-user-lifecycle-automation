# Offboarding Flow

The offboarding workflow accepts CSV or JSON records with these fields:

| Field | Purpose |
| --- | --- |
| `work_email` | Mock user email to offboard. |
| `last_working_day` | Validated as `YYYY-MM-DD`. |
| `manager` | Used for mailbox delegation recommendations. |
| `offboarding_type` | Captures voluntary, involuntary, contract end, or similar context. |
| `ticket_id` | Audit reference for the lifecycle request. |

## Steps

1. Validate all required fields.
2. Read mock Graph user state from `data/mock-graph-responses.json`.
3. Prepare sign-in disablement in simulation mode.
4. Prepare session revocation in simulation mode.
5. List licenses to remove.
6. List groups to remove.
7. Generate SaaS deprovisioning payloads through `tool_payloads.py`.
8. Generate mailbox delegation and forwarding recommendations.
9. Write Markdown and JSON reports.

## Example

```bash
python3 scripts/python/lifecycle_cli.py offboard --input data/sample-offboarding.csv
```

The output report includes access removal actions, SaaS deprovisioning payloads, mailbox recommendations, and audit-friendly ticket metadata.
