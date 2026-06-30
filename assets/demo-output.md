# Demo Output

Run:

```bash
python3 scripts/python/lifecycle_cli.py onboard --input data/sample-users.csv
python3 scripts/python/lifecycle_cli.py offboard --input data/sample-offboarding.csv
```

Example output:

```text
Workflow: onboarding
Subject: Priya Shah <priya.shah@example.invalid>
Mode: simulation
Groups: 4
SaaS payloads: 5
Markdown report: reports/onboarding-report-01-priya-shah-at-example-invalid.md
JSON report: reports/onboarding-report-01-priya-shah-at-example-invalid.json

Workflow: onboarding
Subject: Jordan Lee <jordan.lee@example.invalid>
Mode: simulation
Groups: 3
SaaS payloads: 5
Markdown report: reports/onboarding-report-02-jordan-lee-at-example-invalid.md
JSON report: reports/onboarding-report-02-jordan-lee-at-example-invalid.json

Workflow: offboarding
Subject: priya.shah@example.invalid <priya.shah@example.invalid>
Mode: simulation
Groups: 4
SaaS payloads: 5
Markdown report: reports/offboarding-report-01-priya-shah-at-example-invalid.md
JSON report: reports/offboarding-report-01-priya-shah-at-example-invalid.json

Workflow: offboarding
Subject: jordan.lee@example.invalid <jordan.lee@example.invalid>
Mode: simulation
Groups: 3
SaaS payloads: 5
Markdown report: reports/offboarding-report-02-jordan-lee-at-example-invalid.md
JSON report: reports/offboarding-report-02-jordan-lee-at-example-invalid.json
```
