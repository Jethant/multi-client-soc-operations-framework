# SOC-012 — Application Credential Creation

## Scope

Secrets or certificates added to applications or service principals, including related ownership, consent, permissions, and token use.

## Required telemetry

- Application, service-principal, credential, and directory audit records
- Actor sign-in, PIM, MFA, device, token, and session activity
- Application owners, status, permissions, roles, and consent
- Credential type, lifetime, storage, and rotation workflow
- Deployment, change, vendor, or project record

## Baseline inputs

Consult the **SOC-012** section of the [baseline](../baselines/README.md). Confirm authorized actors and owners, approved applications, deployment pipelines, credential standards, and expected permissions.

## Investigation and correlation

1. Validate the actor, application owner, target application, service principal, deployment, and change record.
2. Correlate the actor's sign-in, device, PIM, MFA, token, and audit activity.
3. Review credential type, lifetime, storage, permissions, consent, ownership, and application status.
4. Search for token use, new sign-ins, permission grants, consent, or role changes after credential creation.
5. Determine whether the credential bypassed the approved deployment and rotation workflow.

## Decision guidance

**BenignPositive candidate:** Authorized actor and owner, approved deployment, managed device, change record, credential type and lifetime, storage, and unchanged permission scope all agree.

**Escalate or classify TruePositive when:** A long-lived credential is added to a dormant or privileged application, ownership is missing, permissions or consent expand, or risky actor or token activity is present.

**Undetermined when:** Actor, owner, credential, deployment, permission, consent, or subsequent token-use evidence cannot be verified.

## Containment and follow-up

- Remove or rotate unauthorized credentials.
- Revoke affected tokens and restrict the application or service principal.
- Review and remove unexpected consent, permissions, roles, and owners.
- Hunt subsequent token use, sign-ins, and resource access.

## Tuning restrictions

Do not tune during investigation or containment. After classification, use the **SOC-012** section of the [tuning guidance](../tuning/mapped-tuning-guidelines.md) as the authoritative automation gate.

## Closure record

Record the actor, application and owner, credential type and lifetime, deployment and change evidence, permissions and consent, token use, containment, Sentinel classification, and any remaining uncertainty.
