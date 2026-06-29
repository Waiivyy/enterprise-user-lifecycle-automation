# Onboarding Report - Priya Shah

**Execution mode:** Simulation
**Generated at:** 2026-06-29T19:47:09+00:00

> This report is generated from mock data and is safe for public demo repositories.

## Summary

- Validated onboarding record
- Generated standardized UPN
- Resolved license assignment
- Resolved Entra ID group assignments
- Generated SaaS provisioning payloads from configuration
- Prepared Microsoft Graph actions in simulation mode

## Subject

| Field | Value |
| --- | --- |
| first_name | Priya |
| last_name | Shah |
| display_name | Priya Shah |
| work_email | priya.shah@example.invalid |
| department | Engineering |
| job_title | Cloud Automation Engineer |
| region | Europe |
| location | Berlin |
| employment_type | Full-time |
| manager | Alex Morgan |
| start_date | 2026-07-15 |

## Account

| Field | Value |
| --- | --- |
| user_principal_name | priya.shah@example.invalid |
| mail_nickname | priya.shah |

## Licenses

```json
[
  {
    "assignment_reason": "Default license for full-time employees",
    "display_name": "Microsoft 365 Business Premium",
    "sku": "M365_BUSINESS_PREMIUM"
  }
]
```

## Groups

- group-start2-engineering
- group-start2-github-engineering
- group-start2-europe
- group-start2-office-berlin

## SaaS Payloads

```json
[
  {
    "action": "create_member",
    "payload": {
      "accessProfile": "engineering-workspace",
      "department": "Engineering",
      "displayName": "Priya Shah",
      "email": "priya.shah@example.invalid",
      "jobTitle": "Cloud Automation Engineer",
      "location": "Berlin",
      "manager": "Alex Morgan",
      "userPrincipalName": "priya.shah@example.invalid"
    },
    "tool": "Slack"
  },
  {
    "action": "create_managed_user",
    "payload": {
      "accessProfile": "standard-collaboration",
      "department": "Engineering",
      "displayName": "Priya Shah",
      "email": "priya.shah@example.invalid",
      "jobTitle": "Cloud Automation Engineer",
      "location": "Berlin",
      "manager": "Alex Morgan",
      "userPrincipalName": "priya.shah@example.invalid"
    },
    "tool": "Box"
  },
  {
    "action": "create_basic_user",
    "payload": {
      "accessProfile": "standard",
      "department": "Engineering",
      "displayName": "Priya Shah",
      "email": "priya.shah@example.invalid",
      "jobTitle": "Cloud Automation Engineer",
      "location": "Berlin",
      "manager": "Alex Morgan",
      "userPrincipalName": "priya.shah@example.invalid"
    },
    "tool": "Zoom"
  },
  {
    "action": "invite_member",
    "payload": {
      "accessProfile": "engineering-teamspace",
      "department": "Engineering",
      "displayName": "Priya Shah",
      "email": "priya.shah@example.invalid",
      "jobTitle": "Cloud Automation Engineer",
      "location": "Berlin",
      "manager": "Alex Morgan",
      "userPrincipalName": "priya.shah@example.invalid"
    },
    "tool": "Notion"
  },
  {
    "action": "create_asset_user",
    "payload": {
      "accessProfile": "hardware-eligible",
      "department": "Engineering",
      "displayName": "Priya Shah",
      "email": "priya.shah@example.invalid",
      "jobTitle": "Cloud Automation Engineer",
      "location": "Berlin",
      "manager": "Alex Morgan",
      "userPrincipalName": "priya.shah@example.invalid"
    },
    "tool": "Snipe-IT"
  }
]
```

## Microsoft Graph Simulation Actions

```json
[
  {
    "endpoint": "/users",
    "method": "POST",
    "payload": {
      "accountEnabled": true,
      "department": "Engineering",
      "displayName": "Priya Shah",
      "givenName": "Priya",
      "jobTitle": "Cloud Automation Engineer",
      "mailNickname": "priya.shah",
      "surname": "Shah",
      "usageLocation": "Europe",
      "userPrincipalName": "priya.shah@example.invalid"
    },
    "simulation": true,
    "status": "mocked"
  },
  {
    "endpoint": "/users/priya.shah@example.invalid/assignLicense",
    "method": "POST",
    "payload": {
      "addLicenses": [
        {
          "skuId": "M365_BUSINESS_PREMIUM"
        }
      ],
      "removeLicenses": []
    },
    "simulation": true,
    "status": "mocked"
  },
  {
    "endpoint": "/groups/group-start2-engineering/members/$ref",
    "method": "POST",
    "payload": {
      "userPrincipalName": "priya.shah@example.invalid"
    },
    "simulation": true,
    "status": "mocked"
  },
  {
    "endpoint": "/groups/group-start2-github-engineering/members/$ref",
    "method": "POST",
    "payload": {
      "userPrincipalName": "priya.shah@example.invalid"
    },
    "simulation": true,
    "status": "mocked"
  },
  {
    "endpoint": "/groups/group-start2-europe/members/$ref",
    "method": "POST",
    "payload": {
      "userPrincipalName": "priya.shah@example.invalid"
    },
    "simulation": true,
    "status": "mocked"
  },
  {
    "endpoint": "/groups/group-start2-office-berlin/members/$ref",
    "method": "POST",
    "payload": {
      "userPrincipalName": "priya.shah@example.invalid"
    },
    "simulation": true,
    "status": "mocked"
  }
]
```

## Recommendations

- Review generated groups and license selections before production execution.
- Store production Graph credentials in environment variables or managed identity.
