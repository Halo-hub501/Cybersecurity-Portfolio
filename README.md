# Hi, I'm Olayinka 👋

**Aspiring Cybersecurity Analyst | Google Cybersecurity Certificate (In Progress) | Based in Canada**

I'm transitioning into cybersecurity with a focus on becoming a **Tier 1 SOC Analyst**. I'm building hands-on skills through the Google Cybersecurity Professional Certificate and documenting real project work here as I go.

- 🔗 [LinkedIn](https://www.linkedin.com/in/olayinka-abimbowo-b3369b2b0)
- 📁 [GitHub](https://github.com/Halo-hub501)

---

## 🎯 Career Goal

Secure a **Junior Cybersecurity Analyst** or **Tier 1 SOC Analyst** role where I can apply my growing skills in threat detection, incident response, and network security to protect organizations and their data.

---

## 📚 Google Cybersecurity Certificate — My Journey

| # | Module | Status | Projects |
|---|--------|--------|---------|
| 1 | Foundations of Cybersecurity | ✅ Completed | [Professional Statement](projects/module-1-foundations/professional-statement/) |
| 2 | Play It Safe: Manage Security Risks | ✅ Completed | [Botium Toys Security Audit](projects/module-2-play-it-safe/botium-toys-audit/) |
| 3 | Connect and Protect: Networks & Network Security | ✅ Completed | [5 Network Security Projects](projects/module-3-networks/) |
| 4 | Tools of the Trade: Linux and SQL | ✅ Completed | [13 Linux & SQL Labs](projects/module-4-linux-sql/) |
| 5 | Assets, Threats, and Vulnerabilities | ✅ Completed | [9 Labs](projects/module-5-assets-threats-vulnerabilities/) |
| 6 | Sound the Alarm: Detection and Response | ⬜ Upcoming | — |
| 7 | Automate Cybersecurity Tasks with Python | ⬜ Upcoming | — |
| 8 | Put It to Work: Prepare for Cybersecurity Jobs | ⬜ Upcoming | — |

---

## 🗂️ Projects

### Module 1 — Foundations of Cybersecurity
**[Professional Statement](projects/module-1-foundations/professional-statement/)**
Drafted a professional statement communicating my strengths, values, and career goals in cybersecurity — designed to introduce myself to potential employers.

---

### Module 2 — Play It Safe: Manage Security Risks
**[Botium Toys Internal Security Audit](projects/module-2-play-it-safe/botium-toys-audit/)**
Conducted a full internal security audit for a fictional toy company expanding its online presence. Assessed administrative, technical, and physical controls; identified PCI DSS, GDPR, and SOC compliance gaps; delivered prioritized remediation recommendations.
- Controls checklist (20 controls evaluated)
- Compliance gap analysis (PCI DSS, GDPR, SOC 1/2)
- Prioritized remediation roadmap

---

### Module 3 — Connect and Protect: Networks & Network Security

**[1. DNS and ICMP Traffic Analysis](projects/module-3-networks/01-dns-icmp-traffic-analysis/)**
Analyzed a tcpdump log to investigate a website outage. Identified that the DNS server's port 53 was returning ICMP "unreachable" errors, blocking all DNS resolution.

**[2. SYN Flood Attack Analysis](projects/module-3-networks/02-syn-flood-attack-analysis/)**
Analyzed a Wireshark TCP log to identify a SYN flood DoS attack against a travel agency's web server. Explained the TCP handshake exploitation and recommended mitigations.

**[3. Brute Force and Malware Injection](projects/module-3-networks/03-brute-force-malware-injection/)**
Investigated a two-stage attack: a former employee brute-forced the admin login, then injected malware into the website that redirected visitors to a fake site and delivered trojan downloads.

**[4. Security Risk Assessment](projects/module-3-networks/04-security-risk-assessment/)**
Post-breach network assessment for a social media organization. Identified four critical vulnerabilities (no MFA, no firewall rules, password sharing, default credentials) and provided hardening recommendations.

**[5. NIST CSF Incident Report — DDoS ICMP Flood](projects/module-3-networks/05-nist-csf-ddos-icmp-analysis/)**
Applied all five NIST CSF functions (Identify, Protect, Detect, Respond, Recover) to a DDoS/ICMP flood attack on a multimedia company.

---

### Module 4 — Tools of the Trade: Linux and SQL
**Certificate:** [Tools of the Trade: Linux and SQL — Mar 27, 2026](https://coursera.org/verify/MWB4N40G0FWE)

**[1. Install Software in a Linux Distribution](projects/module-4-linux-sql/01-install-software-linux/)**
Used the APT package manager to install, uninstall, and verify software in a Debian-based Linux environment. Managed the full lifecycle of Suricata and tcpdump — two tools directly used in security monitoring and network analysis.

**[2. Examine Input/Output in the Linux Shell](projects/module-4-linux-sql/02-examine-input-output-linux-shell/)**
Used `echo` and `expr` in the Bash shell to generate output and perform integer calculations. Applied the `expr` command to a realistic analyst scenario: calculating total annual login attempts from monthly averages (3,500/month × 12 = 42,000/year).

**[3. Find Files with Linux Commands](projects/module-4-linux-sql/03-find-files-linux-commands/)**
Navigated the Linux Filesystem Hierarchy Standard using `pwd`, `ls`, `cd`, `cat`, and `head`. Located and read employee user records from a structured data file, and analyzed a server log to identify 3 warning messages within the first 10 lines.

**[4. Filter with grep](projects/module-4-linux-sql/04-filter-with-grep/)**
Used `grep` and piping (`|`) to search log files and user data files for specific strings. Identified 6 error entries in a server log, filtered file listings by name pattern, and located a deleted user and HR additions across quarterly user reports.

**[5. Manage Files with Linux Commands](projects/module-4-linux-sql/05-manage-files-linux-commands/)**
Organized the `/home/analyst` directory by creating a `logs` subdirectory, removing the `temp` directory, moving `Q3patches.txt` to `reports`, deleting an unused file, creating a new `tasks.txt` file, and editing it with the nano text editor.

**[6. Manage Authorization with Linux](projects/module-4-linux-sql/06-manage-authorization/)**
Used `chmod` to manage file and directory permissions in Linux. Identified and removed unauthorized write access, removed read access for others, and applied recursive permission changes — all using the symbolic and numeric permission system.

**[7. Add and Manage Users in Linux](projects/module-4-linux-sql/07-add-manage-users-linux/)**
Used `useradd`, `usermod`, `chown`, `userdel`, and `groupdel` to manage user accounts. Added a new researcher, changed file ownership, assigned a supplementary group, and deleted both a user and their group at the end of a contract.

**[8. Get Help in the Command Line](projects/module-4-linux-sql/08-get-help-command-line/)**
Used `man`, `whatis`, and `apropos` to find information about Linux commands without leaving the terminal. Identified the `-e` flag for setting account expiration dates and found the `groupadd` command using keyword search.

**[9. Basic SQL Queries](projects/module-4-linux-sql/09-basic-sql-queries/)**
Used `SELECT`, `FROM`, and `ORDER BY` to retrieve and sort data from the `machines` and `log_in_attempts` tables. Practiced ordering results by single and multiple columns to surface meaningful patterns in security data.

**[10. SQL Filters with WHERE and LIKE](projects/module-4-linux-sql/10-sql-filters-where-like/)**
Applied `WHERE` and `LIKE` with the `%` wildcard to filter records by operating system, department, and office building. Retrieved targeted subsets of employee and machine data to support a security update operation.

**[11. SQL Filters with Numbers and Dates](projects/module-4-linux-sql/11-sql-filters-numbers-dates/)**
Used comparison operators (`>`, `>=`, `<`, `<=`) and `BETWEEN` to filter login attempts by date and time ranges, and events by ID. Identified after-hours activity and narrowed investigation windows using precise date/time filtering.

**[12. Apply Filters to SQL Queries — AND, OR, NOT](projects/module-4-linux-sql/12-sql-filters-and-or-not/)**
Applied `AND`, `OR`, and `NOT` operators to combine multiple filter conditions across the `log_in_attempts` and `employees` tables. Identified failed after-hours logins, logins outside Mexico, and employees in specific departments needing security updates.

**[13. SQL Joins](projects/module-4-linux-sql/13-sql-joins/)**
Used `INNER JOIN`, `LEFT JOIN`, and `RIGHT JOIN` to combine data from the `machines`, `employees`, and `log_in_attempts` tables. Matched employees to their machines and retrieved all login attempt records for active employees during a security investigation.

---

### Module 5 — Assets, Threats, and Vulnerabilities

**[1. Home Asset Inventory](projects/module-5-assets-threats-vulnerabilities/01-home-asset-inventory/)**
Created a home office network asset inventory by identifying devices connected to the network, documenting ownership, location, and network access characteristics, and classifying each device by sensitivity level (Restricted, Confidential, Internal-only). Applied the CIA triad to evaluate risk for each asset.

**[2. Risk Register](projects/module-5-assets-threats-vulnerabilities/02-risk-register/)**
Conducted a risk assessment for a commercial bank by evaluating five vulnerabilities. Scored each risk by likelihood and severity, calculated priority scores (Likelihood x Severity), and ranked threats from critical to low — identifying a publicly accessible backup server as the highest-priority risk.

**[3. Data Leak Worksheet](projects/module-5-assets-threats-vulnerabilities/03-data-leak-worksheet/)**
Analyzed a data leak incident caused by overly broad folder access. Reviewed NIST SP 800-53: AC-6 (Least Privilege), identified the contributing factors, and recommended role-based access restrictions and regular privilege audits to prevent recurrence.

**[4. Decrypt an Encrypted Message](projects/module-5-assets-threats-vulnerabilities/04-decrypt-encrypted-message/)**
Used Linux Bash commands to decrypt an encrypted file. Found a hidden file containing a Caesar cipher, decoded it using the `tr` command, then decrypted an AES-256-CBC encrypted file using `openssl`. Demonstrated practical skills in filesystem navigation, classical cipher decryption, and symmetric encryption.

**[5. Generate and Compare Hashes](projects/module-5-assets-threats-vulnerabilities/05-generate-compare-hashes/)**
Used `sha256sum` to generate cryptographic hashes for two files that appeared visually identical but produced different hash values. Wrote hashes to separate files and used `cmp` to confirm the difference byte by byte — demonstrating how hashing verifies data integrity.

**[6. Access Controls Worksheet](projects/module-5-assets-threats-vulnerabilities/06-access-controls-worksheet/)**
Investigated an unauthorized payroll transaction by reviewing an event log and cross-referencing it with an employee directory. Identified that a former contractor's account was never deactivated and had excessive access to payroll systems. Recommended offboarding procedures, role-based access control (RBAC), and multi-factor authentication (MFA) as mitigations.

**[7. Vulnerability Assessment Report](projects/module-5-assets-threats-vulnerabilities/07-vulnerability-assessment-report/)**
Conducted a vulnerability assessment for an e-commerce company's publicly accessible remote database server using NIST SP 800-30 Rev. 1. Identified three threat sources (hacker, competitor, employee), scored risk using likelihood × severity, and proposed remediation including AAA controls, MFA, IP allow-listing, TLS encryption, and RBAC.

**[8. Parking Lot USB Exercise](projects/module-5-assets-threats-vulnerabilities/08-parking-lot-usb-exercise/)**
Assessed the attack vectors of a USB drive found in a hospital parking lot. Analyzed contents containing PII and HR records, considered how the information could be used against the owner and organization, and recommended managerial, operational, and technical controls including employee awareness training, antivirus scans, and disabling AutoPlay.

**[9. PASTA Threat Model](projects/module-5-assets-threats-vulnerabilities/09-pasta-threat-model/)**
Applied the PASTA (Process of Attack Simulation and Threat Analysis) framework to evaluate a new sneaker company mobile app across all seven stages. Identified SQL injection and session hijacking as primary threats, with vulnerabilities in prepared statements and authentication. Recommended MFA, parameterized queries, SHA-256 hashing, and PKI encryption as controls.

---

## 🛠️ Tools & Technologies

### Network Analysis
![Wireshark](https://img.shields.io/badge/-Wireshark-1679A7?&style=for-the-badge&logo=Wireshark&logoColor=white)
![Suricata](https://img.shields.io/badge/-Suricata-EF3B2D?&style=for-the-badge&logo=Suricata&logoColor=white)

### SIEM
![Splunk](https://img.shields.io/badge/-Splunk-000000?&style=for-the-badge&logo=Splunk&logoColor=white)
![Chronicle](https://img.shields.io/badge/-Google_Chronicle-4285F4?&style=for-the-badge&logo=Google&logoColor=white)

### Operating Systems & Shell
![Linux](https://img.shields.io/badge/-Linux-FCC624?&style=for-the-badge&logo=Linux&logoColor=black)

### Languages (In Development)
![Python](https://img.shields.io/badge/-Python-3776AB?&style=for-the-badge&logo=Python&logoColor=white)
![SQL](https://img.shields.io/badge/-SQL-4479A1?&style=for-the-badge&logo=MySQL&logoColor=white)

### Frameworks
- NIST Cybersecurity Framework (CSF) — all 5 functions
- CIA Triad (Confidentiality, Integrity, Availability)
- PCI DSS, GDPR, SOC 1/2 compliance

---

## 📜 Certifications

### Google Cybersecurity Professional Certificate — Course Completions

| # | Course | Completed | Verify |
|---|--------|-----------|--------|
| 1 | Foundations of Cybersecurity | Mar 9, 2026 | [Verify](https://coursera.org/verify/M6YX7WL9BDAB) |
| 2 | Play It Safe: Manage Security Risks | Mar 10, 2026 | [Verify](https://coursera.org/verify/7HQ8W6WYSQC9) |
| 3 | Connect and Protect: Networks and Network Security | Mar 17, 2026 | [Verify](https://coursera.org/verify/D6PKZARZOAAP) |
| 4 | Tools of the Trade: Linux and SQL | Mar 27, 2026 | [Verify](https://coursera.org/verify/MWB4N40G0FWE) |
| 5 | Assets, Threats, and Vulnerabilities | ✅ Completed | [9 Labs](projects/module-5-assets-threats-vulnerabilities/) |
| 6 | Sound the Alarm: Detection and Response | ⬜ Upcoming | — |
| 7 | Automate Cybersecurity Tasks with Python | ⬜ Upcoming | — |
| 8 | Put It to Work: Prepare for Cybersecurity Jobs | ⬜ Upcoming | — |

### Other Certifications

| Certification | Status |
|---------------|--------|
| CompTIA Security+ | ⬜ Planned |

---

## 📫 Let's Connect

I'm actively looking for entry-level cybersecurity opportunities and open to connecting with security professionals.

- 📍 Canada
- 💼 Open to: Junior SOC Analyst, Security Analyst Intern, IT Security roles
- 🔗 [LinkedIn](https://www.linkedin.com/in/olayinka-abimbowo-b3369b2b0)

---

*This portfolio is a living document — updated as I complete each module of the Google Cybersecurity Certificate.*
