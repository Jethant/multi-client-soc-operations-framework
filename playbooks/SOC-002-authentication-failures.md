# SOC-002 — Authentication Failures

## Scope

Failed sign-ins, failure-to-success sequences, password spraying, credential stuffing, lockouts, and MFA-related failures.

## Required telemetry

- Sign-in results, authentication method, application, device, IP, and session identifiers
- MFA prompts and outcomes
- Identity risk and token activity
- Cross-user activity from the same source
- Current user and population authentication baseline

## Baseline inputs

Consult the **SOC-002** section of the [baseline](../baselines/README.md). Use normal volumes and failure-to-success timing as context only after validating the current device and session.

## Investigation and correlation

1. Build the failure and success sequence by user, application, method, device, IP, and session.
2. Search the same source, infrastructure, or client fingerprint across other users.
3. Review MFA prompts, risk detections, token activity, lockouts, and follow-on access.
4. Compare volume, timing, and distribution with the current baseline.
5. Determine whether any successful sign-in followed suspicious failures.

## Decision guidance

**BenignPositive candidate:** A low-volume failure sequence is followed promptly by success from the same managed device and consistent session, with no cross-user source pattern, MFA anomaly, risky sign-in, or suspicious follow-on activity.

**Escalate or classify TruePositive when:** Failures span users, methods, applications, locations, or autonomous systems; success follows suspicious failures; or password-spray, credential-stuffing, impossible-travel, or MFA-fatigue behavior is present.

**Undetermined when:** Session, MFA, device, cross-user, or follow-on activity cannot be verified.

## Containment and follow-up

- Block confirmed hostile sources when appropriate.
- Reset affected credentials and revoke sessions when compromise is possible.
- Review and remove unauthorized MFA methods.
- Hunt the source and attempted credentials across the client environment.

## Tuning restrictions

Do not tune during investigation or containment. After classification, use the **SOC-002** section of the [tuning guidance](../tuning/mapped-tuning-guidelines.md) as the authoritative automation gate.

## Closure record

Record the failure-to-success timeline, affected users and applications, source distribution, device/session match, MFA and risk results, follow-on activity, Sentinel classification, and any remaining uncertainty.
