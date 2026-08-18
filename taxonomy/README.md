# Alert taxonomy

The taxonomy supplies stable identifiers for every alert category supported by the framework. The machine-readable source is [alert-types.json](alert-types.json).

| ID | Category | Scope |
| --- | --- | --- |
| SOC-001 | Privileged Operations | Administrative actions, role changes, and privileged access activity |
| SOC-002 | Authentication Failures | Failed sign-ins, failure-to-success sequences, spraying, and MFA-related failures |
| SOC-003 | Conditional Access Changes | Creation, modification, deletion, or bypass of access policies |
| SOC-004 | Guest and External User Lifecycle | Guest invitations, access changes, and offboarding |
| SOC-005 | Local Group Membership Changes | Additions to privileged local groups on endpoints or servers |
| SOC-006 | Authentication Method Changes | MFA registration, replacement, removal, and recovery changes |
| SOC-007 | Insider Risk Data Movement | Unusual access, download, upload, sharing, or transfer of organizational data |
| SOC-008 | Account Creation and Deletion | User, service, test, and automation identity lifecycle activity |
| SOC-009 | Device-Linked Identity Events | Identity activity that requires endpoint or provisioning context |
| SOC-010 | User-Initiated Threat Activity | Phishing, malicious-link, and risky user-interaction events |
| SOC-011 | Device Threat Activity | Malware, persistence, credential theft, suspicious processes, and network activity |
| SOC-012 | Application Credential Creation | Secrets or certificates added to applications or service principals |

## Change rule

Adding or renaming a category requires the same `ID — Category` heading in:

- `baselines/README.md`
- `heuristics/Heuristics-full-framework.md`
- `correlation-workflows/correlation-workflows-list.md`
- `tuning/mapped-tuning-guidelines.md`
- `workflow-guides/mapped-workflow-guides.md`

The repository validator enforces this coverage.
