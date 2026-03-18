# Controls Assessment Checklist
## Botium Toys Internal Security Audit

**Purpose:** Evaluate current controls in place and identify gaps across administrative, technical, and physical control categories.

**Legend:** ✅ In Place | ❌ Not in Place | ⚠️ Partial

---

## Administrative Controls

| Control | Status | Notes |
|---------|--------|-------|
| Least Privilege | ❌ | All employees have access to all internal data, including cardholder data |
| Disaster Recovery Plans | ❌ | No formal disaster recovery or business continuity plan exists |
| Password Policies | ❌ | No minimum password complexity requirements enforced |
| Separation of Duties | ❌ | No role-based access control; single users can perform conflicting actions |
| Access Control Policies | ❌ | No documented access control policy |
| Account Management Policies | ❌ | No formal account provisioning or de-provisioning process |

---

## Technical Controls

| Control | Status | Notes |
|---------|--------|-------|
| Firewall | ✅ | Firewall with defined security zones and rules is in place |
| Antivirus / Anti-malware | ❌ | No antivirus software currently installed on endpoints |
| Intrusion Detection System (IDS) | ❌ | No IDS in place to detect unauthorized access or anomalies |
| Encryption | ❌ | Customer credit card information and PII are not encrypted at rest or in transit |
| Backups | ❌ | No data backup procedures in place |
| Password Management System | ❌ | No centralized password management tool in use |
| Legacy System Monitoring | ⚠️ | Legacy systems exist and are monitored on an irregular schedule |

---

## Physical Controls

| Control | Status | Notes |
|---------|--------|-------|
| Time-Controlled Safe | ✅ | Used for securing high-value physical assets |
| Adequate Lighting | ✅ | Office and warehouse areas are adequately lit |
| Closed-Circuit Television (CCTV) | ✅ | CCTV surveillance is active in storefront and warehouse |
| Locking Cabinets (network gear) | ✅ | Network equipment is secured in locked racks |
| Signage on restricted areas | ✅ | Access restriction signs are posted |
| Fire Detection/Prevention | ✅ | Fire alarm and suppression systems are operational |
| Physical locks on doors | ✅ | Office and server room doors are locked |

---

## Summary

| Category | Controls in Place | Controls Missing |
|----------|-------------------|-----------------|
| Administrative | 0 / 6 | 6 |
| Technical | 1 / 7 | 5 (1 partial) |
| Physical | 7 / 7 | 0 |
| **Total** | **8 / 20** | **11 (1 partial)** |

**Key Takeaway:** Physical security is strong. Administrative and technical controls are critically lacking, particularly around data protection, access management, and incident readiness.
