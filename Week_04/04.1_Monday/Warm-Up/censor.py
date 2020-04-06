'''
Write a function called censor() that takes two strings, text (a multi-word string) and word (a one-word
string), as input. It should return the text with the word you specified replaced with asterisks. 
Assume your input strings will only contain lowercase letters.
The number of asterisks you put should correspond to the number of letters in the censored word.

>>> censor("my dog eats cupcakes", "cupcakes")
'my dog eats ********'

>>> censor("I lost my glasses", "lost")
'I **** my glasses'

'''

def censor(text, word):
    
    # Replace the line below with all your code. Remember to return the requested data.
    pass


censor("It's peach season", "peach")

            
if __name__ == '__main__':
    import doctest
    doctest.testmod()