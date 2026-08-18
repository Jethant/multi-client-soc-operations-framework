# Incident closure library

This section contains an evidence-based closure template and sanitized case studies. Case studies distinguish observed facts, third-party statements, analyst inference, and unknowns.

## Closure requirements

- Document the client scope and UTC investigation window.
- Record every data source checked and any unavailable telemetry.
- Cite evidence for material claims; do not convert absence of evidence into proof of absence.
- State remaining uncertainty and confidence.
- Assign an owner and due date to every follow-up action.

## Incident documentation template

### 1. Incident summary

- Taxonomy ID and category
- Detection source, rule ID, severity, and incident ID
- Created time and investigation window in UTC
- Affected users, devices, applications, or data using approved references
- Concise description of the observed activity

### 2. Initial indicators

- Alert details and suspicious properties
- Immediate risks and containment decisions
- Related alerts, incidents, or threat intelligence

### 3. Evidence and availability

| Source | Time range | Result | Evidence reference | Available? |
| --- | --- | --- | --- | --- |
| Identity | | | | |
| Device | | | | |
| Network | | | | |
| Email or application | | | | |
| Control or audit logs | | | | |

### 4. Baseline and client context

- Baseline reference, owner, and last review date
- Matching expected behavior
- Deviations and expired or missing context

### 5. Correlation timeline

- Ordered identity, device, network, application, MFA, policy, and file events
- Supporting evidence
- Contradictory evidence
- Unknowns or telemetry gaps

### 6. Actions taken

- Containment and remediation
- User, client, or stakeholder outreach
- Evidence preservation
- Threat hunt or scoping activity

### 7. Tuning decision

- No tuning / monitor-only candidate / time-limited exception / production exception
- Conditions, scope, owner, approval, expiration, and rollback trigger
- Historical validation result

### 8. Final determination

Use the native Microsoft Sentinel incident classification values:

- `TruePositive` — the detection accurately identified suspicious or malicious activity
- `BenignPositive` — the detection accurately identified suspicious-looking but expected activity
- `FalsePositive` — the incident resulted from incorrect alert logic or inaccurate data
- `Undetermined` — the available evidence is insufficient or contradictory
- Classification reason, when applicable
- Confidence: low / medium / high
- Remaining uncertainty

### 9. Closure statement

> Reviewed **[incident]** for **[client scope]** over **[UTC time range]**. Evidence from **[sources]** established **[observed facts]**. The activity **[matched/did not match]** baseline **[reference]**. Unavailable or contradictory evidence: **[details or none]**. Disposition: **[classification]**, confidence **[level]**. Follow-up: **[owner and due date or none]**.

### 10. Follow-up actions

- Action, owner, due date, and verification method
- Baseline, detection, workflow, or outreach updates
- Legal, privacy, financial, or client notification requirements

### 11. Lessons learned

- Detection or telemetry gaps
- New correlation patterns
- Training or process changes
- Reusable sanitized knowledge

### 12. Evidence references

Reference protected source locations; do not copy sensitive evidence into this public repository.

## Sanitized case studies

- [Business email compromise involving an external vendor](case-studies/Business-Email-Compromise.md)
- [Blocked malicious archive on multiple endpoints](case-studies/Blocked-malicious-archive-on-multiple-endpoints.md)
- [Blocked drive-by redirect](case-studies/Blocked-drive-by-redirect.md)
- [Blocked ransomware-linked web activity](case-studies/Ransomware.md)
