# Lab: Get Help in the Command Line

**Course:** Google Cybersecurity Professional Certificate
**Module:** 4 – Linux & SQL
**Lab #:** 08
**Date Completed:** 2026-03-25

---

## Objective

Learn how to use built-in Linux help commands to explore unfamiliar commands and their options without leaving the terminal.

---

## Commands Covered

### `whatis` — One-line description of a command

```bash
whatis cat
# cat (1) - concatenate files and print to the standard output

whatis rm
# rm (1) - remove files or directories

whatis rmdir
# rmdir (1) - remove empty directories
```

**Use case:** Quick lookup when you just need to know what a command does.

---

### `man` — Full manual page for a command

```bash
man useradd
man cat
```

**What I learned:**
- `man` opens the full manual (man page) for any command
- Press `Enter` to scroll line by line, `Space` to go page by page, `Q` to quit
- Man pages list every available option with descriptions
- Example found: `useradd -e` sets an **expiration date** for a temporary account (format: YYYY-MM-DD)

---

### `apropos` — Search by keyword when you don't know the command

```bash
apropos -a create new group
# groupadd (8) - create a new group

apropos -a first part file
# head (1) - output the first part of files
```

**What I learned:**
- `apropos` searches man page descriptions using keywords
- `-a` flag means **all keywords must match** (AND search, not OR)
- Useful when you know what you want to do but not which command to use

---

## Task Answers

| Question | Answer |
|----------|--------|
| Which `useradd` option sets an expiration date? | `-e` (`--expiredate`) |
| What is the difference between `rm` and `rmdir`? | `rm` removes files or directories; `rmdir` only removes **empty** directories |
| Which command creates a new group? | `groupadd` (found via `apropos -a create new group`) |

---

## Key Commands Summary

| Command | Purpose |
|---------|---------|
| `whatis <command>` | One-line description |
| `man <command>` | Full manual/documentation |
| `apropos -a <keywords>` | Find a command by what it does |

---

## Skills Demonstrated

- Using built-in Linux documentation tools
- Reading and navigating man pages
- Searching for commands by keyword with `apropos`
- Identifying correct command options without external resources
