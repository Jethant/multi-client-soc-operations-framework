# SOC-009 — Device-Linked Identity Events

## Scope

Identity activity that requires endpoint, inventory, enrollment, local-account, or provisioning context.

## Required telemetry

- Device inventory, ownership, enrollment, and management records
- Entra device identity, registration, and sign-in activity
- Endpoint process, local-account, and management-tool telemetry
- Network sessions and remote-access activity
- Provisioning, support, and replacement records

## Baseline inputs

Consult the **SOC-009** section of the [baseline](../baselines/README.md). Confirm managed device identities, naming conventions, provisioning tools, local-account patterns, and maintenance windows.

## Investigation and correlation

1. Match the device identity to inventory, enrollment, ownership, and provisioning records.
2. Correlate cloud identity events with endpoint processes, local accounts, network sessions, and management tools.
3. Review duplicate, stale, unmanaged, or unexpectedly privileged device identities.
4. Search for related identity and device behavior across the environment.
5. Determine whether suspicious follow-on access occurred from the device.

## Decision guidance

**BenignPositive candidate:** Device identity, enrollment, owner, actor, approved management process, and provisioning window all agree, with no suspicious follow-on activity.

**Escalate or classify TruePositive when:** The device is unmanaged, duplicated, stale, unexpectedly privileged, associated with abnormal processes or remote access, or correlated with identity risk.

**Undetermined when:** Inventory, enrollment, endpoint, local-account, or network evidence is incomplete.

## Containment and follow-up

- Isolate suspicious devices and revoke associated sessions when required.
- Remove or disable unauthorized, duplicate, or stale registrations.
- Review local privilege, credentials, enrollment, and management state.
- Hunt linked identities, devices, processes, and sessions.

## Tuning restrictions

Do not tune during investigation or containment. After classification, use the **SOC-009** section of the [tuning guidance](../tuning/mapped-tuning-guidelines.md) as the authoritative automation gate.

## Closure record

Record device identifiers, owner, enrollment and management state, linked identities, processes, local accounts, network sessions, actions taken, Sentinel classification, and any remaining uncertainty.
