# DNS and ICMP Traffic Analysis — Incident Report

**Report Type:** tcpdump Network Traffic Analysis
**Analyst:** Security Analyst Intern (Google Cybersecurity Certificate Program)
**Date:** 2024

---

## Part 1: Summary of the Problem

### Situation

Customers reported they were unable to access the website `yummyrecipesforme.com`. Upon investigation, the cybersecurity team used the network protocol analyzer **tcpdump** to capture and analyze network traffic while attempting to replicate the issue.

### What the tcpdump Log Revealed

The log captured the following sequence of events:

1. The browser sent a **UDP packet** to the DNS server (port 53) requesting to resolve the domain name `yummyrecipesforme.com` to an IP address
2. The DNS server did **not respond** with the expected DNS reply
3. Instead, the DNS server returned an **ICMP error message**: `udp port 53 unreachable`
4. This cycle repeated — the browser retried the DNS request multiple times, and each attempt received the same ICMP error

### Root Cause Identified

The ICMP message `udp port 53 unreachable` indicates that **the DNS server's port 53 was not accessible**. This could mean:
- The DNS server was offline or unresponsive
- A firewall rule was blocking UDP traffic on port 53
- The DNS service had crashed or been stopped

Because DNS resolution failed, the browser could not determine the IP address of the website, making the site completely inaccessible — even though the web server itself may have been functioning normally.

---

## Part 2: Analysis of the Data and Cause

### Protocol Breakdown

| Protocol | Layer | Role in This Incident |
|----------|-------|----------------------|
| **DNS** (UDP port 53) | Application | Used to resolve the domain name to an IP address — failed |
| **UDP** | Transport | Carries DNS requests — connectionless, no error recovery |
| **ICMP** | Network | Returned error message indicating port 53 was unreachable |

### Why UDP Makes This Harder to Detect

DNS uses **UDP** (User Datagram Protocol) rather than TCP. UDP is connectionless — it does not establish a session or automatically retry on failure. This means:
- The client sends a request and simply waits for a reply
- If the DNS server is unreachable, the client gets an ICMP error instead
- Without proper monitoring, this failure can look like a simple timeout rather than a service disruption

### tcpdump Log Interpretation

The key lines from the captured traffic showed:
- **Outbound:** `client.ip.35084 > 203.0.113.2.domain: 35084+ A? yummyrecipesforme.com` — browser requesting DNS resolution via UDP
- **Inbound:** `203.0.113.2 > client.ip: ICMP 203.0.113.2 udp port 53 unreachable` — DNS server rejecting the request

The repeated pattern of request → ICMP error confirms this was a consistent failure, not an intermittent glitch.

---

## Recommended Next Steps

| Action | Purpose |
|--------|---------|
| Verify DNS server status | Confirm whether the DNS service is running on port 53 |
| Check firewall rules | Ensure port 53 UDP/TCP is not being blocked by a recent rule change |
| Test alternate DNS server | Temporarily point clients to a backup DNS (e.g., 8.8.8.8) to restore access |
| Review server logs | Check DNS server logs for crash reports, errors, or unauthorized changes |
| Implement DNS redundancy | Configure a secondary DNS server to prevent single point of failure |

---

## Conclusion

The website outage was caused by **DNS service failure** — specifically, the DNS server's port 53 was unreachable, causing all DNS lookups to fail. Users could not access the website because their browsers could not resolve the domain name to an IP address.

This incident highlights the importance of monitoring DNS infrastructure and having redundant DNS servers. A secondary DNS server would have allowed automatic failover, preventing the outage entirely.
