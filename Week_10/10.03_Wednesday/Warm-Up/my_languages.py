'''
Problem from Codewars (https://www.codewars.com/kata/5b16490986b6d336c900007d)

You are given a dictionary containing some languages and your test results in the given languages. Return the list of languages where your test score is at least 60, in descending order of the results.

Note: the scores will always be unique (so no duplicate values)

>>> my_languages({"Java": 10, "Ruby": 80, "Python": 65})
['Ruby', 'Python']

>>> my_languages({"Hindi": 60, "Dutch" : 93, "Greek": 71})
['Dutch', 'Greek', 'Hindi']

>>> my_languages({"C++": 50, "ASM": 10, "Haskell": 20})
[]

'''

def my_languages(s):

    # Replace the line below with all your code.
    pass


my_languages({"Java": 10, "Ruby": 80, "Python": 65})


if __name__ == '__main__':
    import doctest
    doctest.testmod()
