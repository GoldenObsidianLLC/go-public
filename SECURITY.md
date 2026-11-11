---
title: "Security Policy"
description: "Provides safe guidance for reporting vulnerabilities and handling security-sensitive information."
type: "policy"
status: "published"
owner: "Golden Obsidian LLC"
created: "2026-11-11"
updated: "2026-11-11"
license: "CC-BY-4.0"
tags:
  - security
  - vulnerability-reporting
  - responsible-disclosure
---

# Security Policy

Golden Obsidian LLC takes the safe handling of security reports seriously. This repository is public, so do not disclose exploitable details or sensitive data in public issues, discussions, pull requests, or commits.

## Reporting a vulnerability

1. Check whether GitHub's private vulnerability reporting is enabled for this repository. When available, use the repository's private **Report a vulnerability** flow.
2. If private reporting is not available, do not post proof-of-concept code, exploit steps, credentials, affected personal data, or other sensitive details publicly. Use a verified private maintainer contact channel linked from the official Golden Obsidian GitHub presence. A public issue may ask for the correct private reporting route, but must not contain the vulnerability details.
3. Share only the minimum information needed to reproduce and assess the issue through the private channel. Allow maintainers a reasonable opportunity to investigate and coordinate a fix before public disclosure.

Do not assume that a security feature is enabled until the repository settings confirm it. This policy does not promise a response time or a particular disclosure timeline.

## Public issue hygiene

Use public issues for non-sensitive documentation and project defects only. Remove secrets from logs and screenshots before sharing. If a secret is exposed, revoke or rotate it at its source; deleting the public text alone does not invalidate the credential.

## Scope

This policy applies to the public documentation repository. Project-specific repositories may maintain their own security policies and supported release ranges; consult those sources for project implementation issues.

For licensing and confidential-material boundaries, see the [Licensing Policy](05-governance-and-policies/licensing.md).
