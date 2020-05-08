'''
Problem from Codewars (https://www.codewars.com/kata/5803a6d8db07c59fff00015f)

Challenge: Given two strings in the arguments "string" and "prefix", determine if "string" starts with the "prefix" string. Return 1 if true, 0 if false.

Notes:
    - For this problem, an empty "prefix" string should always return 1 (true) for any value of "string".
    - If the length of the "prefix" string is greater than the length of the "string", return 0.
    - The check should be case-sensitive, i.e. starts_with("hello", "HE") should return 0, whereas starts_with("hello", "he") should return 1.
    - No characters should be ignored and/or omitted during the test, e.g. whitespace characters should not be ignored.

>>> starts_with("hello world!", "hello")
1

>>> starts_with("hello world!", "HELLO")
0

>>> starts_with("nowai", "nowaisir")
0

'''

def starts_with(string, prefix):

    # Replace the line below with all your code.
    pass


starts_with("hello world!", "hello")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
