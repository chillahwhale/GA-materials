# Advanced SQL - Special Functions
_**Author**: Boom Devahastin Na Ayudhya (DSI-NYC), adapted by Noelle Brown (DSI-DEN)_

Throughout this entire session, we'll be running the queries in PostgreSQL using pgAdmin4. This markdown file will just be a written record of what we've learned so that you'll have all of these functions in one location.

Note that **THIS IS BY NO MEANS AN EXHAUSTIVE LIST** -- these are cherry-picked for ones that are commonly asked in interviews and/or useful on the job.

## Contents
**I. String Manipulation**
- [`UPPER()`](#UPPER())
- [`LOWER()`](#LOWER())
- [`INITCAP()`](#LOWER())
- [`LENGTH()`](#LENGTH())
- [`TRIM()`](#TRIM())
- [`SUBSTRING()`](#SUBSTRING())
- [Concatenation Methods](#Concatenation)
- [`REPLACE()`](#REPLACE())
- [`COALESCE()`](#COALESCE())

**II. Conditionals**
- [Boolean Statements](#Boolean-Statements)
- [`CASE WHEN`](#CASE-WHEN)

**III. Date-Time Manipulation**
- [Type Conversion](#Type-Conversion)
- [`EXTRACT()`](#EXTRACT())

## I. String Manipulation

### `LOWER()`
This is the same as the `.lower()` method for strings in Python used to convert every letter in a string to lower case

_Example_: Convert all letters of the string `HeLlO, wOrLd!` to lower case
```SQL
SELECT LOWER('HeLlO, wOrLd!')
```

**DISCUSS:** Why do you think this can be useful? Does case matter in SQL?

**THINK:** Consider the following queries. Which of these will run? <br>
(A) `SELECT first_name FROM people WHERE first_name = 'eddard'` <br>
(B) `select first_name from people where first_name = 'eddard'` <br>
(C) `SELECT first_name FROM people WHERE first_name = 'Eddard'` <br>
(D) `select first_name from people where first_name = 'Eddard'`

**EXERCISE 1:** Write a query that returns the first name employees in Canada, but make sure the letters are all in lower case.

_Answer:_

```SQL
SELECT LOWER(e.first_name)
FROM employees AS e
    INNER JOIN regions AS r ON e.region_id = r.region_id
WHERE r.country = 'Canada'
```

### `UPPER()`
For completeness, this is the same as the `.upper()` method for strings in Python used to capitalize every letter in a string

_Example_: Capitalize all letters of the string `Hello World`

```SQL
SELECT UPPER('Hello, world!')
```

**EXERCISE 2:** Write a query that capitalizes every letter of every department name from the `departments` table.

_Answer:_

```SQL
SELECT UPPER(d.department)
FROM departments AS d
```

### `INITCAP()`
This is the same as the `.capitalize()` method for strings in Python that is used to convert the first letter to upper case.

**EXERCISE 3:** Write a SQL query that returns the first name and department of all employees whose first name begins with the prefix "an-" or "An-", but make sure that only the first letter is capitalized in both of those columns.

```SQL
SELECT INITCAP(e.first_name), INITCAP(e.department)
FROM employees AS e
WHERE e.first_name ILIKE 'an%'
```

### `LENGTH()`
This is the same as the `len()` function in Python. However, since we don't have lists or tuples in SQL, this is only applicable to objects with characters.

**EXERCISE 4:** Write a query that displays the first name and department of employees that work in the Sports department, but only if their first name is at least 6 characters long.

_Answer:_

```SQL
SELECT e.first_name, e.department
FROM employees AS e
WHERE e.department = 'Sports' AND LENGTH(e.first_name) >= 6
```

### `TRIM()`
This is the same as the `.strip()` method for strings in Python that eliminates leading and trailing white spaces.

_Example:_ Write a query that strips out the white space from the string `'     Hello, world!     '`

```SQL
SELECT TRIM('     Hello, world!     ')
```

### `SUBSTRING()`
Python doesn't have a function that extracts a substring since we can just do it by directly indexing through the string. If you're familiar with R though, then you'll recognize this is similar to the `substr()` function.

Syntax for this function:

```SQL
SELECT SUBSTRING(string_column FROM <start_position> FOR <num_characters_ahead>)
```
OR
```SQL
SELECT SUBSTRING(string_column, <start_position>, <num_characters_ahead>)
```

**Example #1:**
```SQL
SELECT SUBSTRING('Hello there, friend! Hehe.' FROM 1 FOR 5)
```
OR
```SQL
SELECT SUBSTRING('Hello there, friend! Hehe.', 1, 5)
```
will return `'Hello'`

**Example #2:**
```SQL
SELECT SUBSTRING('Hello there, friend! Hehe.' FROM 14)
```
OR
```SQL
SELECT SUBSTRING('Hello there, friend! Hehe.', 14)
```
will return `'friend! Hehe.`

### Concatenation

This is the equivalent of string concatenation in Python using `+`. The `+` in Python is replaced by `||` in PostgreSQL. Alternatively, you can use the `CONCAT()` function.

_Example:_ Write a query that prints every employees's full name (i.e. first name then last name)
```SQL
SELECT INITCAP(e.first_name) || ' ' || INITCAP(e.last_name)
FROM employees e
```

**EXERCISE 5:** Write a query that automatically generates the sentence `<employee first name> works in the <department> department.`

_Answer:_
```SQL
SELECT INITCAP(e.first_name) || ' works in the ' || e.department || ' department.'
FROM employees e
```

### `REPLACE()`

This is the equivalent of the `.replace()` method for strings in Python and the `gsub()` function in R.

_Example:_ Replace the 'Jewelry' department with 'Bling' in the employee table.
```SQL
SELECT first_name,
       REPLACE(department, 'Jewelry', 'Bling') AS new_dept
FROM employees
```

Does the function work when replacing `NULL` values though? Try this and let me know what you see
```SQL
SELECT first_name,
       REPLACE(email, NULL, 'missing') AS new_email
FROM employees
```

## `COALESCE()`
This is an extremely powerful function that lets us handle missing values on a column-by-column basis.

The syntax is pretty straight forward for this one:
```SQL
COALESCE(<column_name>, <fill_value>)
```

Alright, your turn!

**EXERCISE 6**: Write a query that prints every employees's first name in one column and their email in another, but make sure to replace all `NULL` emails with `¯\_(ツ)_/¯`.

_Answer:_
```SQL
SELECT first_name,
       COALESCE(email, '¯\_(ツ)_/¯') AS cleaned_email
FROM employees
```

## II. Conditionals

### Boolean Statements

**Review Discussion:** What is a Boolean statement? Can you think of an example where you've used this before?

We can also include Booleans to create dummy variables in SQL on the fly.

_Example:_
```SQL
SELECT  e.first_name,
        e.last_name,
        e.salary >= 100000 AS "sixfigs"
FROM employees AS e
```

## `CASE WHEN`
This is the equivalent of if-elif-else statements, except embedded into a query. This takes Boolean Statements to the next level by allowing you to customize what happens on a case-by-case basis

_Example_: Write a query that groups salary amounts into 'high' (100,000+), 'medium' (50,000-99,999), 'low' (<50,000)

```SQL
SELECT  e.first_name,
        e.salary,
        CASE WHEN e.salary >= 100000 THEN 'high'                 -- if
             WHEN e.salary BETWEEN 50000 AND 100000 THEN 'medium'   -- elif
             ELSE 'low'                                   -- else
             END AS "salary_group"                           -- end it! (and rename if you want)
FROM employees AS e
```

## III. Date-Time Manipulation

### Type Conversion
_(Complete documentation here: https://www.postgresql.org/docs/8.1/functions-formatting.html)_

#### `to_timestamp()`
If you have a string that's both date and time and want to convert it to a datetime objecttime want the date and time,
```SQL
SELECT to_timestamp('2019 May 13 15:00:05', 'YYYY-MON-DD HH24:MI:SS')
```

#### `to_date()`
If you have a string where you want to convert to a date without any timestamp
```SQL
SELECT to_date('2019 May 13 14:00:58', 'YYYY-MON-DD')
```

#### `current_date`
You can use this to pull the current date from your computer's clock and manipulate it as you desired.
```SQL
SELECT current_date
```

**EXERCISE 7:** Write a query that returns what the date was 21 days ago

_Answer:_

```SQL
SELECT current_date - 21
```

### `EXTRACT()`
_(More datetime manipulation functions: https://www.postgresql.org/docs/9.1/functions-datetime.html)_

If you want to extract certain parts of a datetime object, this function is MAGICAL!

```SQL
SELECT current_timestamp AS today,
	   EXTRACT(day from current_date) AS "Day",
	   EXTRACT(month from current_date) AS "Month",
	   EXTRACT(year from current_timestamp) AS "Year",
	   EXTRACT(hour from current_timestamp) AS "Hour",
	   EXTRACT(minute from current_timestamp) AS "Minute"
```

### Challenge: Interview Questions
Lyft recently acquired the rights to add CitiBike to its app as part of its Bikes & Scooters business. You are a Data Scientist studying a `rides` table containing data on completed trips taken by riders, and a `deployed_bikes` table which contains information on the locations where each unique bike is deployed (i.e. where it is stationed).

**`rides`** schema:
- `ride_id`: int **[PRIMARY KEY]**
- `bike_id`: int
- `ride_datetime`: string
- `duration`: int

**`deployed_bikes`** schema:
- `bike_id`: int **[PRIMARY KEY]**
- `deploy_location`: string

**EXERCISE 8: For the last week, find the number of rides that occurred on each date, ordered from most recent to least recent**

_Answer:_
```SQL
SELECT  ride_datetime,
        COUNT(ride_id)
FROM rides
WHERE to_date(ride_datetime, 'YYYY-MON-DD') BETWEEN (current_date - 7) AND (current_date - 1)
GROUP BY ride_datetime
ORDER BY ride_datetime DESC
```

**EXERCISE 9: Which deployment location did the best over the past week?**

_Answer:_

```SQL
SELECT  d.deploy_location,
        COUNT(r.ride_id)
FROM rides AS r
    INNER JOIN deployed_bikes AS d ON r.bike_id = d.bike_id
WHERE to_date(ride_date, 'YYYY-MON-DD') BETWEEN (current_date - 7) AND (current_date - 1)
GROUP BY d.deploy_location
ORDER BY COUNT(ride_id) DESC
LIMIT 1
```

Note this is actually _not the best_ solution since it only returns 1 row and doesn't account for the case where we have more than 1 deployment location with tied highest ride counts. The best solution would require a subquery, which I won't be covering until Advanced SQL II (Subqueries), so you can try revisiting this question and coming up with the best solution after we go through that!
