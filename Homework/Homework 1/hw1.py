# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Homework 1

from functools import reduce

def mult(x, y):
    """Returns the product of x and y"""
    return x*y

def factorial(n):
    """Returns the factorial of an input provided by user"""
    return reduce(mult, range(1, n+1))

def mean(L):
    """Returns the mean of a list"""
    return reduce(lambda x, y: x + y, L)//len(L)
