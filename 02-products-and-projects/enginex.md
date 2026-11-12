---
title: "EnginEx - Public Project Overview"
description: "Review-stage overview of EnginEx as Golden Obsidian LLC's enabling developer technology."
type: showcase
status: review
owner: "Golden Obsidian LLC"
created: "2026-11-12"
updated: "2026-11-12"
license: "CC-BY-4.0"
tags:
  - developer-infrastructure
  - node-js
  - templating
  - project-showcase
---

# EnginEx

> **Review status:** This is a high-level public overview. EnginEx's repository, README, package metadata, and project notices remain authoritative for implementation, compatibility, release, and license details.

## Overview

EnginEx is a Node.js HTML template engine. Its public README describes a restricted template-expression language, reusable template composition, bounded rendering, machine-readable grammar and data contracts, and optional AI-provider and Model Context Protocol integrations. These are project-described capabilities; this overview is not an independent implementation or security assessment.

Within Golden Obsidian LLC's portfolio, EnginEx is enabling developer infrastructure. It is maintained in its own repository and is consumed by VirgoScorpio Hub as a pinned Git submodule, rather than being a separately versioned component that automatically follows the latest branch.

## Status and availability

**Source snapshot verified: 2026-11-12.** The public repository's package.json identifies the package as enginex-ai-native, version 7.0.0, with a Node.js engine requirement of >=22.23.4. The default branch was master; its inspected head was [commit d7c10e14835ac7a8a02af7c152d3e1dd24b81e10](https://github.com/GoldenObsidianLLC/EnginEx/commit/d7c10e14835ac7a8a02af7c152d3e1dd24b81e10), committed on 2026-11-06.

No Git tag or GitHub release was present when this snapshot was checked. The 7.0.0 package version must therefore not be represented as a tagged GitHub release or as proof of production qualification.

The project README characterizes 7.0.0 as a security-hardening candidate with remaining validation and independent-review gaps. Automated tests, CI, restricted template execution, or removal of a legacy feature do not by themselves establish an independent security audit or production certification. Consult the project's current security and release-readiness documents before relying on any assurance statement.

## Relationship to VirgoScorpio Hub

VirgoScorpio Hub vendors EnginEx at vendor/enginex as a pinned Git submodule. The exact submodule commit checked out by a VirgoScorpio Hub revision is controlled by that repository's Git tree; it may differ from the current EnginEx master head. See the [VirgoScorpio Hub repository](https://github.com/GoldenObsidianLLC/VirgoScorpio-Hub) for its current integration state.

## Licensing

The EnginEx [project notice](https://github.com/GoldenObsidianLLC/EnginEx/blob/master/NOTICE.md) declares GPL-2.0-or-later for original project materials, subject to file-specific notices and third-party terms. Review the project's [LICENSE](https://github.com/GoldenObsidianLLC/EnginEx/blob/master/LICENSE), [NOTICE](https://github.com/GoldenObsidianLLC/EnginEx/blob/master/NOTICE.md), and third-party notices before reusing code or assets.

The CC-BY-4.0 metadata on this page applies to this documentation page only. It does not relicense EnginEx source code, vendored dependencies, or third-party materials.

## Sources of truth

- [EnginEx repository](https://github.com/GoldenObsidianLLC/EnginEx)
- [Project README](https://github.com/GoldenObsidianLLC/EnginEx/blob/master/README.md)
- [Package metadata](https://github.com/GoldenObsidianLLC/EnginEx/blob/master/package.json)
- [Project notice](https://github.com/GoldenObsidianLLC/EnginEx/blob/master/NOTICE.md), [license text](https://github.com/GoldenObsidianLLC/EnginEx/blob/master/LICENSE), and [third-party notices](https://github.com/GoldenObsidianLLC/EnginEx/blob/master/THIRD-PARTY-NOTICES.md)
- [Inspected default-branch commit](https://github.com/GoldenObsidianLLC/EnginEx/commit/d7c10e14835ac7a8a02af7c152d3e1dd24b81e10)
- [GitHub releases](https://github.com/GoldenObsidianLLC/EnginEx/releases) and [Git tags](https://github.com/GoldenObsidianLLC/EnginEx/tags)

## Limitations and maintenance

This page does not assert that EnginEx is independently audited, certified, production-qualified, or faster than alternatives. Do not turn package metadata, project-authored test results, or optional adapter descriptions into broader claims about safety, compatibility, or performance.

Refresh this page against the exact default-branch head before changing it to published. Keep detailed API references, migration guidance, benchmarks, test results, and release-readiness evidence in the EnginEx repository.
