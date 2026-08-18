# SOC-011 — Device Threat Activity

## Scope

Malware, suspicious processes, persistence, credential theft, defense evasion, remote execution, network activity, and lateral movement on devices.

## Required telemetry

- Endpoint alerts, file, signer, hash, path, and reputation data
- Process tree, command line, user, and execution context
- Persistence, credential-access, and defense-evasion evidence
- Device network, remote-session, and lateral-movement activity
- Software ownership, approval, testing, and expiration context

## Client baseline checks

Compare software, scripts, administrative tools, signers, paths, process relationships, owners, network destinations, update behavior, and testing exceptions with the client profile.

## Investigation and correlation

1. Review the file, signer, hash, path, parent process, command line, user, and software owner.
2. Correlate persistence, credential access, defense evasion, network, remote execution, and lateral-movement telemetry.
3. Search the same artifacts and behavior across endpoints.
4. Compare activity with approved software and testing context, including owner and expiration.
5. Determine whether a nominally approved binary was used abnormally.

## Potential MITRE ATT&CK® mappings

This category spans many endpoint behaviors and has no fixed category-level mapping. Assign the most specific technique supported by the process, persistence, credential-access, network, remote-execution, or lateral-movement evidence.

## Decision guidance

**BenignPositive candidate:** Software owner, signer, hash, path, parent process, command line, and network behavior all match an approved use, with no malicious capability or follow-on activity.

**Escalate or classify TruePositive when:** Credential theft, persistence, evasion, remote execution, lateral movement, abnormal approved-tool use, or repeated low-severity behavior across devices is present.

**Undetermined when:** Endpoint, process-tree, network, signer, or follow-on activity is unavailable.

## Containment and follow-up

- Isolate affected endpoints and stop malicious execution.
- Quarantine artifacts and preserve forensic evidence.
- Revoke exposed credentials and sessions when required.
- Hunt files, hashes, processes, commands, destinations, and behavior across devices.

## Tuning

**Keep under analyst review:** Credential theft, persistence, defense evasion, remote execution, lateral movement, abnormal use of an approved binary, or repeated low-severity detections across devices.

## Closure record

Record the file and process evidence, user and device context, malicious behaviors checked, network findings, environment-wide hunt, containment, Sentinel classification, and any remaining uncertainty.
