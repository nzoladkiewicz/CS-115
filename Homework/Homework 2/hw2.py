# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Homework 2

from functools import reduce
import sys
# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Functions implemented below:
def letterScore(letter, scorelist):
    '''
        Converts a single letter into its corresponding "scrabble score" value according
        to a list of scrabble scores provided by user.

    '''
    if scorelist == []:
        return 0
    
    first = scorelist[0][0]
    rest = scorelist[1:]

    if first == letter:
        return scorelist[0][1]
    else:
        return letterScore(letter, rest)

def wordScore(S, scorelist):
    '''
        Converts a lowercase string into its reduced corresponding "scrabble score" value
        according to a list of scrabble scores provided by user.
    '''
    if scorelist == [] or len(S) == 0:
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def dictScore(dictionary, scores):
    '''
        Takes a list of strings from a dictionary and returns a list of the string
        with its scrabble score.
    '''
    if dictionary == []:
        return []
    else:
        return [[dictionary[0], wordScore(dictionary[0], scores)]]  + dictScore(dictionary[1:], scores)

def listCharacters(list1):
    '''
        Given a list of characters in a list, function will concatenate into one string.
    '''
    if list1 == []:
        return ""
    else:
        return list1[0] + listCharacters(list1[1:])

def addScore(word):
    '''
        Converts a word into a list containing the word and its corresponding scrabble score.
    '''
    return [word] + [wordScore(word, scrabbleScores)]

def stringToList(S):
    '''
        Converts characters in a string to a list separated by commas.
    '''
    if S == "":
        return []
    else:
        return [S[0]] + stringToList(S[1:])

def remove(character, lst):
    '''
        Removes inputted character from list. To recurse through later Rack and remove specific
        characters.
    '''
    if lst == []:
        return []
    elif character == lst[0]:
        return lst[1:]
    else:
        return [lst[0]] + remove(character, lst[1:])

def checkDict(Rack, lettersList):
    '''
        Checks if any words can be formed with the Rack provided.
    '''
    if lettersList == []:
        return True
    elif Rack == []:
        return False

    # Recursive Cases
    if Rack[0] in lettersList:
        return checkDict(Rack[1:], remove(Rack[0], lettersList))
    else: 
        return checkDict(Rack[1:], lettersList)

def scoreList(Rack):
    '''
        Returns all the combinations of words and their scrabble scores that can be created
        from the characters provided.
    '''
    return list(map(addScore, list(map(listCharacters, filter(lambda x: checkDict(Rack, x), list(map(stringToList, Dictionary)))))))

def bestWord(Rack):
    '''
        Picks the word with the largest scrabble score and returns it in a list containing
        the word and its score.
    '''

    def biggestScore(scores, biggest):
        '''
            Helper function for bestWord(). Goes through combinations and selects the
            word with the highest score.
        '''
        if scores == []:
            return biggest
        elif scores[0][1] > biggest[1]:
            return biggestScore(scores[1:], scores[0])
        else:
            return biggestScore(scores[1:], biggest)
    return biggestScore(scoreList(Rack), ["", 0])
