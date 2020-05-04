# Advanced SQL - Subqueries
_**Author**: Boom Devahastin Na Ayudhya (DSI-NYC), adapted by Noelle Brown (DSI-DEN)_

Throughout this entire session, we'll be running the queries in PostgreSQL using pgAdmin4. This markdown file will just be a written record of what we've learned so that you'll have all of this in one location.

## What is a subquery?

Exactly what it sounds like: literally inception because **it's a query within a query**!

...What?! Sounds complicated...why do we need this?

**Motivation:** The `employees` table has a department column amongst other employee-specific information. The `departments` table shows information on each of the departments. However, some departments have recently turned over their entire team and so there may not be any employees listed in those departments. How can we figure out which departments did this?

TL;DR - How do we determine which departments exist in the `employees` table but not the `departments` table? Think through the logic in English first before you attempt to convert it to code.

_Answer:_

```SQL
SELECT DISTINCT department
FROM employees
WHERE department NOT IN (SELECT department
                         FROM departments)
```

### Subqueries in `WHERE`

How did we think about this?
- The output of a subquery is a "dataframe" (or rather a subset of a table).
- If we choose to extract just one column from a table using a query, we essentially have a list
- We've written WHERE statements before with `IN` and `NOT IN` and compared results to a list
- Connecting the dots: we can replace the list in a WHERE clause with a subquery to make things more dynamic

**Exercise 1:** Write a query that returns all information about employees who work in the Electronics division.

_Answer:_
```SQL

```

_**Short Note on Efficient Queries**_

Some `JOIN` commands (especially `INNER JOIN`) can be very computationally intensive. This is why sometimes we would prefer to write subqueries.

**Exercise 2:** Without using any kind of `JOIN`, find all employees who work in the Asia and Canada regions who make more than 13,000 dollars.

```SQL

```

### Subqueries in `SELECT`

Subqueries can show up almost anywhere in the query! If we want to compare values to a single value, we could include the result of a subquery in the `SELECT` clause. This is especially important when you want to construct some sort of **_benchmark_** (e.g. how much you have missed/beaten a sales target by, what the active returns of a mutual fund is compared to its benchmark index, etc.)  

**Exercise 3:** Show me the first_name, last_name, and salary of all employees next to the salary of the employee who earns the least at the company.

```SQL

```

#### _Short Note on Order of Execution in SQL Queries_

Across clauses, there is a sequence that queries follow. SQL queries will run FROM first, then WHERE and other filters, and then SELECT last. So in the exercise **below**, the `highest_salary` is already going to be calculated based on Asia and Canada employees because WHERE executes before SELECT.

However, within a clause (e.g. within SELECT) everything runs _**simultaneously**_, not sequentially! So you cannot use `highest_salary` in say a calculation for "difference" -- you will need to use the actual subquery in the calculation.

**Exercise 4:** Among all employees who work in Asia and Canada, calculate the how much less each employee makes compared to the highest earner across those regions.

_Answer:_
```SQL

```

### Subqueries using `ALL` keyword

**Motivation:** We've learned convenient functions like `MAX` and `MIN` which helps us find the highest or lowest value in a field/column.

```SQL
SELECT MAX(salary) FROM employees
```

What if your interviewer asked you to find the highest salary of all employees in the company **WITHOUT** using any built in SQL functions though?

```SQL
SELECT salary
FROM employees
WHERE salary >= ALL(SELECT salary
                    FROM employees)
```

Interview aside though, here's a more practical problem. You're not going to be able to use MAX or MIN when it comes to this situation:

**Exercise 5:** Find the mode salar(ies) of all employees in the company.

_Answer:_
```SQL

```

### Challenge Interview Question \#1

A retailer store information about all of its products in a `Products` table, which contain the following columns:
- `id`: the unique identification number for the product
- `name`: the name the product
- `manuf_id`: the identification number of the manufacturer we acquired this from
- `grade`: the quality score on a scale of 1 (bad) to 100 (good) of the product according to reviews.

Write a SQL query that returns the names of all products (there are ties) that have the **_SECOND_ lowest** score.

_Answer:_
```SQL

```

### Challenge Interview Question #2

A table called `eval` has 3 columns: <br>
- case_id (int) <br>
- timestamp (datetime) <br>
- score (int) <br>

But case_id is not unique. For a given case_id, there may be scores on different dates.

Write a query to get the score for each case_id at most recent date.

_Answer:_

```SQL

```
