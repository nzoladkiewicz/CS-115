# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Lab 9

def update(c, n):
    '''
    Update starts with z = 0 and runs z = z**2 + c
    for a total of n times. It returns the final z.
    '''
    z = 0
    for i in range(n):
        z = z ** 2 + c
    return z

def inMSet(c, n):
    '''
    inMSet takes in
        c for the update step for z = z ** 2 + c
        n, the maximum number of times to run that step
    Then, it should return
        False as soon as abs(z) gets larger than 2
        True if abs(z) never gets larger than 2 (for n iterations)
    '''
    z = 0
    i = 0
    for i in range(n):
        z = z ** 2 + c
        if abs(z) > 2:
            return False
    return True

from cs5png import *

def weWantThisPixel(col, row):
    '''
    A function that returns True if we want the pixel
    at col, row and False otherwise.
    '''
    if col % 10 == 0 and row % 10 == 0:
        return True
    else:
        return False

def test(): 
    '''
    A function to demonstrate how 
    to create and save a png image 
    '''
    width = 300 
    height = 200 
    image = PNGImage(width, height) 
 
    # create a loop in order to draw some pixels 
     
    for col in range(width): 
        for row in range(height): 
            if weWantThisPixel( col, row ) == True: 
                image.plotPoint(col, row) 
 
    # we looped through every image pixel; we now write the file 
 
    image.saveFile()

def scale(pix, pixMax, floatMin, floatMax):
    '''
    Scale takes in 
        pix, the CURRENT pixel column (or row) 
        pixMax, the total # of pixel columns 
        floatMin, the min floating-point value 
        floatMax, the max floating-point value 
    Scale returns the floating-point value that corresponds to pix 
    '''
    return floatMin + (floatMax - floatMin) / pixMax * pix

def mset():
    '''
    Creates a 300x200 image of the Mandelbrot set
    '''
    width = 300
    height = 200
    image = PNGImage(width, height)

    for col in range(width):
        for row in range(height):
            y = scale(row, height, -1, 1)
            x = scale(col, width, -2, 1)
            c = x + y * 1j
            if inMSet(c, 25) == True:
                image.plotPoint(col, row)
    image.saveFile()
