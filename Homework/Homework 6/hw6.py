# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Homework 6

# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

from functools import reduce

def consecCount(S):
    '''
        Returns the number of consecutive integers.
    '''
    if S == '':
        return 0
    elif len(S) == 1:
        return 1
    elif S[0] == S[1]:
        return 1 + consecCount(S[1:])
    else:
        return 1

def listConsec(S):
    '''
        Returns a list of the values with consecutive matching integers.
    '''
    if S == '':
        return []
    else:
        return [consecCount(S)] + listConsec(S[consecCount(S):])

def checkRunLen(L):
    '''
        Checks the numbers against the given MAX_RUN_LENGTH.
    '''
    if L == []:
        return []
    if L[0] > MAX_RUN_LENGTH:
        L[0] = L[0] - MAX_RUN_LENGTH
        return [MAX_RUN_LENGTH, 0] + checkRunLen(L)
    else:
        return [L[0]] + checkRunLen(L[1:])

def add(x, y):
    '''
        Adds x and y.
    '''
    return x + y
    
def isOdd(n):
    '''
    Returns whether or not the integer argument is odd.
    '''
    if n % 2 == 0:
        return False
    return True
    
def numToBinary(n):
    '''
    Returns the string with the binary representation of non-negative integer n
    '''
    if n == 0:
        return ''
    elif (isOdd(n) == False):
        return numToBinary (n // 2) + '0'
    else:
        return numToBinary (n // 2) + '1'

def binaryToNum(s):
    '''
    Returns the integer corresponding to the binary representation in s
    '''
    if s == '':
        return 0
    elif isOdd(int(s[-1])):
        return 2 * binaryToNum(s[:-1])+1
    else:
        return 2 * binaryToNum(s[:-1])

def checkBlock(s):
    '''
        Returns the binary digits with the correct bits.
    '''
    if len(s) >= COMPRESSED_BLOCK_SIZE:
        return s
    else:
        return checkBlock('0'+s)
    
def compress(S):
    '''
        Takes a binary string of length 64 as input and returns another run-length
        encoded binary string as output.
    '''
    if S == '':
        return ''
    elif S[0] == '1':
        return '0' * COMPRESSED_BLOCK_SIZE + reduce(add, map(checkBlock, map(numToBinary, checkRunLen(listConsec(S)))))
    else:
        return reduce(add, map(checkBlock, map(numToBinary, checkRunLen(listConsec(S)))))

# Since the MAX_RUN_LENGTH is 9, we are allowed 9 bits. The maximum image size is 511x511 because the width and
# height can only be expressed with maximum of 9 bits. Next, you need to add the bits accounting for the metadata,
# which are the width plus height (9 + 9) = 18.
# Therefore, the total is 511 ** 511 + 18 = 26,1139.

def helperFunction(n, s):
    '''
        Helper function for uncompress function. Reverses RLE encoding method.
    '''
    if s == '':
        return ''
    elif n == 1:
        return binaryToNum(s[:5]) * '1' + helperFunction(0, s[5:])
    elif n == 0:
        return binaryToNum(s[:5]) * '0' + helperFunction(1, s[5:])
    
def uncompress(S):
    '''
        Returns the uncompressed value of S.
    '''
    if S == '':
        return 0
    else:
        return helperFunction(0, S)

def compression(s):
    '''
        Returns the ratio of a compressed string and the original.
    '''
    return len(compress(s))/len(s)

# Laicompress/Laiuncompress

# The reason why Laicompress cannot work is because when an object is compressed, it cannot be fully reverted
# to its original form. The result of uncompressing a compressed object is a near approximation of the
# original object, but it does not recover the object completely. For example, if I take a sheet of paper and
# wrinkle it, then I straighten all the wrinkles, it does not revert to a new sheet of paper. It still has a
# history of being wrinkled.
