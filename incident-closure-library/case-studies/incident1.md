Incident Overview
A multi‑stage ransomware‑linked incident was generated after a user attempted to access several known malicious websites associated with established threat activity groups. Microsoft Defender and VirusTotal confirmed the domains as malicious and tied to ransomware distribution infrastructure. All outbound connections were blocked by Microsoft Defender Network Protection and Exploit Guard browser controls, preventing communication with the malicious infrastructure.
No ransomware payloads executed on the endpoint, and no evidence of compromise, persistence, lateral movement, or post‑exploitation activity was identified. Sentinel correlated the blocked events into a multi‑stage incident due to the nature of the domains involved, but investigation confirmed the activity was fully contained.
Summary of Findings
Investigation determined the user was the target of a drive‑by compromise attempt leveraging a known Google Chrome vulnerability capable of enabling remote code execution. The user accessed a website that appeared legitimate, which redirected through injected scripts to multiple malicious domains.
The endpoint generated DNS traffic followed by outbound connection attempts to several confirmed malicious IP addresses and domains geolocated across multiple regions. All communication attempts were successfully blocked by Microsoft Defender Network Protection and Exploit Guard.
The malicious domains were added to Microsoft Defender tenant indicators to prevent future inbound or outbound communication. Microsoft Defender Antivirus scans completed successfully with no evidence of malware. A tenant‑wide threat hunt for the identified indicators of compromise found no additional affected devices or users.
A comprehensive review of the device timeline and collected forensic evidence found no signs of successful exploitation, no persistence, no lateral movement, and no post‑exploitation activity.
Indicators of Malicious Infrastructure (Sanitized)
	• Hxxps://solar‑mems.cxm
	• Hxxps://goodpersonofourcentury.cxm — confirmed malicious (VirusTotal)
	• IP: 213.109.203.57 — geolocated to NL
	• Hxxps://besthappyfamily.cxm — confirmed malicious (VirusTotal)
	• IP: 149.56.95.166 — geolocated to Estonia
	• Hxxps://waysmakeyourlifebetter.cxm — confirmed malicious (VirusTotal)
	
Next Steps & Remediation
	• Update Google Chrome to the latest supported version to remediate the exploited vulnerability.
	• Verify Microsoft Defender Antivirus definitions and Windows security updates are current.
	• Confirm Microsoft Defender Network Protection and Exploit Guard remain enabled and enforcing policy.
	• Maintain tenant‑wide blocks for the identified malicious domains and IP addresses.
	• Continue monitoring the affected endpoint for any additional suspicious activity.
	• Remind users to promptly install browser updates and report unusual browser behavior.
Final Assessment
This incident represents a blocked drive‑by compromise attempt involving ransomware‑linked infrastructure. All malicious activity was contained by existing security controls, and no compromise occurred. The investigation demonstrates effective detection, correlation, threat hunting, and remediation practices.

