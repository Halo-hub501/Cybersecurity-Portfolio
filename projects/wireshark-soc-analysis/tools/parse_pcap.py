#!/usr/bin/env python3
"""
Parse PCAP file and extract security alerts (IoCs - Indicators of Compromise).
Converts network traffic into security events for SOC analysis.
"""

import json
from pathlib import Path
from collections import defaultdict

# Known malicious indicators
SUSPICIOUS_DOMAINS = [
    "easyasI23.tech",  # From the PCAP exercise
]

SUSPICIOUS_PROTOCOLS = [
    "CLDAP",  # Lightweight Directory Access Protocol - often used for recon
]

SUSPICIOUS_PORTS = [
    443,   # Could indicate C2
    445,   # SMB - common for lateral movement
    3389,  # RDP - remote access
]


def parse_pcap_json(pcap_file):
    """Parse Wireshark JSON export and extract suspicious indicators."""
    alerts = []

    try:
        with open(pcap_file, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("[ERROR] Could not parse PCAP as JSON. File may be corrupted.")
        return alerts

    # Handle both array and dict formats from Wireshark
    packets = data if isinstance(data, list) else data.get('packets', [])

    # Track unique conversations
    dns_queries = defaultdict(list)
    protocols_seen = defaultdict(int)
    source_ips = set()
    dest_ips = set()

    print(f"[PARSING] Processing {len(packets)} packets...")

    for packet_idx, packet in enumerate(packets):
        if not isinstance(packet, dict):
            continue

        packet_data = packet.get('_source', {}).get('layers', {})
        if not packet_data:
            continue

        # Extract DNS queries
        if 'dns' in packet_data:
            dns_layer = packet_data['dns']
            if isinstance(dns_layer, dict):
                queries = dns_layer.get('Queries', {})
                if isinstance(queries, dict):
                    for q_name, q_data in queries.items():
                        if isinstance(q_data, dict) and 'dns.qry.name' in q_data:
                            domain = q_data['dns.qry.name']
                            dns_queries[domain].append({
                                'packet': packet_idx,
                                'query_type': q_data.get('dns.qry.type', 'A'),
                            })

        # Extract protocols
        if 'cldap' in packet_data or 'ldap' in packet_data:
            protocols_seen['CLDAP'] += 1

        # Extract IPs
        if 'ip' in packet_data:
            ip_layer = packet_data['ip']
            if isinstance(ip_layer, dict):
                src = ip_layer.get('ip.src')
                dst = ip_layer.get('ip.dst')
                if src:
                    source_ips.add(src)
                if dst:
                    dest_ips.add(dst)

    # Generate alerts from findings

    # DNS-based alerts
    for domain, queries in dns_queries.items():
        if domain in SUSPICIOUS_DOMAINS:
            alerts.append({
                'id': f'alert_{len(alerts) + 1}',
                'type': 'suspicious_dns_query',
                'severity': 'high',
                'data': {
                    'alert_type': 'suspicious_dns_query',
                    'domain': domain,
                    'query_count': len(queries),
                    'timestamp': str(Path(pcap_file).stat().st_mtime),
                }
            })

    # Protocol-based alerts
    if protocols_seen['CLDAP'] > 0:
        alerts.append({
            'id': f'alert_{len(alerts) + 1}',
            'type': 'suspicious_protocol',
            'severity': 'high',
            'data': {
                'alert_type': 'suspicious_protocol',
                'protocol': 'CLDAP',
                'occurrence_count': protocols_seen['CLDAP'],
                'description': 'CLDAP reconnaissance detected - possible active directory enumeration',
                'timestamp': str(Path(pcap_file).stat().st_mtime),
            }
        })

    # Network reconnaissance alert
    if len(source_ips) > 1 or len(dest_ips) > 5:
        alerts.append({
            'id': f'alert_{len(alerts) + 1}',
            'type': 'network_reconnaissance',
            'severity': 'medium',
            'data': {
                'alert_type': 'network_reconnaissance',
                'source_ip_count': len(source_ips),
                'dest_ip_count': len(dest_ips),
                'description': 'Network scanning activity detected',
                'timestamp': str(Path(pcap_file).stat().st_mtime),
            }
        })

    return alerts


def main():
    pcap_file = Path(".tmp") / "malware.pcap"

    if not pcap_file.exists():
        print("[ERROR] malware.pcap not found in .tmp/")
        return

    print(f"[INPUT] Parsing PCAP: {pcap_file.name} ({pcap_file.stat().st_size / 1024 / 1024:.1f} MB)")

    # Parse PCAP
    alerts = parse_pcap_json(pcap_file)

    # If we got alerts, save them
    if alerts:
        alerts_output = Path(".tmp") / "pcap_alerts.json"
        with open(alerts_output, 'w') as f:
            json.dump(alerts, f, indent=2)

        print(f"[OK] Extracted {len(alerts)} security alerts from PCAP")
        print(f"[FILE] Saved to: {alerts_output.absolute()}")

        # Print summary
        print("\n[ALERTS]")
        for alert in alerts:
            severity = alert['severity'].upper()
            alert_type = alert['type']
            print(f"  - [{severity}] {alert_type}")
    else:
        print("[WARNING] No suspicious indicators found in PCAP")
        print("         (PCAP may be in binary format; use Wireshark's JSON export)")


if __name__ == "__main__":
    main()
