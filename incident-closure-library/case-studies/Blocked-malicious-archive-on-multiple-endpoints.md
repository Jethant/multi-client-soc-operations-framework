# Blocked malicious archive on multiple endpoints

## Scenario

Several managed workstations downloaded the same shortcut-based archive containing an unsigned executable. Endpoint protection classified the file as potentially malicious and recorded blocked execution activity.

## Observed

- The same archive or file hash appeared on multiple endpoints.
- Endpoint protection produced a malicious or suspicious verdict.
- Available telemetry showed prevention before successful payload execution.
- The scoped timelines showed no persistence, credential access, lateral movement, or suspicious identity activity.

## Not established

- No command-and-control session was demonstrated by the available evidence.
- A separate local administrator change was correlated by the platform but was validated as approved activity.

## Response

- Removed or quarantined the artifact on every identified endpoint.
- Verified endpoint telemetry and scan completion.
- Hunted hashes, filenames, source URLs, and behavior across the environment.
- Reviewed delivery source and affected-user activity.
- Monitored for delayed execution or follow-on behavior.

## Determination

Blocked malicious-file activity affecting multiple endpoints. The scoped evidence did not establish command and control or successful compromise.

**Remaining limitation:** The determination depends on complete endpoint telemetry for every affected device.
