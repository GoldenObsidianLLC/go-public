# Changelog

All notable changes to the public documentation repository are recorded here. This file tracks repository-level releases; it is not a duplicate of the changelogs maintained by individual product repositories.

The format follows the Keep a Changelog model, and tagged repository releases follow the Semantic Versioning policy in [Documentation Standards](DOCUMENTATION-STANDARDS.md).

## [Unreleased]

### Added

- Established the root documentation landing page and six section indexes.
- Added canonical documentation, licensing, contribution, and security guidance.
- Added the public documentation roadmap and reusable Markdown templates.
- Added local-vault ignore rules for machine-specific state and sensitive working files.
- Added the canonical company identity and portfolio hierarchy reference.
- Added structured GitHub issue forms, a default label taxonomy, and a pull request review checklist.
- Added a dependency-free Markdown validator, standard-library regression tests, and a GitHub Actions quality workflow.
- Added review-stage, source-backed showcase candidates for VirgoScorpio Hub and EnginEx.

### Changed

- Defined a single canonical home for each topic and a link-first approach to reduce duplication.
- Aligned the root landing page, vision index, and products index with the review status of the company identity and current public project sources.
- Clarified the Phase 2 roadmap: projects without approved public source material remain index-only, and package versions are not treated as public releases.
- Updated contribution guidance and the roadmap to reflect implemented baseline controls and the next-phase content work.

### Security

- Explicitly excluded protected intellectual property, confidential architecture, trade secrets, and sensitive operational details from the public vault.
- Enabled GitHub private vulnerability reporting for the public repository.
- Restricted the documentation workflow to read-only repository permissions and disabled persisted checkout credentials.
- Added best-effort checks for selected high-confidence credential patterns; these checks do not replace secret scanning or private security review.

## Release history

No versioned repository release has been published yet. Create a version heading only when a reviewed Git tag is cut.
