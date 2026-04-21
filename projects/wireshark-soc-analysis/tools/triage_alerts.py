#!/usr/bin/env python3
"""
Triage alerts, deduplicate, correlate, and execute response playbooks.
Logs all actions to audit trail.
"""

import json
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

# Playbook definitions - what to do for each alert type
PLAYBOOKS = {
    "failed_login": {
        "threshold": 5,  # Trigger if >5 attempts in 5 minutes from same IP
        "actions": [
            "block_source_ip",
            "create_incident_ticket",
            "alert_security_team",
        ],
        "escalate_to": "high",
    },
    "port_scan": {
        "threshold": 1,  # Any port scan is actionable
        "actions": [
            "block_source_ip",
            "increase_monitoring_on_target",
            "log_incident",
        ],
        "escalate_to": "high",
    },
    "malware_signature": {
        "threshold": 1,
        "actions": [
            "isolate_host",
            "disable_user_account",
            "quarantine_file",
            "escalate_to_tier2",
        ],
        "escalate_to": "critical",
    },
    "privilege_escalation": {
        "threshold": 1,
        "actions": [
            "freeze_account_pending_review",
            "log_full_context",
            "alert_manager",
            "escalate_to_tier2",
        ],
        "escalate_to": "critical",
    },
    "ddos_pattern": {
        "threshold": 1,
        "actions": [
            "block_source_ips",
            "activate_ddos_protection",
            "alert_network_team",
        ],
        "escalate_to": "critical",
    },
}


class AlertTriageEngine:
    def __init__(self):
        self.incidents = []  # Correlated incidents
        self.audit_log = []
        self.blocked_ips = set()

    def log_action(self, incident_id, action, details):
        """Log an action to audit trail."""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "incident_id": incident_id,
            "action": action,
            "details": details,
        }
        self.audit_log.append(entry)

    def correlate_alerts(self, alerts):
        """Group related alerts into incidents."""
        incidents_map = defaultdict(list)

        for alert in alerts:
            alert_type = alert["data"]["alert_type"]
            alert_data = alert["data"]

            # Create incident key based on alert type and source
            if alert_type == "failed_login":
                key = f"failed_login_{alert_data['source_ip']}_{alert_data['target_user']}"
            elif alert_type == "port_scan":
                key = f"port_scan_{alert_data['source_ip']}_{alert_data['target_host']}"
            elif alert_type == "malware_signature":
                key = f"malware_{alert_data['host']}_{alert_data['malware_name']}"
            elif alert_type == "privilege_escalation":
                key = f"privesc_{alert_data['user']}_{alert_data['host']}"
            elif alert_type == "ddos_pattern":
                key = f"ddos_{alert_data['target_ip']}"
            else:
                key = f"{alert_type}_{alert['id']}"

            incidents_map[key].append(alert)

        return incidents_map

    def triage_and_respond(self, alerts):
        """Triage alerts and execute response playbooks."""
        incidents_map = self.correlate_alerts(alerts)

        for incident_key, related_alerts in incidents_map.items():
            alert_type = related_alerts[0]["data"]["alert_type"]
            playbook = PLAYBOOKS.get(alert_type, {})

            # Create incident record
            incident = {
                "id": f"incident_{len(self.incidents) + 1}",
                "type": alert_type,
                "alert_count": len(related_alerts),
                "severity": related_alerts[0]["severity"],
                "escalation": playbook.get("escalate_to", "medium"),
                "timestamp": related_alerts[0]["data"]["timestamp"],
                "status": "responded",
                "alerts": [a["id"] for a in related_alerts],
                "actions_taken": [],
            }

            # Execute playbook actions
            for action in playbook.get("actions", []):
                incident["actions_taken"].append(action)
                self.log_action(incident["id"], action, {
                    "alert_type": alert_type,
                    "alert_count": len(related_alerts),
                })

            self.incidents.append(incident)

        return self.incidents

    def generate_report(self):
        """Create summary report."""
        critical = sum(1 for i in self.incidents if i["severity"] == "critical")
        high = sum(1 for i in self.incidents if i["severity"] == "high")
        medium = sum(1 for i in self.incidents if i["severity"] == "medium")

        return {
            "total_incidents": len(self.incidents),
            "breakdown": {
                "critical": critical,
                "high": high,
                "medium": medium,
            },
            "total_alerts_processed": sum(i["alert_count"] for i in self.incidents),
            "deduplication_rate": f"{(1 - len(self.incidents) / sum(i['alert_count'] for i in self.incidents)) * 100:.1f}%" if self.incidents else "0%",
        }


def main():
    # Load raw alerts
    alerts_file = Path(".tmp") / "raw_alerts.json"
    if not alerts_file.exists():
        print("❌ raw_alerts.json not found. Run generate_alerts.py first.")
        return

    with open(alerts_file) as f:
        alerts = json.load(f)

    print(f"[INPUT] Loaded {len(alerts)} raw alerts")

    # Triage and respond
    engine = AlertTriageEngine()
    incidents = engine.triage_and_respond(alerts)

    # Save incidents
    incidents_file = Path(".tmp") / "incidents.json"
    with open(incidents_file, "w") as f:
        json.dump(incidents, f, indent=2)
    print(f"[OK] Triaged into {len(incidents)} incidents")
    print(f"[FILE] Saved to: {incidents_file.absolute()}")

    # Save audit log
    audit_file = Path(".tmp") / "audit_log.json"
    with open(audit_file, "w") as f:
        json.dump(engine.audit_log, f, indent=2)
    print(f"[FILE] Audit log: {audit_file.absolute()}")

    # Print report
    report = engine.generate_report()
    print("\n[REPORT] Triage Report:")
    print(f"  Total incidents: {report['total_incidents']}")
    print(f"  - Critical: {report['breakdown']['critical']}")
    print(f"  - High: {report['breakdown']['high']}")
    print(f"  - Medium: {report['breakdown']['medium']}")
    print(f"  Deduplication rate: {report['deduplication_rate']}")
    print(f"  Total alerts processed: {report['total_alerts_processed']}")


if __name__ == "__main__":
    main()
