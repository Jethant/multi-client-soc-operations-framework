# Category playbooks

After choosing a taxonomy category, use its playbook as the investigation and response checklist.

## Universal triage sequence

1. Confirm the correct client and UTC investigation window.
2. Preserve the original alert, entities, detection rule, and evidence references.
3. Select the category in the [taxonomy](../taxonomy/README.md).
4. Open the matching playbook from the taxonomy table.
5. Load the client's current [profile and baseline](../client-profile/README.md) and complete the playbook's baseline checks.
6. Record supporting, contradicting, and unavailable evidence.
7. Contain or escalate as needed.
8. When repeated incidents reveal the same benign or expected pattern, raise representative examples for team review. Apply the playbook criteria and central [tuning policy](../tuning/README.md) only after the team accepts a tuning candidate.
9. Document the result with the [incident closure template](../incident-closure-library/README.md).

## Classification

Use the native Microsoft Sentinel values defined in the [incident closure template](../incident-closure-library/README.md). Classify missing required telemetry as `Undetermined`.

## MITRE ATT&CK® mapping

Playbook mappings are candidates, not defaults. Apply a mapping only when the investigation establishes the described adversary behavior, use the most specific supported technique or sub-technique, and leave legitimate or inconclusive activity unmapped. An incident may support more than one mapping.

## Tuning

After team review accepts a recurring pattern for tuning evaluation, the candidate must meet the playbook's `BenignPositive` conditions, remain outside its `Keep under analyst review` conditions, and pass the central [tuning policy](../tuning/README.md).
