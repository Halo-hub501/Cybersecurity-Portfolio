# Add and Manage Users with Linux Commands

**Course:** Tools of the Trade: Linux and SQL (Course 4)
**Certificate:** Google Cybersecurity Professional Certificate
**Status:** Completed

---

## Project Description

As a security analyst, managing user access is a core responsibility. In this lab, I was tasked with onboarding a new employee (`researcher9`) into the system and managing their access throughout their time at the organization. This included creating the user account, assigning primary and secondary group membership, transferring file ownership, and eventually removing the user when they left the organization. All tasks were performed using `sudo` to run privileged commands as root.

---

## Task 1: Add a New User

I used the `useradd` command to create the new user account, then `usermod` to assign them to the correct primary group.

```bash
analyst@e0fa4c40ce0f:~$ sudo useradd researcher9
analyst@e0fa4c40ce0f:~$ sudo usermod -g research_team researcher9
```

![Task 1 — Adding researcher9 and assigning primary group](assets/task1-add-user.png)

The `useradd` command creates a new user account and automatically creates a matching group with the same name (`researcher9`). The `usermod -g` command then sets `research_team` as the primary group. The lowercase `-g` flag is used specifically for setting the primary group — this is different from `-G`, which is used for supplementary groups.

---

## Task 2: Assign File Ownership

The new employee (`researcher9`) was taking responsibility for `project_r`. I used the `chown` command to transfer ownership of the file.

```bash
analyst@e0fa4c40ce0f:~$ sudo chown researcher9 /home/researcher2/projects/project_r.txt
```

![Task 2 — Transferring file ownership to researcher9](assets/task2-chown.png)

The `chown` command changes who owns a file. Here, ownership of `project_r.txt` was transferred from `researcher2` to `researcher9`. Only root (via `sudo`) can reassign ownership to a different user.

---

## Task 3: Add the User to a Secondary Group

A few months later, `researcher9` began working across both the Research and Sales departments. I added them to the `sales_team` group as a supplementary group while keeping `research_team` as their primary group.

```bash
analyst@e0fa4c40ce0f:~$ sudo usermod -a -G sales_team researcher9
```

![Task 3 — Adding researcher9 to sales_team as a secondary group](assets/task3-secondary-group.png)

The `-G` flag (uppercase) specifies a supplementary group. The `-a` flag is critical — it **appends** the new group to the user's existing memberships rather than replacing them. Without `-a`, running `usermod -G sales_team researcher9` would have removed them from `research_team`. Options are case-sensitive: `-a` and `-G` must be exact.

---

## Task 4: Delete a User

After `researcher9` left the organization, I removed their account from the system.

```bash
analyst@e0fa4c40ce0f:~$ sudo userdel researcher9
analyst@e0fa4c40ce0f:~$ sudo groupdel researcher9
```

The `userdel` command removes the user account. However, because Linux automatically creates a group with the same name as the user when they are first added, that group (`researcher9`) is not deleted automatically when the user is removed — the system outputs a notice that the group was not removed since it is no longer anyone's primary group. I then ran `groupdel researcher9` to clean up the empty orphaned group. This is good security practice — leaving unused groups behind creates unnecessary access entries in the system.

---

## Summary

In this lab, I managed the full lifecycle of a user account in Linux — from creation to deletion. I used `useradd` to create the account, `usermod -g` to set a primary group, `chown` to transfer file ownership, `usermod -a -G` to add a supplementary group without overwriting existing memberships, and `userdel` followed by `groupdel` to remove the user and clean up. Each step reflects real security analyst responsibilities for maintaining least-privilege access in an organization.

| Command | Purpose |
|---------|---------|
| `sudo useradd researcher9` | Create new user account |
| `sudo usermod -g research_team researcher9` | Set primary group |
| `sudo chown researcher9 /home/researcher2/projects/project_r.txt` | Transfer file ownership |
| `sudo usermod -a -G sales_team researcher9` | Add supplementary group |
| `sudo userdel researcher9` | Delete user account |
| `sudo groupdel researcher9` | Remove orphaned group |
