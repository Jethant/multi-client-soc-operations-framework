# Incident Overview
A malicious website block alert was generated after a user attempted to access a suspicious domain associated with potential drive‑by compromise activity. Microsoft Defender Network Protection successfully blocked all outbound connections to the malicious site, preventing any payload delivery. The activity originated from a managed workstation during routine browsing.
Detonation of the referenced URL (Deivhu) in Joe Sandbox resolved to an abnormal index page containing a fraudulent sign‑in prompt, and the service classified the URL as malicious. No internal identities, mailboxes, or systems were compromised.

# Summary of Findings
Analysis confirmed that the user attempted to access a malicious website that triggered browser‑initiated redirects consistent with drive‑by compromise behavior. Investigation identified:
	
  • A malicious URL verdict from Joe Sandbox
	• Redirect behavior consistent with exploit delivery
	• Rapid outbound connection attempts blocked by Network Protection
	• No evidence of payload execution or persistence
	• No anomalous identity or MFA activity
	• No lateral movement or file‑based activity on the device

Additional DNS and HTTPS traffic observed during the same window (e.g., fonts.gstatic.com, encrypted‑tbn0.gstatic.com) was validated as normal Chrome background activity and unrelated to the malicious redirect chain.

# Indicators & Malicious Activity
	• Malicious URL (Deivhu) classified by Joe Sandbox
	• Fraudulent redirect chain observed during detonation
	• Blocked outbound connections to malicious infrastructure
	• Abnormal index page and sign‑in prompt
	• Browser‑initiated redirects consistent with drive‑by compromise attempts
  
# Next Steps & Remediation
	• Add malicious redirect URLs as custom indicators in the tenant
	• Complete antivirus scan on the affected device
	• Validate no payload execution or persistence
	• Reinforce safe browsing guidance with the user
	• Continue monitoring for related activity across the tenant
  
# Final Assessment
This incident represents a blocked drive‑by compromise attempt involving malicious redirect infrastructure. Defender controls prevented communication with the threat infrastructure, and no evidence of compromise, persistence, or lateral movement was identified. The incident is fully contained, and malicious URLs have been added as indicators to prevent future access.
