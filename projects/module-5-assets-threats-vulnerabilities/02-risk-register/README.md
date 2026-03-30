# Risk Register

**Course:** Assets, Threats, and Vulnerabilities (Course 5)
**Certificate:** Google Cybersecurity Professional Certificate
**Status:** Completed

---

## Project Description

In this activity, I conducted a risk assessment for a commercial bank by evaluating five vulnerabilities that threaten the bank's funds. I scored each risk by likelihood and severity, then calculated an overall priority score using the formula **Likelihood x Severity = Risk**. This exercise mirrors how security teams use risk registers to prioritize resources and focus attention on the most critical threats.

---

## Operational Environment

The bank is located in a coastal area with low crime rates. Many people and systems handle the bank's data — 100 on-premise employees and 20 remote employees. The customer base includes 2,000 individual accounts and 200 commercial accounts. The bank's services are marketed by a professional sports team and ten local businesses. Strict financial regulations require the bank to secure its data and funds, including maintaining enough cash to meet Federal Reserve requirements.

**Notes:** Doing business with other companies might increase the risks to data since it presents other avenues for the information to be compromised. The risk of theft is important, but might not be a priority because the bank is in an area with low crime rates.

---

## Risk Register

| Asset | Risk | Description | Likelihood | Severity | Priority |
|-------|------|-------------|-----------|---------|---------|
| Funds | Business email compromise | An employee is tricked into sharing confidential information. | 2 | 2 | 4 |
| Funds | Compromised user database | Customer data is poorly encrypted. | 2 | 3 | 6 |
| Funds | Financial records leak | A database server of backed up data is publicly accessible. | 3 | 3 | 9 |
| Funds | Theft | The bank's safe is left unlocked. | 1 | 3 | 3 |
| Funds | Supply chain disruption | Delivery delays due to natural disasters. | 1 | 2 | 2 |

**Formula:** Likelihood x Severity = Priority Score

---

## Scoring Key

**Likelihood (1-3):**
- 1 = Rare — could happen once in several years
- 2 = Likely — could happen once a month
- 3 = Certain — could happen once a day

**Severity (1-3):**
- 1 = Low — minor impact on operations
- 2 = Moderate — significant impact on operations or reputation
- 3 = Catastrophic — major financial loss, regulatory violation, or business disruption

---

## Risk Matrix

|  | Low Severity (1) | Moderate Severity (2) | Catastrophic Severity (3) |
|--|-----------------|----------------------|--------------------------|
| **Certain (3)** | 3 | 6 | **9** |
| **Likely (2)** | 2 | **4** | **6** |
| **Rare (1)** | 1 | **2** | **3** |

---

## Risk Analysis

| Risk | Priority Score | Interpretation |
|------|--------------|----------------|
| Financial records leak | 9 | **Critical** — Publicly accessible backup server is nearly certain to be exploited and would cause catastrophic regulatory, financial, and reputational damage. Highest priority. |
| Compromised user database | 6 | **High** — Poor encryption on 2,200+ customer accounts exposes the bank to severe regulatory fines and data breach liability. |
| Business email compromise | 4 | **Medium** — With 120 employees, phishing attacks are a moderate risk. Financial and reputational damage is significant but manageable. |
| Theft | 3 | **Low-Medium** — The bank is in a low crime area, making physical theft rare, but the impact of an unlocked safe would be catastrophic. |
| Supply chain disruption | 2 | **Low** — Coastal hurricanes are rare and while they can disrupt operations, they cause moderate rather than permanent damage. |

---

## Summary

The financial records leak received the highest priority score of 9, making it the most urgent risk to address — a publicly accessible backup server must be secured immediately. The compromised user database scored 6 and should be the second priority, requiring immediate encryption improvements to protect customer data. Business email compromise scored 4 and warrants ongoing employee training. Theft and supply chain disruption scored 3 and 2 respectively, and while serious in impact, their low likelihood in this environment makes them lower priorities relative to the digital threats.
