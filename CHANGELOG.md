# Changelog

## 1.0.0 — 2026-08-17

- Added a canonical alert taxonomy with stable IDs.
- Reworked baselines, heuristics, correlation, tuning, and workflows around evidence gates.
- Corrected account-lifecycle tuning and incident-reporting queries.
- Added sanitized client-data and external-service handling guidance.
- Reworked outreach and incident closure templates to avoid unsupported claims.
- Renamed and clarified case studies, including reserved example indicators.
- Added automated taxonomy, link, and naming validation.
- Aligned closure outcomes with native Microsoft Sentinel incident classifications.
- Required the latest incident status to be closed in closure reporting queries.
- Removed confidence scoring fields while preserving evidence limitations and remaining uncertainty.
- Consolidated heuristics, correlation workflows, and workflow guides into one playbook per taxonomy category.
- Combined client context and incident-specific baseline sections into one client-wide profile and operational baseline.
- Moved category-specific tuning criteria into playbooks and reduced the central tuning layer to universal governance.
