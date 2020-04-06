'''
Write a function called no_repeats() that takes in a string argument
and returns the first character in the string that does not have a 
duplicate elsewhere in the string. Assume there are only letters in 
the input string. Letters should count as duplicates regardless of 
capitalization.

>>> no_repeats("")
'No characters in an empty string.'

>>> no_repeats("t")
't'

>>> no_repeats("tt")
'No unique characters found.'

>>> no_repeats("tth")
'h'

>>> no_repeats("Do not go quietly into that dark night")
'q'

'''

def no_repeats(text):

    # Replace the line below with all your code. Remember to return the requested data.
    pass


no_repeats("Four score and seven years ago")


if __name__ == '__main__':
    import doctest
    doctest.testmod()