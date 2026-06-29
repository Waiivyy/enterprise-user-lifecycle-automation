<#
.SYNOPSIS
Builds simulated account disablement actions for offboarding.

.DESCRIPTION
Prints the Microsoft Graph style actions that should be reviewed during offboarding:
disable sign-in, revoke sessions, and prepare license/group cleanup. No live action is
performed by this demo script.

.PARAMETER WorkEmail
Target user's work email.

.PARAMETER TicketId
ITSM ticket associated with the offboarding.

.EXAMPLE
./Disable-UserAccess.ps1 -WorkEmail priya.shah@example.invalid -TicketId ITSM-1001
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory)]
    [string]$WorkEmail,
    [Parameter(Mandatory)]
    [string]$TicketId,
    [switch]$ProductionMode
)

if ($ProductionMode) {
    throw "ProductionMode is intentionally disabled. This portfolio project supports simulation only."
}

@(
    [PSCustomObject]@{
        Simulation = $true
        TicketId = $TicketId
        Method = "PATCH"
        Endpoint = "/users/$WorkEmail"
        Action = "DisableSignIn"
    },
    [PSCustomObject]@{
        Simulation = $true
        TicketId = $TicketId
        Method = "POST"
        Endpoint = "/users/$WorkEmail/revokeSignInSessions"
        Action = "RevokeSessions"
    }
)
