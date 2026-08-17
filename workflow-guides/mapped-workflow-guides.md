## Privileged Operations

   1. Initial Checks
      1. Validate actor identity
      2. Confirm admin role
      3. Check sign‑in success
   2. Baseline Comparison
      1. Actor in expected admin list
      2. IP in expected ranges
      3. Device matches admin baseline
   3. Correlation Workflow
      1. Identity timeline
      2. Device timeline
      3. MFA history
      4. CA evaluation
      5. Escalate if privilege escalation
   4. Closing Note

## Authentication Failures

   1. Validate failure pattern
   2. Check device fingerprint
   3. Check IP location
   4. Review MFA history
   5. Compare to baseline
   6. Apply tuning (single failure → success = suppress)
   7. Correlate identity timeline
   8. Close or escalate
   9. Apply closing note

## Conditional Access Changes

   1. Validate admin identity
   2. Check CA change type
   3. Compare to baseline workflows
   4. Check maintenance window
   5. Correlate identity + device timeline
   6. Evaluate policy impact
   7. Apply tuning (expected = suppress)
   8. Escalate if controls removed
   9. Apply closing note

## Guest / External User Lifecycle

   1. Validate admin identity
   2. Check guest creation/deletion pattern
   3. Compare group assignments to baseline
   4. Check IP legitimacy
   5. Correlate identity timeline
   6. Apply tuning
   7. Escalate privileged guest access
   8. Apply closing note

## Local Group Membership Changes

   1. Validate actor
   2. Check device provisioning status
   3. Compare group change to baseline
   4. Correlate device timeline
   5. Check process legitimacy
   6. Apply tuning
   7. Escalate privileged group additions
   8. Apply closing note

## Authentication Method Changes

   1. Validate admin/user identity
   2. Check method type
   3. Compare to baseline MFA methods
   4. Review MFA history
   5. Correlate identity timeline
   6. Apply tuning
   7. Escalate unfamiliar MFA methods
   8. Apply closing note

## Insider Risk Data Movement

   1. Validate file type
   2. Check file location
   3. Compare volume to baseline
   4. Review sharing patterns
   5. Correlate identity + device timeline
   6. Apply tuning
   7. Escalate external sharing
   8. Apply closing note

## Account Creation / Deletion

   1. Validate admin identity
   2. Check lifecycle pattern
   3. Compare group membership to baseline
   4. Correlate identity timeline
   5. Apply tuning
   6. Escalate privileged role assignment
   7. Apply closing note

## Device-Linked Identity Events

   1. Validate device identity
   2. Check provisioning pattern
   3. Compare processes to baseline
   4. Correlate device + identity timeline
   5. Apply tuning
   6. Escalate suspicious processes
   7. Apply closing note

## User-Initiated Threat Activity

   1. Validate threat type
   2. Check SafeLinks/SmartScreen outcome
   3. Review identity timeline
   4. Check device timeline
   5. Apply tuning
   6. Escalate credential submission
   7. Apply closing note

## Device Threat Activity

   1. Validate process
   2. Compare to baseline safe processes
   3. Review AV/EDR context
   4. Correlate device + identity timeline
   5. Apply tuning
   6. Escalate persistence or credential theft
   7. Apply closing note


