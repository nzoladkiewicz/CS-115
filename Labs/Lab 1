# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Lab 1

from math import factorial
from functools import reduce

def inverse(x):
    return 1/x

def add(x,y):
    return x+y

def e(n):
    list1 = list(range(0, n+1))
    factList = list(map(factorial, list1))
    invList = list(map(inverse, factList))
    return reduce(add, invList)
