# Alert taxonomy

The taxonomy supplies stable identifiers for every alert category supported by the framework. The machine-readable source is [alert-types.json](alert-types.json).

| ID | Category | Scope | Playbook |
| --- | --- | --- | --- |
| SOC-001 | Privileged Operations | Administrative actions, role changes, and privileged access activity | [Open](../playbooks/SOC-001-privileged-operations.md) |
| SOC-002 | Authentication Failures | Failed sign-ins, failure-to-success sequences, spraying, and MFA-related failures | [Open](../playbooks/SOC-002-authentication-failures.md) |
| SOC-003 | Conditional Access Changes | Creation, modification, deletion, or bypass of access policies | [Open](../playbooks/SOC-003-conditional-access-changes.md) |
| SOC-004 | Guest and External User Lifecycle | Guest invitations, access changes, and offboarding | [Open](../playbooks/SOC-004-guest-and-external-user-lifecycle.md) |
| SOC-005 | Local Group Membership Changes | Additions to privileged local groups on endpoints or servers | [Open](../playbooks/SOC-005-local-group-membership-changes.md) |
| SOC-006 | Authentication Method Changes | MFA registration, replacement, removal, and recovery changes | [Open](../playbooks/SOC-006-authentication-method-changes.md) |
| SOC-007 | Insider Risk Data Movement | Unusual access, download, upload, sharing, or transfer of organizational data | [Open](../playbooks/SOC-007-insider-risk-data-movement.md) |
| SOC-008 | Account Creation and Deletion | User, service, test, and automation identity lifecycle activity | [Open](../playbooks/SOC-008-account-creation-and-deletion.md) |
| SOC-009 | Device-Linked Identity Events | Identity activity that requires endpoint or provisioning context | [Open](../playbooks/SOC-009-device-linked-identity-events.md) |
| SOC-010 | User-Initiated Threat Activity | Phishing, malicious-link, and risky user-interaction events | [Open](../playbooks/SOC-010-user-initiated-threat-activity.md) |
| SOC-011 | Device Threat Activity | Malware, persistence, credential theft, suspicious processes, and network activity | [Open](../playbooks/SOC-011-device-threat-activity.md) |
| SOC-012 | Application Credential Creation | Secrets or certificates added to applications or service principals | [Open](../playbooks/SOC-012-application-credential-creation.md) |

## Change rule

Adding or renaming a category requires:

- an entry and playbook path in `taxonomy/alert-types.json`
- a corresponding file in `playbooks/`
- the matching row in this index

Category-specific baseline checks and tuning criteria belong in that category's playbook. The repository validator enforces this coverage.
