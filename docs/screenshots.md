# Screenshots and Sample Outputs

This repository is CLI-first, so the strongest portfolio visuals are terminal output, generated reports, and the architecture diagram.

## Generate Demo Outputs Locally

From the repository root:

```bash
python3 scripts/python/lifecycle_cli.py onboard --input data/sample-users.csv
python3 scripts/python/lifecycle_cli.py offboard --input data/sample-offboarding.csv
python3 scripts/python/generate_report.py
```

The commands generate Markdown and JSON reports in `reports/`.

## Example Terminal Output

```text
Workflow: onboarding
Subject: Priya Shah <priya.shah@example.invalid>
Mode: simulation
Groups: 4
SaaS payloads: 5
Markdown report: reports/onboarding-report-01-priya-shah-at-example-invalid.md
JSON report: reports/onboarding-report-01-priya-shah-at-example-invalid.json

Workflow: offboarding
Subject: priya.shah@example.invalid <priya.shah@example.invalid>
Mode: simulation
Groups: 4
SaaS payloads: 5
Markdown report: reports/offboarding-report-01-priya-shah-at-example-invalid.md
JSON report: reports/offboarding-report-01-priya-shah-at-example-invalid.json
```

## Example Report Output

```markdown
# Onboarding Report - Priya Shah

**Execution mode:** Simulation

## Summary

- Validated onboarding record
- Generated standardized UPN
- Resolved license assignment
- Resolved Entra ID group assignments
- Generated SaaS provisioning payloads from configuration
- Prepared Microsoft Graph actions in simulation mode

## Groups

- group-start2-engineering
- group-start2-github-engineering
- group-start2-europe
- group-start2-office-berlin
```

## Suggested Screenshots For LinkedIn Featured

Capture these visuals:

1. GitHub repository home page with the README title, badges, and Quick Demo section visible.
2. Terminal showing onboarding and offboarding demo output.
3. `reports/onboarding-report-sample.md` rendered in GitHub.
4. `assets/architecture-diagram.svg` rendered in GitHub.
5. `docs/security-considerations.md` showing simulation mode and production-hardening notes.

## Visual Assets

- [Mermaid architecture diagram](../assets/architecture-diagram.md)
- [SVG architecture diagram](../assets/architecture-diagram.svg)
- [Demo terminal output](../assets/demo-output.md)
- [LinkedIn Featured description](../assets/linkedin-featured-description.md)
