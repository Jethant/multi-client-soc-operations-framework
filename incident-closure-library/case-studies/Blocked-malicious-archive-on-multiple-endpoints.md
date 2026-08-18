# Blocked malicious archive on multiple endpoints

## Incident overview

A correlation incident combined a local administrator group modification with activity described by the platform as a potential build-process compromise. Review showed that the administrator-group change was authorized and consistent with expected operational activity.

A separate part of the correlation involved several managed workstations downloading the same shortcut-based archive. The archive contained an unsigned executable that Microsoft Defender classified as a potential trojan. Defender recorded blocked execution activity on each identified device.

## Investigation findings

- The local administrator account addition was expected and unrelated to malicious activity.
- The same `.lnk` archive and unsigned executable appeared on multiple endpoints.
- Defender produced a malicious or suspicious verdict for the executable.
- Available device telemetry showed that execution was prevented.
- No payload execution, persistence, anomalous identity activity, lateral movement, or build-process compromise was identified in the scoped telemetry.
- The downloads were associated with routine user activity rather than an established command-and-control channel.

## Correlation assessment

The platform correlation brought together events that required investigation but did not establish a single attack chain. In particular, the approved administrator change did not validate the build-process-compromise portion of the alert, and the malicious archive did not by itself establish command and control.

## Response and remediation

- Removed or quarantined the archive and executable on every identified endpoint.
- Verified that endpoint protection had prevented execution.
- Reviewed device timelines for payload execution, persistence, and follow-on activity.
- Hunted the file hash and related artifacts across the environment.
- Continued monitoring for delayed execution or related activity.
- Reinforced safe file-handling and download practices with the affected users.
- Retained the build-process correlation logic for continued review rather than treating the unrelated administrator change as malicious.

## Final assessment

This was blocked malicious-file activity involving an unsigned executable delivered through a shortcut-based archive to multiple endpoints. Defender prevented execution, and the scoped investigation found no evidence of successful compromise, persistence, lateral movement, command and control, or build-process compromise.
