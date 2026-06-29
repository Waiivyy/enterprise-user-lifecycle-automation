# Security Policy

This repository is a public-safe lifecycle automation demo. It must not contain real tenant data, secrets, production domains, client IDs, tenant IDs, API keys, or production endpoints.

## Supported Security Model

- Simulation mode is the default and only supported execution mode in this repository.
- Microsoft Graph actions are represented as mock JSON records.
- PowerShell scripts intentionally block `-ProductionMode`.
- Sample identities use `example.invalid`.
- Group IDs are readable fake identifiers.

## Reporting a Security Issue

If you find real secrets, production identifiers, or unsafe live-execution behavior in this repository, remove them from your local copy and open an issue describing the file path and risk without pasting the sensitive value.

## Adapting This Demo

For a real tenant or private lab, add a separate production adapter and keep secrets outside Git. Use environment variables, a cloud secret store, or managed identities. Require explicit approval gates before any account disablement, group removal, license removal, or SaaS deprovisioning action.
