# Multi-Client SOC Triage Framework

A structured triage methodology for analysts working across multiple Microsoft security environments. The framework connects alert taxonomy, client context, baselines, investigation heuristics, correlation, tuning, outreach, and closure documentation.

## Status and intended use

This repository is a reusable reference and sanitized portfolio example. Validate all queries, thresholds, and automation conditions against the target environment before operational use.

Two safety rules apply throughout the framework:

1. Never suppress or auto-close an incident from one contextual signal such as a familiar user, device, IP address, or low severity.
2. Missing required telemetry produces an **Undetermined** classification, not a benign determination.

## Quick start

1. Identify the category in the [taxonomy](taxonomy/README.md).
2. Load the approved [client context](customer-specific-context/README.md).
3. Compare the activity with the relevant [baseline](baselines/README.md).
4. Apply the category's [heuristics](heuristics/Heuristics-full-framework.md).
5. Complete the [correlation workflow](correlation-workflows/correlation-workflows-list.md).
6. Apply [tuning guidance](tuning/mapped-tuning-guidelines.md) only after the evidence gate is satisfied.
7. Follow the [workflow guide](workflow-guides/mapped-workflow-guides.md) and document the result with the [closure template](incident-closure-library/README.md).

## Framework structure

| Layer | Purpose |
| --- | --- |
| [Taxonomy](taxonomy/README.md) | Stable IDs and definitions for supported alert categories |
| [Client context](customer-specific-context/README.md) | Approved, time-bounded context used during triage |
| [Baselines](baselines/README.md) | Expected behavior with owners and review dates |
| [Heuristics](heuristics/Heuristics-full-framework.md) | Benign and suspicious indicators plus evidence requirements |
| [Correlation workflows](correlation-workflows/correlation-workflows-list.md) | Cross-signal checks across identity, device, network, and control telemetry |
| [Tuning](tuning/mapped-tuning-guidelines.md) | Guardrailed suppression and auto-closure candidates |
| [Workflow guides](workflow-guides/mapped-workflow-guides.md) | Repeatable analyst procedures |
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
