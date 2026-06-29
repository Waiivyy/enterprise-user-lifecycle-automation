"""Markdown and JSON report generation for lifecycle workflows."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def build_markdown_report(report: dict[str, Any]) -> str:
    workflow = str(report.get("workflow", "lifecycle")).title()
    subject = report.get("subject", {})
    display_name = subject.get("display_name") or subject.get("work_email", "Unknown user")
    mode = "Simulation" if report.get("simulation_mode", True) else "Production"

    lines = [
        f"# {workflow} Report - {display_name}",
        "",
        f"**Execution mode:** {mode}",
        f"**Generated at:** {report.get('generated_at', 'sample output')}",
        "",
        "> This report is generated from mock data and is safe for public demo repositories.",
        "",
    ]
    lines.extend(_section("Summary", [str(item) for item in report.get("summary", [])]))
    lines.extend(_table_section("Subject", _flatten_mapping(subject)))

    if report.get("account"):
        lines.extend(_table_section("Account", _flatten_mapping(report["account"])))
    if report.get("licenses"):
        lines.extend(_json_section("Licenses", report["licenses"]))
    if report.get("groups"):
        lines.extend(_section("Groups", [str(group) for group in report["groups"]]))
    if report.get("tool_payloads"):
        lines.extend(_json_section("SaaS Payloads", report["tool_payloads"]))
    if report.get("graph_actions"):
        lines.extend(_json_section("Microsoft Graph Simulation Actions", report["graph_actions"]))
    if report.get("mailbox"):
        lines.extend(_table_section("Mailbox Recommendations", _flatten_mapping(report["mailbox"])))
    if report.get("recommendations"):
        lines.extend(_section("Recommendations", [str(item) for item in report["recommendations"]]))

    return "\n".join(lines).rstrip() + "\n"


def write_report_bundle(report: dict[str, Any], output_dir: str | Path, base_name: str) -> dict[str, Path]:
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)

    markdown_path = directory / f"{base_name}.md"
    json_path = directory / f"{base_name}.json"

    markdown_path.write_text(build_markdown_report(report), encoding="utf-8")
    json_path.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    return {"markdown": markdown_path, "json": json_path}


def _section(title: str, items: list[str]) -> list[str]:
    lines = [f"## {title}", ""]
    if not items:
        lines.append("- None")
    else:
        lines.extend(f"- {item}" for item in items)
    lines.append("")
    return lines


def _table_section(title: str, mapping: dict[str, str]) -> list[str]:
    lines = [f"## {title}", "", "| Field | Value |", "| --- | --- |"]
    if not mapping:
        lines.append("| None | None |")
    else:
        for key, value in mapping.items():
            lines.append(f"| {key} | {value} |")
    lines.append("")
    return lines


def _json_section(title: str, payload: Any) -> list[str]:
    return [
        f"## {title}",
        "",
        "```json",
        json.dumps(payload, indent=2, sort_keys=True),
        "```",
        "",
    ]


def _flatten_mapping(mapping: dict[str, Any]) -> dict[str, str]:
    return {str(key): str(value) for key, value in mapping.items()}
