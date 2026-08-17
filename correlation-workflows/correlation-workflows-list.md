# Privileged Operations
1. Identity Timeline — check sign‑ins before/after the privileged action
2. Device Timeline — confirm admin device activity matches baseline
3. Network Context — verify IP matches expected admin ranges
4. MFA History — ensure no unusual MFA prompts
5. CA Evaluation — confirm CA policies didn’t block or challenge the action

# Authentication Failures
1. Identity Timeline — failures → success pattern
2. Device Context — confirm device fingerprint matches baseline
3. Network Context — check IP reputation and location
4. MFA History — ensure no MFA fatigue or repeated prompts
5. User Behavior — confirm user activity aligns with normal workflow

# Conditional Access Changes
1. Identity Timeline — admin sign‑ins before/after change
2. Device Timeline — confirm admin device legitimacy
3. Network Context — verify admin IP
4. MFA History — ensure admin MFA success
5. Policy Impact — check if change affects high‑risk users/apps

# Guest / External User Lifecycle
1. Identity Timeline — admin activity around guest creation/deletion
2. Network Context — confirm admin IP
3. Group Membership — check for privileged or unexpected groups
4. Access Patterns — verify guest access matches project workflow
5. Device Context — ensure no suspicious device activity

# Local Group Membership Changes
1. Device Timeline — confirm provisioning or troubleshooting activity
2. Identity Timeline — check admin sign‑ins
3. Network Context — verify admin IP
4. Process Context — confirm expected provisioning tools
5. Group Membership — ensure no privileged escalation

# Authentication Method Changes
1. Identity Timeline — check sign‑ins around method change
2. Device Context — confirm user/admin device legitimacy
3. Network Context — verify IP matches baseline
4. MFA History — ensure no suspicious MFA prompts
5. User Behavior — confirm expected workflow (new device, reset)

# Insider Risk Data Movement
1. Identity Timeline — check sign‑ins before/after file movement
2. Device Timeline — confirm device behavior matches baseline
3. Network Context — verify no external exfiltration
4. File Access Patterns — check volume, type, location
5. Sharing Context — confirm internal vs external

# Account Creation / Deletion
1. Identity Timeline — admin sign‑ins around lifecycle event
2. Network Context — verify admin IP
3. Group Membership — check for privileged groups
4. Lifecycle Patterns — confirm onboarding/offboarding workflow
5. Device Context — ensure no suspicious device activity

# Device-Linked Identity Events
1. Device Timeline — check provisioning or admin activity
2. Identity Timeline — correlate with user/admin sign‑ins
3. Process Context — confirm OEM/provisioning tools
4. Network Context — verify device IP
5. Threat Context — check for correlated device alerts

# User-Initiated Threat Activity
• Identity Timeline — check sign‑ins around phishing click
• Device Timeline — confirm no malware execution
• Network Context — verify no outbound malicious traffic
• MFA History — ensure no MFA anomalies
• Threat Controls — SafeLinks/SmartScreen/Defender outcomes

# Device Threat Activity
• Device Timeline — check for suspicious processes or persistence
• Identity Timeline — correlate with user/admin sign‑ins
• Network Context — verify no malicious outbound traffic
• Process Context — confirm safe vs suspicious binaries
• Threat Context — check for correlated identity anomalies
















