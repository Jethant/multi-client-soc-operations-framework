# SOC-001 — Privileged Operations

## Scope

Administrative actions, role changes, privileged access, and changes to protected controls.

## Required telemetry

- Administrative audit and role-assignment records
- Sign-in, PIM, MFA, token, and session activity
- Administrative device and endpoint telemetry
- Network source and access-path context
- Change ticket, approval, and maintenance-window records

## Client baseline checks

Confirm expected administrative roles, devices, network paths, maintenance windows, common tasks, change records, and PIM, MFA, and break-glass workflows against the client profile and current evidence.

## Investigation and correlation

1. Identify the actor, role, target resource, action, and resulting privilege scope.
2. Correlate the action with sign-in, PIM activation, MFA, token, and session activity.
3. Validate the device and network path against current administrative context.
4. Compare the exact before-and-after state with the approved ticket and maintenance window.
5. Review identity and endpoint telemetry before and after the change for related anomalies.

## Decision guidance

**BenignPositive candidate:** The actor, managed administrative device, approved workflow and time window, PIM/MFA evidence, action, and resulting scope all agree with current context.

**Escalate or classify TruePositive when:** Privilege expands unexpectedly, a protected control is weakened, a new administrator appears, a break-glass account is used unexpectedly, or related identity/device activity remains unexplained.

**Undetermined when:** Required PIM, sign-in, device, audit, or approval evidence is unavailable or contradictory.

## Containment and follow-up

- Stop or reverse unauthorized changes.
- Disable or restrict affected privileged access and revoke suspicious sessions.
- Preserve before-and-after configuration, audit records, and approval evidence.
- Hunt for related administrative actions, identities, applications, and devices.

## Tuning

**Keep under analyst review:** Privilege expansion, protected-control changes, break-glass use, unexpected role assignment, or correlated identity/device anomalies.

## Closure record

Record the actor, role, target, exact change, PIM/MFA evidence, device and session context, approval reference, resulting scope, Sentinel classification, and any remaining uncertainty.
