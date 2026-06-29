"""Mock Microsoft Graph client used by the demo workflows."""

from __future__ import annotations

from typing import Any


class MockGraphClient:
    """Records simulated Microsoft Graph actions without making network calls."""

    def __init__(self, responses: dict[str, Any] | None = None) -> None:
        self.responses = responses or {}

    def create_user(self, user_payload: dict[str, Any]) -> dict[str, Any]:
        return self._action("POST", "/users", user_payload)

    def assign_license(self, user_principal_name: str, license_sku: str) -> dict[str, Any]:
        return self._action(
            "POST",
            f"/users/{user_principal_name}/assignLicense",
            {"addLicenses": [{"skuId": license_sku}], "removeLicenses": []},
        )

    def add_user_to_group(self, user_principal_name: str, group_id: str) -> dict[str, Any]:
        return self._action(
            "POST",
            f"/groups/{group_id}/members/$ref",
            {"userPrincipalName": user_principal_name},
        )

    def disable_sign_in(self, work_email: str) -> dict[str, Any]:
        return self._action(
            "PATCH",
            f"/users/{work_email}",
            {"accountEnabled": False},
        )

    def revoke_sessions(self, work_email: str) -> dict[str, Any]:
        return self._action("POST", f"/users/{work_email}/revokeSignInSessions", {})

    def remove_license(self, work_email: str, license_sku: str) -> dict[str, Any]:
        return self._action(
            "POST",
            f"/users/{work_email}/assignLicense",
            {"addLicenses": [], "removeLicenses": [license_sku]},
        )

    def remove_from_group(self, work_email: str, group_id: str) -> dict[str, Any]:
        return self._action(
            "DELETE",
            f"/groups/{group_id}/members/{work_email}/$ref",
            {},
        )

    def get_user_snapshot(self, work_email: str) -> dict[str, Any]:
        users = self.responses.get("users", {})
        return dict(users.get(work_email, {}))

    @staticmethod
    def _action(method: str, endpoint: str, payload: dict[str, Any]) -> dict[str, Any]:
        return {
            "simulation": True,
            "method": method,
            "endpoint": endpoint,
            "payload": payload,
            "status": "mocked",
        }
