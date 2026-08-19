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

Check approved simulations, email, browser and endpoint controls, reporting workflows, telemetry coverage, and known gaps in the client profile.

## Investigation and correlation

1. Establish whether the user opened, clicked, submitted, downloaded, or executed.
2. Correlate email, browser, network, endpoint, identity, token, and MFA evidence.
3. Verify control outcomes independently; a block event alone does not prove containment.
4. Hunt the message, sender, URL, hash, infrastructure, and behavior across users and devices.
5. Determine whether credentials, data, sessions, or endpoints require containment.

## Potential MITRE ATT&CK® mappings

- [T1566.001 — Spearphishing Attachment](https://attack.mitre.org/techniques/T1566/001/) when a malicious attachment is delivered to the user.
- [T1566.002 — Spearphishing Link](https://attack.mitre.org/techniques/T1566/002/) when a malicious link is delivered to the user.
- [T1204.001 — Malicious Link](https://attack.mitre.org/techniques/T1204/001/) when the user opens or follows the malicious link.
- [T1204.002 — Malicious File](https://attack.mitre.org/techniques/T1204/002/) when the user opens or executes a malicious attachment or download.
- [T1078 — Valid Accounts](https://attack.mitre.org/techniques/T1078/) when captured credentials are subsequently used for unauthorized access.

## Decision guidance

**BenignPositive candidate:** The event was an authorized simulation or other expected, non-malicious activity that triggered the detection as designed.

**TruePositive:** The message, link, attachment, or destination was confirmed malicious, even when controls blocked it before compromise. Escalate urgently when credentials or data were submitted, an attachment executed, a payload was written, suspicious sessions followed, or related users or devices interacted with the same infrastructure.

**Undetermined when:** Browser, endpoint, network, identity, or interaction telemetry is unavailable or contradictory.

## Containment and follow-up

- Purge confirmed malicious messages and block approved indicators.
- Revoke sessions, reset credentials, and review MFA methods when exposure is possible.
- Isolate affected devices and quarantine artifacts when execution is possible.
- When interaction is unclear or exposure is possible, contact the affected user using the approved [user-interaction confirmation template](../outreach-templates/email-canned-replies.md#user-interaction-confirmation).

## Tuning

**Keep under analyst review:** Unavailable device telemetry, credential or data submission, attachment execution, payload write, repeated interaction, or related affected entities.

## Closure record

Record the message or interaction, user actions, control outcomes, endpoint and identity findings, indicator hunt, containment, Sentinel classification, and any remaining uncertainty.
