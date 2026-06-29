<#
.SYNOPSIS
Generates simulated onboarding actions from a sample CSV file.

.DESCRIPTION
Reads onboarding records, resolves example group and license mappings, and prints a clear
simulation summary. This script does not call Microsoft Graph or Microsoft 365 services.

.PARAMETER UserCsvPath
Path to a CSV file with onboarding fields.

.PARAMETER ConfigDirectory
Directory containing the example JSON configuration files.

.PARAMETER ProductionMode
Reserved for future lab use. Production execution is intentionally blocked in this demo.

.EXAMPLE
./Invoke-Onboarding.ps1 -UserCsvPath ../../data/sample-users.csv
#>

[CmdletBinding()]
param(
    [string]$UserCsvPath = (Join-Path $PSScriptRoot "../../data/sample-users.csv"),
    [string]$ConfigDirectory = (Join-Path $PSScriptRoot "../../config"),
    [switch]$ProductionMode
)

if ($ProductionMode) {
    throw "ProductionMode is intentionally disabled. This portfolio project supports simulation only."
}

$departmentMapPath = Join-Path $ConfigDirectory "department-group-map.example.json"
$licenseMapPath = Join-Path $ConfigDirectory "license-map.example.json"
$settingsPath = Join-Path $ConfigDirectory "settings.example.json"

$groupMap = Get-Content -Path $departmentMapPath -Raw | ConvertFrom-Json
$licenseMap = Get-Content -Path $licenseMapPath -Raw | ConvertFrom-Json
$settings = Get-Content -Path $settingsPath -Raw | ConvertFrom-Json
$users = Import-Csv -Path $UserCsvPath

foreach ($user in $users) {
    $upn = ("{0}.{1}@{2}" -f $user.first_name, $user.last_name, $settings.tenant_domain).ToLower()
    $groups = @()
    $groups += $groupMap.departments.PSObject.Properties[$user.department].Value
    $groups += $groupMap.regions.PSObject.Properties[$user.region].Value
    $groups += $groupMap.locations.PSObject.Properties[$user.location].Value
    $license = $licenseMap.employment_types.PSObject.Properties[$user.employment_type].Value

    Write-Host ""
    Write-Host "Onboarding simulation for $($user.display_name)"
    Write-Host "UPN: $upn"
    Write-Host "License: $($license.display_name)"
    Write-Host "Groups:"
    $groups | Where-Object { $_ } | Sort-Object -Unique | ForEach-Object { Write-Host " - $_" }
    Write-Host "No live Graph or Microsoft 365 action was executed."
}
