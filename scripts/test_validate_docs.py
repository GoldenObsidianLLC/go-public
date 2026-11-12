# SPDX-License-Identifier: MIT
"""Unit tests for the dependency-free documentation validator."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_docs as validator  # noqa: E402


def frontmatter(*, version: str | None = None, created: str = "2026-11-12") -> str:
    version_line = f'version: "{version}"\n' if version is not None else ""
    return (
        "---\n"
        'title: "Test document"\n'
        'description: "A validator test document."\n'
        "type: guide\n"
        "status: draft\n"
        'owner: "Golden Obsidian LLC"\n'
        f'created: "{created}"\n'
        'updated: "2026-11-12"\n'
        f"{version_line}"
        'license: "CC-BY-4.0"\n'
        "tags:\n"
        "  - test-document\n"
        "---\n"
        "\n"
        "# Test document\n"
    )


class FrontmatterTests(unittest.TestCase):
    def test_only_known_indexes_are_exempt(self) -> None:
        root = Path("repo")
        errors: list[str] = []
        text = "# Index\n"
        body, offset = validator.parse_frontmatter(
            root, root / "02-products-and-projects" / "README.md", text, errors
        )
        self.assertEqual(body, text)
        self.assertEqual(offset, 0)
        self.assertEqual(errors, [])

    def test_arbitrary_nested_readme_requires_frontmatter(self) -> None:
        root = Path("repo")
        errors: list[str] = []
        validator.parse_frontmatter(root, root / "guides" / "README.md", "# Guide\n", errors)
        self.assertTrue(any("missing YAML frontmatter" in item for item in errors))

    def test_valid_frontmatter_passes_and_preserves_line_offset(self) -> None:
        root = Path("repo")
        errors: list[str] = []
        text = frontmatter()
        body, offset = validator.parse_frontmatter(root, root / "guide.md", text, errors)
        self.assertEqual(errors, [])
        self.assertEqual(offset, 12)
        self.assertIn("# Test document", body)

    def test_semver_rejects_leading_zero_and_accepts_prerelease(self) -> None:
        root = Path("repo")
        for value, should_pass in (("01.0.0", False), ("1.2.3-rc.1+build.02", True), ("1.2.3-01", False)):
            with self.subTest(value=value):
                errors: list[str] = []
                validator.parse_frontmatter(
                    root, root / "versioned.md", frontmatter(version=value), errors
                )
                self.assertEqual(
                    any("Semantic Versioning" in item for item in errors),
                    not should_pass,
                )

    def test_invalid_calendar_date_is_rejected(self) -> None:
        errors: list[str] = []
        validator.parse_frontmatter(
            Path("repo"),
            Path("repo") / "dated.md",
            frontmatter(created="2026-02-30"),
            errors,
        )
        self.assertTrue(any("valid YYYY-MM-DD date" in item for item in errors))


class StructureAndSafetyTests(unittest.TestCase):
    def test_fenced_headings_are_ignored(self) -> None:
        errors: list[str] = []
        path = Path("guide.md")
        visible = validator.visible_markdown_lines(
            "# Real title\n\n```markdown\n# Example heading\n```\n\n## Detail\n",
            path,
            errors,
        )
        validator.check_structure(path, visible, errors)
        self.assertEqual(errors, [])

    def test_heading_level_skips_are_reported(self) -> None:
        errors: list[str] = []
        path = Path("guide.md")
        visible = validator.visible_markdown_lines("# Title\n\n### Skipped\n", path, errors)
        validator.check_structure(path, visible, errors)
        self.assertTrue(any("skips a level" in item for item in errors))

    def test_missing_link_is_reported(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "docs" / "page.md"
            source.parent.mkdir()
            errors: list[str] = []
            validator.check_links(root, source, [(8, "[missing](not-here.md)")], errors)
            self.assertTrue(any("broken internal link" in item and ":8:" in item for item in errors))

    def test_link_cannot_escape_repository_through_parent_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "repo"
            root.mkdir()
            source = root / "page.md"
            errors: list[str] = []
            validator.check_links(root, source, [(3, "[outside](../outside.md)")], errors)
            self.assertTrue(any("escapes the repository" in item and ":3:" in item for item in errors))

    def test_high_confidence_secret_pattern_is_detected(self) -> None:
        sample = "-----BEGIN OPENSSH PRIVATE KEY-----"
        self.assertTrue(any(pattern.search(sample) for pattern in validator.SECRET_PATTERNS))


if __name__ == "__main__":
    unittest.main()
