# Wireshark SOC Analysis — Tier 1 Alert Triage System

Real-world incident response simulation analyzing actual malware traffic captured with Wireshark.

## Overview

This project demonstrates a complete **Tier 1 SOC workflow**: capturing network traffic with Wireshark, extracting security indicators, triaging alerts, and automating incident response.

## What's Inside

### 📦 Analysis Files

- **`dashboard.html`** — Interactive web dashboard showing detected threats and response actions (open in browser)
- **`incidents.json`** — Triaged security incidents extracted from PCAP analysis
- **`pcap_alerts.json`** — Raw security alerts extracted from network traffic
- **`audit_log.json`** — Complete forensic log of all automated responses

### 🛠️ Tools

- **`tools/parse_pcap.py`** — PCAP parser that extracts security indicators (IoCs) from network traffic
- **`tools/triage_alerts.py`** — Alert triage engine (deduplicates, correlates, responds)
- **`tools/generate_dashboard.py`** — Generates the interactive HTML dashboard
- **`tools/generate_alerts.py`** — Simulates alerts for testing

### 📋 Workflows

- **`workflows/alert_triage_soc.md`** — Complete SOC SOP documenting triage, correlation, and response playbooks

## The Real Data

**Source:** malware-traffic-analysis.net (public security training resource)
- **Files:** 147 MB PCAP (15,512 packets of actual malware traffic)
- **Malware:** NetSupport Manager RAT
- **Scenario:** Internal host compromised, executing reconnaissance against corporate network

## Detected Threats

| Threat | Severity | Detection | Response |
|--------|----------|-----------|----------|
| CLDAP Reconnaissance | HIGH | Active Directory probing detected | Block source IP, escalate to Tier 2 |
| Network Scanning | MEDIUM | Port scanning activity observed | Monitor, increase monitoring |

## How to Use

### View the Analysis
1. Open **`dashboard.html`** in your web browser to see:
   - All detected incidents
   - Severity breakdown
   - Automated response actions executed
   - Full incident lifecycle

### Examine the Data
- **`incidents.json`** — Structured incident data with correlations
- **`audit_log.json`** — Forensic record showing every automated action
- **`pcap_alerts.json`** — Raw extracted indicators

### Run the Full Pipeline
```bash
python tools/parse_pcap.py          # Extract alerts from PCAP
python tools/triage_alerts.py       # Triage and auto-respond
python tools/generate_dashboard.py  # Generate dashboard
```

## Skills Demonstrated

✅ **Network Analysis** — PCAP inspection and packet-level forensics
✅ **Threat Detection** — Identifying malicious patterns in captured traffic
✅ **Incident Correlation** — Grouping related alerts into meaningful incidents
✅ **Alert Triage** — Deduplication and severity assignment
✅ **Security Automation** — Python-based response playbook execution
✅ **Forensic Investigation** — Complete audit trail maintenance
✅ **Real-world Data** — Analysis of actual captured malware activity

## Interview Talking Points

*"I built a Tier 1 SOC alert triage system that processes real malware traffic captured with Wireshark. My system extracts security indicators from 15,000+ packets of actual malware traffic, correlates related events into incidents, and automatically executes response playbooks. From the PCAP, I detected active directory reconnaissance and network probing—demonstrating my ability to identify threat patterns in real network data. The entire workflow—detection, triage, response, and logging—is fully automated and documented, showing both my understanding of SOC operations and my ability to implement security automation in Python."*

---

**Status:** Complete | **Real Data Used:** Yes | **Last Updated:** April 21, 2026
