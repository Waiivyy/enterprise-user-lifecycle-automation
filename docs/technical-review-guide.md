# Technical Review Guide

This project is designed to show practical enterprise automation judgment without claiming production readiness.

## What This Project Demonstrates

Enterprise User Lifecycle Automation models a common IT operations workflow: preparing onboarding and offboarding actions across identity, licensing, groups, SaaS tools, and reporting.

It demonstrates:

- Python orchestration for lifecycle workflow planning.
- PowerShell scripts shaped like Microsoft 365 and Entra administration tasks.
- Microsoft Graph-style action modeling through a mock client.
- Configuration-driven access mapping for departments, regions, locations, licenses, and tools.
- Markdown and JSON audit-style reporting.
- CI-backed tests and public repository hygiene.

## What To Review First

1. [README.md](../README.md) for scope, quick demo commands, architecture, and security boundaries.
2. [assets/architecture-diagram.svg](../assets/architecture-diagram.svg) for the visual workflow.
3. [src/lifecycle/onboarding.py](../src/lifecycle/onboarding.py) for onboarding planning.
4. [src/lifecycle/offboarding.py](../src/lifecycle/offboarding.py) for offboarding planning.
5. [src/lifecycle/graph_client_mock.py](../src/lifecycle/graph_client_mock.py) for Microsoft Graph simulation.
6. [src/lifecycle/tool_payloads.py](../src/lifecycle/tool_payloads.py) for SaaS payload generation.
7. [scripts/powershell/](../scripts/powershell) for PowerShell automation examples.
8. [reports/onboarding-report-sample.md](../reports/onboarding-report-sample.md) for generated output.
9. [tests/](../tests) for validation and regression coverage.

## Why It Is Public-Safe

- Sample identities use `example.invalid`.
- Group IDs are fake readable identifiers.
- Microsoft Graph actions are structured mock records, not live API calls.
- PowerShell production mode is intentionally blocked.
- No tenant IDs, client IDs, API keys, secrets, or production endpoints are included.

## Why Simulation Mode Is Intentional

Identity lifecycle automation can disable access, remove licenses, change group membership, and trigger SaaS deprovisioning. A public lab project should demonstrate design, validation, reporting, and safety boundaries without performing real tenant changes.

Simulation mode makes the workflow reviewable while keeping the repository safe to clone, run, and inspect.

## Engineering Signals

| Signal | Where To Look |
| --- | --- |
| Python structure | `src/lifecycle/` |
| PowerShell automation style | `scripts/powershell/` |
| Microsoft Graph concepts | `src/lifecycle/graph_client_mock.py` |
| Configuration-driven access | `config/*.example.json` |
| Test coverage | `tests/` |
| Reporting output | `reports/*sample*` |
| Security posture | `SECURITY.md` and `docs/security-considerations.md` |
| Visual project assets | `assets/` |

## What This Project Is Not

This is not a shipped enterprise platform, a live Microsoft 365 integration, or a production offboarding tool. It is a realistic demo that illustrates the design shape and safety practices an engineer would use before building a tenant-connected implementation.
