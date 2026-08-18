# SOC-006 — Authentication Method Changes

## Scope

MFA registration, replacement, removal, recovery-detail changes, and helpdesk or self-service recovery.

## Required telemetry

- Authentication-method and identity audit records
- Sign-in, MFA, token, session, and risk activity
- Device registration and ownership context
- Helpdesk, self-service recovery, and user-verification records
- Sensitive actions following the method change

## Client baseline checks

Compare the approved recovery workflow, supported MFA methods, device replacement, and onboarding patterns with the client profile.

## Investigation and correlation

1. Build a timeline of sign-ins, recovery activity, MFA prompts, and method changes.
2. Validate the user or helpdesk identity through the approved recovery process.
3. Confirm ownership of the new method and compare device and IP context.
4. Review sessions, tokens, device registrations, and sensitive actions after the change.
5. Determine whether existing methods were removed or recovery details changed unexpectedly.

## Decision guidance

**BenignPositive candidate:** The verified user or authorized helpdesk followed the approved workflow, and method ownership, device, sign-in, and audit evidence all agree.

**Escalate or classify TruePositive when:** A method appears during risky activity, existing methods are removed unexpectedly, recovery data changes, ownership cannot be verified, or sensitive follow-on activity occurs.

**Undetermined when:** User verification, method ownership, sign-in, device, or follow-on activity cannot be confirmed.

## Containment and follow-up

- Remove unauthorized methods and recovery details.
- Reset credentials and revoke sessions when compromise is possible.
- Reverify the user through an approved independent channel.
- Review related device registrations and sensitive actions.

## Tuning

**Keep under analyst review:** New or removed methods during risky activity, ownership uncertainty, recovery-detail changes, unfamiliar sessions, or sensitive follow-on activity.

## Closure record

Record the actor, verification method, added or removed methods, recovery changes, sign-in and device context, session actions, Sentinel classification, and any remaining uncertainty.
