# Benign project archive flagged on multiple endpoints

## Incident overview

A correlation incident combined a local administrator group modification with activity described by the platform as a potential build-process compromise. Review showed that the administrator-group change was authorized and consistent with expected operational activity.

A separate part of the correlation involved several managed workstations downloading the same shortcut-based archive. The archive contained an unsigned executable that Microsoft Defender classified as a potential trojan. Defender recorded blocked execution activity on each identified device.

## Investigation findings

- The local administrator account addition was expected and unrelated to malicious activity.
- The same `.lnk` archive and unsigned executable appeared on multiple endpoints.
- Defender produced a potential-trojan verdict for the executable.
- Available device telemetry showed that execution was prevented.
- No payload execution, persistence, anomalous identity activity, lateral movement, or build-process compromise was identified in the scoped telemetry.
- The client point of contact identified the archive as a benign file associated with a work-related project.
- The client context and available telemetry did not support command-and-control activity or a malicious attack chain.

## Correlation assessment

The platform correlation brought together events that required investigation but did not establish a single attack chain. The approved administrator change was unrelated to the file activity, and the Defender verdict was resolved through client validation of the file's business purpose.

## Response and follow-up

- Reviewed the affected device timelines and the file activity across the identified endpoints.
- Sent an email to the client point of contact recommending removal of the archive and executable pending validation.
- The point of contact replied that the file was a benign work-related project file and that the detection was a false positive.
- No removal or quarantine action was performed by the analyst.
- Documented the client-provided business context and the unrelated authorized administrator change in the closure record.

## Final assessment

The incident was closed as `FalsePositive` based on the client's confirmation that the archive and executable belonged to a legitimate work-related project. The scoped investigation found no evidence of successful compromise, persistence, lateral movement, command and control, or build-process compromise. The removal recommendation was not recorded as a completed action.

## Lessons learned

- Record recommended actions separately from actions confirmed as completed.
- Validate unfamiliar unsigned files with the client point of contact before treating the file verdict as a confirmed malicious finding.
- Treat correlated events as separate leads until the evidence establishes that they belong to the same attack chain.
