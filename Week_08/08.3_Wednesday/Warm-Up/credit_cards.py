'''
Problem from Hackerrank (https://www.hackerrank.com/challenges/validating-credit-card-number/problem)

You and Fredrick are good friends. Yesterday, Fredrick received credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. He is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:
    - It must start with a 4, 5 or 6.
    - It must contain exactly 16 digits.
    - It must only consist of digits (0-9).
    - It may have digits in groups of 4, separated by one hyphen "-".
    - It must NOT use any other separator like ' ' , '_', etc.
    - It must NOT have 4 or more consecutive repeated digits.

>>> credit_cards(4253625879615786)
'Valid'

>>> credit_cards(4424444424442444)
'Invalid'

>>> credit_cards('44244x4424442444')
'Invalid'

'''

def credit_cards(n):

    # Replace the line below with all your code.
    pass


credit_cards(4253625879615786)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
