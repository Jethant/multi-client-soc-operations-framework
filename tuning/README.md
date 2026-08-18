# Tuning policy

Category-specific tuning limits live in each [playbook](../playbooks/README.md). This file covers requirements shared by every suppression or auto-closure change.

## Eligibility gate

Before implementing a tuning exception, require all of the following:

1. The playbook investigation is complete and the incident is classified.
2. The client's [profile and operational baseline](../client-profile/README.md) is current for the facts being used.
3. Required identity, device, application, network, and control telemetry is available.
4. At least two independent contextual signals support the exception.
5. No playbook exclusion, escalation indicator, or correlated anomaly remains unresolved.
6. The proposed logic was tested in monitor-only mode against representative historical data.

Missing telemetry, contradictory evidence, or stale client information routes to analyst review.

## Change record

Record:

- Analytics or detection rule IDs
- Exact boolean conditions and affected scope
- Historical test window and observed false-positive reduction
- Expected true-positive impact
- Change owner, reason, creation date, and expiration date
- Rollback condition and post-deployment review date

## Deployment and review

- Preserve the original detection before changing production behavior.
- Prefer the narrowest conditions that address the demonstrated pattern.
- Review the change after deployment and at its expiration date.
- Roll back when the exception hides unexpected activity, telemetry changes, or its supporting client context expires.
