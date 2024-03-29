# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Lab 6

def isOdd(n):
    '''
    Returns whether or not the integer argument is odd.
    '''
    if n % 2 == 0:
        return False
    else:
        return True
    
# 101010 is the base-2 representation of the number 42.
# Given an add base-10 number, the least significant bit will be 1.
# Given an even base-10 number, the least significant bit will be 2.
# If you change the ending of a end of a binary number, you will change
#   the value of it entirely. In base-2 number 1010, eliminating the
#   least-significant bit changes the value of the number since the
#   1s represent 8 and 2 meanwhile in 101 the 1s represent 4 and 1.

def numToBinary(n):
    '''
    Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.
    '''
    if n == 0:
        return ""
    elif isOdd(n):
        return numToBinary(n//2) + "1"
    else:
        return numToBinary(n/2) + "0"

def binaryToNum(s):
    '''
    Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.
    '''
    if s == "":
        return 0
    elif s[-1] == "1":
        return (2 * binaryToNum(s[:-1])) + 1
    else:
        return (2*binaryToNum(s[:-1])) + 0
    

def increment(s):
    '''
    Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.
    '''
    if s == "11111111":
        return "0" * 8
    n = binaryToNum(s)
    x = n + 1
    y = numToBinary(x)
    return ("0" * (8 - len(y))) + y

def count(s, n):
    '''
    Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.
    '''
    print(s)
    if n == 0:
        return 0
    else:
        return count(increment(s), n - 1)

def numToTernary(n):
    '''
    Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.
    '''
    if n == 0:
        return ""
    else:
        return numToTernary(int(n / 3)) + str(n%3)

def ternaryToNum(s):
    '''
    Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.
    '''
    if s == "":
        return 0
    else:
        return ternaryToNum(s[:-1]) * 3 + int(s[-1])
