# Lab: Add and Manage Users with Linux Commands

**Course:** Google Cybersecurity Professional Certificate
**Module:** 4 – Linux & SQL
**Lab #:** 07
**Date Completed:** 2026-03-25

---

## Objective

Practice managing user access in Linux using the `useradd`, `usermod`, `userdel`, and `chown` commands. This reflects real security analyst tasks: adding new users, assigning group membership, transferring file ownership, and removing users who leave the organization.

---

## Scenario

A new employee (`researcher9`) joins the Research department. Tasks include adding them to the system, assigning file ownership, adding them to a secondary group, and eventually deleting them from the system.

---

## Task 1: Add a New User

```bash
sudo useradd researcher9
sudo usermod -g research_team researcher9
```

**What I learned:**
- `useradd` creates a new user and automatically creates a matching group (`researcher9`)
- `usermod -g` sets the **primary group** (lowercase `-g`)
- The primary group is stamped on any file the user creates

---

## Task 2: Assign File Ownership

```bash
sudo chown researcher9 /home/researcher2/projects/project_r.txt
```

**What I learned:**
- `chown` transfers file ownership from one user to another
- Only root (via `sudo`) can reassign ownership to a different user
- Useful when responsibility for a file/project changes hands

---

## Task 3: Add User to a Secondary Group

```bash
sudo usermod -a -G sales_team researcher9
```

**What I learned:**
- `-G` specifies a supplementary/secondary group (uppercase)
- `-a` **appends** the group without removing existing group memberships
- Without `-a`, the command would replace all secondary groups — a common mistake
- Options are case-sensitive: `-a` and `-G` are different from `-A` and `-g`

---

## Task 4: Delete a User

```bash
sudo userdel researcher9
sudo groupdel researcher9
```

**What I learned:**
- `userdel` removes the user but leaves behind the auto-created `researcher9` group
- `groupdel` cleans up that orphaned empty group
- Good practice: always clean up unused groups after deleting a user

---

## Key Commands Summary

| Command | Purpose |
|---------|---------|
| `useradd` | Create a new user |
| `usermod -g` | Set primary group |
| `usermod -a -G` | Append supplementary group |
| `chown` | Change file owner |
| `userdel` | Delete a user |
| `groupdel` | Delete a group |

---

## Skills Demonstrated

- Linux user lifecycle management (create → modify → delete)
- Understanding of primary vs. supplementary groups
- File ownership management with `chown`
- Using `sudo` for privileged operations
