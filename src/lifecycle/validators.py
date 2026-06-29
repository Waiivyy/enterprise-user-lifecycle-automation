"""Input validation helpers for lifecycle workflows."""

from __future__ import annotations

import re
import unicodedata
from datetime import date
from typing import Any


class ValidationError(ValueError):
    """Raised when input records do not satisfy lifecycle requirements."""


ONBOARDING_REQUIRED_FIELDS = (
    "first_name",
    "last_name",
    "display_name",
    "work_email",
    "department",
    "job_title",
    "region",
    "location",
    "employment_type",
    "manager",
    "start_date",
)

OFFBOARDING_REQUIRED_FIELDS = (
    "work_email",
    "last_working_day",
    "manager",
    "offboarding_type",
    "ticket_id",
)

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def validate_onboarding_record(record: dict[str, Any]) -> dict[str, str]:
    normalized = _normalize_record(record, ONBOARDING_REQUIRED_FIELDS)
    errors = _required_field_errors(normalized, ONBOARDING_REQUIRED_FIELDS)
    errors.extend(_email_errors(normalized.get("work_email", ""), "work_email"))
    errors.extend(_date_errors(normalized.get("start_date", ""), "start_date"))
    if errors:
        raise ValidationError("; ".join(errors))
    return normalized


def validate_offboarding_record(record: dict[str, Any]) -> dict[str, str]:
    normalized = _normalize_record(record, OFFBOARDING_REQUIRED_FIELDS)
    errors = _required_field_errors(normalized, OFFBOARDING_REQUIRED_FIELDS)
    errors.extend(_email_errors(normalized.get("work_email", ""), "work_email"))
    errors.extend(_date_errors(normalized.get("last_working_day", ""), "last_working_day"))
    if errors:
        raise ValidationError("; ".join(errors))
    return normalized


def generate_standard_upn(first_name: str, last_name: str, tenant_domain: str) -> str:
    first = _slug_name(first_name)
    last = _slug_name(last_name)
    domain = tenant_domain.strip().lower()
    if not first or not last:
        raise ValidationError("first_name and last_name are required to generate a UPN")
    if not EMAIL_RE.match(f"user@{domain}"):
        raise ValidationError("tenant_domain must be a valid email domain")
    return f"{first}.{last}@{domain}"


def _normalize_record(record: dict[str, Any], expected_fields: tuple[str, ...]) -> dict[str, str]:
    normalized: dict[str, str] = {}
    for field in expected_fields:
        value = record.get(field, "")
        normalized[field] = str(value).strip() if value is not None else ""
    return normalized


def _required_field_errors(record: dict[str, str], required_fields: tuple[str, ...]) -> list[str]:
    return [f"{field} is required" for field in required_fields if not record.get(field)]


def _email_errors(value: str, field: str) -> list[str]:
    if value and not EMAIL_RE.match(value):
        return [f"{field} must be a valid email address"]
    return []


def _date_errors(value: str, field: str) -> list[str]:
    if not value:
        return []
    try:
        date.fromisoformat(value)
    except ValueError:
        return [f"{field} must use YYYY-MM-DD format"]
    return []


def _slug_name(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value.strip())
    ascii_only = normalized.encode("ascii", "ignore").decode("ascii").lower()
    ascii_only = re.sub(r"[^a-z0-9-]+", "", ascii_only.replace(" ", "-"))
    return re.sub(r"-{2,}", "-", ascii_only).strip("-")
