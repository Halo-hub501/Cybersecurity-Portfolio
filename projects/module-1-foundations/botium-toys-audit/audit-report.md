# Internal Security Audit Report
## Botium Toys

**Date:** 2024
**Prepared by:** Security Analyst Intern (Google Cybersecurity Certificate Program)
**Classification:** Internal Use Only

---

## 1. Executive Summary

Botium Toys engaged its IT department to conduct a comprehensive internal security audit in response to business growth and increasing regulatory requirements. The company processes customer payment card data and holds personal data of EU customers, making PCI DSS and GDPR compliance critical.

The audit identified **significant gaps** in both technical controls and compliance practices. The overall risk score is rated **8 out of 10** — high risk — primarily due to the absence of encryption for sensitive data, lack of access controls, and no formal incident response or disaster recovery plan.

**Immediate action is required** to protect customer data, avoid regulatory penalties, and maintain business continuity.

---

## 2. Scope

**In Scope:**
- All Botium Toys assets, including on-premises equipment, employee devices, internal networks, and systems
- Storefront products (on-site and online)
- Stored customer data (PII, payment card information)
- Accounting, telecommunications, database, security, e-commerce, and inventory management systems

**Out of Scope:**
- Third-party vendor systems
- Physical storefronts outside the main office

---

## 3. Goals

1. Adhere to the NIST CSF
2. Establish a better process for systems to ensure they are compliant
3. Fortify system controls
4. Implement the concept of least permissions where applicable
5. Establish policies and procedures (including playbooks)
6. Ensure compliance requirements are met

---

## 4. Current Assets

The IT department manages the following assets:

- On-premises equipment for in-office business needs
- Employee equipment: end-user devices (desktops, laptops, smartphones), remote workstations, headsets, cables, keyboards, docking stations, surveillance cameras
- Storefront products in the company's adjoining warehouse, available for retail sale or online orders
- Systems, software, and services: accounting, telecommunication, database, security, e-commerce, and inventory management
- Internet access
- Internal network
- Data retention and storage systems
- Legacy system maintenance: end-of-life systems that require human monitoring

---

## 5. Risk Assessment

### Risk Score: **8 / 10 (High)**

### Risk Description

The risk of fines and data loss is high due to inadequate management of assets. Additionally, the company does not have all necessary controls in place and is not fully compliant with U.S. and international regulations and standards.

### Contributing Risk Factors

| Risk Factor | Detail |
|-------------|--------|
| No encryption | Customer credit card data and PII stored and transmitted in plaintext |
| No access controls | All employees have access to internally stored data, including cardholder data |
| No IDS/IPS | No intrusion detection system in place to identify potential threats |
| No disaster recovery plan | No formal plan to recover from a data breach or system failure |
| No password policy | No minimum password requirements enforced |
| No separation of duties | Single employees have full access across multiple sensitive systems |
| Legacy systems | End-of-life systems monitored on irregular schedule |

---

## 6. Findings Summary

### Critical Findings (Immediate Action Required)

- **No encryption** for stored or transmitted customer PII and payment card data
- **No access controls / least privilege** — all employees have unrestricted access to sensitive data
- **No intrusion detection system (IDS)** to monitor for threats
- **No disaster recovery plan** or data backup procedures
- **No incident response plan or playbooks**

### High Findings (Action Required Soon)

- No separation of duties for sensitive transactions
- No centralized password management
- No formal security policies documented

### Medium Findings (Plan and Address)

- Legacy systems monitored inconsistently — requires formalized schedule
- No antivirus software on all endpoints
- Firewall rules exist but have not been reviewed recently

### Informational

- Physical locks and CCTV are in place — physical security is adequate
- Fire detection and prevention systems are in place

---

## 7. Compliance Gaps

| Standard | Compliant | Key Gaps |
|----------|-----------|----------|
| PCI DSS | No | No encryption, all employees can access cardholder data, no secure password policies |
| GDPR | Partial | EU customer data not properly classified or protected; no breach notification plan |
| SOC 1 / SOC 2 | No | No access controls, no data integrity policies, no availability plan |

---

## 8. Conclusion

Botium Toys faces substantial security and compliance risk. Without immediate remediation, the company is exposed to data breaches, regulatory fines, and reputational damage. The prioritized recommendations in `recommendations.md` provide a roadmap for addressing these gaps systematically.
