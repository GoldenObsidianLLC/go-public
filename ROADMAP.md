---
title: "Public Documentation Roadmap"
description: "Phased plan for establishing, expanding, and maintaining the Golden Obsidian public documentation vault."
type: "roadmap"
status: "published"
owner: "Golden Obsidian LLC"
created: "2026-11-11"
updated: "2026-11-11"
license: "CC-BY-4.0"
tags:
  - roadmap
  - documentation
  - governance
---

# Public Documentation Roadmap

This roadmap records the intended sequence of work for the public documentation repository. It is directional rather than a promise of delivery dates. GitHub issues and pull requests should be used to scope, prioritize, and record implementation.

## Phase 0 — Public foundation

**Scope:** Establish navigation and consistent publishing controls.

- Root landing page and six section indexes.
- Canonical documentation and Markdown standards.
- Scoped licensing policy and explicit protected-material exclusions.
- Contribution and security guidance.
- Reusable general-document and product-showcase templates.
- Initial changelog and safe local-vault ignore rules.

**Acceptance:** Internal links resolve, section responsibilities are clear, frontmatter rules are consistent, licensing scope is explicit, and no private source material is included.

## Phase 1 — GitHub governance and validation

**Scope:** Make contributions predictable and catch common documentation defects early.

- Add issue forms for documentation defects, content proposals, and project showcase requests.
- Add a pull request template with source, licensing, security, link, and review checks.
- Establish a small, consistent label taxonomy and issue triage expectations.
- Add CI checks for Markdown formatting, frontmatter shape, internal links, and accidental secret patterns.
- Confirm the repository's security-reporting settings and branch protections.

**Acceptance:** A contributor can report an issue, submit a focused pull request, and receive automated baseline validation. Security-sensitive reports have a private path.

## Phase 2 — Verified company and product content

**Scope:** Populate the index pages with approved, source-backed documents.

- Add the approved company mission, values, and founder biography.
- Add public showcase pages for Harlan GI, CelestialVerse, and VirgoScorpio Hub.
- Add verified getting-started material and frequently asked questions.
- Link to canonical project repositories and authoritative release records.

**Acceptance:** Every substantive claim has an identified source or approval, planned features are distinguished from released capabilities, and protected architecture or IP evidence remains excluded.

## Phase 3 — Community and communications

**Scope:** Build public-facing participation and announcement resources.

- Add community participation and support guidance.
- Publish partner, supporter, award, and event information only when verified and approved.
- Establish a dated announcement workflow that links to canonical project releases instead of duplicating them.

**Acceptance:** Relationships and recognition are attributable, links are current, and news items do not conflict with product pages or the changelog.

## Phase 4 — Release and maintenance maturity

**Scope:** Introduce predictable releases and ongoing quality controls.

- Define release readiness and review ownership.
- Publish the first tagged documentation release only after the repository has sufficient stable content.
- Maintain the changelog and use Semantic Versioning for tagged repository releases.
- Review links, policies, public claims, and excluded-content safeguards periodically.

**Acceptance:** Each tag maps to a reviewed changelog entry, release notes are reproducible from merged changes, and maintenance responsibilities are clear.

## Prioritization

Security, licensing, accuracy, broken navigation, and contradictory public claims take priority over cosmetic improvements. Prefer small, reversible changes. Use GitHub issues to capture follow-up work and avoid expanding scope without a clear benefit.

No target dates or release versions are assigned at this stage.
