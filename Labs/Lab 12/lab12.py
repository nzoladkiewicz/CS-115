# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Lab 12

from math import sqrt

class QuadraticEquation:
    def __init__(self, a, b, c):
        if (a == 0):
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")

        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c

    def discriminant(self):
        b = self.getB()
        a = self.getA()
        c = self.getC()

        return b ** 2 - 4 * a * c

    def root1(self):
        disc = self.discriminant()
        b = self.getB()
        a = self.getA()
        c = self.getC()
        if disc < 0:
            return None
        return (-1 * b + sqrt(disc))/(2*a)

    def root2(self):
        disc = self.discriminant()
        b = self.getB()
        a = self.getA()
        c = self.getC()
        if disc < 0:
            return None
        return (-1 * b - sqrt(disc))/(2*a)

    def __str__(self):
        a = self.getA()
        b = self.getB()
        c = self.getC()

        parta = ""
        partb = ""
        partc = ""

        if a < 0:
            parta += '-'
        elif a != 1:
            parta += str(a)
        parta += 'x^2'

        if b == 1:
            partb += ' + x'
        elif b == -1:
            partb += ' - x'
        elif b > 0:
            partb += ' + ' + str(b) + 'x'
        elif b < 0:
            partb += ' ' + str(b)[0] + ' ' + str(b)[1:] + 'x'

        if c == 1:
            partc += ' + 1.0'
        elif c == -1:
            partc += ' - 1.0'
        elif c > 0:
            partc += ' + ' + str(c)
        elif c < 0:
            partc += ' ' + str(c)[0] + ' ' + str(c)[1:]

        return parta + partb + partc + ' = 0'
