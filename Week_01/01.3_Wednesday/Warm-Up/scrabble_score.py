'''
From the Codecademy Python track.

Scrabble is a game where players get points by spelling words. 
Words are scored by adding together the point values of each individual letter. 
Leave out the double and triple letter and word scores for now.

A dictionary containing all of the letters in the alphabet 
with their corresponding Scrabble point values is provided.

For example: the word "Helix" would score 15 points 
due to the sum of the letters: 4 + 1 + 1 + 1 + 8.

Write a function called scrabble_score() that takes a word (as a string) as input 
and returns the equivalent scrabble score for that word.

Assume your input is only one word containing only letters.
Your function should work even if the letters you get are uppercase, lowercase, or a mix.
Assume that you're only given non-empty strings.

>>> scrabble_score("orange")
7

>>> scrabble_score("NINJA")
12

>>> scrabble_score("Write")
8

'''

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}

         
def scrabble_score(word):

    # Replace the line below with all your code. Remember to return the requested data.
    pass



if __name__ == '__main__':
    import doctest
    doctest.testmod()