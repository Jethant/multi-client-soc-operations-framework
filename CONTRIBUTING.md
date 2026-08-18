# Contributing

Changes should preserve the framework's safety, taxonomy coverage, and sanitized public scope.

## Category changes

When adding or renaming an alert category:

1. Update `taxonomy/alert-types.json`.
2. Create or rename the matching file in `playbooks/`.
3. Update the taxonomy index.
4. Run `python .github/scripts/validate_framework.py`.

## Playbook changes

Keep the required playbook sections: scope, telemetry, baseline checks, investigation, decision, containment, tuning, and closure. Category-specific logic belongs in the playbook, not in a second index.

## Client profile and baseline changes

- Maintain one profile and baseline per client in the client's approved storage location.
- Organize expected behavior by stable environment domain, not alert category.
- Record sources and review dates for time-sensitive facts and exceptions.
- Treat stale or missing profile data as unknown, never as evidence that activity is benign.

## Tuning changes

- Do not suppress or auto-close from one signal.
- State required telemetry and route missing data to review.
- Put category-specific candidates and exclusions in the relevant playbook.
- Keep universal testing, ownership, scope, expiration, rollback, and review requirements in `tuning/README.md`.
- Preserve an auditable closure reason.

## Query changes

- Identify the product, table, permissions, client scope, and UTC time basis.
- Parameterize time ranges and example entities.
- Test in a non-production or approved workspace.
- Record expected output and known schema assumptions.

## Case studies and client data

- Use sanitized values only.
- Separate observed facts, third-party reports, inference, and unknowns.
- Use reserved documentation domains and IP addresses.
- Never commit live client identities, internal ranges, raw messages, credentials, tokens, or case evidence.

## Pull requests

Summarize what changed, why, how it affects analysts, and what you tested. Keep unrelated edits in separate changes.
