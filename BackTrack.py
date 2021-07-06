#!/usr/bin/env python3
from Board import *
board = Board()

def solve(row, col):
    print("\nNew line")
    print(f"{row=}", end='')
    print(f"{col=}")
    if (row == board.size - 1 and col == board.size):
        return True

    if col == board.size:
        col = 0
        row += 1
    
    for value in range(1, board.size+1):
        if board.grid[row][col] != 0:
            return solve(row, col+1)

        if board.validPlacement(row, col, value):
            print("Value is {} and is being set".format(value))
            board.grid[row][col] = value

            if solve(row, col+1):
                return True

        board.grid[row][col] = 0

    return False