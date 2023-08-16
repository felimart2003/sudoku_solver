import numpy as np

sudoku_game_easy = [[0, 0, 0, 3, 0, 9, 0, 0, 6],
                    [3, 0, 0, 0, 0, 0, 8, 0, 0],
                    [0, 9, 5, 1, 6, 0, 0, 0, 0],
                    [0, 0, 0, 0, 5, 0 ,0, 2, 8],
                    [6, 0, 9, 4, 8, 1, 0, 3, 7],
                    [5, 8, 7, 9, 0, 2, 0, 6, 4],
                    [0, 0, 0, 0, 1, 0, 0, 0, 9],
                    [0, 3, 8, 0, 0, 4, 6, 0, 0],
                    [9, 0, 2, 0, 0, 0, 4, 0, 5]]

def is_candidate(grid, row, col, n):
    for i in range(9):
        #Check if n in row
        if grid[row][i] == n:
            return False
        #Check if n in col
        if grid[i][col] == n:
            return False
    
    #Defining box
    initial_row = row - (row % 3)
    initial_col = col - (col % 3)
    #Check if n in box
    for x in range(3):
        for y in range(3):
            if grid[initial_row + x][initial_col + y] == n:
                return False
    return True

def solve(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_candidate(grid, row, col, num):
                        grid[row][col] = num
                        if solve(grid):
                            return True
                        grid[row][col] = 0 #Backtrack
                return False
    print(np.array(grid))

print("Original Grid:")
print(np.array(sudoku_game_easy), "\n")
print("Solved Grid:")
solve(sudoku_game_easy)