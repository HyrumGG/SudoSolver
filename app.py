#!/usr/bin/python3
import sys

# Recursively solve sudoku
def recursive_solve(su):
    # Find the first empty entry on sudoku board and return row, col
    empty = get_empty_square(su)
    if empty is None:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        # If number i is valid so far
        if is_valid(su, empty, i):
            su[row][col] = i

            # Try solving rest of puzzle after filling in new value
            if recursive_solve(su):
                return True
            # If the rest of puzzle was not solved with position using index then reset that square
            su[row][col] = 0
        
    return False

# Find the first empty entry on sudoku board and return row, col
def get_empty_square(su):
    for i in range(len(su)):
        for j in range(len(su)):
            if su[i][j] == 0:
                return (i, j)

# Check if a number being placed in sudoku board follows the rules of the game
def is_valid(su, square, num):

    # Compare square with current column
    for i in range(len(su)):
        if su[i][square[1]] == num:
            return False

    # Compare square with current row
    for i in range(len(su)):
        if su[square[0]][i] == num:
            return False
    
    # Get the x and y coordinates for the 3x3 box the square is located in
    squareX = int(square[1] / 3) * 3
    squareY = int(square[0] / 3) * 3

    # Loop and compare numbers through the box containing square being tested
    for i in range(squareY, squareY + 3):
        for j in range(squareX, squareX + 3):
            if su[i][j] == num:
                return False
    return True

# Draws numbers from sudoku array onto their respective board positions in command line
def display(su):
    for i in range(len(su)):
        if i % 3 == 0 and i != 0:
            print() 
        for j in range(len(su[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(su[i][j], end = " ")
        print()

board=[]
if (len(sys.argv) > 1):
    fileName=sys.argv[1]
else:
    print('No file found in executable command')
    exit()

# Read sudoku board file and store each number in a 2d list
with open(fileName, 'r') as fp:
        line = []
        while True:
            c = fp.read(1)
            if not c:
                break
            if (c == '\n'):
                board.append(line)
                line = []
            else:
                line.append(int(c))

print('Entered Sudoku Board from file:')
display(board)
recursive_solve(board)
print('\n\n\nSolution to given Sudoku Board:')
display(board)