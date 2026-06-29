# Security Considerations

This repository is safe for public GitHub by design. It uses mock users, mock domains, fake group IDs, fake response payloads, and simulation-only execution. No cloud resource is created, modified, or deleted.

## Never Commit Secrets

Do not commit API keys, client secrets, certificates, private keys, refresh tokens, tenant IDs, real app registration IDs, or production configuration files.

Use `.env`, local secret stores, CI secret stores, or cloud-native secret services for real deployments.

## Use Environment Variables

If this demo is adapted for a lab tenant, load sensitive values from environment variables or a managed identity. Do not place secrets in JSON config files.

## Apply Least Privilege

Microsoft Graph application permissions can be powerful. Use the narrowest delegated or application permissions possible, separate read and write roles, and review admin consent carefully.

For a real implementation, separate duties by workflow stage. For example, a reporting workflow may only need read permissions, while a tightly controlled offboarding workflow may need write permissions for account state, group membership, and license assignment.

## Prefer Managed Identities in Azure

For Azure Functions or other Azure-hosted workers, prefer managed identities over stored credentials. Assign only the permissions required for the workflow.

## Log Only Non-Sensitive Metadata

Reports should avoid sensitive HR details, personal data beyond the minimum needed for the workflow, and raw access tokens. Keep audit logs focused on ticket IDs, action types, timestamps, and non-sensitive status.

## Separate Simulation and Production Modes

Simulation mode must be the default. Production execution should require explicit configuration, strong validation, approval checks, and clear operational runbooks.

In this repository, production mode is intentionally disabled.

## Production Adapter Requirements

Before adding a real Microsoft Graph adapter in a private repository, require:

- A dedicated service principal or managed identity.
- Explicit environment selection such as `LAB`, `STAGING`, or `PRODUCTION`.
- A dry-run summary before any write action.
- Change ticket validation for offboarding actions.
- Positive approval for destructive operations such as sign-in disablement, group removal, and license removal.
- Rate-limit and retry handling that does not hide failed identity actions.
- Audit logs that avoid sensitive payloads and raw tokens.

## Review Offboarding Actions Before Execution

Offboarding can be disruptive. Review account disablement, mailbox delegation, forwarding, license removal, group removal, and SaaS deprovisioning before any production execution.

## Public Repository Safety Checklist

- Use `example.invalid` for email domains.
- Use readable fake IDs such as `group-start2-engineering`.
- Keep mock Graph responses in `data/`.
- Keep local-only settings out of Git.
- Keep generated ad hoc reports out of Git unless they are sanitized samples.
- Review generated reports before committing them.
