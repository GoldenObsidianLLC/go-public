# SPDX-License-Identifier: MIT
"""Validate the public documentation vault using only the Python standard library."""

from __future__ import annotations

import argparse
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote

REQUIRED_FIELDS = (
    "title",
    "description",
    "type",
    "status",
    "owner",
    "created",
    "updated",
    "license",
    "tags",
)
ALLOWED_TYPES = {
    "overview",
    "guide",
    "policy",
    "showcase",
    "announcement",
    "reference",
    "decision",
    "roadmap",
}
ALLOWED_STATUSES = {"draft", "review", "published", "archived"}
ALLOWED_LICENSES = {"CC-BY-4.0", "MIT"}

FENCE_OPEN = re.compile(r"^ {0,3}(\x60{3,}|~{3,})(.*)$")
FENCE_CLOSE = re.compile(r"^ {0,3}(\x60{3,}|~{3,})\s*$")
HEADING = re.compile(r"^ {0,3}(#{1,6})(?:\s+|$)")
LINK = re.compile(
    r"!?(?:\[[^\]]*\])\((<[^>]+>|[^)\s]+)(?:\s+[\"'][^\"']*[\"'])?\)"
)
INLINE_CODE = re.compile(r"(?<!\x60)\x60+.*?\x60+(?!\x60)")
FIELD = re.compile(r"^([a-z][a-z0-9_-]*):\s*(.*)$")

# SemVer 2.0.0: core numbers cannot have leading zeroes; numeric prerelease
# identifiers cannot have leading zeroes; build metadata may contain them.
SEMVER = re.compile(
    r"(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)\.(?:0|[1-9]\d*)"
    r"(?:-(?:0|[1-9]\d*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*)"
    r"(?:\.(?:0|[1-9]\d*|[0-9A-Za-z-]*[A-Za-z-][0-9A-Za-z-]*))*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
)

SECRET_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY-----"),
    re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"),
    re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{24,}\b"),
    re.compile(
        r"(?i)\baws_secret_access_key\s*[:=]\s*[A-Za-z0-9/+=]{40}\b"
    ),
)

# Only the intentional navigation/index documents bypass frontmatter.
FRONTMATTER_EXEMPT = {
    "README.md",
    "01-vision-and-culture/README.md",
    "02-products-and-projects/README.md",
    "03-community-and-ecosystem/README.md",
    "04-knowledge-base/README.md",
    "05-governance-and-policies/README.md",
    "06-news-and-announcements/README.md",
    "templates/README.md",
    "CHANGELOG.md",
    ".github/PULL_REQUEST_TEMPLATE.md",
}


def report(errors: list[str], path: Path, line: int | None, message: str) -> None:
    location = f"{path.as_posix()}:{line}" if line is not None else path.as_posix()
    errors.append(f"{location}: {message}")


def parse_frontmatter(
    root: Path, path: Path, text: str, errors: list[str]
) -> tuple[str, int]:
    """Return document body and the number of frontmatter lines removed."""
    relative = path.relative_to(root).as_posix()
    if relative in FRONTMATTER_EXEMPT:
        return text, 0

    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        report(errors, path.relative_to(root), 1, "missing YAML frontmatter opening delimiter")
        return text, 0

    try:
        closing = lines.index("---", 1)
    except ValueError:
        report(errors, path.relative_to(root), 1, "missing YAML frontmatter closing delimiter")
        return text, 0

    block = lines[1:closing]
    fields: dict[str, str] = {}
    field_order: list[str] = []
    tags: list[str] = []
    current_key = ""

    for number, line in enumerate(block, start=2):
        field_match = FIELD.match(line)
        if field_match:
            key, value = field_match.groups()
            if key in fields:
                report(errors, path.relative_to(root), number, f"duplicate frontmatter field: {key}")
            fields[key] = value.strip().strip('"').strip("'")
            field_order.append(key)
            current_key = key
        elif current_key == "tags":
            tag_match = re.match(r"^\s+-\s+(.+?)\s*$", line)
            if tag_match:
                tags.append(tag_match.group(1).strip().strip('"').strip("'"))

    for key in REQUIRED_FIELDS:
        if key not in fields:
            report(errors, path.relative_to(root), 1, f"missing required frontmatter field: {key}")

    for key in ("title", "description", "type", "status", "owner", "created", "updated", "license"):
        if key in fields and not fields[key]:
            report(errors, path.relative_to(root), 1, f"frontmatter field must not be empty: {key}")

    if fields.get("type") and fields["type"] not in ALLOWED_TYPES:
        report(errors, path.relative_to(root), 1, f"unsupported document type: {fields['type']}")

    if fields.get("status") and fields["status"] not in ALLOWED_STATUSES:
        report(errors, path.relative_to(root), 1, f"unsupported document status: {fields['status']}")

    if fields.get("license") and fields["license"] not in ALLOWED_LICENSES:
        report(errors, path.relative_to(root), 1, f"unsupported repository document license: {fields['license']}")

    is_template = "templates" in path.relative_to(root).parts
    for date_field in ("created", "updated"):
        value = fields.get(date_field, "")
        if is_template and value == "YYYY-MM-DD":
            continue
        if value:
            try:
                parsed = date.fromisoformat(value)
            except ValueError:
                parsed = None
            if parsed is None or parsed.isoformat() != value:
                report(errors, path.relative_to(root), 1, f"{date_field} must be a valid YYYY-MM-DD date")

    version = fields.get("version")
    if version and not SEMVER.fullmatch(version):
        report(errors, path.relative_to(root), 1, "version must use Semantic Versioning 2.0.0")

    raw_tags = fields.get("tags", "")
    if raw_tags not in ("[]", "") and not tags:
        report(errors, path.relative_to(root), 1, "tags must be an empty list or a YAML list")
    for tag in tags:
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", tag):
            report(errors, path.relative_to(root), 1, f"tag must be lowercase kebab-case: {tag}")

    expected_order = [
        "title",
        "description",
        "type",
        "status",
        "owner",
        "created",
        "updated",
    ]
    if "version" in fields:
        expected_order.append("version")
    expected_order.extend(["license", "tags"])
    if field_order != expected_order:
        report(errors, path.relative_to(root), 1, "frontmatter fields are not in the documented order")

    body = "\n".join(lines[closing + 1 :])
    if text.endswith("\n"):
        body += "\n"
    return body, closing + 1


