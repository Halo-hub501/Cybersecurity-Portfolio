#!/usr/bin/env python3
"""
Generate an HTML dashboard showing alert triage results.
"""

import json
from pathlib import Path


def generate_dashboard():
    """Create HTML dashboard from incidents and audit log."""
    # Load data
    incidents_file = Path(".tmp") / "incidents.json"
    audit_file = Path(".tmp") / "audit_log.json"

    if not incidents_file.exists():
        print("[ERROR] incidents.json not found. Run triage_alerts.py first.")
        return

    with open(incidents_file) as f:
        incidents = json.load(f)

    with open(audit_file) if audit_file.exists() else open("/dev/null") as f:
        audit_log = json.load(f) if audit_file.exists() else []

    # Count stats
    critical = sum(1 for i in incidents if i["severity"] == "critical")
    high = sum(1 for i in incidents if i["severity"] == "high")
    medium = sum(1 for i in incidents if i["severity"] == "medium")

    # Generate HTML
    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>[SOC] Tier 1 - Alert Triage Dashboard</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: #0f1419;
            color: #e0e0e0;
            padding: 20px;
        }}
        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}
        .header {{
            margin-bottom: 30px;
        }}
        h1 {{
            color: #00ff88;
            margin-bottom: 10px;
            font-size: 2.5em;
        }}
        .subtitle {{
            color: #888;
            font-size: 1.1em;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 20px;
            margin-bottom: 30px;
        }}
        .stat-card {{
            background: #1a1f2e;
            border-left: 4px solid #00ff88;
            padding: 20px;
            border-radius: 4px;
        }}
        .stat-card.critical {{
            border-left-color: #ff4444;
        }}
        .stat-card.high {{
            border-left-color: #ffaa00;
        }}
        .stat-card.medium {{
            border-left-color: #ffff00;
        }}
        .stat-card.info {{
            border-left-color: #00ff88;
        }}
        .stat-value {{
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .stat-label {{
            color: #888;
            font-size: 0.9em;
        }}
        .incidents-table {{
            background: #1a1f2e;
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 30px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
        }}
        th {{
            background: #0f1419;
            padding: 15px;
            text-align: left;
            border-bottom: 2px solid #333;
            font-weight: 600;
        }}
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #333;
        }}
        tr:hover {{
            background: #242b38;
        }}
        .severity-critical {{
            color: #ff4444;
            font-weight: bold;
        }}
        .severity-high {{
            color: #ffaa00;
            font-weight: bold;
        }}
        .severity-medium {{
            color: #ffff00;
            font-weight: bold;
        }}
        .badge {{
            display: inline-block;
            padding: 4px 8px;
            border-radius: 3px;
            font-size: 0.85em;
            background: #333;
            color: #00ff88;
        }}
        .actions-list {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}
        .action {{
            background: #2a3f4e;
            padding: 4px 8px;
            border-radius: 3px;
            font-size: 0.85em;
            color: #00ff88;
        }}
        .footer {{
            color: #666;
            font-size: 0.9em;
            margin-top: 20px;
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>[SECURE] SOC Tier 1 - Alert Triage Dashboard</h1>
            <p class="subtitle">Real-time incident response automation</p>
        </div>

        <div class="stats">
            <div class="stat-card critical">
                <div class="stat-value">{critical}</div>
                <div class="stat-label">Critical Incidents</div>
            </div>
            <div class="stat-card high">
                <div class="stat-value">{high}</div>
                <div class="stat-label">High Severity</div>
            </div>
            <div class="stat-card medium">
                <div class="stat-value">{medium}</div>
                <div class="stat-label">Medium Severity</div>
            </div>
            <div class="stat-card info">
                <div class="stat-value">{len(incidents)}</div>
                <div class="stat-label">Total Incidents</div>
            </div>
        </div>

        <div class="incidents-table">
            <table>
                <thead>
                    <tr>
                        <th>Incident ID</th>
                        <th>Type</th>
                        <th>Severity</th>
                        <th>Alerts</th>
                        <th>Escalation</th>
                        <th>Actions Taken</th>
                        <th>Timestamp</th>
                    </tr>
                </thead>
                <tbody>
"""

    # Add incident rows
    for incident in sorted(incidents, key=lambda x: x["timestamp"], reverse=True):
        severity_class = f"severity-{incident['severity']}"
        actions_html = " ".join(
            f'<div class="action">{a.replace("_", " ").title()}</div>'
            for a in incident["actions_taken"][:3]
        )
        if len(incident["actions_taken"]) > 3:
            actions_html += f'<div class="action">+{len(incident["actions_taken"]) - 3} more</div>'

        html += f"""                    <tr>
                        <td>{incident['id']}</td>
                        <td><span class="badge">{incident['type']}</span></td>
                        <td><span class="{severity_class}">{incident['severity'].upper()}</span></td>
                        <td>{incident['alert_count']}</td>
                        <td>{incident['escalation'].upper()}</td>
                        <td>
                            <div class="actions-list">
                                {actions_html}
                            </div>
                        </td>
                        <td>{incident['timestamp']}</td>
                    </tr>
"""

    html += """                </tbody>
            </table>
        </div>

        <div class="footer">
            <p>[ACTIVE] Dashboard generated by SOC Alert Triage System</p>
            <p>All incidents triaged and responses automated | Audit log maintained</p>
        </div>
    </div>
</body>
</html>
"""

    # Save HTML
    output_file = Path(".tmp") / "dashboard.html"
    with open(output_file, "w") as f:
        f.write(html)

    print(f"[OK] Dashboard generated")
    print(f"[FILE] Open in browser: {output_file.absolute()}")


if __name__ == "__main__":
    generate_dashboard()
