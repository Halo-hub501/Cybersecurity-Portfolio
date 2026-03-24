# Lab Report: Find Files with Linux Commands

**Environment:** Linux Bash shell (Google Cloud Shell via Qwiklabs)
**Shell user:** `analyst@<instance>`

---

## Objective

Use core Linux Bash commands to navigate the file system, locate files within directory structures, and display their contents — skills directly applicable to log analysis and file investigation in a SOC environment.

---

## Linux Filesystem Hierarchy Standard (FHS)

The FHS defines the standard directory structure for Linux systems:

| Directory | Purpose |
|-----------|---------|
| `/home` | User home directories |
| `/bin` | Binary executables |
| `/etc` | System configuration files |
| `/tmp` | Temporary files (note: writable by all users — a common attacker target) |
| `/mnt` | Mounted external media |

---

## Task 1 — Get Current Location and List Home Directory

```bash
pwd
```
Output: `/home/analyst`

```bash
ls
```
Output: `logs  projects  reports  temp`

The analyst home directory contains four subdirectories relevant to security work.

---

## Task 2 — Navigate to a Subdirectory and List Files

```bash
cd /home/analyst/reports
ls
```
Output: `users`

```bash
cd /home/analyst/reports/users
ls
```
Output: `Q1_added_users.txt  Q1_deleted_users.txt`

---

## Task 3 — Read the Contents of a File

```bash
cat Q1_added_users.txt
```

Output:
```
employee_id   username    department
1001          bmoreno     Marketing
1026          apatel      Human Resources
1041          cgriffin    Sales
1104          mreed       Information Technology
1177          aezra       Human Resources
1188          noshiro     Finance
```

**Quiz answer:** Employee `aezra` works in **Human Resources** ✅

**Employee ID for `mreed` (IT department):** `1104` ✅

---

## Task 4 — Navigate to Logs Directory and Analyze Server Log

```bash
cd /home/analyst/logs
ls
```
Output: `server_logs.txt`

```bash
head server_logs.txt
```

Output (first 10 lines):
```
2022-09-28 13:55:55 info     User logged on successfully
2022-09-28 13:56:22 error    The password is incorrect
2022-09-28 13:56:48 warning  The file storage is 75% full
2022-09-28 15:55:00 info     User logged on successfully
2022-09-28 15:56:22 error    The username is incorrect
2022-09-28 15:56:48 warning  The file storage is 90% full
2022-09-28 16:55:00 info     User navigated to settings page
2022-09-28 16:56:22 error    The password is incorrect
2022-09-28 16:56:48 warning  The current user's password expires in 15 days
2022-09-29 13:55:55 info     User logged on successfully
```

**Quiz answer:** There are **3 warning messages** in the first 10 lines ✅

---

## Key Takeaways

- `pwd` — always know where you are before navigating
- `ls` — list directory contents to understand what files exist
- `cd` — navigate with absolute paths (`/home/analyst/reports`) to avoid errors; relative paths can fail if your current location is unexpected
- `cat` — display full file contents; useful for structured data files
- `head` — display the first N lines of a file (default 10); essential for previewing large log files without overwhelming the terminal
- These commands are foundational for any log investigation, file triage, or incident response task performed on a Linux system