def visible_markdown_lines(
    text: str, path: Path, errors: list[str], line_offset: int = 0
) -> list[tuple[int, str]]:
    """Return non-fenced Markdown lines while preserving original line numbers."""
    visible: list[tuple[int, str]] = []
    fence_char: str | None = None
    fence_length = 0
    lines = text.splitlines()

    for number, line in enumerate(lines, start=1):
        absolute_line = number + line_offset
        if fence_char is None:
            opening = FENCE_OPEN.match(line)
            if opening:
                marker = opening.group(1)
                fence_char = marker[0]
                fence_length = len(marker)
                continue
            visible.append((absolute_line, INLINE_CODE.sub("", line)))
            continue

        closing = FENCE_CLOSE.match(line)
        if closing:
            marker = closing.group(1)
            if marker[0] == fence_char and len(marker) >= fence_length:
                fence_char = None
                fence_length = 0

    if fence_char is not None:
        report(errors, path, line_offset + len(lines), "unclosed fenced code block")

    return visible


def check_structure(
    path: Path, visible_lines: list[tuple[int, str]], errors: list[str]
) -> None:
    heading_levels = [
        len(match.group(1))
        for _, line in visible_lines
        if (match := HEADING.match(line))
    ]

    if path.as_posix() != ".github/PULL_REQUEST_TEMPLATE.md":
        if heading_levels.count(1) != 1:
            report(errors, path, None, "document must contain exactly one H1 heading")
        previous = 0
        for level in heading_levels:
            if previous and level > previous + 1:
                report(errors, path, None, "heading hierarchy skips a level")
                break
            previous = level


def check_links(
    root: Path,
    source: Path,
    lines: list[tuple[int, str]],
    errors: list[str],
) -> None:
    for number, line in lines:
        for match in LINK.finditer(line):
            destination = match.group(1).strip()
            if destination.startswith("<") and destination.endswith(">"):
                destination = destination[1:-1]

            lowered = destination.lower()
            if lowered.startswith(("http://", "https://", "mailto:", "tel:", "data:", "//")):
                continue
            if destination.startswith("#"):
                continue

            target_text = unquote(destination.split("#", 1)[0].split("?", 1)[0])
            if not target_text:
                continue

            if target_text.startswith("/"):
                target = (root / target_text.lstrip("/")).resolve()
            else:
                target = (source.parent / target_text).resolve()

            try:
                target.relative_to(root.resolve())
            except ValueError:
                report(errors, source.relative_to(root), number, "relative link escapes the repository")
                continue

            if not target.exists():
                report(
                    errors,
                    source.relative_to(root),
                    number,
                    f"broken internal link target: {destination}",
                )


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the public Markdown documentation.")
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="documentation repository root (defaults to the parent of scripts/)",
    )
    args = parser.parse_args()
    root = args.root.resolve()

    if not root.is_dir():
        print(f"Repository root does not exist: {root}", file=sys.stderr)
        return 2

    markdown_files = sorted(
        path
        for path in root.rglob("*.md")
        if ".git" not in path.relative_to(root).parts
    )
    errors: list[str] = []

    for path in markdown_files:
        relative = path.relative_to(root)
        try:
            raw = path.read_bytes()
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            report(errors, relative, None, "file is not valid UTF-8")
            continue
        except OSError as exc:
            report(errors, relative, None, f"could not read file: {exc}")
            continue

        if b"\r" in raw:
            report(errors, relative, None, "file contains CR characters; use LF line endings")
        if raw and not raw.endswith(b"\n"):
            report(errors, relative, None, "file must end with a newline")

        body, line_offset = parse_frontmatter(root, path, text, errors)
        visible_lines = visible_markdown_lines(body, relative, errors, line_offset)
        check_structure(relative, visible_lines, errors)
        check_links(root, path, visible_lines, errors)

        for number, line in enumerate(text.splitlines(), start=1):
            if any(pattern.search(line) for pattern in SECRET_PATTERNS):
                report(
                    errors,
                    relative,
                    number,
                    "possible credential or private key detected; verify and remove before publishing",
                )
                break

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"\nValidation failed: {len(errors)} issue(s) across {len(markdown_files)} Markdown file(s).")
        return 1

    print(f"Documentation validation passed: {len(markdown_files)} Markdown file(s) checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
