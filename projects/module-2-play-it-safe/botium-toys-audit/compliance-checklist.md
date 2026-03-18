# Compliance Checklist
## Botium Toys Internal Security Audit

**Purpose:** Assess Botium Toys' adherence to applicable regulatory and industry compliance frameworks.

**Legend:** ✅ Compliant | ❌ Not Compliant | ⚠️ Partially Compliant

---

## PCI DSS (Payment Card Industry Data Security Standard)

**Applies because:** Botium Toys accepts, processes, and stores customer credit/debit card information online and in-store.

| Requirement | Status | Finding |
|-------------|--------|---------|
| Only authorized users can access cardholder data | ❌ | All employees currently have access; no role-based restrictions |
| Credit card information is stored, accepted, processed, and transmitted in a secure environment | ❌ | No encryption in place for stored or transmitted card data |
| Implement data encryption for credit card transaction touchpoints | ❌ | Encryption not implemented |
| Adopt secure password management policies | ❌ | No password policy exists; no complexity requirements enforced |

**Overall PCI DSS Compliance Status: ❌ Non-Compliant**

---

## GDPR (General Data Protection Regulation)

**Applies because:** Botium Toys has customers located in the European Union. GDPR requires protection of EU residents' personal data regardless of where the business is based.

| Requirement | Status | Finding |
|-------------|--------|---------|
| EU customers' data is kept private/secured | ❌ | EU customer data is not encrypted or classified; access is unrestricted |
| There is a plan in place to notify EU customers within 72 hours if their data is compromised | ❌ | No incident response or breach notification plan exists |
| Ensure data is properly classified and inventoried | ⚠️ | Some data inventory exists but is not formalized or classified by sensitivity |
| Enforce privacy policies, procedures, and processes | ⚠️ | Privacy policies exist but are not consistently enforced |

**Overall GDPR Compliance Status: ⚠️ Partially Compliant — Significant Gaps**

---

## SOC 1 / SOC 2 (System and Organization Controls)

**Applies because:** Botium Toys stores and processes sensitive customer and financial data. SOC standards provide a framework for managing data security controls.

| Requirement | Status | Finding |
|-------------|--------|---------|
| User access policies are established | ❌ | No formal access control policy exists |
| Sensitive data (PII) is confidential | ❌ | PII not encrypted; not classified as confidential |
| Data integrity is ensured (accurate, complete, validated) | ❌ | No controls in place to validate data integrity |
| Data is available to individuals authorized to access it | ⚠️ | Data is accessible, but without authorization controls — too broadly available |

**Overall SOC Compliance Status: ❌ Non-Compliant**

---

## Compliance Summary

| Framework | Status | Priority |
|-----------|--------|----------|
| PCI DSS | ❌ Non-Compliant | Critical — risk of fines and card processing suspension |
| GDPR | ⚠️ Partially Compliant | High — risk of regulatory fines up to 4% of annual revenue |
| SOC 1 / SOC 2 | ❌ Non-Compliant | High — required for customer trust and enterprise contracts |

**Overall Assessment:** Botium Toys is not meeting its legal or industry obligations. Immediate remediation is required to avoid regulatory penalties and protect customer trust.
