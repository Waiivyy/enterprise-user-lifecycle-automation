<#
.SYNOPSIS
Generates simulated offboarding actions from a sample CSV file.

.DESCRIPTION
Reads offboarding records and prints the access-removal actions that would be reviewed
before a production offboarding workflow. This script does not disable accounts.

.PARAMETER OffboardingCsvPath
Path to a CSV file with offboarding fields.

.PARAMETER ProductionMode
Reserved for future lab use. Production execution is intentionally blocked in this demo.

.EXAMPLE
./Invoke-Offboarding.ps1 -OffboardingCsvPath ../../data/sample-offboarding.csv
#>

[CmdletBinding()]
param(
    [string]$OffboardingCsvPath = (Join-Path $PSScriptRoot "../../data/sample-offboarding.csv"),
    [switch]$ProductionMode
)

if ($ProductionMode) {
    throw "ProductionMode is intentionally disabled. This public lab project supports simulation only."
}

$records = Import-Csv -Path $OffboardingCsvPath

foreach ($record in $records) {
    Write-Host ""
    Write-Host "Offboarding simulation for $($record.work_email)"
    Write-Host "Ticket: $($record.ticket_id)"
    Write-Host "Last working day: $($record.last_working_day)"
    Write-Host "Planned actions:"
    Write-Host " - Disable sign-in"
    Write-Host " - Revoke active sessions"
    Write-Host " - Review licenses for removal"
    Write-Host " - Review group memberships for removal"
    Write-Host " - Confirm mailbox delegation with $($record.manager)"
    Write-Host "No live Graph or Microsoft 365 action was executed."
}
