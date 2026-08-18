# Client context template

Use this template to record approved context that helps analysts distinguish expected activity from anomalies.

This public repository must contain sanitized examples only. Completed profiles with live client details belong in the access-controlled system used for that client, even when one person maintains this repository.

## Profile metadata

- Non-sensitive client reference:
- Profile owner:
- Approved by:
- Data sources:
- Last validated:
- Next review:
- Overall confidence: low / medium / high

Stale, unowned, or unverified context must not support automated closure.

## 1. Organization and responsibility

- IT, IAM, endpoint, security, helpdesk, and project responsibilities
- External administrators, MSPs, and consultants
- Separation-of-duty or approval requirements

## 2. Privileged actors

- Approved roles and responsible teams
- PIM and break-glass workflow
- Administrative devices and access paths
- Expected maintenance windows

## 3. Network and location context

- Approved corporate, VPN, cloud-egress, and partner ranges
- Office and remote-work locations
- Expected travel patterns
- Owner and expiration for every exception

## 4. Device and provisioning context

- Managed device platforms and naming conventions
- Enrollment, provisioning, and remote-management tools
- Local administrator and support workflows
- Update and replacement windows

## 5. Identity and access workflows

- Onboarding, offboarding, and account recovery
- MFA registration and replacement
- Guest and consultant lifecycle
- Role, application, and Conditional Access changes

## 6. Projects and operational cycles

- Active migrations and deployments
- Consultant engagement periods
- Seasonal activity and workload changes
- Planned maintenance and policy updates

## 7. Known exceptions

For every exception record the behavior, owner, evidence, scope, start date, expiration date, and review date. Avoid permanent exceptions.

## 8. High-risk areas

- Sensitive data and departments
- High-privilege applications and identities
- Externally exposed or legacy systems
- High-impact control dependencies

## 9. Communication and escalation

- Primary and backup contacts by function
- After-hours path
- Severity and notification expectations
- Legal, privacy, financial, or executive escalation triggers

## 10. Historical lessons

- Past incidents and misconfigurations
- Baseline and tuning changes
- Known detection gaps
- Open follow-up actions and owners
