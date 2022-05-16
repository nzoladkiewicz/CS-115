# Name: Natalie Zoladkiewicz
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS 115 Homework 13

class Board(object):
    
    def __init__(self, width=7, height=6):
        '''
        Constructor that takes two named arguments, one for number of rows
        and one for number of columns. Default number of columns and rows
        is 7 and 6.
        '''
        self.width = width
        self.height = height
        board = []
        for i in range(1, self.height + 1):
            board += [[' '] * self.width]
        self.board = board

    def __str__(self):
        '''
        Returns a string representing the Board opbject that calls it.
        '''
        result = ''
        for row in range(self.height):
            result += '|'
            for col in range(self.width):
                result += self.board[row][col] + '|'
            result += '\n'
        result += '-' * (self.width*2+1) + '\n'
        result += '0 1 2 3 4 5 6'
        return result

    def allowsMove(self, col):
        '''
        Returns true if the calling Board object can allow a move into
        column c, False otherwise.
        '''
        room = 0
        if col < 0 or col >= self.width:
            return False
        elif self.board[0][col] != ' ':
            return False
        else:
            return True

    def addMove(self, col, ox):
        '''
        Adds an ox checker, where ox is a variable holding a string that 
        is either "X" or "O" into column col.
        '''
        if self.allowsMove(col) == True:
            x = (self.height - 1)
            while x > -1:
                if self.board[x][col] == ' ':
                    self.board[x][col] = ox
                    x = -1
                else:
                    x -= 1

    def setBoard(self, moveString):
        '''
        Takes in a string of columns and places alternating checkers in
        those columns, starting with "X"

        For example, call b.setBoard('012345') to see X's and O's
        alternate on the bottom row, or b.setBoard('000000') to
        see them alternate in the left column.

        moveString must be a string of integers
        '''
        nextCh = 'X'
        for colStr in moveString:
            col = int(colStr)
            if 0 <= col <= self.width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else:
                nextCh = 'X'

    def winsFor(self, ox):
        '''
        Returns True if the given checker "X" or "O", held in ox, has
        won the calling Board, False otherwise. Checks in 4 different
        directions: horizontally, vertically, diagonally from the top
        left to bottom right, and diagonally from the bottom right to
        the top left, respectively.
        '''
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.board[row][col] == ox and \
                self.board[row][col + 1] == ox and\
                self.board[row][col + 2]  == ox and \
                self.board[row][col + 3] == ox:
                    return True

        for row in range(self.height - 3):
            for col in range(self.width):
                if self.board[row][col] == ox and \
                self.board[row + 1][col] == ox and\
                self.board[row + 2][col]  == ox and \
                self.board[row + 3][col] == ox:
                    return True

        for col in range(self.width - 3):
            for row in range(self.height - 3):
                if self.board[row][col] == ox and \
                self.board[row + 1][col + 1] == ox and\
                self.board[row + 2][col + 2]  == ox and \
                self.board[row + 3][col + 3] == ox:
                    return True

        for row in range(self.height):
            for col in range(self.width - 3):
                if self.board[row][col] == ox and \
                self.board[row - 1][col + 1] == ox and\
                self.board[row - 2][col + 2]  == ox and \
                self.board[row - 3][col + 3] == ox:
                    return True
        return False

    def hostGame(self):
        '''
        When called from a connect four board object, will run a loop
        allowing the user(s) to play a game.
        '''
        print("Welcome to Connect Four!" + "\n")
        player = 0
        while(1):
            print(self)
            if player == 0:
                print('\n')
                choice = input("X's choice: ")
                self.addMove(int(choice), "X")
                print("\n")
                if self.winsFor('X') == True:
                    print("X wins! Congratulations!" + "\n")
                    print(self)
                    break
                else:
                    print(self)
                    player = 1
            if player == 1:
                print('\n')
                choice = input("O's choice: ")
                self.addMove(int(choice), "O")
                print('\n')
                if self.winsFor("O") == True:
                    print("O wins! Congratulatons!" + "\n")
                    print(self)
                    break
                else:
                    player = 0
