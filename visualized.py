import time, pygame

board = [
    [0,8,4,0,0,2,0,3,0],
    [2,0,7,8,3,1,0,0,9],
    [0,1,0,5,0,0,0,0,0],
    [0,7,8,0,1,0,9,0,2],
    [0,0,9,7,6,0,0,8,5],
    [5,0,1,9,0,0,3,0,0],
    [0,3,0,1,0,7,4,0,6],
    [0,0,6,2,0,0,0,0,0],
    [7,0,0,3,9,0,0,0,0]
]

# Recursively solve sudoku
def solve_sudoku(su):
    font = pygame.font.SysFont('Comic Sans', 50)
    window.fill((0,0,0))
    draw_sudoku()
    write_board(board)
    
    # Find the first empty entry on sudoku board and return row, col
    empty = get_empty_square(su)
    if empty is None:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if is_valid(su, empty, i):
            su[row][col] = i

            text = font.render(str(i), 1, (255,0,0))
            window.blit(text, ((26 + (col * 67)), (20 + (row * 67))))
            pygame.display.update()
            time.sleep(0.15)
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

# Draws the lines making up the sudoku board
def draw_sudoku():
    for i in range(0, 620, 67):
        if i % 3 == 0:
            pygame.draw.line(window, (128,128,128), (i, 0), (i, 620), 4)
        else:
            pygame.draw.line(window, (128,128,128), (i, 0), (i, 620))
    for j in range(0, 620, 67):
        if j % 3 == 0:
            pygame.draw.line(window, (128,128,128), (0, j), (620, j), 4)
        else:
            pygame.draw.line(window, (128,128,128), (0, j), (620, j))

# Draws numbers from sudoku array onto their respective board positions
def write_board(su):
    font = pygame.font.SysFont('Comic Sans', 50)
    for i in range(len(su)):
        for j in range(len(su)):
            if su[i][j] != 0:
                text = font.render(str(su[i][j]), 1, (255,255,255))
                window.blit(text, (26 + (67 * j) , 20 + (i * 67)))
    pygame.display.update()

window = pygame.display.set_mode((605, 605))
pygame.display.set_caption('SudoSolve')
pygame.font.init()
draw_sudoku()
write_board(board)
pygame.display.update()
solve_sudoku(board)
time.sleep(5)