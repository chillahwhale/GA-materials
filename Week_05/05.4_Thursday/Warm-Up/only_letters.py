'''Write a function called only_letters() that takes in a string of words separated by spaces.
Assume the words have both lower- and uppercase letters, numbers and punctuation in them. 
Strip out all nonalphabetic characters, then sort the words in alphabetical order (ignore 
capitalization) and return the first word. 

>>> only_letters("c$c. %ba! bb#?")
'ba'

>>> only_letters("M3ery&&l St%r3e3ep i#s aw4eso0me?!")
'awesome'

'''

import re

def only_letters(text):

    # Replace the line below with all your code. Remember to return the requested data.
    pass


only_letters("c$c. %ba! bb#?")


if __name__ == '__main__':
    import doctest
    doctest.testmod()

