## Privileged Operations
Heuristics:

   1. Expected admin performing the action
   2. Expected IP range
   3. Expected device
   4. Expected workflow (CA edit, auth method cleanup, role assignment)
   5. No parallel anomalous sign‑ins
   6. No unexpected privilege escalation
   7. No new admin roles added without justification

Default Closing Note:
The activity was reviewed and determined to be benign. An authorized administrator performed expected privileged operations consistent with routine identity or access management workflows. No indicators of unauthorized modification, privilege escalation, or anomalous identity behavior were identified.
## Authentication Failures
Heuristics:

   1. Same IP → success shortly after
   2. Same device fingerprint
   3. Same location pattern
   4. No repeated failures across multiple methods
   5. No unfamiliar sign‑in properties
   6. No parallel suspicious activity (password spray, MFA fatigue)

Default Closing Note:
The activity was reviewed and determined to be benign. Authentication failures originated from an expected device, IP range, and user behavior pattern, followed by successful sign‑in. No evidence of password spraying, MFA fatigue, or unfamiliar sign‑in properties was observed.
## Conditional Access Changes
Heuristics:

   1. Expected admin actor
   2. Expected IP range
   3. Expected timing (during maintenance windows)
   4. Change aligns with known project or policy update
   5. No unexpected broadening of access
   6. No removal of critical controls (MFA, location restrictions)

Default Closing Note:
The activity was reviewed and determined to be benign. Conditional Access modifications were performed by an authorized administrator as part of expected policy maintenance. No indicators of unauthorized policy broadening, control removal, or anomalous identity behavior were identified.
## Guest / External User Lifecycle
Heuristics:

   1. Expected admin actor
   2. Expected IP range
   3. Expected onboarding/offboarding workflow
   4. Short‑lived accounts match consultant lifecycle
   5. No unexpected group assignments
   6. No privileged roles granted

Default Closing Note:
The activity was reviewed and determined to be benign. Guest account creation, group membership changes, or deletion actions were performed by an authorized administrator and align with expected consultant or external‑user lifecycle workflows. No unauthorized access, privilege escalation, or anomalous identity behavior was identified.
## Local Group Membership Changes
Heuristics:

   1. Expected provisioning workflow
   2. Expected workstation
   3. Expected actor (helpdesk, endpoint team)
   4. No mass additions across multiple devices
   5. No unexpected privileged accounts added
   6. No correlation with suspicious device activity

Default Closing Note:
The activity was reviewed and determined to be benign. Local group membership changes on the workstation were performed by an authorized actor as part of routine provisioning or access adjustments. No indicators of unauthorized privilege escalation, lateral movement, or anomalous device behavior were identified.
## Authentication Method Changes
Heuristics:

   1. Expected admin actor
   2. Expected IP range
   3. Audit logs show activity was initiated by an authorized admin
   4. No unexpected MFA method added (e.g., phone number not belonging to user)
   5. No parallel unfamiliar sign‑ins
   6. No signs of account compromise

Default Closing Note:
The activity was reviewed and determined to be benign. Authentication method updates were performed by an authorized administrator or the user as part of expected MFA maintenance. No evidence of account compromise, unfamiliar sign‑ins, or unauthorized method registration was observed.
## Insider Risk Data Movement
Heuristics:

   1. Expected workflow (file saves, uploads, downloads)
   2. Expected SharePoint/OneDrive location
   3. Expected file types
   4. No mass exfiltration
   5. No external sharing
   6. No access to sensitive folders outside role

Default Closing Note:
The activity was reviewed and determined to be benign. File access, movement, or storage actions align with the user’s normal job responsibilities and expected workflow. No indicators of data exfiltration, unauthorized sharing, or anomalous insider‑risk behavior were identified.
## Account Creation / Deletion
Heuristics:

   1. Expected admin actor
   2. Expected IP range
   3. Expected lifecycle (consultant, automation, testing)
   4. No privileged roles assigned
   5. No unexpected group membership
   6. No correlation with suspicious sign‑ins

Default Closing Note:
The activity was reviewed and determined to be benign. Account creation and/or deletion actions were performed by an authorized administrator and align with expected onboarding, offboarding, or consultant lifecycle workflows. No unauthorized access, privilege escalation, or anomalous identity behavior was identified.
## Device‑Linked Identity Events
Heuristics:

   1. Expected workstation
   2. Expected provisioning workflow
   3. Expected actor
   4. No suspicious processes
   5. No abnormal device timeline
   6. No correlation with identity anomalies

Default Closing Note:
The activity was reviewed and determined to be benign. Identity‑related events originating from the device align with expected provisioning, administrative maintenance, or user workflow. No suspicious processes, abnormal device timeline activity, or correlated identity anomalies were identified.
## User‑Initiated Threat Activity
Heuristics:

   1. User clicked link → SafeLinks/SmartScreen blocked
   2. No credential submission
   3. No malware execution
   4. No lateral movement
   5. No repeated phishing interactions
   6. No parallel identity anomalies

Default Closing Note:
The activity was reviewed and determined to be benign. The user interacted with a potentially malicious link or email, but protective controls (SafeLinks, SmartScreen, Defender) successfully blocked or mitigated the threat. No credential submission, malware execution, or correlated identity anomalies were identified.
## Device Threat Activity
Heuristics:

   1. Process execution matches known software
   2. No persistence mechanisms
   3. No credential theft tooling
   4. No suspicious command‑line activity
   5. No outbound connections to malicious domains
   6. No correlation with identity anomalies

Default Closing Note:
The activity was reviewed and determined to be benign. Device‑side threat detections were associated with expected software behavior or known safe processes. No indicators of malware execution, persistence mechanisms, credential theft tooling, or correlated identity anomalies were identified.

## Admin / Service Configuration Activity — Application Credential Creation
This category covers legitimate administrative actions where a privileged user adds a credential (certificate or secret) to an Azure AD / Entra ID application or service principal. These events commonly occur during application onboarding, vendor integrations, API authentication setup, or service principal lifecycle management. Activity is typically performed by IT administrators, developers, or service accounts responsible for platform configuration.
Heuristics (Triage Logic)
Use these checks to determine whether the activity is expected or suspicious.

   1. Actor Validation
      1. Privileged admin or service account?
      2. Known identity performing configuration tasks?
      3. Matches baseline admin behavior?
   2. IP & Device Validation
      1. IP address aligns with user’s normal sign‑in patterns
      2. Device is managed and baseline‑consistent
      3. No anomalies in identity timeline
   3. Workflow Context
      1. Application/service principal is part of an ongoing project or vendor rollout
      2. Credential creation aligns with expected implementation steps
      3. Operation matches known admin responsibilities
   4. Operation Validation
      1. First credential added to a new or recently onboarded application
      2. No evidence of unauthorized privilege escalation
      3. No lateral movement or suspicious sign‑ins around the event
   5. Threat Controls
      1. No risky sign‑ins
      2. No MFA anomalies
      3. No Conditional Access bypass
      4. No malicious indicators associated with the app or IP

Default Closing Note:
The activity represents expected administrative configuration related to application onboarding. A privileged user added a credential to an Azure AD / Entra ID application as part of an ongoing implementation workflow. The initiating IP, device, and identity timeline are baseline‑consistent, and no indicators of compromise or unauthorized access were identified. The event is classified as benign administrative activity.
   

