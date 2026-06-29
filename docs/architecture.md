# Architecture

Enterprise User Lifecycle Automation is organized around a simulation-first lifecycle pipeline.

## Components

| Component | Responsibility |
| --- | --- |
| `src/lifecycle/validators.py` | Validates onboarding and offboarding input records. |
| `src/lifecycle/config_loader.py` | Loads JSON mappings for groups, licenses, SaaS tools, and settings. |
| `src/lifecycle/onboarding.py` | Builds account, license, group, SaaS, and mock Graph onboarding plans. |
| `src/lifecycle/offboarding.py` | Builds account-disablement, license-removal, group-removal, SaaS, and mailbox recommendation plans. |
| `src/lifecycle/tool_payloads.py` | Builds SaaS provisioning and deprovisioning payloads from enabled tool configuration. |
| `src/lifecycle/graph_client_mock.py` | Produces Microsoft Graph-style responses without network calls. |
| `src/lifecycle/report_builder.py` | Writes Markdown and JSON reports for audit review. |
| `scripts/python/` | Provides CLI orchestration, validation, and sample report generation. |
| `scripts/powershell/` | Demonstrates Microsoft 365 and Entra style administrator automation patterns. |

## Data Flow

```text
Input CSV or JSON
  -> validate required fields
  -> load JSON configuration
  -> resolve user lifecycle actions
  -> build SaaS payloads from tool mappings
  -> create mock Graph action list
  -> write Markdown and JSON reports
```

## Configuration Driven Design

The workflow is intentionally driven by configuration files in `config/`:

- `department-group-map.example.json` maps departments, regions, and locations to fake group IDs.
- `license-map.example.json` maps employment types to example Microsoft 365 license SKUs.
- `tool-access-map.example.json` maps SaaS tools to provisioning and deprovisioning actions.
- `settings.example.json` keeps simulation mode enabled and uses mock endpoints only.

## Simulation Boundary

All Graph actions are represented as structured JSON with:

- HTTP method
- Mock endpoint
- Payload
- `simulation: true`
- `status: mocked`

This keeps the code close to real enterprise integration patterns without executing live tenant changes.

## Module Boundaries

The Python package separates workflow planning from integration boundaries:

- Workflow modules decide what should happen for onboarding or offboarding.
- `tool_payloads.py` converts workflow context into third-party SaaS request payloads.
- `graph_client_mock.py` converts workflow intent into Microsoft Graph-style simulation records.
- `report_builder.py` renders the result for human review.

That split makes it easier to replace the mock Graph client or add a real adapter in a private lab without mixing credential handling into workflow logic.

## Local Execution

The repository runs locally without Azure, Microsoft Graph credentials, or a database. Reports are generated into `reports/`, and tests use Python's standard library test runner.
