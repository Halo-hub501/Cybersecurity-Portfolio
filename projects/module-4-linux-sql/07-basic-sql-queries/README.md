# Basic SQL Queries with SELECT and ORDER BY

**Course:** Tools of the Trade: Linux and SQL (Course 4)
**Certificate:** Google Cybersecurity Professional Certificate
**Status:** Completed

---

## Project Description

As a security analyst, I was tasked with identifying which employee devices needed to be updated and investigating user login activity for any unusual behavior. To do this, I queried the `machines` and `log_in_attempts` tables inside the `organization` database using the MariaDB shell. I used `SELECT` and `FROM` to retrieve specific columns and `ORDER BY` to sort results by date and time.

---

## Task 1: Retrieve Employee Device Data

### Step 1 — Retrieve all device information

```sql
SELECT * FROM machines;
```

The `*` symbol returns every column from the table. This gave a full view of all 200 employee devices including `device_id`, `operating_system`, `email_client`, `OS_patch_date`, and `employee_id`.

```
+--------------+------------------+----------------+---------------+-------------+
| device_id    | operating_system | email_client   | OS_patch_date | employee_id |
+--------------+------------------+----------------+---------------+-------------+
| a184b775c707 | OS 1             | Email Client 1 | 2021-09-01    |        1156 |
| a192b174c940 | OS 2             | Email Client 1 | 2021-06-01    |        1052 |
| a305b818c708 | OS 3             | Email Client 2 | 2021-06-01    |        1182 |
| a317b635c465 | OS 1             | Email Client 2 | 2021-03-01    |        1130 |
| a320b137c219 | OS 2             | Email Client 2 | 2021-03-01    |        1000 |
| ...          |                  |                |               |             |
+--------------+------------------+----------------+---------------+-------------+
200 rows in set (0.356 sec)
```

---

### Step 2 — Select only device_id and email_client

```sql
SELECT device_id, email_client FROM machines;
```

Instead of returning all columns, I specified only the two columns needed. The third row returned **Email Client 2**, confirming how `SELECT` can be used to focus on relevant data only.

---

### Step 3 — Select device_id, operating_system, and OS_patch_date

```sql
SELECT device_id, operating_system, OS_patch_date FROM machines;
```

This query returns only the columns needed to identify which operating system each device runs and when it was last patched. The first entry shows a patch date of **2021-09-01**, which helps the team prioritize which devices need the most urgent updates.

---

## Task 2: Investigate Login Activity

### Step 1 — Check login locations

```sql
SELECT event_id, country FROM log_in_attempts;
```

I retrieved the `event_id` and `country` columns to verify that login attempts were only coming from expected regions (United States, Canada, or Mexico). The results showed that login attempts **were made from Australia**, which is outside the expected regions and warrants further investigation.

---

### Step 2 — Check login times

```sql
SELECT username, login_date, login_time FROM log_in_attempts;
```

I selected the `username`, `login_date`, and `login_time` columns to identify whether any logins occurred outside of normal working hours. The fifth row returned the username **apatel**.

---

### Step 3 — Retrieve all login attempt data

```sql
SELECT * FROM log_in_attempts;
```

Using `*` returns every column from the `log_in_attempts` table, giving a complete picture of all login activity including event IDs, usernames, dates, times, countries, and success status.

---

## Task 3: Order Login Attempts Data

### Step 1 — Sort by login date

```sql
SELECT * FROM log_in_attempts ORDER BY login_date;
```

The `ORDER BY` keyword sorts the results in ascending order by default. Sorting by `login_date` made it easier to identify the earliest login attempts. The first record returned was **ivelasco on 2022-05-08**.

---

### Step 2 — Sort by login date and login time

```sql
SELECT * FROM log_in_attempts ORDER BY login_date, login_time;
```

Adding a second column to `ORDER BY` refines the sort — records with the same date are then sorted by time. This gave a precise chronological view of all login attempts. The first record returned was **wjaffrey at 00:15:55**, indicating a very early morning login that may be worth investigating.

---

## Summary

In this lab, I used fundamental SQL query techniques to retrieve and organize security-relevant data from the `organization` database. I used `SELECT` with specific column names to focus on relevant fields, `SELECT *` to retrieve all data, and `ORDER BY` with multiple columns to sort results chronologically.

| Query | Purpose |
|-------|---------|
| `SELECT * FROM machines` | Retrieve all employee device data |
| `SELECT device_id, email_client FROM machines` | Focus on specific columns |
| `SELECT device_id, operating_system, OS_patch_date FROM machines` | Identify devices needing patches |
| `SELECT event_id, country FROM log_in_attempts` | Check login locations |
| `SELECT username, login_date, login_time FROM log_in_attempts` | Check login times |
| `SELECT * FROM log_in_attempts` | Full view of all login activity |
| `SELECT * FROM log_in_attempts ORDER BY login_date` | Sort by date |
| `SELECT * FROM log_in_attempts ORDER BY login_date, login_time` | Sort by date and time |
