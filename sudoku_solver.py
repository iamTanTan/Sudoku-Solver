import os

# function to print the sudoku board
def print_arr(array):
    for i in range(9):
        for j in range(9):
            print(array[i][j], end="--")
        print()


# determines what to do upon start/restart of the solver
def restart():
    print('''
Main Menu
=========
Type P to Play
''')

    choice = input('Input Here: ').upper()

    if choice != 'P':
        os.clear('cls')
        restart()

# determine if position is empty
def empty_position(arr, position):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                position[0] = row
                position[1] = col
                return True
    return False

# Determine acceptable placement of values based on Sudoku ruleset

def is_allowed_in_row(arr, row, num):
    for col in range(9):
        if arr[row][col] == num:
            return False
    return True


def is_allowed_in_col(arr, col, num):
    for row in range(9):
        if arr[row][col] == num:
            return False
    return True


def is_allowed_in_box(arr, num, pos):
    x_box = pos[0] // 3
    y_box = pos[1] // 3

    for i in range(x_box * 3, x_box * 3 + 3):
        for j in range(y_box * 3, y_box * 3 + 3):
            if arr[i][j] == num and (i, j) != pos:
                return False

    return True

def is_allowed(arr, row, col, num, pos):
    return is_allowed_in_box(arr, num, pos) and is_allowed_in_col(arr, col, num) and is_allowed_in_row(arr, row,
                                                                                                            num)
# Define a recursive function to sole the sudoku puzzle
def solve_sudoku(arr):

    pos =[0, 0]

    if empty_position(arr, pos):
        row = pos[0]
        col = pos[1]
    else:
        return True

    for num in range(1, 10):
        if is_allowed(arr, row, col, num, pos):
            arr[row][col] = num
            if solve_sudoku(arr):
                return True
            arr[row][col] = 0

    return False

# Example input data
arr = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
       [5, 2, 0, 0, 0, 0, 0, 0, 0],
       [0, 8, 7, 0, 0, 0, 0, 3, 1],
       [0, 0, 3, 0, 1, 0, 0, 8, 0],
       [9, 0, 0, 8, 6, 3, 0, 0, 5],
       [0, 5, 0, 0, 9, 0, 6, 0, 0],
       [1, 3, 0, 0, 0, 0, 2, 5, 0],
       [0, 0, 0, 0, 0, 0, 0, 7, 4],
       [0, 0, 5, 2, 0, 6, 3, 0, 0]]

restart()

if solve_sudoku(arr):
    print_arr(arr)
else:
    print("No solution exists")
