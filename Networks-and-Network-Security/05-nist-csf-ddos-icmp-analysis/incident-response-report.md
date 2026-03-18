# Incident Response Report — NIST CSF Framework
## DDoS Attack via ICMP Flood

**Organization:** Multimedia Company (fictional scenario)
**Framework Applied:** NIST Cybersecurity Framework (CSF)
**Analyst:** Security Analyst Intern (Google Cybersecurity Certificate Program)
**Date:** 2024

---

## Incident Overview

A multimedia company that provides web design, graphic design, and social media marketing services experienced a **Distributed Denial of Service (DDoS) attack**. The attack used an **ICMP flood**, overwhelming the company's internal network with ping requests. All network services were disrupted for approximately **two hours** before the incident was resolved.

Investigation revealed that the attacker exploited an **unconfigured firewall** — ICMP packets were not being filtered, allowing the flood traffic to saturate the network.

---

## NIST CSF Response

The following response is structured using the five core functions of the NIST Cybersecurity Framework.

---

### 1. IDENTIFY

**Objective:** Understand the organization's systems, assets, and risks to determine what was affected.

**Actions Taken:**
- Audited the affected systems: internal network infrastructure, servers, and employee workstations
- Identified that all network services became non-responsive during the attack window
- Determined the attack vector: unconfigured firewall allowed unrestricted ICMP traffic inbound
- Identified the affected asset: the entire internal network segment, which had no ICMP rate-limiting or filtering rules

**Key Finding:** The firewall was present but misconfigured — no rules were in place to limit or block ICMP packets. This was a configuration gap, not a hardware or software failure.

---

### 2. PROTECT

**Objective:** Implement controls to limit or prevent the impact of future incidents.

**Controls Implemented / Recommended:**

| Control | Action |
|---------|--------|
| Firewall rule — ICMP rate limiting | Configure firewall to limit ICMP packet rate from any single source to prevent flood conditions |
| Firewall rule — block external ICMP | Block all incoming ICMP echo requests (ping) from external sources by default |
| Network access controls | Implement network segmentation to isolate critical systems from public-facing infrastructure |
| Employee training | Conduct security awareness training on identifying and reporting anomalous network behavior |
| Configuration management | Implement a firewall rule review process; all new rules must be documented and reviewed before deployment |

**Principle applied:** Defense in depth — multiple overlapping controls reduce reliance on any single point of protection.

---

### 3. DETECT

**Objective:** Implement capabilities to identify incidents quickly.

**Actions Taken / Recommended:**

| Tool/Process | Purpose |
|--------------|---------|
| IDS/IPS with ICMP anomaly rules | Deploy intrusion detection rules specifically targeting ICMP flood signatures |
| Network monitoring | Implement continuous network traffic monitoring with alerting on abnormal packet volumes |
| SIEM integration | Forward firewall and network logs to a SIEM for correlation and alerting |
| Baseline traffic analysis | Establish normal ICMP traffic baselines; alert when traffic deviates significantly |

**Detection Gap Identified:** During the incident, the attack went undetected for several minutes before users reported issues. No automated alerting was in place to flag the ICMP flood before it caused service disruption.

---

### 4. RESPOND

**Objective:** Contain the incident and minimize its impact.

**Immediate Response Actions (taken during incident):**
1. The cybersecurity team blocked incoming ICMP echo requests at the firewall
2. All non-critical network services were taken offline temporarily to reduce load
3. Critical network services were restored once the attack traffic was filtered
4. Network traffic was analyzed to confirm the attack vector and source characteristics

**Post-Incident Response:**
- Documented the attack timeline, source, method, and impact
- Reported the incident to senior management and affected stakeholders
- Preserved logs and evidence for forensic review
- Initiated a full firewall configuration audit

**Communication Plan:**
- Internal: Notify IT leadership and management within 1 hour of incident confirmation
- External: Assess whether customer data or services were impacted; notify customers if required

---

### 5. RECOVER

**Objective:** Restore affected systems and services to normal operations.

**Recovery Actions:**
1. Restored all network services once ICMP flood traffic was fully blocked
2. Verified system integrity — confirmed no data was exfiltrated or modified during the incident
3. Conducted a post-incident review with the cybersecurity team to identify lessons learned
4. Implemented permanent firewall rules to prevent recurrence

**Recovery Time:** Approximately 2 hours from incident onset to full service restoration.

**Lessons Learned:**
- Firewalls must be actively configured — a deployed but unconfigured firewall provides no protection
- Detection tooling is as important as prevention; the team needs automated alerting to respond faster
- Incident response playbooks should be created in advance so the team can act immediately without improvising

---

## Summary Table

| NIST Function | Status | Key Action |
|---------------|--------|------------|
| **Identify** | ✅ Complete | Identified unconfigured firewall as root cause |
| **Protect** | ✅ Implemented | ICMP rate limiting and block rules added to firewall |
| **Detect** | ⚠️ In Progress | IDS rules and SIEM alerting being deployed |
| **Respond** | ✅ Complete | Attack contained; firewall rules updated; incident documented |
| **Recover** | ✅ Complete | All services restored; post-incident review conducted |

---

## Conclusion

The DDoS attack exploited a fundamental configuration gap — the firewall was not configured to handle ICMP traffic. The immediate response was effective in restoring services, but the two-hour outage and lack of automated detection highlights the need for proactive controls.

Applying the NIST CSF across all five functions provides a structured approach that not only resolves the current incident but builds a stronger security foundation to prevent and detect future attacks more quickly.
