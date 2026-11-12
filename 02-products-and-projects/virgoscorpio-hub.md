---
title: "VirgoScorpio Hub - Public Project Overview"
description: "Review-stage overview of VirgoScorpio Hub based on its public repository and project notices."
type: showcase
status: review
owner: "Golden Obsidian LLC"
created: "2026-11-12"
updated: "2026-11-12"
license: "CC-BY-4.0"
tags:
  - human-ai-collaboration
  - platform
  - project-showcase
---

# VirgoScorpio Hub

> **Review status:** This is a high-level public documentation draft. The project repository remains authoritative for implementation, release, configuration, and security status.

## Overview

VirgoScorpio Hub is an early-stage, modular Node.js application platform intended to support governed human-AI collaboration and extensible application services. Its project description emphasizes augmenting human capability while retaining secure, governed interaction.

Within Golden Obsidian LLC's portfolio, VirgoScorpio Hub represents the human-AI collaboration domain: task orchestration, governed interaction, and coordination between people and software agents. This page does not duplicate technical documentation or imply that every described module is production-ready.

## Status and availability

**Source snapshot verified: 2026-11-12.** The public repository's package.json identifies the package as virgoscorpio-hub, version 0.6.2, with private set to true and a Node.js engine requirement of >=22.23.4. The project README describes this line as private and unreleased, limited to an isolated self-hosted developer preview, with production status **NO-GO / NOT_PRODUCTION_CERTIFIED**.

The package version is repository metadata, not evidence of a public npm package or a formal GitHub release. No Git tag or GitHub release was present when this snapshot was checked. Do not describe 0.6.2 as a released or production-ready product version.

The default branch was main; its inspected head was [commit 4a9ee181be5d9d46d94ed11a14de64b4dbbe9907](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub/commit/4a9ee181be5d9d46d94ed11a14de64b4dbbe9907), committed on 2026-11-12. The README's detailed status narrative still refers to an earlier main commit (0748f56e01421d13121ec08f7bc036579e5406835). Because that narrative is not synchronized to the inspected head, this page intentionally does not repeat its commit-specific test counts, benchmark figures, or evidence claims. Consult the current project workflows, issues, and source before relying on such details.

## Relationship to EnginEx

VirgoScorpio Hub includes EnginEx as a pinned Git submodule at vendor/enginex. The submodule records a specific source commit; the canonical EnginEx project and its licensing notices remain in the [EnginEx repository](https://github.com/GoldenObsidianLLC/EnginEx). Do not assume that the submodule automatically tracks the latest EnginEx branch.

## Licensing

The VirgoScorpio Hub [project notice](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub/blob/main/NOTICE.md) declares GPL-2.0-or-later for original project materials, subject to file-specific notices and third-party terms. Review the project's [LICENSE](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub/blob/main/LICENSE) and [third-party notices](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub/blob/main/THIRD-PARTY-NOTICES.md) before reusing project code or assets.

The CC-BY-4.0 metadata on this page applies to this documentation page only. It does not relicense VirgoScorpio Hub source code, dependencies, or third-party materials.

## Sources of truth

- [VirgoScorpio Hub repository](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub)
- [Project README and current status](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub/blob/main/README.md)
- [Package metadata](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub/blob/main/package.json)
- [Project notice](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub/blob/main/NOTICE.md), [license text](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub/blob/main/LICENSE), and [third-party notices](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub/blob/main/THIRD-PARTY-NOTICES.md)
- [Inspected default-branch commit](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub/commit/4a9ee181be5d9d46d94ed11a14de64b4dbbe9907)
- [GitHub releases](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub/releases) and [Git tags](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub/tags)

## Limitations and maintenance

This page is not a product specification, security assessment, release announcement, or deployment authorization. Do not infer production readiness, independent assurance, regulatory compliance, customer deployment, or a public release from a package version, workflow badge, or passing test suite.

Refresh this status section against the exact default-branch head before changing it to published. Keep implementation details, current test evidence, supported integrations, and release records in the project repository rather than duplicating them here.
