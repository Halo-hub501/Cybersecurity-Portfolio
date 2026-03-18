# Project: DNS and ICMP Traffic Analysis

**Module:** Connect and Protect — Networks and Network Security
**Type:** tcpdump Incident Report
**Status:** ✅ Completed

## Summary

Analyzed a tcpdump network traffic log to investigate why users were unable to access a company's website. Identified that the issue was caused by an unreachable DNS server — the UDP DNS requests were sending, but ICMP "port unreachable" error messages were being returned instead of DNS responses. Documented the findings in a structured two-part incident report.

## Document

See `dns-icmp-traffic-analysis-report.md` for the full report.

## Skills Demonstrated
- tcpdump log reading and interpretation
- DNS and ICMP protocol analysis
- Network incident identification and documentation
- Two-part incident report writing
