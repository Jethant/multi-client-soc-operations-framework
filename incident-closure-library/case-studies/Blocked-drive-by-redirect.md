# Blocked drive-by redirect

## Incident overview

The incident originated from an alert in Sentinel: **Suspicious activity linked to a financially motivated threat actor detected**, after a user attempted to access a suspicious domain during routine browsing. The alert name reflected threat-intelligence associations between supplied indicators and financially motivated threat activity. The site redirected the browser through infrastructure classified as malicious, and Microsoft Defender Network Protection blocked the resulting outbound connection attempts.

Detonation of the referenced URL in Joe Sandbox resolved to an abnormal index page containing a fraudulent sign-in prompt. The service classified the URL as malicious. The investigation focused on determining whether the redirects resulted in credential entry, payload execution, persistence, or related identity activity.

## Investigation findings

- Browser-initiated redirects were consistent with a drive-by compromise attempt.
- Joe Sandbox returned a malicious verdict and displayed a fraudulent sign-in prompt.
- Rapid outbound connection attempts to the redirect infrastructure were blocked by Network Protection.
- No payload execution, persistence, anomalous identity or MFA activity, lateral movement, or related file activity was identified in the scoped telemetry.
- Additional DNS and HTTPS activity to `fonts.gstatic.com` and `encrypted-tbn0.gstatic.com` was consistent with normal Chrome background traffic and was separated from the malicious redirect chain.


## Response and remediation

- Added the malicious redirect destinations as tenant indicators.
- Completed an antivirus scan on the affected endpoint.
- Reviewed the device and browser timelines for successful payload execution or persistence.
- Hunted the destinations and related activity across the environment.
- Reinforced safe-browsing guidance with the affected user.
- Continued monitoring for related activity.

## Final assessment

This was a blocked drive-by compromise attempt involving malicious redirect infrastructure and a fraudulent sign-in page. Existing controls prevented the observed outbound communication, and the scoped investigation found no evidence of payload execution, persistence, lateral movement, or internal identity compromise.
