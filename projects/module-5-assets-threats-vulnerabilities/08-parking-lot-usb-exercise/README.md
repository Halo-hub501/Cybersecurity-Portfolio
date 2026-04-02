# Parking Lot USB Exercise

**Course:** Assets, Threats, and Vulnerabilities (Course 5)
**Certificate:** Google Cybersecurity Professional Certificate
**Status:** Completed

---

## Project Description

In this activity, I assessed the attack vectors of a USB drive found in a hospital parking lot. I analyzed the contents of the device, considered how an attacker could exploit the information stored on it, and evaluated the risks of USB baiting attacks. The device was examined safely using virtualization software to avoid infecting live systems.

**Scenario:** A USB drive bearing the Rhetorical Hospital logo is found in the parking lot. The contents appear to belong to Jorge Bailey, the hospital's HR Manager.

---

## Contents

The USB drive contains a mix of personal and work-related files belonging to Jorge Bailey, the HR manager at Rhetorical Hospital. Personal files include family and pet photos, while work files include a new hire letter and an employee shift schedule. Storing personal and sensitive work files together on an unencrypted portable device puts both the individual and the organization at risk if the device is lost or stolen.

---

## Attacker Mindset

The work files on this device give a threat actor detailed intelligence about hospital staff — including names, roles, schedules, and newly hired employees who may be less security-aware and easier to manipulate. An attacker could use the HR records to craft convincing spear-phishing emails targeting Jorge, his family members, or new hires. The device itself may have been intentionally planted, with the hospital logo and real-looking files used as a distraction while malicious code executes silently in the background.

---

## Risk Analysis

USB baiting attacks can deliver malicious software such as ransomware, keyloggers, and remote access trojans (RATs) that execute automatically the moment a drive is plugged in. If an infected device had been found and plugged into a live workstation by another employee, it could have compromised the hospital's entire network — putting patient records, financial data, and staff PII at risk. To mitigate these attacks, the hospital should disable USB ports by default on all workstations and only allow approved, encrypted devices. Employees should also receive regular security awareness training on USB baiting and be required to report unknown devices to the security team rather than plug them in.

---

## Summary

This scenario demonstrates that a USB drive does not need to contain malware to be dangerous. The combination of PII, HR records, and personal files stored on an unencrypted device is enough to enable targeted attacks against Jorge, his relatives, or the entire organization. The safest response to finding an unknown USB drive is to never plug it in and report it immediately to the security team.
