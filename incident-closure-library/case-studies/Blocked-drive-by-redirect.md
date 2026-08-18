# Blocked drive-by redirect

## Scenario

A managed workstation attempted to reach a suspicious website that redirected the browser through infrastructure classified as malicious by available security controls and an approved analysis service.

## Observed

- Browser-initiated redirects and rapid outbound connection attempts
- Network Protection block events for suspicious destinations
- No payload execution, persistence, lateral movement, or anomalous identity activity in the scoped telemetry
- Normal browser background traffic separated from the redirect chain

## Inference and limits

The behavior was consistent with a drive-by compromise attempt. The evidence did not establish the identity or financial motivation of a threat actor, so no actor attribution was assigned.

## Response

- Added approved indicators with an owner and review date.
- Completed endpoint scans and reviewed browser and device timelines.
- Hunted destinations and related artifacts across the environment.
- Provided targeted safe-browsing guidance to the user.

## Determination

Blocked access to malicious redirect infrastructure with no successful compromise identified in the available telemetry.

**Confidence:** Medium; closure depends on complete endpoint and network telemetry.
