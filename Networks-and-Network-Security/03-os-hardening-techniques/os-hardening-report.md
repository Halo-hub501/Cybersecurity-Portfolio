# OS Hardening — Security Incident Report

**Incident:** Unauthorized Access via Brute-Force Attack
**Organization:** Yummy Recipes for Me (fictional bakery website)
**Analyst:** Security Analyst Intern (Google Cybersecurity Certificate Program)
**Date:** 2024

---

## 1. Incident Summary

The owner of *Yummy Recipes for Me*, a baking website, reported that the site was defaced — recipes had been replaced with offensive content. An investigation revealed that a former employee used a **brute-force attack** to gain access to the site's admin panel and made unauthorized changes.

---

## 2. How the Attack Occurred

### Attack Method: Brute-Force via Password Spraying

Review of the web application logs and the attacker's browser history (accessed from a shared workstation) revealed the following sequence of events:

1. The former employee visited the website's admin login page
2. The browser history showed the attacker had accessed **"Best_Brute_Force_Passwords_08.2022"**, a publicly available list of commonly used passwords
3. The attacker systematically tried multiple passwords from this list against the admin account
4. The account had a **weak, commonly-used password** — the attack succeeded after a small number of attempts
5. Once inside, the attacker modified the website content

### Why the Attack Succeeded

| Factor | Detail |
|--------|--------|
| Weak password policy | Admin password was a common, easily guessable value |
| No account lockout | The login page did not lock accounts after repeated failed attempts |
| No MFA | A second authentication factor would have blocked access even with the correct password |
| No access revocation | The former employee's credentials were not deactivated upon termination |

---

## 3. OS and Application Hardening Recommendations

### 3.1 Enforce a Strong Password Policy

- **Minimum length:** 12–16 characters
- **Complexity requirements:** Uppercase, lowercase, numbers, and symbols
- **Password history:** Prevent reuse of last 10 passwords
- **Expiration:** Force password rotation every 90 days for privileged accounts
- **Deploy a password manager** to reduce the temptation to use simple, memorable passwords

### 3.2 Implement Account Lockout Policies

- **Lockout threshold:** Lock account after 3–5 consecutive failed login attempts
- **Lockout duration:** 15–30 minute lockout, or require manual admin unlock for repeat offenses
- **Alert on lockout:** Trigger a security alert to IT when lockouts occur — this is a signal of a potential brute-force attempt

This single control would have prevented the brute-force attack from succeeding.

### 3.3 Enable Multifactor Authentication (MFA)

- Require MFA for **all admin panel access** — even if an attacker obtains the correct password, they cannot log in without the second factor
- Use an authenticator app (TOTP) or hardware key rather than SMS
- Enforce MFA for all privileged and remote access accounts

### 3.4 Implement an Offboarding Security Checklist

- **Immediately revoke** all credentials, tokens, and VPN access upon employee departure
- Remove the former employee from all access groups and shared accounts
- Review and rotate any shared credentials the employee had access to
- Audit login activity for terminated accounts in the 30 days following their departure

### 3.5 Additional Hardening Measures

| Control | Action |
|---------|--------|
| Patch management | Ensure OS, CMS (e.g., WordPress), and plugins are fully patched and up to date |
| Principle of least privilege | Ensure admin accounts are used only when needed; use standard accounts for routine work |
| Login audit logging | Enable logging of all login attempts (success and failure) with timestamps and IP addresses |
| CAPTCHA on login | Add CAPTCHA to the admin login page to block automated brute-force tools |
| Fail2ban or equivalent | Deploy an automated tool that blocks IP addresses after repeated failed login attempts |

---

## 4. Conclusion

The attack was entirely preventable. A combination of weak credentials, no account lockout, no MFA, and failure to revoke a terminated employee's access created an easy path for the attacker.

Implementing even one of the above controls — particularly account lockout or MFA — would have stopped the attack. Implementing all of them creates defense in depth, significantly raising the cost and complexity for any future attacker.

**Immediate actions required:**
1. Change all admin credentials on the affected website
2. Enable MFA on the admin panel
3. Configure account lockout after 5 failed attempts
4. Audit all active accounts and remove any associated with former employees
