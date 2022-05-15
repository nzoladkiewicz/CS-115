# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Lab 2

from functools import reduce

def dot(L, K):
    ''' 
    Returns dot product given lists L and K 
    '''
    if L == []:
        return 0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])

def explode(s):
    ''' 
    Separates a list into characters 
    '''
    if s == '':
        return []
    else:
        letterOne = list(s[0])
        return letterOne + explode(s[1:])

def ind(e,L):
    ''' 
    Returns index of a value inside list L 
    '''
    if e == L[0]:
        return 0
    else:
        return 1 + ind(e, L[1:])
    if L == []:
            return 1

def removeAll(e,L):
    ''' 
    Removes all instances of a given value in the list L 
    '''
    if e in L:
        if e == L[0]:
            case = [L[1]] + removeAll(e, L[2:])
        else:
            case = [L[0]] + removeAll(e, L[1:])
        return case
    else:
        return L

def myFilter(f,L):
    ''' 
    Filters instances of elements in list L 
    '''
    if not L:
        return []
    return [f(L[0])] + myFilter(f, L[1:])

def deepReverse(L):
    ''' 
    Reverses list 
    '''
    if not isinstance(L, list):
        return L
    else:
        result = []
        L = L[::-1]
  
    for i in L:   
        result.append(deepReverse(i))
  
    return result
