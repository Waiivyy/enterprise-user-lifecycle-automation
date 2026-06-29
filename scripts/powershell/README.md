# PowerShell Scripts

The PowerShell scripts mirror common Microsoft 365 and Entra ID lifecycle automation tasks:

- `Invoke-Onboarding.ps1` reads onboarding CSV records and prints simulated account, group, and license actions.
- `Invoke-Offboarding.ps1` reads offboarding CSV records and prints simulated account-disablement actions.
- `Set-UserGroups.ps1` resolves fake Entra ID group IDs from department, region, and location.
- `Set-UserLicenses.ps1` resolves example Microsoft 365 license assignments.
- `Disable-UserAccess.ps1` prints Microsoft Graph-style offboarding actions.

## Safety Model

Production execution is intentionally disabled. The `-ProductionMode` switch exists only to make that boundary explicit; every script throws if it is used.

```powershell
./Invoke-Onboarding.ps1 -UserCsvPath ../../data/sample-users.csv
./Invoke-Offboarding.ps1 -OffboardingCsvPath ../../data/sample-offboarding.csv
```

No tenant IDs, app registrations, secrets, real domains, or production endpoints are included.
