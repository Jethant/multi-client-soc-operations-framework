# Client profile and operational baseline

Maintain one profile and operational baseline per client. It is the authoritative source for both client context and expected behavior; incident-specific baseline copies are not needed. Each playbook identifies which parts of this profile to check.

This public repository contains the template only. Completed profiles with live client identities, ranges, systems, contacts, or case details belong in the approved storage location for that client.

## Profile metadata

- Non-sensitive client reference
- Profile maintainer
- Data sources and records used
- Last reviewed date
- Next review date

Time-sensitive facts should include their source and review date. Stale, missing, or unverified information is unknown and must not support automated closure or tuning.

## 1. Organization and responsibilities

- IT, IAM, endpoint, security, helpdesk, privacy, and project responsibilities
- External administrators, service providers, and consultants
- Separation-of-duty and change-control expectations
- Primary, backup, and after-hours contacts by function

## 2. Identities and privileged access

- Administrative roles, responsible teams, and expected named or service identities
- PIM, MFA, break-glass, and privileged-access workflows
- Administrative devices, jump hosts, network paths, and maintenance windows
- Normal onboarding, offboarding, role-change, and account-recovery processes

## 3. Authentication patterns

- Supported authentication and MFA methods
- Normal failure volume and failure-to-success timing by user population
- Expected service accounts, legacy clients, lockouts, and recovery activity
- Familiar locations and managed-device patterns used only as supporting context

## 4. Network and location

- Corporate, VPN, cloud-egress, office, remote-work, and partner ranges
- Expected travel and remote-access patterns
- Externally exposed and legacy systems
- Owner and expiration for every temporary network or location exception

## 5. Devices and software

- Managed platforms, inventory sources, ownership, and naming conventions
- Enrollment, provisioning, remote-management, support, update, and replacement workflows
- Expected local identities and privileged groups
- Approved software, scripts, administration tools, signers, processes, and network destinations

## 6. Applications and automation

- Important applications, service principals, owners, and current status
- Approved deployment pipelines and credential administrators
- Credential type, lifetime, storage, and rotation standards
- Expected permissions, consent, application roles, and automation identities

## 7. Data and collaboration

- Sensitive data, departments, repositories, and classifications
- Role-appropriate access, sharing audiences, and external destinations
- Typical transfer volume, frequency, and workflow
- Approved migration, backup, legal-discovery, and collaboration activity

## 8. Operational cycles and lifecycle workflows

- Guest, contractor, employee, test-account, and service-account lifecycle processes
- Active migrations, deployments, maintenance, simulations, and project windows
- Seasonal activity and workload changes
- Expected change records, deployment rings, access packages, and expiration practices

## 9. Security controls and telemetry

- Available identity, endpoint, email, network, application, data, and audit telemetry
- Expected protective controls and reporting workflows
- Telemetry retention and known coverage gaps
- Protected controls and high-impact dependencies requiring escalation

## 10. Known exceptions

For each exception, record the behavior, owner, evidence, scope, start date, expiration date, and review date. Do not convert a temporary exception into a permanent assumption.

## 11. Historical lessons and open actions

- Past incidents and configuration problems
- Known detection gaps
- Previous tuning changes and their outcomes
- Open follow-up actions, owners, and due dates

## Profile maintenance

Update the single client profile when the environment changes. Playbooks should point to relevant profile fields without copying client facts into category-specific baseline records.
