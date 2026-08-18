# SOC-005 — Local Group Membership Changes

## Scope

Additions to or removals from privileged local groups on endpoints and servers.

## Required telemetry

- Local group membership and operating-system audit events
- Endpoint process, command-line, and user activity
- Remote session and management-tool activity
- Device inventory, ownership, and provisioning state
- Support, provisioning, or change ticket

## Baseline inputs

Consult the **SOC-005** section of the [baseline](../baselines/README.md). Confirm approved management tools, actors, target groups, device populations, and maintenance windows.

## Investigation and correlation

1. Identify the actor, intended member, target group, target device, and change method.
2. Correlate the event with management-tool activity, remote sessions, processes, and command lines.
3. Validate the device's provisioning or support state and the associated ticket.
4. Search for the same actor, member, command, or tool across other devices.
5. Confirm removal when access was intended to be temporary.

## Decision guidance

**BenignPositive candidate:** An approved management tool performed the expected membership change on the intended device population under a valid ticket and maintenance window.

**Escalate or classify TruePositive when:** An unexpected user, script, or remote session adds privileged membership; changes span devices; suspicious processes are present; or membership persists beyond its approved window.

**Undetermined when:** Actor, process, remote-session, device, or ticket evidence is unavailable.

## Containment and follow-up

- Remove unauthorized membership and terminate related remote access.
- Isolate affected devices when malicious execution is possible.
- Preserve commands, processes, sessions, and group membership history.
- Hunt the actor, member, tool, and command across endpoints.

## Tuning restrictions

Do not tune during investigation or containment. After classification, use the **SOC-005** section of the [tuning guidance](../tuning/mapped-tuning-guidelines.md) as the authoritative automation gate.

## Closure record

Record the actor, member, target group and devices, tool or command, ticket, process and session context, removal status, Sentinel classification, and any remaining uncertainty.
