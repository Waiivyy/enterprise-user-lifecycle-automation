# Offboarding Report - priya.shah@example.invalid

**Execution mode:** Simulation
**Generated at:** 2026-06-30T13:57:32+00:00

> This report is generated from mock data and is safe for public demo repositories.

## Summary

- Validated offboarding record
- Prepared sign-in disablement
- Prepared session revocation
- Listed licenses and groups for removal
- Generated SaaS deprovisioning payloads from configuration
- Prepared Microsoft Graph actions in simulation mode

## Subject

| Field | Value |
| --- | --- |
| work_email | priya.shah@example.invalid |
| last_working_day | 2026-12-31 |
| manager | Alex Morgan |
| offboarding_type | Voluntary |
| ticket_id | ITSM-1001 |

## Licenses

```json
[
  {
    "action": "remove",
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
    "action": "deactivate_member",
    "payload": {
      "email": "priya.shah@example.invalid",
      "lastWorkingDay": "2026-12-31",
      "manager": "Alex Morgan",
      "offboardingType": "Voluntary",
      "ticketId": "ITSM-1001"
    },
    "tool": "Slack"
  },
  {
    "action": "transfer_and_deactivate",
    "payload": {
      "email": "priya.shah@example.invalid",
      "lastWorkingDay": "2026-12-31",
      "manager": "Alex Morgan",
      "offboardingType": "Voluntary",
      "ticketId": "ITSM-1001"
    },
    "tool": "Box"
  },
  {
    "action": "deactivate_user",
    "payload": {
      "email": "priya.shah@example.invalid",
      "lastWorkingDay": "2026-12-31",
      "manager": "Alex Morgan",
      "offboardingType": "Voluntary",
      "ticketId": "ITSM-1001"
    },
    "tool": "Zoom"
  },
  {
    "action": "remove_member",
    "payload": {
      "email": "priya.shah@example.invalid",
      "lastWorkingDay": "2026-12-31",
      "manager": "Alex Morgan",
      "offboardingType": "Voluntary",
      "ticketId": "ITSM-1001"
    },
    "tool": "Notion"
  },
  {
    "action": "mark_assets_for_return",
    "payload": {
      "email": "priya.shah@example.invalid",
      "lastWorkingDay": "2026-12-31",
      "manager": "Alex Morgan",
      "offboardingType": "Voluntary",
      "ticketId": "ITSM-1001"
    },
    "tool": "Snipe-IT"
  }
]
```

## Microsoft Graph Simulation Actions

```json
[
  {
    "endpoint": "/users/priya.shah@example.invalid",
    "method": "PATCH",
    "payload": {
      "accountEnabled": false
    },
    "simulation": true,
    "status": "mocked"
  },
  {
    "endpoint": "/users/priya.shah@example.invalid/revokeSignInSessions",
    "method": "POST",
    "payload": {},
    "simulation": true,
    "status": "mocked"
  },
  {
    "endpoint": "/users/priya.shah@example.invalid/assignLicense",
    "method": "POST",
    "payload": {
      "addLicenses": [],
      "removeLicenses": [
        "M365_BUSINESS_PREMIUM"
      ]
    },
    "simulation": true,
    "status": "mocked"
  },
  {
    "endpoint": "/groups/group-start2-engineering/members/priya.shah@example.invalid/$ref",
    "method": "DELETE",
    "payload": {},
    "simulation": true,
    "status": "mocked"
  },
  {
    "endpoint": "/groups/group-start2-github-engineering/members/priya.shah@example.invalid/$ref",
    "method": "DELETE",
    "payload": {},
    "simulation": true,
    "status": "mocked"
  },
  {
    "endpoint": "/groups/group-start2-europe/members/priya.shah@example.invalid/$ref",
    "method": "DELETE",
    "payload": {},
    "simulation": true,
    "status": "mocked"
  },
  {
    "endpoint": "/groups/group-start2-office-berlin/members/priya.shah@example.invalid/$ref",
    "method": "DELETE",
    "payload": {},
    "simulation": true,
    "status": "mocked"
  }
]
```

## Mailbox Recommendations

| Field | Value |
| --- | --- |
| recommended_delegate | Alex Morgan |
| forwarding | Review business requirement before enabling forwarding. |
| retention | Apply legal hold or retention policy only when approved. |

## Recommendations

- Confirm mailbox delegation or forwarding with manager Alex Morgan.
- Export required audit metadata before deleting or purging any account data.
- Review offboarding actions with the ticket owner before production execution.
