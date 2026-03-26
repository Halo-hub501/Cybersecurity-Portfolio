# Apply Filters to SQL Queries

**Course:** Tools of the Trade: Linux and SQL (Course 4)
**Certificate:** Google Cybersecurity Professional Certificate
**Status:** Completed

---

## Project Description

As a security professional at a large organization, I investigated potential security issues involving login attempts and employee machines. I used SQL filters with the `AND`, `OR`, and `NOT` operators to query the `log_in_attempts` and `employees` tables in the organization's database, retrieving specific records needed to support the security investigation and plan system updates.

---

## Retrieve After-Hours Failed Login Attempts

I needed to identify all failed login attempts that occurred after business hours (after 18:00). I used the `AND` operator to require both conditions to be true simultaneously — the login time must be after 18:00 and the login must have failed. `FALSE` is not placed in single quotes because it is Boolean data, not a string.

```sql
SELECT *
FROM log_in_attempts
WHERE login_time > '18:00' AND success = FALSE;
```

![Failed login attempts after 18:00](assets/task1-after-hours.png)

This returned **19 failed login attempts** after business hours.

---

## Retrieve Login Attempts on Specific Dates

A suspicious event occurred on 2022-05-09. I used the `OR` operator to retrieve all login attempts from that day and the day before (2022-05-08), since either date could contain related activity. The `OR` operator returns a record when at least one of the conditions is true.

```sql
SELECT *
FROM log_in_attempts
WHERE login_date = '2022-05-09' OR login_date = '2022-05-08';
```

![Login attempts on 2022-05-08 and 2022-05-09](assets/task2-specific-dates.png)

This returned **75 login attempts** across both days.

---

## Retrieve Login Attempts Outside of Mexico

The team determined the suspicious activity did not originate in Mexico. I used `NOT` combined with `LIKE` and the `%` wildcard to exclude all login attempts from Mexico. The `%` wildcard was necessary because the country column stores values as both `MEX` and `MEXICO` — using `'MEX%'` ensures both formats are matched and excluded.

```sql
SELECT *
FROM log_in_attempts
WHERE NOT country LIKE 'MEX%';
```

![Login attempts outside of Mexico](assets/task3-not-mexico.png)

This returned **144 login attempts** from outside Mexico.

---

## Retrieve Employees in Marketing

My team needed to update machines for Marketing department employees located in the East building. I first viewed the full employees table to understand the structure of the data.

```sql
SELECT *
FROM employees;
```

![View all employees table](assets/task4-employees-view.png)

I then used the `AND` operator to require both conditions and `LIKE` with `%` to match all East building offices (such as East-170, East-320, etc.), since there are multiple offices in that building.

```sql
SELECT *
FROM employees
WHERE department = 'Marketing' AND office LIKE 'East%';
```

![Marketing employees in East building](assets/task4-marketing-east.png)

The first employee returned was **elarson**.

---

## Retrieve Employees in Finance or Sales

My team needed to update machines for employees in the Finance or Sales departments. I used the `OR` operator to return employees from either department. Even though both conditions reference the same column, each full condition must be written out separately.

```sql
SELECT *
FROM employees
WHERE department = 'Finance' OR department = 'Sales';
```

![Employees in Finance or Sales](assets/task5-finance-sales.png)

The first employee in the Sales department returned was **lrodriqu**.

---

## Retrieve All Employees Not in IT

The IT department had already received the final update. I used `NOT` to exclude Information Technology employees and return everyone else who still needed the update applied to their machines.

```sql
SELECT *
FROM employees
WHERE NOT department = 'Information Technology';
```

![Employees not in IT](assets/task6-not-it.png)

This returned **161 employees** outside the IT department.

---

## Summary

In this investigation, I applied SQL filters using the `AND`, `OR`, and `NOT` operators to retrieve targeted records from the `log_in_attempts` and `employees` tables. I used `AND` to narrow results by combining multiple required conditions, `OR` to expand results across multiple possible values, and `NOT` to exclude specific groups. I also used the `LIKE` operator with the `%` wildcard to match partial string patterns, such as country codes and office locations. These queries enabled me to identify suspicious login activity and locate the employee machines that needed security updates.

| Query | Operator(s) | Result |
|-------|------------|--------|
| `WHERE login_time > '18:00' AND success = FALSE` | `AND` | 19 failed attempts |
| `WHERE login_date = '2022-05-09' OR login_date = '2022-05-08'` | `OR` | 75 attempts |
| `WHERE NOT country LIKE 'MEX%'` | `NOT`, `LIKE` | 144 attempts |
| `WHERE department = 'Marketing' AND office LIKE 'East%'` | `AND`, `LIKE` | First: elarson |
| `WHERE department = 'Finance' OR department = 'Sales'` | `OR` | First in Sales: lrodriqu |
| `WHERE NOT department = 'Information Technology'` | `NOT` | 161 employees |
