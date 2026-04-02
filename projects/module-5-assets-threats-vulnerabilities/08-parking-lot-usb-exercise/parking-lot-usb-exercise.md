# Parking Lot USB Exercise

**Course:** Google Cybersecurity Certificate — Module 5: Assets, Threats & Vulnerabilities  
**Scenario:** A USB drive bearing the Rhetorical Hospital logo is found in the parking lot. The device is examined safely inside a virtual environment (no live network connection). The contents appear to belong to Jorge Bailey, the hospital's HR Manager.

---

## Contents

The USB drive contains a mix of personal and work-related files belonging to Jorge Bailey, HR Manager at Rhetorical Hospital. Personal files include family and pet photos. Work files include a new hire letter and an employee shift schedule — both of which contain personally identifiable information (PII) about current and incoming staff.

**Key questions:**
- **Are there files that can contain PII?** Yes — the new hire letter and shift schedule contain employee names, roles, and likely contact details.
- **Are there sensitive work files?** Yes — HR documents such as new hire letters and shift schedules are confidential internal records.
- **Is it safe to store personal files with work files?** No — mixing personal and work files on the same device increases the risk of data exposure if the device is lost, stolen, or compromised.

---

## Attacker Mindset

The personal and HR files on this device give a threat actor detailed intelligence about Rhetorical Hospital's staff — names, roles, schedules, and new hires. This information could be used to craft convincing spear-phishing emails targeting Jorge, his family members, or newly hired employees who are less security-aware. The device itself may have been planted intentionally: an attacker could have loaded it with malware and placed it where a curious employee would find it, using the hospital logo and real-looking files as a distraction while malicious code executes in the background.

**Key questions:**
- **Could the information be used against other employees?** Yes — the shift schedule exposes coworker names and working hours, enabling targeted social engineering.
- **Could the information be used against relatives?** Yes — personal photos may reveal family members' identities, which could be leveraged in extortion or social engineering attacks.
- **Could the information provide access to the business?** Yes — HR credentials and internal documents could be used to impersonate Jorge or manipulate new hires into disclosing access credentials.

---

## Risk Analysis

USB baiting attacks can deliver a wide range of malicious software including keyloggers, ransomware, remote access trojans (RATs), and firmware-level attacks — some of which activate the moment the drive is plugged in, before any file is opened. If an infected device had been found and plugged in by another employee on a live workstation, it could have silently established a backdoor into the hospital's network, potentially compromising patient records, financial systems, and staff PII at scale.

Even without malware, the sensitive HR files on this drive give a threat actor enough information to conduct spear-phishing campaigns, impersonate employees, or manipulate new hires who may not yet know security protocols.

**Recommended controls:**

| Type | Control |
|------|---------|
| Technical | Disable USB ports by default on all workstations via endpoint management (e.g., Group Policy); only allow approved, encrypted devices |
| Technical | Deploy endpoint detection & response (EDR) software to flag unknown USB connections |
| Operational | Establish a clear policy: unknown USB drives must be handed to the security team — never plugged in |
| Operational | Use virtualization or an air-gapped machine (as done here) whenever USB investigation is necessary |
| Managerial | Conduct regular security awareness training on USB baiting and social engineering tactics |
| Managerial | Enforce a policy separating personal and work storage devices entirely |

---

## Key Takeaway

This scenario illustrates that a USB drive does not need to contain malware to be dangerous. The combination of PII, HR records, and personal files alone is enough to enable targeted attacks against an individual, their family, or the entire organization. The safest response upon finding an unknown USB drive is to **not plug it in** and report it immediately to the security team.
