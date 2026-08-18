# Reporting queries

The `SecurityIncident` table can contain updated snapshots of the same incident. These examples select the latest record per `IncidentName` before reporting. Run them in the correct client workspace and apply the deployment's approved customer discriminator when multiple clients share a workspace.

## Incidents created in the last seven days by severity

```kusto
let Lookback = 7d;
let LatestIncidents =
    SecurityIncident
    | where CreatedTime >= ago(Lookback)
    | summarize arg_max(TimeGenerated, *) by IncidentName;
LatestIncidents
| summarize Total = count() by Severity
| union (
    LatestIncidents
    | summarize Total = count()
    | extend Severity = "All"
)
| order by Total desc
```

## Mean time to first incident modification

`FirstModifiedTime` records the first modification, not necessarily analyst triage. Do not label this metric mean time to triage unless the operating process guarantees that the first modification represents triage.

```kusto
let Lookback = 7d;
SecurityIncident
| where CreatedTime >= ago(Lookback)
| summarize arg_max(TimeGenerated, *) by IncidentName
| where isnotnull(FirstModifiedTime)
| extend MinutesToFirstModification = datetime_diff("minute", FirstModifiedTime, CreatedTime)
| where MinutesToFirstModification >= 0
| summarize MeanTimeToFirstModificationHours = avg(MinutesToFirstModification) / 60.0,
            IncidentCount = count()
```

## Mean closure time for incidents closed in the last seven days

```kusto
let Lookback = 7d;
SecurityIncident
| summarize arg_max(TimeGenerated, *) by IncidentName
| where isnotnull(ClosedTime) and ClosedTime >= ago(Lookback)
| extend ClosureMinutes = datetime_diff("minute", ClosedTime, CreatedTime)
| where ClosureMinutes >= 0
| summarize MeanTimeToClosureHours = avg(ClosureMinutes) / 60.0,
            IncidentCount = count()
```

## Incidents created in the last 30 days by severity

```kusto
let Lookback = 30d;
let LatestIncidents =
    SecurityIncident
    | where CreatedTime >= ago(Lookback)
    | summarize arg_max(TimeGenerated, *) by IncidentName;
LatestIncidents
| summarize Total = count() by Severity
| union (
    LatestIncidents
    | summarize Total = count()
    | extend Severity = "All"
)
| order by Total desc
```

## High-severity incidents closed in the last 30 days

```kusto
let Lookback = 30d;
SecurityIncident
| summarize arg_max(TimeGenerated, *) by IncidentName
| where isnotnull(ClosedTime) and ClosedTime >= ago(Lookback)
| where Severity =~ "High"
| project ClosedTime, IncidentNumber, Title, Classification,
          ClassificationReason, ClassificationComment, Owner
| order by ClosedTime desc
```

## Quarantined email events in the last 30 days by threat type

```kusto
let Lookback = 30d;
let QuarantinedThreats =
    EmailEvents
    | where TimeGenerated >= ago(Lookback)
    | where DeliveryLocation =~ "Quarantine"
    | where isnotempty(ThreatTypes)
    | mv-expand Threat = split(ThreatTypes, ",")
    | extend Threat = trim(" ", tostring(Threat))
    | where isnotempty(Threat);
QuarantinedThreats
| summarize Total = count() by Threat
| union (
    QuarantinedThreats
    | summarize Total = count()
    | extend Threat = "All"
)
| order by Total desc
```
