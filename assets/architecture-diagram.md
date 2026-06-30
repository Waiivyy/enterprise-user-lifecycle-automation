# Architecture Diagram

```mermaid
flowchart LR
    input["CSV / JSON input"]
    validation["Input validation"]
    config["Config mapping<br/>groups, licenses, SaaS tools"]
    planner["Onboarding / offboarding planner"]
    graph["Mock Microsoft Graph actions"]
    saas["SaaS payloads<br/>Slack, Box, Zoom, Notion, Snipe-IT"]
    reports["Markdown / JSON reports"]

    input --> validation
    validation --> config
    config --> planner
    planner --> graph
    planner --> saas
    graph --> reports
    saas --> reports
```

This diagram represents the simulation-first workflow. The project does not authenticate to Microsoft Graph or execute live tenant changes.
