# Incident closure library

This section provides a concise closure format and sanitized case studies. A routine closure should let another analyst understand what triggered the incident, what the investigation established, what actions were taken, and why the final classification was selected.

## Routine closure template

### Incident overview

- Alert name, category, and severity
- Affected users, devices, applications, or other entities
- Investigation window
- Brief description of the activity that triggered the incident

### Investigation findings

- Evidence that determined the outcome
- Relevant client context or expected behavior
- Important telemetry gaps or contradictory evidence, when they affect the conclusion

### Actions taken

- Containment, remediation, outreach, or threat-hunting actions
- Record `None` when no action was required

### Final assessment

- Microsoft Sentinel classification
- Concise reason for the classification
- Remaining risk or follow-up, when applicable

## Short closure statement

> Investigated **[alert]** affecting **[entities]** during **[time range]**. Findings: **[decisive evidence]**. Actions: **[actions or none]**. Closed as **[Microsoft Sentinel classification]** because **[reason]**. Follow-up: **[item or none]**.

## Microsoft Sentinel classifications

- `TruePositive` — the detection accurately identified suspicious or malicious activity
- `BenignPositive` — the detection accurately identified suspicious-looking but expected activity
- `FalsePositive` — the incident resulted from incorrect alert logic or inaccurate data
- `Undetermined` — the available evidence was insufficient or contradictory

## Optional detail

Add detail when it materially helps explain the investigation:

- Indicators or threat-intelligence context
- Event timeline
- Third-party findings and their source
- Client baseline deviations
- Unavailable telemetry
- Evidence references to protected source locations
- Legal, privacy, financial, or notification requirements
- Lessons learned from a major or unusual incident

Follow-up actions should include an owner and due date when they are assigned.

## Recurring-alert follow-up

Routine closure does not require a tuning decision. When repeated incidents show the same benign or expected pattern, record representative incident examples and raise a tuning candidate for team review. Assessment, approval, testing, and implementation occur separately under the [tuning policy](../tuning/README.md).

## Sanitized case studies

- [Business email compromise involving an external vendor](case-studies/Business-Email-Compromise.md)
- [Benign project archive flagged on multiple endpoints](case-studies/Blocked-malicious-archive-on-multiple-endpoints.md)
- [Blocked drive-by redirect](case-studies/Blocked-drive-by-redirect.md)
- [Blocked ransomware-linked web activity](case-studies/Ransomware.md)
