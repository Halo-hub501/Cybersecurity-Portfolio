#!/usr/bin/env python3
"""
Generate realistic SOC alerts for testing triage system.
Outputs simulated security events that a SIEM would produce.
"""

import json
import random
from datetime import datetime, timedelta
from pathlib import Path

# Common malicious IPs for simulation
MALICIOUS_IPS = [
    "192.168.1.42",
    "10.0.0.15",
    "172.16.0.88",
    "203.0.113.45",
    "198.51.100.23",
]

# Internal network ranges
INTERNAL_IPS = [
    "192.168.0.50",
    "192.168.0.75",
    "192.168.0.100",
    "10.0.1.20",
    "10.0.1.50",
]

# Common usernames
USERS = ["jsmith", "kchen", "mrodriguez", "ashah", "djones", "ewhite"]

# Alert templates
ALERT_TEMPLATES = [
    {
        "type": "failed_login",
        "severity": "medium",
        "description": "Multiple failed login attempts",
        "template": {
            "alert_type": "failed_login",
            "source_ip": None,  # Will be populated
            "target_user": None,
            "attempts": None,
            "timestamp": None,
        },
    },
    {
        "type": "port_scan",
        "severity": "high",
        "description": "Possible network reconnaissance",
        "template": {
            "alert_type": "port_scan",
            "source_ip": None,
            "target_host": None,
            "ports_scanned": None,
            "timestamp": None,
        },
    },
    {
        "type": "malware_signature",
        "severity": "critical",
        "description": "Known malware pattern detected",
        "template": {
            "alert_type": "malware_signature",
            "host": None,
            "malware_name": None,
            "file_path": None,
            "timestamp": None,
        },
    },
    {
        "type": "privilege_escalation",
        "severity": "critical",
        "description": "Unauthorized privilege escalation attempt",
        "template": {
            "alert_type": "privilege_escalation",
            "user": None,
            "host": None,
            "command": None,
            "timestamp": None,
        },
    },
    {
        "type": "ddos_pattern",
        "severity": "high",
        "description": "Possible DDoS attack detected",
        "template": {
            "alert_type": "ddos_pattern",
            "target_ip": None,
            "requests_per_sec": None,
            "source_ips": None,
            "timestamp": None,
        },
    },
]


def generate_alert():
    """Generate a single realistic alert."""
    template_choice = random.choice(ALERT_TEMPLATES)
    alert_template = template_choice["template"].copy()
    alert_type = template_choice["type"]

    # Generate alert-specific data
    if alert_type == "failed_login":
        alert_template["source_ip"] = random.choice(MALICIOUS_IPS)
        alert_template["target_user"] = random.choice(USERS)
        alert_template["attempts"] = random.randint(3, 12)

    elif alert_type == "port_scan":
        alert_template["source_ip"] = random.choice(MALICIOUS_IPS)
        alert_template["target_host"] = random.choice(INTERNAL_IPS)
        alert_template["ports_scanned"] = random.randint(50, 500)

    elif alert_type == "malware_signature":
        alert_template["host"] = random.choice(INTERNAL_IPS)
        alert_template["malware_name"] = random.choice(
            ["Trojan.Emotet", "Ransomware.Sodinokibi", "Backdoor.Netcat"]
        )
        alert_template["file_path"] = f"C:\\Users\\{random.choice(USERS)}\\AppData\\Local\\Temp\\{random.randint(1000, 9999)}.exe"

    elif alert_type == "privilege_escalation":
        alert_template["user"] = random.choice(USERS)
        alert_template["host"] = random.choice(INTERNAL_IPS)
        alert_template["command"] = random.choice(
            ["whoami /groups", "net localgroup administrators", "powershell.exe -NoProfile -ExecutionPolicy Bypass"]
        )

    elif alert_type == "ddos_pattern":
        alert_template["target_ip"] = random.choice(INTERNAL_IPS)
        alert_template["requests_per_sec"] = random.randint(5000, 50000)
        alert_template["source_ips"] = random.sample(MALICIOUS_IPS, k=random.randint(2, 4))

    # Add timestamp (within last hour)
    time_offset = random.randint(0, 3600)
    alert_template["timestamp"] = (datetime.now() - timedelta(seconds=time_offset)).isoformat()

    # Add metadata
    alert = {
        "id": f"alert_{random.randint(10000, 99999)}",
        "severity": template_choice["severity"],
        "data": alert_template,
    }

    return alert


def main():
    """Generate 30 simulated alerts and save to JSON."""
    num_alerts = 30
    alerts = [generate_alert() for _ in range(num_alerts)]

    # Save raw alerts
    output_file = Path(".tmp") / "raw_alerts.json"
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, "w") as f:
        json.dump(alerts, f, indent=2)

    print(f"[OK] Generated {num_alerts} alerts")
    print(f"[FILE] Saved to: {output_file.absolute()}")
    print(f"\nAlert breakdown:")
    alert_types = {}
    for alert in alerts:
        alert_type = alert["data"]["alert_type"]
        alert_types[alert_type] = alert_types.get(alert_type, 0) + 1

    for atype, count in sorted(alert_types.items()):
        print(f"  - {atype}: {count}")


if __name__ == "__main__":
    main()
