# Multi-Client SOC Triage Framework

A structured triage methodology for analysts working across multiple Microsoft security environments. The framework connects alert taxonomy, a client-wide operational baseline, category playbooks, tuning governance, outreach, and closure documentation.

## Status and intended use

This repository is a reusable reference and sanitized portfolio example. Validate all queries, thresholds, and automation conditions against the target environment before operational use.

Two safety rules apply throughout the framework:

1. Never suppress or auto-close an incident from one contextual signal such as a familiar user, device, IP address, or low severity.
2. Missing required telemetry produces an **Undetermined** classification, not a benign determination.

## Quick start

1. Identify the category in the [taxonomy](taxonomy/README.md).
2. Load the client's current [profile and operational baseline](client-profile/README.md).
3. Follow the category's [playbook](playbooks/README.md), including its baseline checks, investigation, decision, containment, and category-specific tuning criteria.
4. Apply the central [tuning policy](tuning/README.md) only after the investigation is complete.
5. Document the result with the [closure template](incident-closure-library/README.md) and use approved [outreach](outreach-templates/email-canned-replies.md) when needed.

## Framework structure

| Layer | Purpose |
| --- | --- |
| [Taxonomy](taxonomy/README.md) | Stable IDs and definitions for supported alert categories |
| [Client profile and baseline](client-profile/README.md) | One current source for client context, expected behavior, operational cycles, and exceptions |
| [Category playbooks](playbooks/README.md) | Baseline checks, investigation, correlation, decision, containment, tuning criteria, and closure steps by category |
| [Tuning policy](tuning/README.md) | Universal testing, ownership, expiration, rollback, and review requirements |
| [Outreach templates](outreach-templates/email-canned-replies.md) | Conditional, user-safe communications |
| [Incident closure library](incident-closure-library/README.md) | Evidence-based documentation and sanitized examples |
| [Threat hunting](threat-hunting/Threat-Hunting-Topics.md) | Hypothesis-driven follow-up investigations |
| [Reference material](reference-material/README.md) | Tested queries and approved research resources |

## Client data

Only sanitized examples belong in this public repository. Do not commit live client names, user identities, internal network ranges, raw messages, credentials, tokens, case evidence, or escalation contacts. Completed client profiles should remain in the access-controlled system used for that client.

## Validation

Run the repository checks before proposing a change:

```text
python scripts/validate_framework.py
```

The validator checks taxonomy coverage, internal links, and common sanitization or naming mistakes.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for the update rules that keep the framework's layers synchronized.
