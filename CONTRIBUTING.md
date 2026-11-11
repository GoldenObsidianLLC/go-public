---
title: "Contributing Guide"
description: "Explains how to propose, review, and contribute public documentation changes."
type: "policy"
status: "published"
owner: "Golden Obsidian LLC"
created: "2026-11-11"
updated: "2026-11-11"
license: "CC-BY-4.0"
tags:
  - contributing
  - github
  - community
---

# Contributing Guide

Thank you for helping improve the public documentation vault. Contributions should be focused, accurate, attributable, safe to disclose, and consistent with the [Documentation Standards](DOCUMENTATION-STANDARDS.md).

## Before opening an issue

Search existing issues and documentation first to avoid duplicates. For a documentation defect, include the page path, the observed problem, and the proposed correction. For a new topic, explain its audience, value, authoritative source, and proposed location.

Do not place credentials, private correspondence, personal data, confidential source material, or security-sensitive details in a public issue. Use the private process in [Security](SECURITY.md) for vulnerability reports.

## Pull request expectations

- Keep one logical change per pull request where practical.
- Link the related issue, or explain why an issue was unnecessary.
- Use the appropriate template and frontmatter for new documents.
- Prefer updating a canonical page over adding a duplicate.
- Verify relative links, attribution, dates, and factual claims.
- Confirm that no confidential or excluded material is present.
- Describe any meaningful policy, navigation, or metadata impact.

## Branches and commits

Use short descriptive branch names, such as docs/section-indexes, fix/broken-links, or feat/product-showcase. Prefer Conventional Commit prefixes such as docs, fix, feat, chore, and security. Keep commit messages specific and avoid bundling unrelated changes.

## Review and merge

A change is ready when its scope is clear, factual statements are sourced or approved, licensing is correct, public-release safeguards are satisfied, and the changed Markdown renders correctly in GitHub. Automated checks will be added as part of the governance roadmap; until then, contributors should perform these checks manually.

## Scope boundaries

This repository is for approved public documentation. Do not submit intellectual-property proofs, detailed private architecture specifications, trade secrets, internal incident records, private security assessments, credentials, or other confidential material. See the [Licensing Policy](05-governance-and-policies/licensing.md) for the explicit exclusions.
