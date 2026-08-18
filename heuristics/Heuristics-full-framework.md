# Investigation heuristics

Heuristics guide investigation; they do not replace evidence. A **BenignPositive** classification requires all required telemetry, at least two independent benign indicators, no unresolved escalation indicator, and a current client baseline. Otherwise classify the incident as **Undetermined** or escalate it.

## Required closure record

- Time range and client scope investigated
- Data sources checked and any unavailable telemetry
- Evidence supporting and contradicting the conclusion
- Correlated alerts or incidents
- Analyst confidence and remaining uncertainty
- Closure classification and follow-up owner

## SOC-001 — Privileged Operations

**Benign indicators**

- Actor, managed admin device, time window, and workflow match a current baseline.
- A valid change or approval record explains the action.
- PIM activation and MFA records align with the activity.

**Escalate when**

- Privilege increased, a protected control changed, or a new administrator appeared unexpectedly.
- The activity used a break-glass account, unmanaged device, unusual token, or unfamiliar session.
- Related identity or device anomalies remain unexplained.

## SOC-002 — Authentication Failures

**Benign indicators**

- A small failure sequence is followed promptly by a successful sign-in from the same managed device and session context.
- Volume and timing remain within a current user or population baseline.

**Escalate when**

- Failures span users, methods, applications, locations, or autonomous systems.
- Success follows suspicious failures, MFA fatigue, impossible travel, or unfamiliar session properties.
- The same source exhibits password-spray or credential-stuffing behavior.

## SOC-003 — Conditional Access Changes

**Benign indicators**

- The actor, device, maintenance window, and change record all align.
- The resulting policy scope and controls match the approved design.

**Escalate when**

- MFA, device compliance, location, risk, or session controls were weakened.
- Users or applications were broadly excluded.
- The change originated from an anomalous identity or device session.

## SOC-004 — Guest and External User Lifecycle

**Benign indicators**

- Sponsor, domain, project, access package, group, and expiration match approved context.
- The guest's activity remains within the documented purpose.

**Escalate when**

- Privileged roles, sensitive groups, broad application consent, or persistent access are introduced.
- No sponsor or business purpose can be verified.
- Guest activity shows suspicious sign-ins, downloads, or cross-tenant access.

## SOC-005 — Local Group Membership Changes

**Benign indicators**

- An approved management tool performed the change during provisioning or support work.
- The actor, device, target group, and ticket all align.

**Escalate when**

- A user, script, or remote session adds unexpected privileged membership.
- Changes occur across many devices or correlate with suspicious processes.
- Membership persists beyond the approved work window.

## SOC-006 — Authentication Method Changes

**Benign indicators**

- The user or helpdesk followed the approved recovery or device-replacement process.
- Method ownership, device, IP context, and audit trail agree.

**Escalate when**

- A new method appears during risky sign-ins or immediately before sensitive activity.
- Existing methods are removed, recovery data changes unexpectedly, or ownership cannot be verified.
- Session revocation and identity containment may be required.

## SOC-007 — Insider Risk Data Movement

**Benign indicators**

- Data classification, source, destination, volume, role, and project context all align.
- Sharing remains within the approved audience and retention rules.

**Escalate when**

- Sensitive data moves to personal, external, newly created, or unsanctioned destinations.
- Volume, timing, compression, staging, or deletion behavior is abnormal.
- Activity coincides with resignation, access changes, or suspicious identity/device events.

## SOC-008 — Account Creation and Deletion

**Benign indicators**

- An approved lifecycle system or administrator performed the action.
- HR, contractor, service-account, or test-account documentation matches timing and attributes.
- Initial groups, licenses, roles, credentials, and expiration match the approved profile.

**Escalate when**

- A new identity receives privilege, bypasses lifecycle controls, or signs in unexpectedly.
- Deletion disables investigation, audit, retention, or recovery.
- The actor, source, business owner, or purpose cannot be verified.

## SOC-009 — Device-Linked Identity Events

**Benign indicators**

- Device identity, enrollment, actor, management process, and provisioning window align.
- Endpoint telemetry shows the expected parent process and no suspicious follow-on activity.

**Escalate when**

- The device is unmanaged, duplicated, stale, or associated with suspicious identity activity.
- Unexpected processes, persistence, remote access, or local privilege changes are present.

## SOC-010 — User-Initiated Threat Activity

**Benign indicators**

- Protective controls blocked the interaction and device telemetry confirms no execution.
- Identity evidence confirms no credential submission, new session, token abuse, or MFA change.

**Escalate when**

- Credentials or sensitive data were submitted, an attachment executed, or a payload was written.
- Browser, network, device, or identity telemetry is unavailable or contradictory.
- Related users or devices interacted with the same infrastructure.

## SOC-011 — Device Threat Activity

**Benign indicators**

- File hash, signer, path, parent process, command line, and software owner support an approved use.
- No persistence, credential access, defense evasion, or malicious network activity is present.

**Escalate when**

- The alert involves credential theft, persistence, evasion, remote execution, or lateral movement.
- A nominally approved binary exhibits an abnormal path, parent, command line, or destination.
- Low severity repeats across endpoints or correlates with higher-confidence telemetry.

## SOC-012 — Application Credential Creation

**Benign indicators**

- The actor, application owner, managed device, deployment workflow, and change record align.
- Credential type, lifetime, permissions, and storage meet the approved standard.
- The application and service principal are expected and recently reviewed.

**Escalate when**

- The credential is long-lived, added to a dormant or high-privilege application, or lacks an owner.
- Consent, permissions, or role assignments expand unexpectedly.
- The actor or application has risky sign-ins, anomalous tokens, or unrelated suspicious activity.

## Evidence-based closing note

> Reviewed **[category and incident]** for **[client scope]** over **[UTC time range]**. Evidence from **[data sources]** showed **[observed facts]**. The activity **[matched/did not match]** baseline **[reference and review date]**. Contradictory or unavailable evidence: **[details or none]**. Disposition: **[classification]**, confidence **[low/medium/high]**. Follow-up: **[action, owner, and due date or none]**.
