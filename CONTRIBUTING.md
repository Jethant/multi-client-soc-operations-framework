# Contributing

Changes should preserve the framework's safety, taxonomy coverage, and sanitized public scope.

## Category changes

When adding or renaming an alert category:

1. Update `taxonomy/alert-types.json`.
2. Create or rename the matching file in `playbooks/`.
3. Add the exact `## ID — Category` heading to the baseline and tuning files.
4. Update the taxonomy index.
5. Run `python scripts/validate_framework.py`.

## Playbook changes

Every category playbook must retain its scope, required telemetry, baseline inputs, investigation and correlation steps, decision guidance, containment and follow-up, tuning restrictions, and closure record. Keep category-specific investigation logic in the playbook instead of duplicating it in a second workflow file.

## Tuning changes

- Do not suppress or auto-close from one signal.
- State required telemetry and route missing data to review.
- Require an owner, approval, scope, expiration, rollback condition, and historical validation.
- Preserve an auditable closure reason.

## Query changes

- Identify the product, table, permissions, client scope, and UTC time basis.
- Parameterize time ranges and example entities.
- Test in a non-production or approved workspace.
- Record expected output and known schema assumptions.

## Case studies and client context

- Use sanitized values only.
- Separate observed facts, third-party reports, inference, and unknowns.
- Use reserved documentation domains and IP addresses.
- Never commit live client identities, internal ranges, raw messages, credentials, tokens, or case evidence.

## Pull requests

Summarize what changed, why it changed, operational impact, and validation performed. Keep unrelated edits in separate changes.
