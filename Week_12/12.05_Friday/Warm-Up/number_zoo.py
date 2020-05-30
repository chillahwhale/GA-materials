'''
Problem from Codewars (https://www.codewars.com/kata/5276c18121e20900c0000235)

You're working in a number zoo, and it seems that one of the numbers has gone missing!

Zoo workers have no idea what number is missing, and are too incompetent to figure it out, so they're hiring you to do it for them.

In case the zoo loses another number, they want your program to work regardless of how many numbers there are in total.

Task:
Write a function that takes a shuffled list of unique numbers from 1 to n with one element missing (which can be any number including n). Return this missing number.

Note: huge lists can be tested.

>>> number_zoo([1, 2, 3, 4, 5])
6

>>> number_zoo([7, 3, 4, 5, 10, 11, 1, 6, 8, 9])
2

>>> number_zoo([4, 2, 3])
1

'''

def number_zoo(l):

    # Replace the line below with all your code.
    pass


number_zoo([1, 2, 3, 4, 5])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
