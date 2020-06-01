'''
Problem from Codewars (https://www.codewars.com/kata/59e19a747905df23cb000024)

Take a string str and return a string that is made up of the number of occurances of each english letter in str, followed by that letter. The string shouldn't contain zeros; leave them out. Ignore all case.

An empty string, or one with no letters, should return an empty string.

>>> letter_count("This is a test sentence.")
'1a1c4e1h2i2n4s4t'

>>> letter_count("")
''

>>> letter_count("555")
''

'''

def letter_count(s):

    # Replace the line below with all your code.
    pass


letter_count("This is a test sentence.")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
