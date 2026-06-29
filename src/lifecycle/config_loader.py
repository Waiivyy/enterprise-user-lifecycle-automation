"""Configuration loading for lifecycle automation workflows."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class ConfigError(ValueError):
    """Raised when configuration files are missing or malformed."""


@dataclass(frozen=True)
class LifecycleConfig:
    """Resolved lifecycle configuration used by onboarding and offboarding."""

    department_groups: dict[str, list[str]]
    region_groups: dict[str, list[str]]
    location_groups: dict[str, list[str]]
    license_map: dict[str, dict[str, Any]]
    tool_map: dict[str, dict[str, Any]]
    settings: dict[str, Any]

    @property
    def simulation_mode(self) -> bool:
        return bool(self.settings.get("simulation_mode", True))

    @property
    def tenant_domain(self) -> str:
        return str(self.settings.get("tenant_domain", "example.invalid")).lower()

    @property
    def report_timezone(self) -> str:
        return str(self.settings.get("report_timezone", "UTC"))

    def license_for(self, employment_type: str) -> dict[str, Any]:
        if employment_type in self.license_map:
            return dict(self.license_map[employment_type])

        default_license = self.settings.get(
            "default_license",
            {
                "sku": "M365_BUSINESS_STANDARD",
                "display_name": "Microsoft 365 Business Standard",
                "assignment_reason": "Default fallback for unmapped employment type",
            },
        )
        return dict(default_license)

    def groups_for(self, department: str, region: str, location: str) -> list[str]:
        groups: list[str] = []
        groups.extend(self.department_groups.get(department, []))
        groups.extend(self.region_groups.get(region, []))
        groups.extend(self.location_groups.get(location, []))
        return _dedupe(groups)

    def tool_specs(self) -> list[dict[str, Any]]:
        """Return enabled SaaS tool specs with the tool name included."""

        tools: list[dict[str, Any]] = []
        for name, spec in self.tool_map.items():
            if bool(spec.get("enabled", True)):
                tool_spec = dict(spec)
                tool_spec["name"] = name
                tools.append(tool_spec)
        return tools

    def enabled_tools(self) -> list[dict[str, Any]]:
        """Backward-compatible alias for older callers."""

        return self.tool_specs()


REQUIRED_CONFIG_FILES = {
    "department_group_map": "department-group-map.example.json",
    "license_map": "license-map.example.json",
    "tool_access_map": "tool-access-map.example.json",
    "settings": "settings.example.json",
}


def load_lifecycle_config(config_dir: str | Path) -> LifecycleConfig:
    """Load all JSON configuration files from a directory."""

    directory = Path(config_dir)
    if not directory.exists():
        raise ConfigError(f"Config directory does not exist: {directory}")

    department_group_map = _read_json(directory / REQUIRED_CONFIG_FILES["department_group_map"])
    license_map = _read_json(directory / REQUIRED_CONFIG_FILES["license_map"])
    tool_access_map = _read_json(directory / REQUIRED_CONFIG_FILES["tool_access_map"])
    settings = _read_json(directory / REQUIRED_CONFIG_FILES["settings"])

    return LifecycleConfig(
        department_groups=_string_list_map(department_group_map.get("departments", {}), "departments"),
        region_groups=_string_list_map(department_group_map.get("regions", {}), "regions"),
        location_groups=_string_list_map(department_group_map.get("locations", {}), "locations"),
        license_map=_mapping_map(license_map.get("employment_types", {}), "employment_types"),
        tool_map=_mapping_map(tool_access_map.get("tools", {}), "tools"),
        settings=_require_mapping(settings, "settings.example.json"),
    )


def _read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ConfigError(f"Missing required configuration file: {path.name}")
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ConfigError(f"Invalid JSON in {path.name}: {exc.msg}") from exc
    return _require_mapping(data, path.name)


def _require_mapping(value: Any, label: str) -> dict[str, Any]:
    if not isinstance(value, dict):
        raise ConfigError(f"{label} must contain a JSON object")
    return dict(value)


def _string_list_map(value: Any, label: str) -> dict[str, list[str]]:
    mapping = _require_mapping(value, label)
    normalized: dict[str, list[str]] = {}
    for key, entries in mapping.items():
        if not isinstance(key, str) or not isinstance(entries, list):
            raise ConfigError(f"{label} must map names to lists of group IDs")
        if not all(isinstance(entry, str) and entry.strip() for entry in entries):
            raise ConfigError(f"{label}.{key} contains an invalid group ID")
        normalized[key] = [entry.strip() for entry in entries]
    return normalized


def _mapping_map(value: Any, label: str) -> dict[str, dict[str, Any]]:
    mapping = _require_mapping(value, label)
    normalized: dict[str, dict[str, Any]] = {}
    for key, spec in mapping.items():
        if not isinstance(key, str) or not isinstance(spec, dict):
            raise ConfigError(f"{label} must map names to JSON objects")
        normalized[key] = dict(spec)
    return normalized


def _dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
