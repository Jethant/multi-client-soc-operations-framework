# Baselines

Baselines describe expected behavior; they are context, not proof that an event is benign. A familiar identity, address, device, or process can still be compromised.

## Baseline record template

Every operational baseline should record:

- Client reference: non-sensitive internal identifier
- Owner and approver
- Data sources used to establish the baseline
- Expected actors, devices, locations, processes, and time windows
- Change or project reference, when applicable
- Known exceptions and their expiration dates
- Last validated date and next review date
- Confidence: low, medium, or high

Expired or unowned baselines must not support automated closure.

## SOC-001 — Privileged Operations

- Expected administrative roles and named teams
- Managed administrative workstations or jump hosts
- Approved network paths and maintenance windows
- Common tasks and associated change records
- Normal use of PIM, MFA, and break-glass accounts

## SOC-002 — Authentication Failures

- Normal failure-to-success timing by user population
- Managed device and familiar-location patterns
- Expected legacy clients, service accounts, and lockout behavior
- Normal failure volume per user and across users

## SOC-003 — Conditional Access Changes

- Authorized policy administrators
- Approved policy naming and change workflow
- Maintenance windows and deployment rings
- Protected controls that require separate approval

## SOC-004 — Guest and External User Lifecycle

- Authorized inviters and sponsors
- Approved domains, projects, groups, and access duration
- Review and expiration cadence
- Expected partner locations only when documented and current

## SOC-005 — Local Group Membership Changes

- Approved endpoint-management actors and tools
- Device provisioning and support workflows
- Expected privileged local groups
- Normal change volume and deployment windows

## SOC-006 — Authentication Method Changes

- Approved self-service and helpdesk recovery workflows
- Supported MFA methods
- Expected device-replacement and onboarding patterns
- High-risk methods or recovery paths requiring escalation

## SOC-007 — Insider Risk Data Movement

- Role-appropriate repositories and data classifications
- Typical volume, frequency, destination, and sharing scope
- Approved migration, backup, and legal-discovery workflows
- High-risk repositories and external destinations

## SOC-008 — Account Creation and Deletion

- Authorized identity-lifecycle systems and administrators
- HR, contractor, test, and service-account workflows
- Expected initial groups, licenses, and roles
- Start, end, and expiration timing

## SOC-009 — Device-Linked Identity Events

- Managed device inventory and naming conventions
- Approved provisioning tools and enrollment workflows
- Expected local identities and management processes
- Normal update and maintenance windows

## SOC-010 — User-Initiated Threat Activity

- Expected protective controls and reporting workflow
- Normal browser, email, and device posture
- Approved simulations and awareness-testing identifiers
- Required evidence for clicks, credential submission, or execution

## SOC-011 — Device Threat Activity

- Approved software, scripts, administration tools, and signers
- Normal parent-child process relationships
- Expected network destinations and update behavior
- Known testing tools with owners and expiration dates

## SOC-012 — Application Credential Creation

- Authorized application owners and credential administrators
- Approved applications, service principals, and deployment pipelines
- Credential type, lifetime, and rotation standards
- Change, vendor, or project references
- Expected permission grants and consent workflow
