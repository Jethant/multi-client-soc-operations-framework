# SOC-007 — Insider Risk Data Movement

## Scope

Unusual access, download, upload, sharing, transfer, staging, compression, or deletion of organizational data.

## Required telemetry

- File, repository, sharing, and application audit activity
- Data classification, source, destination, audience, and volume
- Endpoint process, archive, removable-media, and browser activity
- Network, proxy, upload, and cloud-service telemetry
- Role, project, HR, legal, and approved-migration context

## Client baseline checks

Compare repositories, data classifications, normal volume and frequency, destinations, sharing scope, approved projects, and high-risk data locations with the client profile.

## Investigation and correlation

1. Determine the data classification, source, destination, volume, audience, and business purpose.
2. Correlate identity, device, application, file, and network timelines.
3. Compare activity with the user's role, project, historical behavior, and approved workflows.
4. Search for staging, compression, deletion, concealment, external upload, or personal destinations.
5. Review resignation, access-change, off-hours, and related identity/device context when authorized.

## Potential MITRE ATT&CK® mappings

- [T1530 — Data from Cloud Storage](https://attack.mitre.org/techniques/T1530/) when unauthorized collection is confirmed from SaaS or cloud storage.
- [T1560.001 — Archive via Utility](https://attack.mitre.org/techniques/T1560/001/) when collected data is compressed or packaged with an archive utility before movement.
- [T1567.002 — Exfiltration to Cloud Storage](https://attack.mitre.org/techniques/T1567/002/) when data is transferred to an adversary-controlled or unapproved cloud-storage service.

## Decision guidance

**BenignPositive candidate:** Role, approved project, classification, source, destination, audience, volume, device, and timing all agree with current context.

**Escalate or classify TruePositive when:** Sensitive data moves to personal or unsanctioned destinations, volume or timing is abnormal, concealment or deletion is present, or related identity/device anomalies exist.

**Undetermined when:** Data classification, destination, device, business purpose, or required audit evidence is unavailable.

## Containment and follow-up

- Stop unauthorized sharing or transfer using approved procedures.
- Preserve file, endpoint, identity, and network evidence.
- Restrict affected sessions or access when required.
- Coordinate legal, privacy, HR, and client notification through approved channels.

## Tuning

**Keep under analyst review:** Sensitive data, external or personal destinations, unusual volume, staging or compression, concealment, off-hours activity, or identity/device anomalies.

## Closure record

Record the data classification, source, destination, audience, volume, business purpose, correlated timeline, actions taken, Sentinel classification, and any remaining uncertainty.
