# Correlation workflows

Use the client-approved UTC time window and record every source checked. Do not treat missing telemetry as a negative finding.

## SOC-001 — Privileged Operations

1. Correlate the administrative action with sign-in, PIM, MFA, and token activity.
2. Validate the device and network session against the current baseline.
3. Compare the exact change with its ticket, approval, and resulting privilege scope.
4. Review device and identity telemetry before and after the action.

## SOC-002 — Authentication Failures

1. Build the user's failure and success sequence by application, method, device, IP, and session.
2. Search the same source across other users to detect spraying or stuffing.
3. Review MFA prompts, risk detections, token activity, and follow-on access.
4. Compare volume and timing with the current baseline.

## SOC-003 — Conditional Access Changes

1. Correlate the actor's sign-in, device, PIM, and MFA history.
2. Capture the before-and-after policy configuration and affected scope.
3. Validate the change record and maintenance window.
4. Search for policy evaluation failures, exclusions, bypass, and follow-on risky access.

## SOC-004 — Guest and External User Lifecycle

1. Validate inviter, sponsor, domain, project, access package, and expiration.
2. Review group, role, application, and consent assignments.
3. Correlate the guest's sign-ins, device, downloads, and sharing activity.
4. Confirm removal or review at the expected lifecycle boundary.

## SOC-005 — Local Group Membership Changes

1. Correlate the target device, actor, management tool, remote session, and support ticket.
2. Review process creation and command-line telemetry around the change.
3. Search for the same member or actor across other devices.
4. Confirm removal when access was intended to be temporary.

## SOC-006 — Authentication Method Changes

1. Build a timeline of sign-ins, recovery activity, MFA prompts, and method changes.
2. Validate user or helpdesk identity through the approved recovery workflow.
3. Review sessions, tokens, device registrations, and sensitive actions after the change.
4. Check whether existing methods were removed or recovery details changed.

## SOC-007 — Insider Risk Data Movement

1. Correlate identity, device, application, file, and network timelines.
2. Determine data classification, source, destination, volume, and sharing audience.
3. Compare activity with role, project, and historical baseline.
4. Search for staging, compression, deletion, external upload, or other concealment behavior.

## SOC-008 — Account Creation and Deletion

1. Validate actor, lifecycle source, business owner, ticket, and intended account type.
2. Review initial groups, roles, licenses, credentials, and expiration.
3. Correlate first sign-ins, application access, and device activity.
4. For deletion, confirm retention, audit, ownership transfer, and offboarding requirements.

## SOC-009 — Device-Linked Identity Events

1. Match the device identity to inventory, enrollment, ownership, and provisioning records.
2. Correlate identity events with processes, local accounts, network sessions, and management tools.
3. Search for duplicate or stale device identities.
4. Review suspicious follow-on activity across both device and cloud timelines.

## SOC-010 — User-Initiated Threat Activity

1. Establish what the user opened, clicked, submitted, downloaded, or executed.
2. Correlate email, browser, network, endpoint, identity, and MFA evidence.
3. Hunt the same indicators across users and devices.
4. Verify control outcomes independently; a block event alone does not prove containment.

## SOC-011 — Device Threat Activity

1. Review file, signer, hash, path, parent-child process, command line, and user context.
2. Correlate persistence, credential access, defense evasion, network, and lateral movement telemetry.
3. Search the same artifacts and behavior across endpoints.
4. Compare with approved software and testing baselines, including owner and expiration.

## SOC-012 — Application Credential Creation

1. Correlate the actor's sign-in, device, PIM, MFA, and audit activity.
2. Review the target application, service principal, owners, permissions, consent, and recent changes.
3. Validate credential type, lifetime, storage workflow, and change record.
4. Search for token use, new sign-ins, or privilege changes after credential creation.
