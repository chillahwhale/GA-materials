'''
Problem from Codewars (https://www.codewars.com/kata/55aea0a123c33fa3400000e7)

Sort array by last character. Complete the function to sort a given array or list by last character of elements. Element can be an integer or a string.

Example:
['acvd', 'bcc']  -->  ['bcc', 'acvd']
The last characters of the strings are d and c. As c comes before d, sorting by last character will give ['bcc', 'acvd'].

If two elements don't differ in the last character, then they should be sorted by the order they come in the array.

>>> sort_array(['acvd', 'bcc'])
['bcc', 'acvd']

>>> sort_array(['general', 'assembly'])
['general', 'assembly']

>>> sort_array(['this', 'is', 'a', 'test', 'example'])
['a', 'example', 'this', 'is', 'test']

'''

def sort_array(a):

    # Replace the line below with all your code.
    pass


sort_array(['acvd', 'bcc'])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
