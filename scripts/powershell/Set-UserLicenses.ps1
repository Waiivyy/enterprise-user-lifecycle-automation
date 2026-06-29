<#
.SYNOPSIS
Builds simulated Microsoft 365 license assignment actions for a user.

.DESCRIPTION
Maps employment type to an example Microsoft 365 license SKU. It does not call Microsoft
Graph or assign a real license.

.PARAMETER EmploymentType
Employment type from the onboarding record.

.PARAMETER UserPrincipalName
Target user's generated UPN.

.EXAMPLE
./Set-UserLicenses.ps1 -EmploymentType "Full-time" -UserPrincipalName priya.shah@example.invalid
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string]$EmploymentType,
    [Parameter(Mandatory)]
    [string]$UserPrincipalName,
    [string]$ConfigDirectory = (Join-Path $PSScriptRoot "../../config"),
    [switch]$ProductionMode
)

if ($ProductionMode) {
    throw "ProductionMode is intentionally disabled. This portfolio project supports simulation only."
}

$licenseMap = Get-Content -Path (Join-Path $ConfigDirectory "license-map.example.json") -Raw | ConvertFrom-Json
$license = $licenseMap.employment_types.PSObject.Properties[$EmploymentType].Value

if (-not $license) {
    $license = [PSCustomObject]@{
        sku = "M365_BUSINESS_STANDARD"
        display_name = "Microsoft 365 Business Standard"
    }
}

[PSCustomObject]@{
    Simulation = $true
    UserPrincipalName = $UserPrincipalName
    Action = "AssignLicense"
    LicenseSku = $license.sku
    LicenseName = $license.display_name
}
