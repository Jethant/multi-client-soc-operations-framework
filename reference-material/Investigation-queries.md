# Query to get a table's layout:
TableName
| take 10

# Query for broad search last 7 days:
Search "[term to find]"
| where TimeGenerated > ago (7d)

# Query to retrieve Antivirus scan from defender:
DeviceEvents
| where ActionType contains "Antivirus"
| where DeviceName == "devicename"
| where TimeGenerated > ago (7d)

# Query for detailed port scan info:
set query_now = datetime();
let PortScanThreshold = 50;
let PortCounts =
    _Im_NetworkSession
    | where ipv4_is_private(SrcIpAddr) == false
    | summarize AttemptedPortsCount = dcount(DstPortNumber)
        by SrcIpAddr, TimeGenerated = bin(TimeGenerated, 5m);
_Im_NetworkSession
| where ipv4_is_private(SrcIpAddr) == false
| extend TimeGenerated = bin(TimeGenerated, 5m)
| join kind=inner PortCounts on SrcIpAddr, TimeGenerated
| where AttemptedPortsCount > PortScanThreshold
