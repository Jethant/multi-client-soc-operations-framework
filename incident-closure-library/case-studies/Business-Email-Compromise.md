# Incident Overview
A Business Email Compromise (BEC) incident was identified after an external vendor’s mailbox was compromised and used to impersonate the vendor in financial communications. The attacker leveraged access to the vendor’s email account to send fraudulent payment instructions to an internal user. Two ACH payments were processed before the activity was questioned and escalated.
The incident was triggered by unusual communication patterns and suspicious banking‑change requests. Investigation confirmed that the attacker operated exclusively through the compromised vendor mailbox, and no internal identities, mailboxes, or systems were compromised.

# Summary of Findings
Analysis determined that an external vendor’s mailbox had been compromised by an unauthorized actor. The attacker used the mailbox to impersonate the vendor and initiate fraudulent ACH banking changes and payment requests.
A third‑party security team supporting the vendor conducted the mailbox‑level investigation and confirmed:
	• unauthorized access to the vendor mailbox
	• malicious mailbox rules designed to hide inbound and outbound communications
	• attacker‑controlled forwarding and filtering behavior
	• fraudulent payment instructions originating from the compromised account
Internal investigation focused on validating that:
	• no internal mailboxes were accessed
	• no internal identities were compromised
	• no lateral movement occurred
	• no malicious activity originated from internal systems
	• the fraudulent communications were isolated to the compromised vendor mailbox
The incident was escalated when an internal employee questioned a suspicious banking‑change request, prompting verification with the real vendor and discovery of the compromise.

# Indicators & Malicious Activity
	• Fraudulent ACH change requests sent from the compromised vendor mailbox
	• Communication tone and urgency inconsistent with normal vendor behavior
	• External IPs associated with credential‑theft and BEC infrastructure
	• Hidden mailbox rules confirmed by the vendor’s security team
  
# Next Steps & Remediation
	• Confirm removal of malicious mailbox rules (performed by vendor’s security team)
	• Block attacker IPs and domains in the tenant
	• Audit internal mailboxes for unauthorized access
	• Strengthen financial verification workflows for payment requests
	• Provide user education on identifying fraudulent communications
	• Document the incident for legal, compliance, and financial recovery processes
	• Continue monitoring for related suspicious activity across the tenant
  
# Final Assessment
This incident represents a successful Business Email Compromise of an external vendor mailbox, resulting in unauthorized financial transactions. Internal systems and identities remained uncompromised, and the attacker operated solely through the vendor’s mailbox. The incident was contained through coordination with the vendor’s security team, internal mailbox validation, indicator blocking, workflow hardening, and user notification. No further malicious activity was identified during tenant‑wide review.
