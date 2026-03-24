# Lab 5: Manage Files with Linux Commands

**Course:** Tools of the Trade: Linux and SQL (Course 4)
**Module:** Linux commands in the Bash shell
**Status:** ✅ Completed

---

## Objective

Organize the `/home/analyst` directory by creating and removing directories, moving and deleting files, and editing a file using the nano text editor — core file management skills for any security analyst working in a Linux environment.

---

## Starting Structure

```
home
└── analyst
    ├── notes
    │   ├── Q3patches.txt
    │   └── tempnotes.txt
    ├── reports
    │   ├── Q1patches.txt
    │   └── Q2patches.txt
    └── temp
```

## Target Structure

```
home
└── analyst
    ├── logs
    ├── notes
    │   └── tasks.txt
    └── reports
        ├── Q1patches.txt
        ├── Q2patches.txt
        └── Q3patches.txt
```

---

## Tasks & Commands

### Task 1 — Create a new directory

```bash
mkdir /home/analyst/logs
ls /home/analyst
```
**Output:** `logs  notes  reports  temp` ✅

---

### Task 2 — Remove a directory

```bash
rmdir /home/analyst/temp
ls /home/analyst
```
**Output:** `logs  notes  reports` ✅

---

### Task 3 — Move a file

```bash
cd /home/analyst/notes
mv Q3patches.txt /home/analyst/reports
ls /home/analyst/reports
```
**Output:** `Q1patches.txt  Q2patches.txt  Q3patches.txt` ✅

---

### Task 4 — Remove a file

```bash
rm tempnotes.txt
ls /home/analyst/notes
```
**Output:** (empty — no files listed) ✅

---

### Task 5 — Create a new file

```bash
touch /home/analyst/notes/tasks.txt
ls /home/analyst/notes
```
**Output:** `tasks.txt` ✅

---

### Task 6 — Edit a file with nano

```bash
nano /home/analyst/notes/tasks.txt
```
Typed inside nano:
```
Completed tasks
1. Managed file structure in /home/analyst
```
Saved with `CTRL+X` → `Y` → `ENTER`, then verified:

```bash
clear
cat /home/analyst/notes/tasks.txt
```
**Output:**
```
Completed tasks
1. Managed file structure in /home/analyst
```
✅

---

## Key Skills Demonstrated

| Skill | Command |
|-------|---------|
| Create a directory | `mkdir /home/analyst/logs` |
| Remove a directory | `rmdir /home/analyst/temp` |
| Move a file | `mv Q3patches.txt /home/analyst/reports` |
| Delete a file | `rm tempnotes.txt` |
| Create an empty file | `touch tasks.txt` |
| Edit a file | `nano tasks.txt` |
| Display file contents | `cat tasks.txt` |

---

## Key Takeaways

- `mkdir` and `rmdir` manage directories; `rmdir` only works on empty directories
- `mv` moves files between directories — no copy left behind
- `rm` permanently deletes files — no recycle bin in Linux
- `touch` creates an empty file instantly without opening an editor
- `nano` is a beginner-friendly terminal text editor; `CTRL+X` → `Y` → `ENTER` saves and exits
- These file management skills are foundational for SOC work: organizing log files, managing evidence directories, and maintaining audit trails
