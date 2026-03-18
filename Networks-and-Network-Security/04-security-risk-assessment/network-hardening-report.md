# Network Hardening Analysis Report

**Scenario:** Social Media Organization — Post-Breach Security Assessment
**Analyst:** Security Analyst Intern (Google Cybersecurity Certificate Program)
**Date:** 2024

---

## 1. Situation Overview

A social media organization experienced a major data breach that compromised the personal information of millions of customers. During the investigation, four key vulnerabilities were identified that allowed the breach to occur and go undetected:

1. Employees sharing passwords
2. The admin password for the database was set to the default value
3. Firewalls had no rules configured to filter incoming and outgoing traffic
4. No multifactor authentication (MFA) was in place

This report provides an assessment of each vulnerability and recommends specific network hardening measures to prevent recurrence.

---

## 2. Identified Vulnerabilities & Recommendations

### Vulnerability 1: Employees Sharing Passwords

**Description:** Employees were sharing login credentials, which eliminates individual accountability and dramatically increases the risk of unauthorized access.

**Risk:** If one employee's credentials are compromised or misused, an attacker gains access under a legitimate identity, making detection difficult. Password sharing also violates the principle of least privilege.

**Recommendation:** Enforce a strict password policy prohibiting credential sharing. Implement a centralized Identity and Access Management (IAM) system to ensure each user has a unique account. Conduct security awareness training on password hygiene. Deploy a password manager to reduce the friction that leads employees to share credentials.

**Implementation Frequency:** One-time policy rollout + ongoing enforcement via technical controls (audit logs, account lockout policies).

---

### Vulnerability 2: Default Admin Password on Database

**Description:** The database admin account retained its default password, which is publicly known and trivial for attackers to exploit.

**Risk:** Default credentials are the first thing automated attack tools try. An attacker with network access to the database could gain full administrative control — reading, modifying, or deleting all stored data — with no special skill required.

**Recommendation:** Immediately change all default credentials across all systems and devices. Enforce a password policy requiring strong, unique passwords (minimum 16 characters, mixed case, numbers, symbols) for all admin accounts. Implement MFA for all database administrative access. Regularly audit admin accounts and remove any that are unused.

**Implementation Frequency:** Immediate one-time action for credential rotation; ongoing enforcement via password expiration policy (every 90 days for privileged accounts).

---

### Vulnerability 3: Firewall with No Traffic Rules Configured

**Description:** The organization's firewalls were deployed but had no rules configured to filter inbound or outbound network traffic.

**Risk:** Without firewall rules, the network has no perimeter defense. Any external traffic — including malicious traffic from known bad IPs, port scans, and exploit attempts — passes through unchecked. Similarly, outbound data exfiltration would not be blocked or flagged.

**Recommendation:** Configure firewall rules based on the principle of least access — block all traffic by default, then explicitly allow only what is required for business operations. Define rules for:
- Inbound: Allow only specific ports required for services (e.g., 443 for HTTPS, 22 for SSH from trusted IPs only)
- Outbound: Restrict traffic to known business destinations; block known malicious IP ranges
- Enable logging on all firewall rules to support incident investigation

Review and audit firewall rules on a regular schedule.

**Implementation Frequency:** Immediate configuration; quarterly review of rules; update whenever infrastructure changes.

---

### Vulnerability 4: No Multifactor Authentication (MFA)

**Description:** The organization relied solely on passwords for authentication across all systems — including administrative accounts and customer-facing portals.

**Risk:** Passwords alone are insufficient protection. Credential stuffing, phishing, and brute-force attacks can bypass single-factor authentication. Once a password is compromised, the attacker has full access.

**Recommendation:** Implement MFA organization-wide. Prioritize:
1. All administrative and privileged accounts (immediate)
2. All employee accounts (within 30 days)
3. Customer-facing login portals (within 60 days)

Use authenticator apps (TOTP) or hardware security keys (FIDO2/WebAuthn) rather than SMS-based MFA, which is susceptible to SIM-swapping attacks.

**Implementation Frequency:** One-time rollout; review MFA method strength annually as standards evolve.

---

## 3. Summary of Recommendations

| Vulnerability | Severity | Recommended Control | Timeline |
|---------------|----------|---------------------|----------|
| Password sharing | High | IAM system, security awareness training, password manager | 30 days |
| Default admin password | Critical | Immediate credential rotation, MFA on admin accounts | Immediate |
| No firewall rules | Critical | Configure deny-all + allow-list rules, enable logging | Immediate |
| No MFA | High | Deploy TOTP/FIDO2 MFA org-wide | 30–60 days |

---

## 4. Conclusion

The data breach was largely preventable. All four vulnerabilities represent foundational security failures — basic controls that are standard practice in any security-conscious organization. Implementing the above recommendations will significantly reduce the organization's attack surface and bring its security posture to an acceptable baseline.

Future hardening should include network segmentation, intrusion detection, and regular penetration testing to identify vulnerabilities before attackers do.
