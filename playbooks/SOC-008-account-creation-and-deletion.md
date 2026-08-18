# SOC-008 — Account Creation and Deletion

## Scope

Creation, deletion, disablement, and lifecycle activity for user, service, test, contractor, and automation identities.

## Required telemetry

- Identity-provider and lifecycle-system audit records
- Actor, business owner, HR or project source, and ticket
- Initial groups, roles, licenses, credentials, and expiration
- First sign-ins, applications, device activity, and resource access
- Retention, ownership-transfer, recovery, and offboarding records

## Baseline inputs

Consult the **SOC-008** section of the [baseline](../baselines/README.md). Confirm authorized lifecycle systems, administrators, account types, initial-access profiles, timing, and expiration practices.

## Investigation and correlation

1. Validate the actor, lifecycle source, business owner, account type, purpose, timing, and ticket.
2. Review initial groups, roles, licenses, credentials, and expiration.
3. Correlate first sign-ins, application access, device activity, and subsequent privilege changes.
4. For deletion, confirm retention, audit, ownership transfer, recovery, and offboarding requirements.
5. Determine whether the action bypassed the approved lifecycle workflow.

## Decision guidance

**BenignPositive candidate:** The approved lifecycle source or authorized administrator performed the documented action, and account type, owner, timing, initial access, and expiration all agree.

**Escalate or classify TruePositive when:** A new identity receives unexpected privilege, bypasses lifecycle controls, signs in unexpectedly, lacks an owner or expiration, or deletion interferes with audit and recovery.

**Undetermined when:** Actor, lifecycle source, owner, purpose, initial access, sign-in, or retention evidence cannot be established.

## Containment and follow-up

- Disable unauthorized accounts and remove unexpected privilege.
- Revoke sessions and credentials associated with suspicious identities.
- Preserve lifecycle, audit, and access evidence before deletion.
- Transfer ownership and restore retention or recovery controls when required.

## Tuning restrictions

Do not tune during investigation or containment. After classification, use the **SOC-008** section of the [tuning guidance](../tuning/mapped-tuning-guidelines.md) as the authoritative automation gate.

## Closure record

Record the actor, lifecycle source, owner, purpose, account type, initial access, expiration, first activity or deletion safeguards, Sentinel classification, and any remaining uncertainty.
