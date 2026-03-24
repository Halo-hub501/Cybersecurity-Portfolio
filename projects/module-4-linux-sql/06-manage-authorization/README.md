# Lab 6: Manage Authorization

**Course:** Tools of the Trade: Linux and SQL (Course 4)
**Module:** Linux commands in the Bash shell
**Platform:** Google Skills Boost
**Status:** ✅ Completed

---

## Objective

Use Linux commands to examine and update file and directory permissions for a research team environment. The goal is to ensure that only authorized users have the correct level of access — a core principle of the least-privilege security model.

**Working directory:** `/home/researcher2/projects`

---

## Task 1 — Check File and Directory Details

Used `ls -la` to view all files, including hidden ones, with their full permission strings.

```bash
researcher2@9e8bcde30f6f:~/projects$ ls -la
```

```
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Mar 24 20:56 .
drwxr-xr-x 3 researcher2 research_team 4096 Mar 24 21:31 ..
-rw--w---- 1 researcher2 research_team   46 Mar 24 20:56 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 Mar 24 20:56 drafts
-rw-rw-rw- 1 researcher2 research_team   46 Mar 24 20:56 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Mar 24 20:56 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_t.txt
```

Then used `ls -l` to check visible files only (standard view used throughout the lab):

```bash
researcher2@9e8bcde30f6f:~/projects$ ls -l
```

```
total 20
drwx--x--- 2 researcher2 research_team 4096 Mar 24 20:56 drafts
-rw-rw-rw- 1 researcher2 research_team   46 Mar 24 20:56 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Mar 24 20:56 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_t.txt
```

---

## Task 2 — Interpret the Permission String

The 10-character permission string is structured as follows:

```
d  rwx  r-x  ---
│   │    │    │
│   │    │    └── Other permissions
│   │    └─────── Group permissions
│   └──────────── Owner (user) permissions
└──────────────── Type: d = directory, - = file
```

| Character | Meaning |
|-----------|---------|
| `r` | Read |
| `w` | Write |
| `x` | Execute (or enter, for directories) |
| `-` | Permission not granted |

**Example analysis — `project_k.txt` (`-rw-rw-rw-`):**
- File (not directory)
- Owner: read + write
- Group: read + write
- Other: read + write ← **others should not have write access**

---

## Task 3 — Remove Write Permission for Others on `project_k.txt`

The file had world-writable permissions, which violates the organization's policy.

```bash
researcher2@9e8bcde30f6f:~/projects$ chmod o-w project_k.txt
researcher2@9e8bcde30f6f:~/projects$ ls -l
```

```
total 20
drwx--x--- 2 researcher2 research_team 4096 Mar 24 20:56 drafts
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_k.txt
-rw-r----- 1 researcher2 research_team   46 Mar 24 20:56 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_t.txt
```

| | Before | After |
|---|--------|-------|
| `project_k.txt` | `-rw-rw-rw-` | `-rw-rw-r--` ✅ |

---

## Task 4 — Remove Group Read Permission on `project_m.txt`

The research team (group) should not have read access to this file.

```bash
researcher2@9e8bcde30f6f:~/projects$ chmod g-r project_m.txt
researcher2@9e8bcde30f6f:~/projects$ ls -la
```

```
total 32
drwxr-xr-x 3 researcher2 research_team 4096 Mar 24 20:56 .
drwxr-xr-x 3 researcher2 research_team 4096 Mar 24 21:31 ..
-rw--w---- 1 researcher2 research_team   46 Mar 24 20:56 .project_x.txt
drwx--x--- 2 researcher2 research_team 4096 Mar 24 20:56 drafts
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_k.txt
-rw------- 1 researcher2 research_team   46 Mar 24 20:56 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_t.txt
```

| | Before | After |
|---|--------|-------|
| `project_m.txt` | `-rw-r-----` | `-rw-------` ✅ |

---

## Task 5 — Fix Permissions on Hidden File `.project_x.txt`

This archived file should not be writable by anyone. Both the owner and group need to lose write access; the group also needs read access added for reference.

```bash
researcher2@9e8bcde30f6f:~/projects$ chmod u-w,g-w,g+r .project_x.txt
researcher2@9e8bcde30f6f:~/projects$ ls -l
```

```
total 20
drwx--x--- 2 researcher2 research_team 4096 Mar 24 20:56 drafts
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_k.txt
-rw------- 1 researcher2 research_team   46 Mar 24 20:56 project_m.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_r.txt
-rw-rw-r-- 1 researcher2 research_team   46 Mar 24 20:56 project_t.txt
```

| | Before | After |
|---|--------|-------|
| `.project_x.txt` | `-rw--w----` | `-r--r-----` ✅ |

> **Note:** A single `chmod` call can apply multiple changes at once using comma-separated clauses: `u-w,g-w,g+r`

---

## Task 6 — Remove Group Execute Permission on `drafts/` Directory

The `drafts` directory had group execute (`x`) set, which allows the group to enter the directory. Only the owner should have access.

```bash
researcher2@9e8bcde30f6f:~/projects$ chmod g-x drafts
researcher2@9e8bcde30f6f:~/projects$
```

| | Before | After |
|---|--------|-------|
| `drafts/` | `drwx--x---` | `drwx------` ✅ |

> **Key concept:** Execute on a **directory** controls the ability to enter it (`cd`), not to run scripts. Removing `x` from the group locks them out entirely.

---

## Summary of All Permission Changes

| File / Directory | Original | Final | Change Made |
|-----------------|----------|-------|-------------|
| `project_k.txt` | `-rw-rw-rw-` | `-rw-rw-r--` | Removed write from others |
| `project_m.txt` | `-rw-r-----` | `-rw-------` | Removed read from group |
| `.project_x.txt` | `-rw--w----` | `-r--r-----` | Removed write from owner & group; added read to group |
| `drafts/` | `drwx--x---` | `drwx------` | Removed execute from group |

---

## Key Takeaways

- `ls -l` shows visible files with permissions; `ls -la` includes hidden files (prefixed with `.`)
- `chmod` symbolic syntax: `u` = user/owner, `g` = group, `o` = others, `a` = all; `+` adds, `-` removes
- Multiple permission changes can be chained in one command: `chmod u-w,g-w,g+r <file>`
- **Execute on a directory** controls entry access, not just script execution
- Authorization management enforces least privilege — users should only have the access their role requires
