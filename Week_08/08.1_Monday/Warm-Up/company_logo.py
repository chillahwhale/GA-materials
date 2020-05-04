'''
Problem from Hackerrank (https://www.hackerrank.com/challenges/most-commons/problem)

A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
    - Print the three most common characters along with their occurrence count each on a separate line.
    - Sort in descending order of occurrence count.
    - If the occurrence count is the same, sort the characters in alphabetical order.

For example, according to the conditions described above, GOOGLE would have it's logo with the letters G, O, E.

>>> company_logo('aabbbccde')
b 3
a 2
c 2

>>> company_logo('GOOGLE')
G 2
O 2
E 1

>>> company_logo('generalassembly')
e 3
a 2
l 2

'''

def company_logo(s):

    # Replace the line below with all your code.
    pass


company_logo('aabbbccde')


if __name__ == '__main__':
    import doctest
    doctest.testmod()
