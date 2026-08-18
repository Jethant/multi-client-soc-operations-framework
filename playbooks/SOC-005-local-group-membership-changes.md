# SOC-005 — Local Group Membership Changes

## Scope

Additions to or removals from privileged local groups on endpoints and servers.

## Required telemetry

- Local group membership and operating-system audit events
- Endpoint process, command-line, and user activity
- Remote session and management-tool activity
- Device inventory, ownership, and provisioning state
- Support, provisioning, or change ticket

## Client baseline checks

Check approved management actors and tools, device populations, support workflows, privileged local groups, normal change volume, and deployment windows against the client profile.

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

## Tuning

**Never auto-close:** Interactive or remote manual additions, broad device scope, unexpected privileged membership, suspicious processes, or missing endpoint telemetry.

## Closure record

Record the actor, member, target group and devices, tool or command, ticket, process and session context, removal status, Sentinel classification, and any remaining uncertainty.
