# Data Leak Worksheet

**Course:** Assets, Threats, and Vulnerabilities (Course 5)
**Certificate:** Google Cybersecurity Professional Certificate
**Status:** Completed

---

## Project Description

In this activity, I analyzed a data leak incident at an educational technology company. A customer success representative accidentally shared a link to an internal folder of confidential business documents with an external business partner, who then posted it to social media. I identified the factors that led to the leak, reviewed NIST SP 800-53: AC-6 (Least Privilege), recommended control enhancements, and justified how those improvements would prevent similar incidents.

---

## Incident Summary

A customer success representative received access to a folder of internal documents from a manager. It contained files associated with a new product offering, including customer analytics and marketing materials. The manager forgot to unshare the folder. Later, the representative copied a link to the marketing materials to share with a business partner during a sales call. Instead, the representative shared a link to the entire folder. During the sales call, the business partner received the link to internal documents and posted it to their social media page.

---

## Data Leak Worksheet

**Control:** Least Privilege

---

### Issue(s)
*What factors contributed to the information leak?*

The manager granted the representative access to an entire internal folder rather than sharing only the specific files needed for the meeting. Access to the folder was not revoked after the meeting ended. As a result, the representative was able to accidentally share the full folder — including confidential documents — with an external business partner who had no authorization to view them.

---

### Review
*What does NIST SP 800-53: AC-6 address?*

NIST SP 800-53: AC-6 defines the principle of least privilege, which states that users should only be given the minimum access and authorization required to complete their tasks. It requires that user accounts, roles, and processes be enforced to prevent users from operating at privilege levels higher than necessary. Control enhancements include restricting access based on user role, automatically revoking access after a period of time, maintaining activity logs, and regularly auditing user privileges.

---

### Recommendation(s)
*How might the principle of least privilege be improved at the company?*

Based on NIST SP 800-53: AC-6 control enhancements, two improvements are recommended:

1. **Automatically revoke access to information after a period of time** — shared folder access should expire automatically after the meeting or sales call ends, eliminating the risk of prolonged unauthorized access.
2. **Restrict access to sensitive resources based on user role** — employees should only be granted access to the specific files relevant to their role, not entire folders containing confidential documents beyond their scope of work.

---

### Justification
*How might these improvements address the issues?*

Automatically revoking access would have ensured the internal folder was no longer accessible after the meeting, preventing the representative from being able to share it later. Restricting access by role would have limited the representative to only the marketing materials they needed, so even if the wrong link was shared, the confidential documents would not have been exposed.

---

## Security Plan Reference

| Function | Category | Subcategory | Reference |
|----------|----------|-------------|-----------|
| Protect | PR.DS: Data security | PR.DS-5: Protections against data leaks | NIST SP 800-53: AC-6 |

---

## Summary

This incident demonstrates how the failure to apply least privilege — both in granting overly broad folder access and in not revoking that access after the meeting — created the conditions for a data leak. Implementing automatic access expiration and role-based access restrictions would significantly reduce the likelihood of similar incidents by limiting both the scope and duration of access to sensitive internal documents.
