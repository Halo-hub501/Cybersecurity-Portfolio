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
| **Note(s)** | - The event took place on 10/03/23. - The user is Legal/Administrator. - The IP address of the computer used to login is 152.207.255.255. |
| **Issue(s)** | - Robert Taylor Jr. is a contractor with admin access. - His contract ended in 2019, but his account accessed payroll systems in 2023. |
| **Recommendation(s)** | - User accounts should expire after 30 days. - Contractors should have limited access to business resources. - Enable multi-factor authentication (MFA). |

---

## Notes

- The event took place on 10/03/23.
- The user is Legal/Administrator.
- The IP address of the computer used to login is 152.207.255.255.

---

## Issues Identified

- Robert Taylor Jr. is a contractor with admin access.
- His contract ended in 2019, but his account accessed payroll systems in 2023.

---

## Recommendations

- User accounts should expire after 30 days.
- Contractors should have limited access to business resources.
- Enable multi-factor authentication (MFA).

---

## Summary

This incident was caused by a failure to apply two fundamental access control principles. First, the company had no offboarding procedure — a contractor's account remained active for four years after his contract ended. Second, there were no role-based access restrictions — a legal contractor had access to payroll systems they had no business reason to use. Together, these gaps allowed an unauthorized user to add a fraudulent payroll entry to an external bank account. Implementing formal offboarding procedures, role-based access control, and multi-factor authentication would significantly reduce the likelihood of this type of incident recurring.
