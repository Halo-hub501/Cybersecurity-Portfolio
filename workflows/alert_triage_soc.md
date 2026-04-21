# SOC Tier 1: Alert Triage & Incident Response System

## Objective
Build a simulation of a Tier 1 SOC that:
1. Receives security alerts from multiple sources
2. Triages them by severity/priority
3. Deduplicates and correlates related alerts
4. Automatically responds based on playbooks
5. Logs all actions with audit trail

## Why This Matters
Real Tier 1 SOC work is: raw alerts → apply rules → prioritize → execute response playbooks → escalate. This system demonstrates you understand the workflow and can handle alert fatigue (the #1 SOC problem).

## Inputs
- Alert source data (simulated or real logs)
- Playbook definitions (what to do for each alert type)
- Threat intelligence data (IPs/domains to block, etc.)

## Process

### 1. Generate Simulated Alerts
Use `tools/generate_alerts.py` to create realistic security alerts:
- Failed login attempts
- Port scans
- Suspicious file access
- Malware signatures
- DDoS patterns
- Privilege escalation attempts

### 2. Triage & Deduplicate
Use `tools/triage_alerts.py` to:
- Assign severity (Critical, High, Medium, Low)
- Deduplicate identical alerts (same source, same alert type within 5 min window)
- Correlate related alerts (same IP failing multiple logins = 1 incident, not 10)
- Auto-escalate Critical/High severity

### 3. Execute Playbooks
For each alert, apply the appropriate playbook:
- **Failed Logins**: If >5 in 5 min from same IP → block IP, create ticket, alert manager
- **Port Scan**: Block source IP, increase monitoring on target, escalate if internal
- **Malware Detection**: Isolate host, disable user, escalate immediately
- **Privilege Escalation**: Log full context, escalate, freeze account pending review

### 4. Output
- Dashboard showing:
  - Real-time alert feed (newest first)
  - Triage status (Raw → Triaged → Responded → Resolved)
  - Escalation history
  - Audit log of all actions
- JSON export for integration with ticketing systems

## Success Criteria
- ✅ At least 20 simulated alerts generated
- ✅ Alerts de-duped and correlated correctly
- ✅ Playbooks execute and log actions
- ✅ Dashboard shows full incident lifecycle
- ✅ Audit trail is complete and queryable

## Edge Cases
- Same alert from multiple sources (count as 1 incident)
- Cascading alerts from single root cause (correlate them)
- Alert storm (>100 alerts/min) - don't crash, prioritize Critical
- Response failures (e.g., IP block fails) - log error, escalate manually

## Tech Stack
- Python (pandas for triage logic, json for playbooks)
- SQLite for audit logging
- Optional: Flask web UI for dashboard

## Known Limitations
- Simulated data (real IPs/logs would be better but harder to control)
- Playbooks are hardcoded (real SOCs have dynamic runbooks)
- No ML-based anomaly detection (v2 enhancement)

## Next Steps
1. Run `generate_alerts.py` to see raw alert data
2. Run `triage_alerts.py` to see triage + response
3. Open `dashboard.html` to see the visualization
4. Review audit log in `.tmp/audit_log.json`
