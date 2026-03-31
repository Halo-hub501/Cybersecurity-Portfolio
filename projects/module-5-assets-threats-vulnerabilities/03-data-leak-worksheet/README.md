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

Access to the internal folder was not limited to the sales team and the manager. The business partner should not have been given permission to share the promotional information to social media.

---

### Review
*What does NIST SP 800-53: AC-6 address?*

NIST SP 800-53: AC-6 addresses how an organization can protect their data privacy by implementing least privilege. It also suggests control enhancements to improve the effectiveness of least privilege.

---

### Recommendation(s)
*How might the principle of least privilege be improved at the company?*

1. Restrict access to sensitive resources based on user role.
2. Regularly audit user privileges.

---

### Justification
*How might these improvements address the issues?*

Data leaks can be prevented if shared links to internal files are restricted to employees only. Also, requiring managers and security teams to regularly audit access to team files would help limit the exposure of sensitive information.

---

## Security Plan Reference

| Function | Category | Subcategory | Reference |
|----------|----------|-------------|-----------|
| Protect | PR.DS: Data security | PR.DS-5: Protections against data leaks | NIST SP 800-53: AC-6 |

---

## Summary

This incident demonstrates how the failure to apply least privilege — both in granting overly broad folder access and in not revoking that access after the meeting — created the conditions for a data leak. Implementing automatic access expiration and role-based access restrictions would significantly reduce the likelihood of similar incidents by limiting both the scope and duration of access to sensitive internal documents.
