# SOC-010 — User-Initiated Threat Activity

## Scope

Phishing, malicious links, attachments, downloads, credential submission, and other risky user interactions.

## Required telemetry

- Message, sender, authentication, delivery, URL, and attachment records
- Browser, URL-click, network, and web-control activity
- Endpoint file, process, and protection telemetry
- Sign-in, token, session, MFA, and authentication-method activity
- Indicator prevalence across users and devices

## Client baseline checks

Use the [client profile and operational baseline](../client-profile/README.md) to verify approved simulations, expected email, browser and endpoint controls, reporting workflows, available telemetry, and known coverage gaps.

## Investigation and correlation

1. Establish whether the user opened, clicked, submitted, downloaded, or executed.
2. Correlate email, browser, network, endpoint, identity, token, and MFA evidence.
3. Verify control outcomes independently; a block event alone does not prove containment.
4. Hunt the message, sender, URL, hash, infrastructure, and behavior across users and devices.
5. Determine whether credentials, data, sessions, or endpoints require containment.

## Decision guidance

**BenignPositive candidate:** Control telemetry confirms a block and independent endpoint plus identity evidence confirms no execution, submission, new session, token abuse, or MFA change.

**Escalate or classify TruePositive when:** Credentials or data were submitted, an attachment executed, a payload was written, suspicious sessions followed, or related users or devices interacted with the same infrastructure.

**Undetermined when:** Browser, endpoint, network, identity, or interaction telemetry is unavailable or contradictory.

## Containment and follow-up

- Purge confirmed malicious messages and block approved indicators.
- Revoke sessions, reset credentials, and review MFA methods when exposure is possible.
- Isolate affected devices and quarantine artifacts when execution is possible.
- Notify affected users using the approved [outreach template](../outreach-templates/email-canned-replies.md).

## Tuning

Apply the central [tuning policy](../tuning/README.md) after investigation and containment.

**Automation candidate:** Control telemetry confirms a block and independent endpoint plus identity evidence confirms no execution, submission, new session, token abuse, or MFA change.

**Never auto-close:** Unavailable device telemetry, credential or data submission, attachment execution, payload write, repeated interaction, or related affected entities.

## Closure record

Record the message or interaction, user actions, control outcomes, endpoint and identity findings, indicator hunt, containment, Sentinel classification, and any remaining uncertainty.
