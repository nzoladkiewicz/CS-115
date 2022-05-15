# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Lab 10

import random, sys

def createOneRow(width):
    '''
    Returns one row of zeros of width "width"
    '''
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    '''
    Returns a 2d array with "height" rows and "width" cols
    '''
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard(A):
    '''
    This function prints the 2d list-of-lists
    A without  spaces
    '''
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

def diagonalize(width, height):
    '''
    Creates an empty board and then modifies it
    so that it has a diagonali strip of "on" cells.
    '''
    A = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    '''
    Returns a 2d array of all live cells except for a one-cell-wide
    boarder of empty cells around the edge of the 2d array
    '''
    array = []
    for i in range(h):
        if i != 0 and i != h-1:
            row = []
            for j in range(w):
                if j != 0 and j != w-1:
                    row.append(1)
                else:
                    row.append(0)
            array.append(row)
        else:
            array.append([0] * w)
    return array

def randomCells(w,h):
    '''
    Returns an array of randomly-assigned 1's and 0's except that the
    outer edge of the array is still all 0's
    '''
    array = []
    for i in range(h):
        row = []
        for j in range(w):
            if i == 0 or j == 0 or i == h-1 or j == w-1:
                row.append(0)
        array.append(row)
    return array

def copy(A):
    '''
    Deep copy of A
    '''
    array = []
    for x in A:
        row = []
        for y in x:
            row.append(y)
        array.append(row)
    return array

def innerReverse(A):
    '''
    Reverses the values in the old array
    '''
    array = []
    for x in A:
        row = []
        for y in x:
            if x == 0 or y == 0 or x == len(A) - 1 or y == len(A[x])-1:
                row.append(0)
                continue
            row.append(1 if y == 0 else 0)
        array.append(row)
    return array

def next_life_generation(A):
    '''
    Makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    '''
    array = []
    i = j = 0
    for i in range(len(A)):
        row = []
        for j in range(len(A[i])):
            sum = 0
            if i == 0 or i == len(A) - 1 or j == 0 or j == len(A[i]) - 1:
                row.append(0*j)
                continue
            for neighbor_i in range(i-1, i+2):
                for neighbor_j in range(j-1, j+2):
                    sum += A[neighbor_i][neighbor_j]
            if A[i][j] == 1:
                row.append(1 if sum - A[i][j] ==3 or sum - A[i][j] == 2 else 0)
            else:
                row.append(1 if sum - A[i][j] == 3 else 0)
        array.append(row)
    return array
