# External-vendor business email compromise

## Scenario

An external vendor's mailbox was used to send fraudulent payment-change instructions to an internal employee. Two payments were processed before the request was independently verified and escalated.

## Observed internally

- Fraudulent instructions arrived from the vendor's legitimate mailbox.
- Communication style and urgency differed from the established process.
- No evidence available to the internal investigation showed access to internal mailboxes or identities.
- Internal review did not identify lateral movement or malicious activity originating from managed internal systems during the scoped window.

## Reported by the vendor's security team

- Unauthorized access to the vendor mailbox
- Mailbox rules and forwarding behavior intended to conceal communications
- Fraudulent payment instructions sent by the unauthorized actor

These statements were third-party findings and should be referenced to the vendor's protected report in an operational case.

## Response

- Verified the request through a separate trusted vendor contact.
- Audited internal identities, mailboxes, and relevant endpoints.
- Preserved messages, headers, payment records, and communication timelines.
- Coordinated bank recall or recovery, legal, insurance, and law-enforcement actions as required.
- Strengthened independent verification for payment and banking-detail changes.
- Monitored for related infrastructure and impersonation attempts.

## Determination

Confirmed compromise of an external vendor mailbox with financial impact. The scoped internal review found no evidence of internal identity or system compromise, but that finding does not resolve the vendor's containment or financial-recovery status.

**Confidence:** High for the fraudulent messages and financial impact; dependent on third-party reporting for vendor-mailbox details.
