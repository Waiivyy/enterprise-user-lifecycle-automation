# Recruiter Review Guide

This project is designed to show practical cloud and IT automation judgment without claiming production readiness.

## What To Review First

1. [README.md](../README.md) for scope, commands, architecture, and security boundaries.
2. [src/lifecycle/onboarding.py](../src/lifecycle/onboarding.py) for the onboarding workflow.
3. [src/lifecycle/offboarding.py](../src/lifecycle/offboarding.py) for the offboarding workflow.
4. [src/lifecycle/tool_payloads.py](../src/lifecycle/tool_payloads.py) for SaaS payload generation.
5. [reports/onboarding-report-sample.md](../reports/onboarding-report-sample.md) for the generated audit output.
6. [tests/](../tests) for validation and regression coverage.

## Engineering Signals

- Configuration-driven mapping rather than hard-coded access decisions.
- Simulation boundary around Microsoft Graph-style actions.
- Separate validation, workflow planning, SaaS payload generation, and reporting modules.
- PowerShell scripts that mirror administrator workflows while blocking production execution.
- Public repository hygiene: no real domains, tenant identifiers, app IDs, or secrets.

## What This Project Is Not

This is not a shipped enterprise platform, a live Microsoft 365 integration, or a production offboarding tool. It is a realistic demo that illustrates the design shape and safety practices an engineer would use before building a tenant-connected implementation.
