<#
.SYNOPSIS
Builds simulated Entra ID group assignment actions for a user.

.DESCRIPTION
Uses readable fake group IDs from department, region, and location mappings. It prints the
actions that would be sent to Microsoft Graph in a production implementation.

.PARAMETER Department
User department.

.PARAMETER Region
User region.

.PARAMETER Location
User office location.

.PARAMETER UserPrincipalName
Target user's generated UPN.

.EXAMPLE
./Set-UserGroups.ps1 -Department Engineering -Region Europe -Location Berlin -UserPrincipalName priya.shah@example.invalid
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string]$Department,
    [Parameter(Mandatory)]
    [string]$Region,
    [Parameter(Mandatory)]
    [string]$Location,
    [Parameter(Mandatory)]
    [string]$UserPrincipalName,
    [string]$ConfigDirectory = (Join-Path $PSScriptRoot "../../config"),
    [switch]$ProductionMode
)

if ($ProductionMode) {
    throw "ProductionMode is intentionally disabled. This public lab project supports simulation only."
}

$map = Get-Content -Path (Join-Path $ConfigDirectory "department-group-map.example.json") -Raw | ConvertFrom-Json
$groups = @()
$groups += $map.departments.PSObject.Properties[$Department].Value
$groups += $map.regions.PSObject.Properties[$Region].Value
$groups += $map.locations.PSObject.Properties[$Location].Value

$groups | Where-Object { $_ } | Sort-Object -Unique | ForEach-Object {
    [PSCustomObject]@{
        Simulation = $true
        UserPrincipalName = $UserPrincipalName
        Action = "AddUserToGroup"
        GroupId = $_
    }
}
