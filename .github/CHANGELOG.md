# Changelog

## Unreleased

- Renamed the project to Multi-Client SOC Operations Framework to reflect its broader investigation, response, and improvement scope.
- Clarified that the operational alert taxonomy routes investigations and complements MITRE ATT&CK®.
- Added evidence-conditional ATT&CK mapping guidance to every category playbook.
- Extended repository validation to require mapping guidance and catch ATT&CK link ID mismatches.
- Limited tuning review to recurring patterns accepted by the team instead of making it part of every closure.
- Clarified classification for blocked malicious activity and for matters reported outside Microsoft Sentinel.
- Distinguished historical external threat indicators from protected client-specific data.

## 1.0.0 — 2026-08-17

- Added a stable taxonomy and 12 category playbooks covering investigation, response, tuning limits, and closure.
- Added one client profile and baseline template, plus a shared tuning policy.
- Added investigation and reporting queries with client-scoping and closed-incident safeguards.
- Added a closure template using native Microsoft Sentinel classifications and sanitized case studies.
- Added outreach templates, a threat-hunting workflow, and external-service handling guidance.
- Added automated checks for taxonomy coverage, playbook structure, links, and naming.
