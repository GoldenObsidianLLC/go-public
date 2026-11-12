---
title: "Security Policy"
description: "Provides safe guidance for reporting vulnerabilities and handling security-sensitive information."
type: "policy"
status: "published"
owner: "Golden Obsidian LLC"
created: "2026-11-11"
updated: "2026-11-12"
license: "CC-BY-4.0"
tags:
  - security
  - vulnerability-reporting
  - responsible-disclosure
---

# Security Policy

Golden Obsidian LLC takes the safe handling of security reports seriously. This repository is public, so do not disclose exploitable details or sensitive data in public issues, discussions, pull requests, or commits.

## Reporting a vulnerability

1. As verified on 2026-11-12, GitHub private vulnerability reporting is enabled for this repository. Open the repository's **Security** tab and use the private **Report a vulnerability** flow.
2. If the private reporting control is unavailable in your account or the interface, do not post proof-of-concept code, exploit steps, credentials, affected personal data, or other sensitive details publicly. Ask a maintainer through an already established private communication channel for a verified secure reporting route; do not send vulnerability details until that route is confirmed. A public issue may ask for the correct private reporting route, but must not contain the vulnerability details.
3. Share only the minimum information needed to reproduce and assess the issue through the private channel. Allow maintainers a reasonable opportunity to investigate and coordinate a fix before public disclosure.

The repository setting was confirmed through GitHub's API on 2026-11-12. This policy does not promise a response time or a particular disclosure timeline.

## Automated dependency maintenance

The repository's dependency graph, Dependabot alerts, and Dependabot security updates were enabled on 2026-11-12. The [Dependabot configuration](.github/dependabot.yml) schedules weekly version-update checks for GitHub Actions. The documentation workflow continues to pin actions to full commit SHAs.

Review Dependabot pull requests like other code changes: verify the upstream action and target commit, retain immutable full-SHA references, inspect workflow permissions and behavior changes, and require the protected-branch documentation check to pass before merging. Automated alerts and updates are useful signals, not proof that the repository is free of vulnerabilities.

## Public issue hygiene

Use public issues for non-sensitive documentation and project defects only. Remove secrets from logs and screenshots before sharing. If a secret is exposed, revoke or rotate it at its source; deleting the public text alone does not invalidate the credential.

## Scope

This policy applies to the public documentation repository. Project-specific repositories may maintain their own security policies and supported release ranges; consult those sources for project implementation issues.

For licensing and confidential-material boundaries, see the [Licensing Policy](05-governance-and-policies/licensing.md).
