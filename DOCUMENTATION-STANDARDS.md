---
title: "Documentation Standards"
description: "Canonical Markdown, Obsidian, GitHub, maintenance, and versioning standards for this repository."
type: "policy"
status: "published"
owner: "Golden Obsidian LLC"
created: "2026-11-11"
updated: "2026-11-11"
license: "CC-BY-4.0"
tags:
  - documentation
  - markdown
  - obsidian
  - standards
---

# Documentation Standards

These standards are the canonical authoring and maintenance rules for the public vault. They are designed to keep Markdown consistent across Obsidian, VS Code, and GitHub while minimizing duplication and avoiding accidental disclosure.

## 1. Source of truth and document ownership

- Keep one canonical document for each topic. Other pages should link to it rather than copying the same explanation.
- Put a document in the section that best matches its primary purpose. Do not create parallel copies for navigation convenience.
- Use the root README as the entry point, section README files as indexes, and this document for authoring rules.
- Treat project-specific repositories as the source of truth for code, implementation details, releases, and project issue tracking. This vault should link to those sources rather than mirror them.
- When two documents conflict, prefer the explicitly designated canonical policy or the newer approved source. Record meaningful policy changes in the pull request.

## 2. Markdown and Obsidian compatibility

- Use standard Markdown and relative links with explicit .md extensions. This renders in GitHub and remains usable in Obsidian.
- Prefer descriptive link text over raw URLs. Use Obsidian-specific wikilinks only when a GitHub-compatible Markdown link cannot express the relationship.
- Use one H1 per document, followed by logically nested H2 and H3 headings. Do not skip heading levels for visual styling.
- Use tables for compact comparisons, not for long prose. Use meaningful alt text for informative images.
- Keep paragraphs focused and lists parallel. Avoid decorative formatting that harms accessibility or mobile readability.
- Use lowercase kebab-case for new Markdown filenames. Section index files use README.md. News and announcement files use YYYY-MM-DD-title.md.
- Use UTF-8 text and LF line endings. Avoid embedding large binary assets when a link to a verified, appropriately licensed asset is sufficient.

## 3. Frontmatter

Every maintained Markdown document should use the shared YAML frontmatter schema shown in the document template. The root README, section README files, templates README, and root CHANGELOG are intentional exceptions so GitHub can present them cleanly.

Required fields:

| Field | Rule |
| --- | --- |
| title | Human-readable document title. |
| description | One sentence explaining the document's purpose. |
| type | One of overview, guide, policy, showcase, announcement, reference, decision, or roadmap. |
| status | One of draft, review, published, or archived. |
| owner | Responsible publishing owner; use Golden Obsidian LLC unless formally delegated. |
| created | Creation date in YYYY-MM-DD format. |
| updated | Last substantive update date in YYYY-MM-DD format. |
| license | CC-BY-4.0 or MIT, as defined by the licensing policy. |
| tags | Short, lowercase, hyphenated topic labels. |

The optional version field is reserved for documents that are independently versioned because they define a stable public contract or reusable interface. Do not increment a document version for ordinary typo fixes.

Use one field order consistently: title, description, type, status, owner, created, updated, optional version, license, tags. Do not add ad hoc fields unless the standards are deliberately updated first.

## 4. Accuracy, evidence, and public-release review

- Separate verified current capabilities from planned work, hypotheses, and proposals.
- Support claims about performance, compatibility, security, awards, partnerships, and availability with a traceable source.
- Include dates or supported version ranges when instructions can become stale.
- Identify assumptions and limitations. Do not turn estimates into facts.
- Review screenshots, diagrams, quotations, and external assets for accuracy, accessibility, permission, and attribution.
- Before every public change, check for credentials, tokens, private URLs, personal data, internal logs, confidential source material, unreleased security findings, and protected intellectual property.
- Do not publish architecture details, IP proofs, or trade secrets simply because they have been placed in a Markdown file.

## 5. Links, assets, and duplication control

- Use relative links for documents in this repository. Verify every changed internal link before merging.
- Link to the canonical project repository for implementation details and release records.
- Avoid duplicated FAQs, copied release notes, repeated policy text, and conflicting project descriptions.
- If a topic grows, split it into focused pages and keep the section README as a short index.
- Store only approved public assets. Prefer descriptive filenames and useful alt text; record third-party source and license information.

## 6. Status and maintenance lifecycle

Use the status field consistently:

- draft — work in progress; not a public statement of fact.
- review — ready for accuracy, licensing, security, and editorial review.
- published — approved as current public documentation.
- archived — retained for context but no longer current; include a replacement link when one exists.

When a page becomes outdated, update it or mark it archived. Do not silently leave contradictory copies in multiple sections. Update the updated field only when the content changes substantively.

## 7. Semantic versioning and release records

Use Semantic Versioning (MAJOR.MINOR.PATCH) for tagged releases of this documentation repository when a stable release process is established:

- MAJOR — incompatible changes to the published documentation contract, navigation, required metadata, or templates that require consumers or contributors to migrate.
- MINOR — backward-compatible additions such as new sections, templates, or substantial public documentation.
- PATCH — corrections, clarifications, link fixes, and other non-breaking maintenance.

Before 1.0.0, the 0.y.z series is pre-stable and does not promise compatibility. Do not assign a version to every Markdown file or tag a release merely because a commit was merged. Every tagged release must have a corresponding entry in the root CHANGELOG and a concise release summary. Use a vX.Y.Z Git tag after release checks pass.

## 8. Git and review conventions

Use focused changes, descriptive commit messages, and pull requests that explain purpose, scope, sources, and risk. Prefer Conventional Commit prefixes such as docs, fix, feat, chore, and security. Link related issues and keep changes small enough to review. Do not force-push shared branches or bypass required reviews and checks once they are configured.

See [Contributing](CONTRIBUTING.md), [Licensing](05-governance-and-policies/licensing.md), and [Security](SECURITY.md) for the related canonical policies.
