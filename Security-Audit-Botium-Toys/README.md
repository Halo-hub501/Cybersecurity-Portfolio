# Botium Toys — Internal Security Audit
**Conducted by:** Olayinka Abimbowo
**Date:** March 2026
**Course:** Google Cybersecurity Professional Certificate — Module 2

---

## Scenario Summary

Botium Toys is a small US based toy company with a growing 
online presence. The IT manager initiated an internal security 
audit to identify risks, threats, and vulnerabilities to the 
company's assets and ensure compliance with regulations 
related to online payments and business operations in the EU.

---

## Controls Assessment Checklist

| Control | In Place? | Notes |
|---|---|---|
| Least Privilege | No | All employees have access to customer data — should be role based |
| Disaster Recovery Plans | No | No plans exist to ensure business continuity |
| Password Policies | No | Minimal requirements that do not meet current standards |
| Separation of Duties | No | CEO manages operations and payroll — conflict of interest |
| Firewall | Yes | Firewall is in place blocking traffic based on defined rules |
| Intrusion Detection System (IDS) | No | No IDS installed — threats could go undetected |
| Backups | No | No backups exist for critical data |
| Antivirus Software | Yes | Installed and monitored regularly |
| Legacy System Monitoring | No | Not monitored on a regular schedule |
| Encryption | No | No encryption protecting customer credit card data |
| Password Management System | No | No centralized password management system |
| Physical Locks | Yes | Adequate locks at physical location |
| CCTV Surveillance | Yes | Operational at physical location |
| Fire Detection | Yes | Fire detection and prevention systems in place |

---

## Compliance Checklist

### PCI DSS — Payment Card Industry Data Security Standard

| Best Practice | In Place? |
|---|---|
| Only authorized users have access to customer credit card data | No |
| Credit card data is stored in a secure environment | No |
| Encryption is implemented for credit card transactions | No |
| Secure password management policies are adopted | No |

### GDPR — General Data Protection Regulation

| Best Practice | In Place? |
|---|---|
| EU customer data is kept private and secure | No |
| A plan exists to notify EU customers within 72 hours of a breach | Yes |
| Data is properly classified and inventoried | No |
| Privacy policies are enforced among staff | Yes |

### SOC Type 1 and Type 2

| Best Practice | In Place? |
|---|---|
| User access policies are established | No |
| Sensitive data (PII) is kept confidential | No |
| Data integrity is consistent and validated | Yes |
| Data is available to authorized individuals | Yes |

---

## Recommendation To The IT Manager

Based on the internal security audit conducted for Botium Toys,
multiple critical controls are currently missing that present
significant risk to the organization.

**Most urgent priorities:**

1. Implement least privilege access controls immediately —
   no employee should have access to data beyond what their
   role requires.

2. Encrypt all customer credit card data to achieve PCI DSS
   compliance — failure to do so exposes the company to
   significant legal and financial liability.

3. Establish a disaster recovery plan and data backup
   system — without this, a single incident could shut
   down operations permanently.

4. Deploy an Intrusion Detection System (IDS) to monitor
   for threats in real time.

5. Implement a formal password policy and a centralized
   password management system to reduce credential risks.

Physical security controls including locks, CCTV, and fire
detection are adequate. The primary gaps are in digital
security controls and regulatory compliance, which should
be addressed as a matter of urgency.

---

## Self Assessment

| Statement | Yes/No |
|---|---|
| I selected Yes or No for each control in the checklist | Yes |
| I selected Yes or No for each compliance best practice | Yes |
| My answers are based on the Botium Toys scenario | Yes |
| I provided a recommendation for the IT manager | Yes |
| I reviewed my work against the audit scope and goals | Yes |

---

## What I Learned From This Activity

This audit taught me how to apply security controls assessment
in a real world business scenario. I learned that most
organizations have gaps between physical security and digital
security — Botium Toys had strong physical controls but
significant weaknesses in data protection and compliance.

The most important takeaway is that compliance frameworks like
PCI DSS and GDPR exist to protect both the customer and the
business. As a security analyst my job is to identify where
those gaps are and clearly communicate the risk to leadership
so informed decisions can be made.
