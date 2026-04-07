# PASTA Threat Model — Sneaker Company App

**Course:** Assets, Threats, and Vulnerabilities (Course 5)
**Certificate:** Google Cybersecurity Professional Certificate
**Status:** Completed

---

## Project Description

In this activity, I applied the PASTA (Process of Attack Simulation and Threat Analysis) threat modeling framework to evaluate the security of a new mobile shopping app for a sneaker company. I worked through all seven PASTA stages — from defining business objectives to identifying threats, vulnerabilities, and security controls — to assess whether the app is safe to launch.

---

## Supporting Materials

### Data Flow Diagram

The data flow diagram shows a single process: a user searches for sneakers for sale, the request is handled by the product search process, which queries the database and returns listings of current inventory to the user.

```
User  ──────────────────────────────►  Product search  ──────────────────►  Database
      "Searching for sneakers for sale"     process       "Listings of current inventory"
      ◄──────────────────────────────                    ◄──────────────────
```

### Attack Tree

The attack tree shows two attack paths targeting user data:

```
                        User data
                       /          \
             SQL injection       Session hijacking
                  |                      |
        Lack of prepared           Weak login
           statements              credentials
```

---

## PASTA Worksheet

### Stage I — Define Business and Security Objectives

1. The app must allow users to easily sign up, log in, and manage their accounts while keeping their data private and secure.
2. Sales must be processed quickly and clearly, with multiple payment options — proper payment handling is critical to avoid legal issues.
3. Users must be able to message sellers directly and rate them, so the platform needs secure, reliable communication and data integrity.

---

### Stage II — Define Technical Scope

**Technologies used:** API, PKI (AES + RSA), SHA-256, SQL

**Priority technology — API:**

The application programming interface (API) is the most critical technology to evaluate first because it controls how all components of the app communicate — including user authentication, product searches, messaging, and payment processing. A vulnerability in the API could expose user data across every function of the application, making it the highest-risk attack surface.

---

### Stage III — Decompose Application

The data flow diagram illustrates how user data moves through the app. When a user searches for sneakers, the request is sent to the product search process, which queries the SQL database and returns a list of current inventory. This process involves user input that must be sanitized to prevent injection attacks, and data in transit that must be encrypted using the app's PKI framework.

*(See Data Flow Diagram above)*

---

### Stage IV — Threat Analysis

| # | Threat Type | Description |
|---|------------|-------------|
| 1 | **Internal** | A disgruntled employee or insider with database access could intentionally exfiltrate or manipulate sensitive user and payment data. |
| 2 | **External** | A malicious actor could conduct a SQL injection attack or session hijacking to steal user credentials, payment information, or personal data from the app. |

---

### Stage V — Vulnerability Analysis

| # | Vulnerability | Description |
|---|--------------|-------------|
| 1 | **Lack of prepared statements** | SQL queries that are not parameterized are vulnerable to injection attacks, allowing an attacker to manipulate the database directly through user input fields. |
| 2 | **Weak login credentials / broken authentication** | If the app does not enforce strong password policies or session management, attackers can exploit weak credentials to hijack user sessions and gain unauthorized access. |

---

### Stage VI — Attack Modeling

The attack tree identifies two main attack vectors targeting user data:

- **SQL injection** — exploited through a lack of prepared statements in the app's database queries
- **Session hijacking** — exploited through weak login credentials and poor session management

Both attack paths lead to unauthorized access to user data, including personal information and payment details.

*(See Attack Tree above)*

---

### Stage VII — Risk Analysis and Impact

| # | Security Control | Purpose |
|---|-----------------|---------|
| 1 | **Prepared statements (parameterized queries)** | Prevents SQL injection by separating SQL code from user input, ensuring malicious input cannot alter database queries |
| 2 | **Multi-factor authentication (MFA)** | Reduces the risk of session hijacking by requiring a second form of verification beyond just a password |
| 3 | **SHA-256 hashing** | Protects stored passwords and sensitive data by converting them into irreversible digests, so breached data cannot be directly used |
| 4 | **PKI encryption (AES + RSA)** | Secures data in transit using AES for sensitive data (e.g., credit card numbers) and RSA for key exchange — preventing interception of payment data |

---

## Summary

This PASTA threat model identified SQL injection and session hijacking as the two primary attack vectors threatening the sneaker company's mobile app. Both vulnerabilities stem from weaknesses in the app's database handling and authentication system. Implementing prepared statements, MFA, SHA-256 hashing, and end-to-end PKI encryption would significantly reduce the risk of a data breach before the app goes live.
