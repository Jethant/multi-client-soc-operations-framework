# Investigation queries

Validate table availability, field names, permissions, and time zone in the target environment. Run queries in the correct client workspace and add the deployment's approved customer discriminator when multiple clients share a workspace.

Replace example values before execution. Start with a narrow time range to control cost and noise.

## Inspect a table sample

```kusto
TableName
| take 10
```

## Broad search over the last seven days

Broad search can be expensive. Narrow the tables and time range whenever possible.

```kusto
search in (*) "term to find"
| where TimeGenerated >= ago(7d)
| take 100
```

## Defender antivirus-related device events

```kusto
let Lookback = 7d;
let TargetDevice = "device-name";
DeviceEvents
| where TimeGenerated >= ago(Lookback)
| where DeviceName =~ TargetDevice
| where ActionType contains "Antivirus"
| project TimeGenerated, DeviceName, ActionType, InitiatingProcessAccountName,
          InitiatingProcessFileName, AdditionalFields
| order by TimeGenerated desc
```

## Potential port scan from a public source

Tune the time bin and threshold for the environment. Validate direction and authorized scanner ranges before operational use.

```kusto
let Lookback = 1h;
let BinSize = 5m;
let PortScanThreshold = 50;
_Im_NetworkSession
| where TimeGenerated >= ago(Lookback)
| where isnotempty(SrcIpAddr) and isnotempty(DstIpAddr)
| where ipv4_is_private(SrcIpAddr) == false
| summarize AttemptedPorts = dcount(DstPortNumber),
            DestinationCount = dcount(DstIpAddr),
            FirstSeen = min(TimeGenerated),
            LastSeen = max(TimeGenerated)
    by SrcIpAddr, bin(TimeGenerated, BinSize)
| where AttemptedPorts > PortScanThreshold
| order by AttemptedPorts desc
```
