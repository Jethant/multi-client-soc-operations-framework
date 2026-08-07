Query to get alerts from the last 7 days, sorted by severity:  
SecurityIncident 
| where TimeGenerated >= ago(7d) 
| where ProviderName in ("Azure Sentinel", "Microsoft 365 Defender", "Microsoft XDR") 
| where Status == "Closed" 
| summarize Total = count() by Severity 
| union ( 
    SecurityIncident 
    | where TimeGenerated >= ago(7d) 
    | where ProviderName in ("Azure Sentinel", "Microsoft 365 Defender", "Microsoft XDR") 
    | where Status == "Closed" 
    | summarize Severity = "All", Total = count() 
) 
            
Query to get mean triage time for all incidents:  
SecurityIncident 
| where TimeGenerated > ago(7d) 
| extend TriageDurationMinutes = datetime_diff('minute', FirstModifiedTime, CreatedTime) 
| extend TriageDurationHours = TriageDurationMinutes / 60.0 
| summarize MeanTimeToTriage_Hours = avg(TriageDurationHours) 


Query for mean closure time for all incidents:  
SecurityIncident 
| where TimeGenerated > ago(7d) 
| extend ClosureDurationMinutes = datetime_diff('minute', ClosedTime, CreatedTime) 
| extend ClosureDurationHours = ClosureDurationMinutes / 60.0 
| summarize MeanTimeToClosure_Hours = avg(ClosureDurationHours) 


Query to get a count of all incidents generated in last 30 days, sorted by severity:
SecurityIncident 
| where TimeGenerated >= ago(30d) 
| where ProviderName in ("Azure Sentinel", "Microsoft 365 Defender", "Microsoft XDR") 
| where Status == "Closed" 
| summarize Total = count() by Severity 
| union ( 
    SecurityIncident 
    | where TimeGenerated >= ago(30d) 
    | where ProviderName in ("Azure Sentinel", "Microsoft 365 Defender", "Microsoft XDR") 
    | where Status == "Closed" 
    | summarize Severity = "All", Total = count() 
) 


Query to get closing notes for high severity incidents closed in the last 30 days:
SecurityIncident 
| where TimeGenerated >= ago(30d) 
| where ProviderName in ("Azure Sentinel", "Microsoft 365 Defender", "Microsoft XDR") 
| where Severity == "High" and Status == "Closed" 
| sort by Title 
| project TimeGenerated, Title, ClassificationComment, Severity, IncidentNumber 

 
Query to get a count of quarantined emails sorted by type in the last 30 days:
EmailEvents 
| where TimeGenerated >= ago(30d) 
| where DeliveryLocation == "Quarantine" 
| where ThreatTypes has_any ("Phish","Malware","Spam") 
| mv-expand Threat = split(ThreatTypes, ",") 
| extend Threat = trim(" ", tostring(Threat)) 
| summarize Count = count() by Threat 
| union ( 
    EmailEvents 
    | where TimeGenerated >= ago(30d) 
    | where DeliveryLocation == "Quarantine" 
    | where ThreatTypes has_any ("Phish","Malware","Spam") 
    | mv-expand Threat = split(ThreatTypes, ",") 
    | extend Threat = trim(" ", tostring(Threat)) 
    | summarize Count = count() 
    | extend Threat = "Total" 
) 
| order by Count desc 




