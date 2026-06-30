# Roadmap Issue Ideas

These are suggested future GitHub issues for extending the demo without changing its public-safe simulation model.

## Add FastAPI Demo Endpoint

Create optional local API endpoints for onboarding and offboarding workflow planning.

- Keep it disabled by default.
- Accept the same CSV/JSON-shaped payloads used by the CLI.
- Return the same report structure currently written by `report_builder.py`.
- Do not add authentication or production Graph calls.

## Add HTML Report Rendering

Generate simple HTML versions of onboarding and offboarding reports.

- Keep Markdown and JSON as the source of truth.
- Use static HTML with no external dependencies where possible.
- Include simulation mode and security disclaimers in the rendered page.

## Add Optional Azure Functions Folder

Add an Azure Functions-style folder layout for a future queue or HTTP-triggered workflow.

- Keep it runnable locally without Azure.
- Document required environment variables as placeholders only.
- Do not add real tenant IDs, app IDs, or secrets.

## Add Graph Adapter Interface

Define an interface for a future Microsoft Graph adapter while keeping `MockGraphClient` as the only implementation in this public repo.

- Keep live execution disabled.
- Document permission boundaries and approval gates.
- Add tests that prove workflow modules can use the adapter contract.

## Add Policy Validation For License And Group Mappings

Add checks that detect risky or inconsistent mapping rules.

- Flag unknown departments, regions, locations, and employment types.
- Detect duplicate groups.
- Validate that contractor or intern access is intentionally limited.

## Add Sample GitHub Pages Project Site

Create a lightweight GitHub Pages site for technical review.

- Include architecture diagram, sample terminal output, and links to reports.
- Keep the site static.
- Avoid adding unnecessary frontend frameworks.
