# SOC-003 — Conditional Access Changes

## Scope

Creation, modification, deletion, disablement, exclusion, or bypass of Conditional Access policies.

## Required telemetry

- Conditional Access audit history and before-and-after policy configuration
- Administrator sign-in, PIM, MFA, token, and session activity
- Administrative device and network context
- Policy evaluation and sign-in results
- Change ticket, approval, design, and maintenance-window records

## Client baseline checks

Check authorized policy administrators, naming, protected controls, deployment rings, maintenance windows, and the change workflow in the client profile.

## Investigation and correlation

1. Identify the actor and capture the exact before-and-after policy scope, controls, exclusions, and state.
2. Correlate the actor's sign-in, device, PIM, MFA, token, and session activity.
3. Validate the ticket, approval, intended design, deployment ring, and maintenance window.
4. Review policy evaluations, failures, exclusions, bypass, and risky follow-on access.
5. Determine whether the change weakened protection for privileged identities, sensitive applications, or broad populations.

## Potential MITRE ATT&CK® mappings

- [T1556.009 — Conditional Access Policies](https://attack.mitre.org/techniques/T1556/009/) when a policy is disabled or modified to enable persistent access or bypass expected authentication controls.

## Decision guidance

**BenignPositive candidate:** The authorized actor, managed device, approval, maintenance window, intended configuration, and resulting controls all agree.

**Escalate or classify TruePositive when:** MFA, compliance, location, risk, or session controls are weakened; broad exclusions are added; policies are disabled; or the change originates from an anomalous session.

**Undetermined when:** Before-and-after configuration, approval, actor session, or policy-evaluation evidence is incomplete.

## Containment and follow-up

- Restore approved controls or disable the unauthorized change.
- Revoke suspicious administrator sessions and restrict affected access.
- Review sign-ins that occurred while protection was weakened.
- Preserve policy configuration and audit evidence.

## Tuning

**Keep under analyst review:** Control removal, broad exclusions, policy disablement, access expansion, or an anomalous administrative session.

## Closure record

Record the actor, approval, before-and-after policy, affected scope, PIM/MFA and device evidence, policy impact, remediation, Sentinel classification, and any remaining uncertainty.
