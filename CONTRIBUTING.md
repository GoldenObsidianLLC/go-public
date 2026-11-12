---
title: "Contributing Guide"
description: "Explains how to propose, review, and contribute public documentation changes."
type: policy
status: published
owner: "Golden Obsidian LLC"
created: "2026-11-11"
updated: "2026-11-12"
license: "CC-BY-4.0"
tags:
  - contributing
  - github
  - community
---

# Contributing Guide

Thank you for helping improve the public documentation vault. Contributions should be focused, accurate, attributable, safe to disclose, and consistent with the [Documentation Standards](DOCUMENTATION-STANDARDS.md).

## Before opening an issue

Search existing issues and documentation first to avoid duplicates. Select the issue form that best matches the request:

- **Documentation defect:** identify the page, observed problem, and expected correction.
- **Content proposal:** explain the audience, value, authoritative source, and proposed location.
- **Project showcase request:** provide the public source, verifiable current status, and evidence suitable for disclosure.

Do not place credentials, private correspondence, personal data, confidential source material, or security-sensitive details in a public issue. Use the private process described in [Security](SECURITY.md) for vulnerability reports. If private vulnerability reporting is unavailable, ask maintainers for a verified private route without including vulnerability details.

## Issue triage

Use the existing documentation, bug, and enhancement labels where they fit. Add one priority: high, priority: normal, or priority: low label to communicate urgency, and use one focused type label such as governance, security, or project-showcase when it adds useful routing context. Prefer priority: normal when impact is unclear; do not label a public issue with sensitive vulnerability details.

Triage duplicates and requests for clarification first. Prioritize security-reporting, licensing, privacy, materially incorrect public claims, and broken navigation over cosmetic changes. Do not promise a response or resolution time unless an owner has explicitly adopted one.

## Pull request expectations

- Keep one logical change per pull request where practical.
- Link the related issue, or explain why an issue was unnecessary.
- Use the appropriate document template and frontmatter for new content.
- Prefer updating a canonical page over adding a duplicate.
- Verify relative links, attribution, dates, and factual claims.
- Confirm that no confidential or excluded material is present.
- Describe any meaningful policy, navigation, or metadata impact.
- Ensure the documentation-quality workflow passes; automated checks supplement rather than replace editorial, legal, licensing, and security review.

## Local validation

Run the repository's dependency-free validator from the repository root:

    python scripts/validate_docs.py

The validator checks maintained Markdown frontmatter, heading and code-fence structure, local Markdown link targets, line-ending basics, and a limited set of high-confidence credential patterns. It does not validate external URLs, prove factual accuracy, parse every possible Markdown extension, or guarantee detection of all secrets. Review the changed content manually as well.

Run the unit tests before validation:

    python -m unittest discover -s scripts -p "test_*.py"

The same unit tests and validator run in GitHub Actions for pushes and pull requests targeting the default branch.

## Branches and commits

Use short descriptive branch names, such as docs/company-identity, fix/broken-links, or feat/product-showcase. Prefer Conventional Commit prefixes such as docs, fix, feat, chore, and security. Keep commit messages specific and avoid bundling unrelated changes.

## Review and merge

A change is ready when its scope is clear, factual statements are sourced or approved, licensing is correct, public-release safeguards are satisfied, and the changed Markdown renders correctly in GitHub. Required status checks and branch protection must be confirmed in repository settings before they are treated as enforced controls.

## Scope boundaries

This repository is for approved public documentation. Do not submit intellectual-property proofs, detailed private architecture specifications, trade secrets, internal incident records, private security assessments, credentials, or other confidential material. See the [Licensing Policy](05-governance-and-policies/licensing.md) for the explicit exclusions.
