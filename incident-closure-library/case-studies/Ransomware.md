# Blocked ransomware-linked web activity

## Scenario

A user's browser was redirected to infrastructure associated by available threat intelligence with malware or ransomware distribution. Network controls blocked the observed outbound attempts.

## Observed

- DNS and outbound connection attempts to suspicious destinations
- Network Protection and browser-control block events
- Successful endpoint scan completion
- No payload execution, persistence, lateral movement, or post-exploitation activity in the scoped telemetry
- No additional affected users or devices found during an indicator hunt

## Sanitized example indicators

The original indicators were replaced with reserved documentation values:

- `hxxps://redirect-a[.]invalid`
- `hxxps://redirect-b[.]invalid`
- `192.0.2.57`
- `198.51.100.166`

Do not use these example values as production indicators.

## Inference and limits

Threat-intelligence context linked the infrastructure to ransomware distribution. The available evidence supported a blocked delivery attempt, not successful exploitation or ransomware execution. No browser CVE attribution was made without version and exploit evidence.

## Response

- Updated the browser, endpoint protection, and operating system.
- Verified Network Protection and relevant browser controls remained enforced.
- Added approved indicators with owners and review dates.
- Hunted the environment for related destinations and artifacts.
- Continued targeted monitoring of the affected endpoint.

## Determination

Blocked web activity involving ransomware-linked infrastructure. No successful compromise was identified within the available evidence and investigation window.

**Confidence:** Medium to high, dependent on endpoint and network telemetry completeness.
