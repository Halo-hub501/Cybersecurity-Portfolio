# Lab Report: Examine Input/Output in the Linux Shell

**Environment:** Linux Bash shell (Google Cloud Shell via Qwiklabs)
**Shell user:** `analyst@<instance>`

---

## Objective

Use the `echo` and `expr` commands to generate output and perform calculations in the Linux shell. Apply these skills to an analyst scenario involving login attempt data.

---

## Task 1 — Generate Output with echo

The `echo` command prints text to standard output. Tested several variations:

```bash
echo hello
```
Output: `hello`

```bash
echo "hello"
```
Output: `hello`

```bash
echo "olayinka"
```
Output: `olayinka`

The `echo` command works with or without quotes. Quotes are used when the output includes spaces or special characters.

---

## Task 2 — Perform Calculations with expr

The `expr` command performs integer arithmetic in the shell. All terms and operators must be separated by spaces.

```bash
expr 32 - 8
```
Output: `24`

**Analyst scenario:** Calculate total expected login attempts over a year.

Given: An average of 3500 login attempts per month.

```bash
expr 3500 * 12
```
Output: `42000`

Total projected logins for the year: **42,000**

---

## Optional Task — Additional Calculations

```bash
expr 1000 - 615 + 115 - 120
```
Output: `380`

---

## Key Takeaways

- `echo` is used to output text to the terminal — useful for displaying values, writing to files, and scripting
- `expr` performs integer-only arithmetic; it does not support decimals
- All operators in `expr` must be surrounded by spaces (e.g., `expr 32 - 8`, not `expr 32-8`)
- These shell fundamentals underpin more complex scripting and automation tasks in security operations
