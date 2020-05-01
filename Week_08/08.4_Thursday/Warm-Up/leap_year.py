'''
Problem from Hackerrank (https://www.hackerrank.com/challenges/write-a-function/problem)

We add a Leap Day on February 29, almost every four years. The leap day is an extra, or intercalary day and we add it to the shortest month of the year, February.
In the Gregorian calendar three criteria must be taken into account to identify leap years:
- The year can be evenly divided by 4, is a leap year, unless:
    - The year can be evenly divided by 100, it is NOT a leap year, unless:
        - The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.

Task
You are given the year, and you have to write a function to check if the year is leap or not.

>>> leap_year(1990)
False

>>> leap_year(2000)
True

>>> leap_year(2100)
False

'''

def leap_year(n):

    # Replace the line below with all your code.
    pass


leap_year(1990)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
