'''
Problem from Codewars (https://www.codewars.com/kata/56b7f2f3f18876033f000307)

Your function receives an array of integers as input. Your task is to determine whether the numbers are in ascending order. An array is said to be in ascending order if there are no two adjacent integers where the left integer exceeds the right integer in value.

You may assume that all inputs are valid, i.e. non-empty arrays containing only integers.

Note that an array of 1 integer is automatically considered to be sorted in ascending order since all (zero) adjacent pairs of integers satisfy the condition that the left integer does not exceed the right integer in value. An empty list is considered a degenerate case and therefore will not be tested.

>>> in_order([1,2,4,7,19])
True

>>> in_order([1,6,10,18,2,4,20])
False

>>> in_order([9,8,7,6,5,4,3,2,1])
False

'''

def in_order(l):

    # Replace the line below with all your code.
    pass


in_order([1,2,4,7,19])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
