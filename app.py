board = [
    [0,0,0,0,0,0,0,2,8],
    [0,6,0,0,0,0,0,0,7],
    [0,0,0,4,0,1,0,0,0],
    [5,0,0,9,7,0,3,0,0],
    [2,0,4,0,0,8,0,0,0],
    [3,0,0,0,0,4,5,0,0],
    [1,3,0,0,9,0,0,0,0],
    [0,5,7,0,0,0,0,9,0],
    [0,0,8,3,1,7,0,0,0]
]

# Recursively solve sudoku
def solve_sudoku(su):
    # Find the first empty entry on sudoku board and return row, col
    empty = get_empty_square(su)
    if empty is None:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if is_valid(su, empty, i):
            su[row][col] = i

            # Try solving rest of puzzle after filling in new value
            if solve_sudoku(su):
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
    
    # Get the starting x and y coordinates for the 3x3 box the square is located in
    startPosX = int(square[1] / 3) * 3
    startPosY = int(square[0] / 3) * 3

    # Loop and compare numbers through the box containing square being tested
    for i in range(startPosY, startPosY + 3):
        for j in range(startPosX, startPosX + 3):
            if su[i][j] == num:
                return False
    return True

# Draws numbers from sudoku array onto their respective board positions
def print_sudoku(su):
    for i in range(len(su)):
        if i % 3 == 0 and i != 0:
            print("----------------------") 
        for j in range(len(su[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            print(su[i][j], end = " ")
        print()

print_sudoku(board)
print("\n\n\n")
solve_sudoku(board)
print_sudoku(board)