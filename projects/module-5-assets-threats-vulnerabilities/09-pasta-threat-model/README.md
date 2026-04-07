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

1. Users can create member profiles internally or by connecting external accounts.
2. The app must process financial transactions.
3. The app should be in compliance with PCI-DSS.

---

### Stage II — Define Technical Scope

**Technologies used:** API, PKI (AES + RSA), SHA-256, SQL

**Priority technology — API:**

APIs facilitate the exchange of data between customers, partners, and employees, so they should be prioritized. They handle a lot of sensitive data while they connect various users and systems together. However, details such as which APIs are being used should be considered before prioritizing one technology over another. So, they can be more prone to security vulnerabilities because there's a larger attack surface.

---

### Stage III — Decompose Application

The data flow diagram illustrates how user data moves through the app. When a user searches for sneakers, the request is sent to the product search process, which queries the SQL database and returns a list of current inventory. This process involves user input that must be sanitized to prevent injection attacks, and data in transit that must be encrypted using the app's PKI framework.

*(See Data Flow Diagram above)*

---

### Stage IV — Threat Analysis

| # | Threat Type | Description |
|---|------------|-------------|
| 1 | **Injection** | Injection attacks are common for SQL databases and can allow attackers to manipulate or extract data from the app's database through malicious input. |
| 2 | **Session hijacking** | Session hijacking is possible because the app communicates cookies between multiple layers, making it vulnerable to interception and unauthorized access. |

---

### Stage V — Vulnerability Analysis

| # | Vulnerability | Description |
|---|--------------|-------------|
| 1 | **Lack of prepared statements** | SQL queries that are not parameterized are vulnerable to injection attacks, allowing an attacker to manipulate the database directly through user input fields. |
| 2 | **Broken API token** | If API tokens are mishandled or improperly validated, session hijacking is possible when cookies are passed between input and output sources. |

---

### Stage VI — Attack Modeling

The attack tree identifies two main attack vectors targeting user data:

- **SQL injection** — exploited through a lack of prepared statements in the app's database queries
- **Session hijacking** — exploited through weak login credentials and poor session management

Both attack paths lead to unauthorized access to user data, including personal information and payment details.

*(See Attack Tree above)*

---

### Stage VII — Risk Analysis and Impact

| # | Security Control | Type |
|---|-----------------|------|
| 1 | **SHA-256** | Technical — hashes sensitive data like passwords and credit card numbers to protect stored information |
| 2 | **Incident response procedures** | Operational — ensures the team is prepared to detect, contain, and recover from security incidents quickly |
| 3 | **Password policy** | Managerial — enforces strong password requirements to reduce the risk of session hijacking through weak credentials |
| 4 | **Principle of least privilege** | Technical/Managerial — limits user and system access to only what is necessary, reducing the blast radius of any breach |

---

## Summary

This PASTA threat model identified SQL injection and session hijacking as the two primary attack vectors threatening the sneaker company's mobile app. Both vulnerabilities stem from weaknesses in the app's database handling and authentication system. Implementing prepared statements, MFA, SHA-256 hashing, and end-to-end PKI encryption would significantly reduce the risk of a data breach before the app goes live.
