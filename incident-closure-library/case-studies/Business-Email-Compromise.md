# External-vendor business email compromise

## Incident overview

An external vendor's mailbox was compromised and used to impersonate the vendor in financial communications. The attacker sent fraudulent banking-change and payment instructions to an internal employee, and two ACH payments were processed before the activity was questioned and independently verified.

The incident was escalated after the employee contacted the vendor through a separate trusted channel. Investigation established that the malicious communications originated from the vendor's legitimate mailbox. The internal investigation focused on determining whether any internal identities, mailboxes, endpoints, or payment workflows had also been compromised.

## Internal findings

- The fraudulent requests came from the vendor's legitimate email account.
- The tone, urgency, and requested banking changes differed from the established vendor process.
- Review of the available internal identity, mailbox, and endpoint telemetry found no evidence of unauthorized access to internal accounts.
- No related lateral movement or malicious activity originating from managed internal systems was identified during the scoped investigation window.
- The financial impact consisted of two ACH payments made before the request was challenged.

## Findings reported by the vendor's security team

- Unauthorized access to the vendor mailbox
- Mailbox rules intended to conceal inbound and outbound communications
- Attacker-controlled forwarding and filtering behavior
- Fraudulent payment instructions sent from the compromised account

These mailbox-level findings came from the vendor's investigation rather than direct access to the vendor's environment.

## Indicators and investigative context

- Fraudulent ACH and banking-change requests
- Communication tone and urgency inconsistent with normal vendor behavior
- External infrastructure associated with credential theft and BEC activity
- Hidden mailbox rules and forwarding behavior reported by the vendor's security team

## Response and remediation

- Verified the request with the vendor through a separate trusted contact.
- Audited internal mailboxes and identities for related unauthorized access.
- Strengthened independent verification requirements for payment requests and banking-detail changes.
- Provided targeted guidance on recognizing fraudulent financial communications.
- Documented the incident for legal, compliance, and financial-recovery processes.
- Continued monitoring for related infrastructure and impersonation attempts.

## Final assessment

This was a confirmed compromise of an external vendor mailbox that resulted in fraudulent payment instructions and financial loss. The scoped internal review found no evidence that internal identities, mailboxes, or systems were compromised. Vendor-mailbox containment remained dependent on actions and reporting from the vendor's security team.
