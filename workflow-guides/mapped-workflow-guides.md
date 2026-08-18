# Mapped workflow guides

## Universal workflow

1. Confirm the correct client and UTC investigation window.
2. Preserve the original alert, entities, detection rule, and evidence references.
3. Identify the taxonomy category and required telemetry.
4. Load current client context and baseline; note ownership and review date.
5. Build identity, device, network, application, and control timelines as applicable.
6. Record supporting, contradicting, and unavailable evidence.
7. Choose **Benign**, **Suspicious**, **Confirmed threat**, **Misconfiguration**, or **Needs more evidence**.
8. Contain or escalate before tuning. Apply automation only through the documented tuning gate.
9. Complete outreach, closure documentation, and follow-up ownership.

## SOC-001 — Privileged Operations

- Validate actor, role, PIM activation, MFA, device, session, and change record.
- Capture the exact before-and-after configuration or privilege scope.
- Correlate identity and device timelines.
- Escalate protected-control changes, privilege expansion, or unexplained activity.

## SOC-002 — Authentication Failures

- Build failure-to-success sequences by user, application, device, IP, and method.
- Search the source across other users.
- Review MFA, risk, token, and follow-on activity.
- Escalate spraying, suspicious success, or incomplete telemetry.

## SOC-003 — Conditional Access Changes

- Validate actor, device, PIM, MFA, ticket, and maintenance window.
- Compare before-and-after policy scope, exclusions, and controls.
- Review policy evaluations and follow-on access.
- Escalate any unexplained weakening or bypass.

## SOC-004 — Guest and External User Lifecycle

- Verify sponsor, purpose, domain, access package, groups, and expiration.
- Review sign-ins, applications, downloads, and sharing.
- Confirm periodic review and offboarding.
- Escalate privilege, sensitive access, or missing ownership.

## SOC-005 — Local Group Membership Changes

- Validate actor, tool, device, target group, intended member, and ticket.
- Review remote sessions, processes, and command lines.
- Search for the same change across endpoints.
- Confirm temporary access was removed.

## SOC-006 — Authentication Method Changes

- Validate the user or helpdesk recovery process.
- Compare the new method with approved methods and ownership evidence.
- Review surrounding sign-ins, sessions, device registrations, and sensitive activity.
- Revoke sessions and escalate when compromise is possible.

## SOC-007 — Insider Risk Data Movement

- Determine data classification, business purpose, source, destination, audience, and volume.
- Compare role and project context with historical behavior.
- Correlate identity, device, file, application, and network evidence.
- Escalate external, personal, concealed, or unusually large transfers.

## SOC-008 — Account Creation and Deletion

- Validate lifecycle source, actor, business owner, account type, timing, and ticket.
- Review initial groups, roles, licenses, credentials, and expiration.
- Correlate first sign-ins and resource access.
- For deletion, confirm retention, evidence, and ownership-transfer requirements.

## SOC-009 — Device-Linked Identity Events

- Match the device to inventory, enrollment, ownership, and management records.
- Correlate identity events with endpoint processes and network activity.
- Review duplicate, stale, unmanaged, or unexpectedly privileged devices.
- Escalate suspicious follow-on activity.

## SOC-010 — User-Initiated Threat Activity

- Establish whether the user clicked, submitted, downloaded, opened, or executed.
- Correlate email, browser, endpoint, network, identity, and MFA evidence.
- Hunt the indicators across other users and devices.
- Contain credentials, sessions, devices, or messages before closure when required.

## SOC-011 — Device Threat Activity

- Review signer, hash, path, parent process, command line, user, and network activity.
- Search for persistence, credential access, evasion, execution, and lateral movement.
- Hunt artifacts and behavior across endpoints.
- Escalate abnormal use even when the binary or severity appears familiar.

## SOC-012 — Application Credential Creation

- Validate actor, application owner, PIM, MFA, device, deployment, and ticket.
- Review credential type, lifetime, storage, permissions, consent, and application status.
- Correlate subsequent token use, sign-ins, and privilege changes.
- Remove or rotate unauthorized credentials and escalate unexplained access.
