# SOC-004 — Guest and External User Lifecycle

## Scope

Guest invitations, access changes, sponsorship, review, expiration, and offboarding.

## Required telemetry

- Guest invitation and lifecycle audit records
- Sponsor, project, domain, access-package, group, role, and expiration data
- Guest sign-ins, applications, consent, downloads, and sharing activity
- Access-review and offboarding records
- Inviter and administrator session context

## Client baseline checks

Check approved inviters, sponsors, partner domains, projects, access packages, groups, access duration, and review cadence against the client profile.

## Investigation and correlation

1. Validate the inviter, sponsor, business purpose, domain, project, access package, groups, and expiration.
2. Review role, application, group, consent, and sensitive-resource assignments.
3. Correlate the guest's sign-ins, device context, downloads, sharing, and application activity.
4. Verify periodic access review and removal at the expected lifecycle boundary.
5. Determine whether access persisted or expanded beyond the approved purpose.

## Decision guidance

**BenignPositive candidate:** Sponsor, purpose, domain, access package, group set, expiration, and observed activity all agree with current context.

**Escalate or classify TruePositive when:** Privileged or sensitive access is introduced, sponsorship cannot be verified, access persists unexpectedly, or suspicious sign-in, download, consent, or cross-tenant activity is present.

**Undetermined when:** Sponsor, purpose, expiration, assignment, or activity evidence cannot be established.

## Containment and follow-up

- Disable or restrict unauthorized guest access.
- Remove unexpected groups, roles, consent, and application access.
- Notify the sponsor and resource owner through approved channels.
- Hunt for related external identities, invitations, and data access.

## Tuning

**Never auto-close:** Privileged access, sensitive-group membership, missing sponsor, persistent access, unusual sign-ins, or unexpected data movement.

## Closure record

Record the inviter, sponsor, purpose, domain, assignments, expiration, observed activity, review/offboarding result, Sentinel classification, and any remaining uncertainty.
