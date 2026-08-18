# Tuning guidelines

Tuning reduces repeatable false positives without removing visibility into abuse. An expected user, device, IP address, process, maintenance window, low severity, or successful control action is never sufficient by itself.

## Automation gate

Before suppressing or auto-closing, require all of the following:

1. The client baseline is current, owned, and independently verified.
2. At least two independent contextual signals match.
3. Required identity, device, and control telemetry is available.
4. No escalation indicator or correlated anomaly is unresolved.
5. The exception records its owner, reason, scope, creation date, expiration date, and change reference.
6. The proposed logic was tested in monitor-only mode against representative historical data.

Missing telemetry, contradictory evidence, or an expired exception routes to analyst review.

## SOC-001 — Privileged Operations

**Automation candidate:** actor, managed admin device, approved workflow, PIM/MFA evidence, change record, and time window all match.

**Never auto-close:** privilege expansion, protected-control changes, break-glass use, unexpected role assignment, or correlated identity/device anomalies.

## SOC-002 — Authentication Failures

**Automation candidate:** a low-volume failure sequence is followed promptly by success from the same managed device and consistent session context, with no cross-user source pattern or MFA anomaly.

**Never auto-close:** distributed failures, password spraying, success after suspicious failures, unfamiliar session properties, risky sign-ins, or repeated MFA prompts.

## SOC-003 — Conditional Access Changes

**Automation candidate:** actor, managed device, approved ticket, maintenance window, before-and-after policy scope, and resulting controls all match.

**Never auto-close:** control removal, broad exclusions, policy disablement, access expansion, or an anomalous admin session.

## SOC-004 — Guest and External User Lifecycle

**Automation candidate:** inviter, sponsor, approved domain, project, access package, group set, and expiration all match current context.

**Never auto-close:** privileged access, sensitive-group membership, missing sponsor, persistent access, unusual sign-ins, or unexpected data movement.

## SOC-005 — Local Group Membership Changes

**Automation candidate:** approved management tool, support or provisioning ticket, expected device population, intended member, target group, and maintenance window all match.

**Never auto-close:** interactive or remote manual additions, broad device scope, unexpected privileged membership, suspicious processes, or missing endpoint telemetry.

## SOC-006 — Authentication Method Changes

**Automation candidate:** approved self-service or helpdesk workflow, verified user, managed device, expected method, and clean sign-in timeline all agree.

**Never auto-close:** new or removed methods during risky activity, ownership uncertainty, recovery-detail changes, unfamiliar sessions, or sensitive follow-on activity.

## SOC-007 — Insider Risk Data Movement

**Automation candidate:** role, approved project, data classification, source, destination, audience, volume, and device context all match a current baseline.

**Never auto-close:** sensitive data, external or personal destinations, unusual volume, staging or compression, concealment, off-hours activity, or identity/device anomalies.

## SOC-008 — Account Creation and Deletion

**Automation candidate:** approved lifecycle source, authorized actor, business owner, ticket, account type, initial access profile, and timing all match.

**Never auto-close:** privileged or unowned accounts, lifecycle bypass, unexpected first sign-in, abnormal credential creation, missing expiration, or deletion that affects audit and retention.

## SOC-009 — Device-Linked Identity Events

**Automation candidate:** managed device, approved enrollment or provisioning workflow, expected management process, actor, and time window all match.

**Never auto-close:** unmanaged or duplicate devices, abnormal processes, remote access, local privilege changes, or correlated identity risk.

## SOC-010 — User-Initiated Threat Activity

**Automation candidate:** control telemetry confirms a block and independent endpoint plus identity evidence confirms no execution, submission, new session, token abuse, or MFA change.

**Never auto-close:** unavailable device telemetry, credential or data submission, attachment execution, payload write, repeated interaction, or related affected entities.

## SOC-011 — Device Threat Activity

**Automation candidate:** approved software owner, signer, hash, path, parent process, command line, and network behavior all match; no malicious capability or follow-on activity is present.

**Never auto-close:** credential theft, persistence, defense evasion, remote execution, lateral movement, abnormal use of an approved binary, or repeated low-severity detections across devices.

## SOC-012 — Application Credential Creation

**Automation candidate:** authorized actor and application owner, approved deployment, change record, managed device, expected credential type and lifetime, and unchanged permission scope all match.

**Never auto-close:** long-lived secrets, dormant or high-privilege applications, missing owners, new consent, expanded permissions, risky actor activity, or unexplained token use.

## Tuning review record

Every production exception should record:

- Analytics or detection rule IDs
- Exact boolean conditions
- Historical test window and false-positive reduction
- Expected true-positive impact
- Owner, approver, change reference, and expiration
- Rollback condition and post-deployment review date
