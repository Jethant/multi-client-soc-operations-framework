# SOC-003 — Conditional Access Changes

## Scope

Creation, modification, deletion, disablement, exclusion, or bypass of Conditional Access policies.

## Required telemetry

- Conditional Access audit history and before-and-after policy configuration
- Administrator sign-in, PIM, MFA, token, and session activity
- Administrative device and network context
- Policy evaluation and sign-in results
- Change ticket, approval, design, and maintenance-window records

## Baseline inputs

Consult the **SOC-003** section of the [baseline](../baselines/README.md). Confirm authorized administrators, protected controls, deployment rings, and current change procedures.

## Investigation and correlation

1. Identify the actor and capture the exact before-and-after policy scope, controls, exclusions, and state.
2. Correlate the actor's sign-in, device, PIM, MFA, token, and session activity.
3. Validate the ticket, approval, intended design, deployment ring, and maintenance window.
4. Review policy evaluations, failures, exclusions, bypass, and risky follow-on access.
5. Determine whether the change weakened protection for privileged identities, sensitive applications, or broad populations.

## Decision guidance

**BenignPositive candidate:** The authorized actor, managed device, approval, maintenance window, intended configuration, and resulting controls all agree.

**Escalate or classify TruePositive when:** MFA, compliance, location, risk, or session controls are weakened; broad exclusions are added; policies are disabled; or the change originates from an anomalous session.

**Undetermined when:** Before-and-after configuration, approval, actor session, or policy-evaluation evidence is incomplete.

## Containment and follow-up

- Restore approved controls or disable the unauthorized change.
- Revoke suspicious administrator sessions and restrict affected access.
- Review sign-ins that occurred while protection was weakened.
- Preserve policy configuration and audit evidence.

## Tuning restrictions

Do not tune during investigation or containment. After classification, use the **SOC-003** section of the [tuning guidance](../tuning/mapped-tuning-guidelines.md) as the authoritative automation gate.

## Closure record

Record the actor, approval, before-and-after policy, affected scope, PIM/MFA and device evidence, policy impact, remediation, Sentinel classification, and any remaining uncertainty.
