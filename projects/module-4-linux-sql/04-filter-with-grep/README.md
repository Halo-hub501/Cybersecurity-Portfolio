# Lab 4: Filter with grep

**Course:** Tools of the Trade: Linux and SQL (Course 4)
**Module:** Linux commands in the Bash shell
**Status:** ✅ Completed

---

## Objective

Use the `grep` command and piping (`|`) to search for specific strings in log files and user data files — a core skill for security analysts who need to quickly isolate relevant information from large datasets.

---

## Tasks & Commands

### Task 1 — Search for error messages in a log file

Navigated to the logs directory and used `grep` to filter only error entries from the server log.

```bash
cd /home/analyst/logs
grep error server_logs.txt
```

**Output (6 error lines found):**
```
2022-09-28 13:56:22 error   The password is incorrect
2022-09-28 15:56:22 error   The username is incorrect
2022-09-28 16:56:22 error   The password is incorrect
2022-09-29 13:56:22 error   An unexpected error occurred
2022-09-29 16:56:22 error   Unauthorized access
2022-09-29 16:56:22 error   Unauthorized access
```

**Answer:** 6 error lines

---

### Task 2 — Find files containing specific strings

Navigated to the users directory and piped `ls` output into `grep` to filter files by name pattern.

```bash
cd /home/analyst/reports/users

# Files containing "Q1" in name
ls | grep Q1
```
**Output:** Q1_access.txt, Q1_added_users.txt, Q1_deleted_users.txt → **3 files**

```bash
# Files containing "access" in name
ls | grep access
```
**Output:** Q1_access.txt, Q2_access.txt, Q3_access.txt, Q4_access.txt → **4 files**

---

### Task 3 — Search file contents

Used `grep` to search for specific usernames and department entries inside user data files.

```bash
# Search for username jhill in Q2 deleted users
grep jhill Q2_deleted_users.txt
```
**Output:** `1025  jhill  Sales` → **Yes, jhill was found** (deleted in Q2, from Sales dept)

```bash
# Search for Human Resources additions in Q4
grep "Human Resources" Q4_added_users.txt
```
**Output:**
```
1151    sshah    Human Resources
1145    msosa    Human Resources
```
**Answer:** 2 users added to Human Resources in Q4

---

## Key Skills Demonstrated

| Skill | Command Used |
|-------|-------------|
| Search file contents by string | `grep error server_logs.txt` |
| Pipe command output for filtering | `ls \| grep Q1` |
| Search for multi-word strings | `grep "Human Resources" file.txt` |
| Locate specific user records | `grep jhill Q2_deleted_users.txt` |

---

## Key Takeaways

- `grep` searches file contents line by line and returns only matching lines
- Piping (`|`) chains commands — `ls | grep pattern` filters file listings without opening any file
- Multi-word search strings must be wrapped in quotes: `grep "Human Resources"`
- These techniques are directly applicable to SOC work: filtering auth logs, searching for specific IPs, usernames, or error codes in large log files
