# Category playbooks

After choosing a taxonomy category, use its playbook as the investigation and response checklist.

## Universal triage sequence

1. Confirm the correct client and UTC investigation window.
2. Preserve the original alert, entities, detection rule, and evidence references.
3. Select the category in the [taxonomy](../taxonomy/README.md).
4. Open the matching playbook from the taxonomy table.
5. Load the client's current [profile and baseline](../client-profile/README.md) and complete the playbook's baseline checks.
6. Record supporting, contradicting, and unavailable evidence.
7. Contain or escalate before considering tuning.
8. Consider tuning only after the investigation is complete; apply both the playbook criteria and the central [tuning policy](../tuning/README.md).
9. Document the result with the [incident closure template](../incident-closure-library/README.md).

## Classification

Use the native Microsoft Sentinel values defined in the [incident closure template](../incident-closure-library/README.md). Missing required telemetry results in `Undetermined`, not `BenignPositive`.

## Tuning

The `BenignPositive` conditions in a playbook are the minimum evidence for a tuning candidate, not automatic approval. The playbook's `Never auto-close` rule and the central [tuning policy](../tuning/README.md) also apply.
