# Access Controls Worksheet

**Course:** Assets, Threats, and Vulnerabilities (Course 5)
**Certificate:** Google Cybersecurity Professional Certificate
**Status:** Completed

---

## Project Description

In this activity, I investigated an unauthorized payroll transaction at a growing business. A deposit was made to an unknown bank account (FAUX_BANK), which the finance manager did not authorize. I reviewed the event log of the incident, cross-referenced it with the employee directory to identify the threat actor, identified access control issues that enabled the incident, and recommended mitigations to prevent similar events in the future.

---

## Supporting Materials

### Event Log (Accounting Exercise — Event Log Tab)

| Field | Value |
|-------|-------|
| Event Type | Information |
| Event Source | AdsmEmployeeService |
| Event Category | None |
| Event ID | 1227 |
| Date | 10/03/2023 |
| Time | 8:29:57 AM |
| User | Legal\Administrator |
| Computer | Up2-NoGud |
| IP Address | 152.207.255.255 |
| Description | Payroll event added. FAUX_BANK |

### Employee Directory (Accounting Exercise — Employee Directory Tab)

Cross-referencing the event log with the employee directory revealed that the **Legal\Administrator** account belongs to **Robert Taylor Jr.**, a contractor who worked in the legal department. His contract ended in **2019** — four years before this incident occurred in 2023. Despite his departure, his account remained active and retained access to the company's shared cloud drive, including payroll resources.

---

## Access Controls Worksheet

### Authorization / Authentication

| Column | Details |
|--------|---------|
| **Note(s)** | The event was triggered by the **Legal\Administrator** account on 10/03/2023 at 8:29:57 AM. This account belongs to **Robert Taylor Jr.**, a former contractor whose contract ended in 2019. The IP address **152.207.255.255** and computer name **Up2-NoGud** are associated with an external or unauthorized device — not a recognized internal workstation. |
| **Issue(s)** | 1. **Inactive account not deactivated** — Robert Taylor Jr.'s account remained active years after his contract ended, allowing him to authenticate and access company systems. 2. **Excessive access privileges** — The account had access to payroll and financial resources on the shared cloud drive, far beyond what a legal contractor's role requires. |
| **Recommendation(s)** | 1. **Implement formal offboarding procedures** — Establish a process to immediately deactivate user accounts and revoke access to all company resources when an employee or contractor leaves the organization. 2. **Apply the principle of least privilege** — Restrict access to sensitive resources (e.g., payroll, financials) based on job role. Only finance team members should have access to payroll systems. 3. **Enable multi-factor authentication (MFA)** — Require MFA for access to all sensitive resources so that a stolen or forgotten credential alone cannot be used to authenticate. |

---

## Notes

**Who caused this incident?**
Robert Taylor Jr. — a former legal department contractor whose account was not deactivated after his contract ended in 2019.

**When did it occur?**
10/03/2023 at 8:29:57 AM — approximately four years after the user's contract expired.

**What device was used?**
Computer: Up2-NoGud | IP: 152.207.255.255 — not a recognized internal device, suggesting external access.

---

## Issues Identified

1. **Account not deactivated after offboarding** — The contractor's system access was never revoked, leaving an open pathway into company resources for years after his departure.

2. **Overly broad access privileges** — All employees, including contractors, managed resources through a single shared cloud drive with insufficient role-based restrictions. A legal contractor should never have had access to payroll functionality.

---

## Recommendations

| # | Recommendation | Control Type |
|---|---------------|-------------|
| 1 | Establish a formal offboarding process to deactivate accounts and revoke access immediately when an employee or contractor leaves | Operational |
| 2 | Implement role-based access control (RBAC) — restrict payroll and financial resources to authorized finance team members only | Technical |
| 3 | Enable multi-factor authentication (MFA) on all systems that handle sensitive or financial data | Technical |

---

## Summary

This incident was caused by a failure to apply two fundamental access control principles. First, the company had no offboarding procedure — a contractor's account remained active for four years after his contract ended. Second, there were no role-based access restrictions — a legal contractor had access to payroll systems they had no business reason to use. Together, these gaps allowed an unauthorized user to add a fraudulent payroll entry to an external bank account. Implementing formal offboarding procedures, role-based access control, and multi-factor authentication would significantly reduce the likelihood of this type of incident recurring.
