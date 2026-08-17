## Privileged Operations

   1. Suppress when expected admin actor — matches baseline
   2. Suppress when expected IP range — corporate VPN, office subnets
   3. Auto‑close when workflow matches baseline — CA edits, MFA resets
   4. Escalate when privilege escalation detected
   5. Escalate when new admin role appears

## Authentication Failures

   1. Suppress single failure → success
   2. Suppress expected device/location
   3. Auto‑close mistyped password patterns
   4. Escalate repeated failures across methods
   5. Escalate unfamiliar sign‑in properties

## Conditional Access Changes

   1. Suppress expected admin actor
   2. Suppress scheduled maintenance window
   3. Auto‑close expected policy tuning
   4. Escalate removal of critical controls
   5. Escalate broadening of access scope

## Guest / External User Lifecycle

   1. Suppress expected onboarding/offboarding
   2. Auto‑close expected group assignments
   3. Escalate privileged role assignment
   4. Escalate unexpected external IP patterns

## Local Group Membership Changes

   1. Suppress provisioning workflow
   2. Auto‑close expected group additions
   3. Escalate privileged group additions
   4. Escalate mass changes across devices

## Authentication Method Changes

   1. Suppress expected admin actor
   2. Suppress user re‑registration after device change
   3. Auto‑close expected MFA methods
   4. Escalate unfamiliar MFA method
   5. Escalate method added during suspicious sign‑in

## Insider Risk Data Movement

   1. Suppress expected file types
   2. Suppress expected locations
   3. Auto‑close small batch movement
   4. Escalate mass downloads/uploads
   5. Escalate external sharing

## Account Creation / Deletion

   1. Suppress expected file types
   2. Suppress expected locations
   3. Auto‑close small batch movement
   4. Escalate mass downloads/uploads
   5. Escalate external sharing

## Device-Linked Identity Events

   1. Suppress expected provisioning patterns
   2. Auto‑close expected OEM processes
   3. Escalate suspicious processes
   4. Escalate abnormal device timeline

## User-Initiated Threat Activity

   1. Suppress SafeLinks/SmartScreen blocks
   2. Auto‑close no credential submission
   3. Escalate credential submission
   4. Escalate malware execution

## Device Threat Activity

   1. Suppress known safe processes
   2. Suppress low‑severity AV/EDR detections
   3. Auto‑close expected provisioning activity
   4. Escalate persistence mechanisms
   5. Escalate credential theft tooling
