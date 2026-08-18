# Threat-hunting workflow

Start each threat hunt with a falsifiable hypothesis. Alert volume helps define scope.

## 1. Select and scope a hypothesis

- State the suspected behavior, affected client, entities, data sources, and UTC time range.
- Define what evidence would support or reject the hypothesis.
- Confirm that the correct client workspace and customer discriminator are applied.

## 2. Establish the baseline

- Review alert and incident trends by taxonomy ID, rule, client, severity, and disposition.
- Compare the current period with an appropriate historical period.
- Identify telemetry gaps before interpreting an absence of results.

## 3. Investigate behavior

- Start from the detection logic and understand scheduling statements before removing them.
- Expand across identity, endpoint, network, email, application, and audit sources.
- Search for repeated entities, infrastructure, files, processes, sessions, and techniques.
- Track supporting, contradicting, and unknown evidence.

## 4. Record the outcome

- Confirmed finding, rejected hypothesis, inconclusive result, or detection gap
- Queries and exact time ranges used
- Affected entities and evidence references
- Detection, hardening, baseline, or tuning recommendations
- Owner, priority, and due date

Route proposed suppression logic through the [tuning policy](../tuning/README.md) and its testing requirements.
