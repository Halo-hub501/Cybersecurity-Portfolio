# Home Asset Inventory

**Course:** Assets, Threats, and Vulnerabilities (Course 5)
**Certificate:** Google Cybersecurity Professional Certificate
**Status:** Completed

---

## Project Description

Asset management is a critical part of every organization's security plan. In this activity, I created a home office network asset inventory by identifying devices connected to the network, documenting their characteristics, and classifying each device based on its sensitivity level. This process mirrors how security analysts track and protect organizational assets in real-world environments.

---

## Asset Inventory

| # | Asset | Network Access | Owner | Location | Notes | Sensitivity |
|---|-------|---------------|-------|----------|-------|-------------|
| 1 | Network router | Continuous | Internet service provider (ISP) | On-premises | Has a 2.4 GHz and 5 GHz connection. All devices on the home network connect to the 5 GHz frequency. | Confidential |
| 2 | Desktop | Occasional | Homeowner | On-premises | Contains private information, like photos. | Restricted |
| 3 | Guest smartphone | Occasional | Friend | On and Off-premises | Connects to my home network. | Internal-only |
| 4 | Printer | Occasional | Homeowner | On-premises | Stores print history and may cache documents containing sensitive business information. Not always updated with the latest firmware. | Confidential |
| 5 | Webcam | Occasional | Homeowner | On-premises | Captures live video feed. If compromised, could expose private home office activity. Connected via USB and Wi-Fi. | Restricted |
| 6 | External hard drive | Occasional | Homeowner | On-premises | Stores backups of sensitive business files and financial records. Physically portable, increasing risk of theft or loss. | Restricted |

---

## Sensitivity Classification Guide

| Category | Access Designation |
|----------|--------------------|
| Restricted | Need-to-know |
| Confidential | Limited to specific users |
| Internal-only | Users on-premises |
| Public | Anyone |

---

## Summary

In this activity, I identified six devices connected to a home office network and evaluated each based on network access, ownership, location, and the type of information they handle. I classified three new devices:

- **Printer** — Classified as **Confidential** because it caches sensitive documents and is accessible to anyone on the network, but should be limited to specific users.
- **Webcam** — Classified as **Restricted** because it captures live video and if compromised could expose private business activity — access should be need-to-know only.
- **External hard drive** — Classified as **Restricted** because it stores sensitive business backups and financial records, and its portability increases the risk of physical theft.

Effective asset classification helps prioritize which devices require the most protection and informs decisions about access controls, encryption, and monitoring.
