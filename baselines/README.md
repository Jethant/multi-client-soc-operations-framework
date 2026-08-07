# Baselines
This file contains baseline definitions used to compare user, device, and access behavior against expected norms across tenants. The template below is a starting point to build future tailored baselines off of for individual clients. Each category is tied to common alert types and associated known actors, systems, or telemetry commonly found in that respective category. Full operational content intentionally omitted.

# 1. Privileged Operations
	• Expected Admin Actors — IAM team, helpdesk leads, cloud engineers
	• Expected IP Ranges — corporate VPN, office subnets
	• Expected Devices — managed workstations, jump boxes
	• Expected Workflows — CA edits, MFA resets, role assignments
	• Expected Timing — business hours, maintenance windows

# 2. Authentication Failures
	• Expected Failure Patterns — mistyped password, expired session
	• Expected Devices — user’s primary workstation or mobile
	• Expected Locations — home, office, usual travel
	• Expected MFA Behavior — single failure → immediate success

# 3. Conditional Access Changes
	• Expected Admin Actors — IAM team, cloud architects
	• Expected Workflows — policy tuning, onboarding new apps
	• Expected Change Types — session controls, sign‑in frequency
	• Expected Timing — scheduled maintenance

# 4. Guest / External User Lifecycle
	• Expected Admin Actors — helpdesk, project managers
	• Expected Group Assignments — project‑specific, limited access
	• Expected Lifecycle Patterns — short‑term access, cleanup cycles
	• Expected IP Ranges — external but consistent with partner org

# 5. Local Group Membership Changes
	• Expected Actors — endpoint team, helpdesk
	• Expected Devices — newly provisioned workstations
	• Expected Workflows — provisioning, troubleshooting
	• Expected Groups — Administrators, Remote Desktop Users

# 6. Authentication Method Changes
	• Expected Admin Actors — IAM team
	• Expected User Behavior — re‑registering MFA after device change
	• Expected Methods — Authenticator app, phone, FIDO2
	• Expected Timing — during onboarding or device replacement

# 7. Insider Risk Data Movement
	• Expected File Types — documents, spreadsheets, PDFs
	• Expected Locations — SharePoint, OneDrive, team folders
	• Expected Volume — small batches, routine saves
	• Expected Sharing Patterns — internal only

# 8. Account Creation / Deletion
	• Expected Admin Actors — IAM team, HR onboarding
	• Expected Lifecycle Patterns — consultant onboarding/offboarding
	• Expected Group Membership — role‑appropriate, non‑privileged
	• Expected Timing — start/end of projects

# 9. Device‑Linked Identity Events
	• Expected Devices — managed workstations
	• Expected Provisioning Patterns — local admin creation, enrollment
	• Expected Actors — endpoint team
	• Expected Processes — OEM tools, provisioning scripts

# 10. User‑Initiated Threat Activity
	• Expected User Behavior — occasional phishing clicks without credential submission
	• Expected Controls — SafeLinks, SmartScreen, Defender
	• Expected Outcomes — blocked URL, no malware execution
	• Expected Follow‑Up — user notified, password reset if needed

# 11. Device Threat Activity
	• Expected Processes — OEM tools, IT scripts, known safe binaries
	• Expected AV/EDR Behavior — low‑severity detections, false positives
	• Expected Network Behavior — no outbound malicious connections
	• Expected Timeline — activity during provisioning or updates
