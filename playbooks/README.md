# Category playbooks

The playbooks are the analyst's primary investigation layer. Each one combines the former heuristic, correlation, and workflow guidance for a single taxonomy category.

## Universal triage sequence

1. Confirm the correct client and UTC investigation window.
2. Preserve the original alert, entities, detection rule, and evidence references.
3. Select the category in the [taxonomy](../taxonomy/README.md).
4. Open the matching playbook below.
5. Load current [client context](../customer-specific-context/README.md) and the relevant [baseline](../baselines/README.md).
6. Record supporting, contradicting, and unavailable evidence.
7. Contain or escalate before considering tuning.
8. Apply the [tuning gate](../tuning/mapped-tuning-guidelines.md) only after the investigation is complete.
9. Document the result with the [incident closure template](../incident-closure-library/README.md).

## Classification

Use the native Microsoft Sentinel values defined in the [incident closure template](../incident-closure-library/README.md). Missing required telemetry results in `Undetermined`, not `BenignPositive`.

## Select a playbook

Use the [taxonomy table](../taxonomy/README.md) as the single category index. Its Playbook column opens the correct investigation file.
