# Blocked ransomware-linked web activity

## Incident overview

Microsoft Sentinel generated a multi-stage incident after a user's browser attempted to connect to several malicious destinations associated by available threat intelligence with malware or ransomware distribution. Microsoft Defender Network Protection and Exploit Guard browser controls blocked the observed outbound connections.

The user had visited a website that appeared legitimate before the browser was redirected through injected scripts to multiple malicious domains. DNS activity was followed by outbound connection attempts to infrastructure across multiple regions. The investigation focused on whether the redirect activity resulted in exploitation, payload execution, or follow-on compromise.

## Investigation findings

- Defender and VirusTotal classified the destinations as malicious or associated with malware distribution.
- Network Protection and browser controls blocked the observed communication attempts.
- Endpoint antivirus scans completed without identifying a ransomware payload.
- Review of the device timeline and available forensic evidence found no payload execution, persistence, lateral movement, or post-exploitation activity.
- A tenant-wide hunt for the identified destinations found no additional affected users or devices.
- Threat context suggested that the redirect activity could target a Chrome vulnerability, but the available evidence did not establish exploitation of a specific CVE on the endpoint.

## Sanitized indicators

The original domains and IP addresses were replaced with reserved documentation values:

- `hxxps://redirect-a[.]invalid`
- `hxxps://redirect-b[.]invalid`
- `hxxps://redirect-c[.]invalid`
- `192.0.2.57`
- `198.51.100.166`

## Response and remediation

- Updated Google Chrome to the latest supported version.
- Verified that Microsoft Defender Antivirus definitions and Windows security updates were current.
- Confirmed that Network Protection and relevant browser controls remained enabled and enforced.
- Added the identified malicious destinations to tenant indicators.
- Completed a tenant-wide hunt for related destinations and artifacts.
- Continued monitoring of the affected endpoint for follow-on activity.
- Reinforced prompt browser updates and reporting of unusual browser behavior.

## Final assessment

This was a blocked drive-by compromise attempt involving ransomware-linked infrastructure. Sentinel correlated the events because of the destination context, but the scoped evidence did not show ransomware execution or a successful endpoint compromise. Existing controls blocked the observed activity before follow-on behavior was identified.
