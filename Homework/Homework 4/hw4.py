# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Homework 4

def addRows(x):
    '''
        Helper function: adds the rows together.
    '''
    if x == []:
        return []
    elif len(x) == 1:
        return [1]
    else:
        return [x[0] + x[1]] + addRows(x[1:])

def pascal_row(number):
    '''
        Returns a list of elements found in a certain row of Pascal's Triangle.
    '''
    if number == 0:
        return [1]
    elif number == 1:
        return [1,1]
    else:
        return [1] + addRows(pascal_row(number - 1))

def pascal_triangle(n):
    '''
        Takes a single integer n as an input and returns a list of lists containing
        the values of all the rows up and including row n.
    '''
    if n == 0:
        return [[1]]
    elif n == 1:
        return [[1], [1,1]]
    else:
        return pascal_triangle(n - 1) + [pascal_row(n)]
    
def test_pascal_row():
    '''
        Tests the pascal_row function.
    '''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(6) == [1,6,15,20,15,6,1]
    assert pascal_row(10) == [1,10,45,120,210,252,210,120,45,10,1]
    assert pascal_row(15) == [1,15,105,455,1365,3003,5005,6435,6435,5005,3003,1365,455,105,15,1]

def test_pascal_triangle():
    '''
        Tests the pascal_triangle function.
    '''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1,1]]
    assert pascal_triangle(5) == [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1], [1,5,10,10,5,1]]
    assert pascal_triangle(10) == [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1], [1,5,10,10,5,1], [1,6,15,20,15,6,1], [1,7,21,35,35,21,7,1], [1,8,28,56,70,56,28,8,1], [1,9,36,84,126,126,84,36,9,1], [1,10,45,120,210,252,210,120,45,10,1]]
