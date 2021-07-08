#!/usr/bin/env python3
from Board import *
import time
import os

board = Board()

def solve(row, col, progressive):
    # print("\nNew line")
    # print(f"{row=}", end='')
    # print(f"{col=}")
    if (row == board.size - 1 and col == board.size):
        return True

    if col == board.size:
        col = 0
        row += 1
    
    for value in range(1, board.size+1):
        if board.grid[row][col] != 0:
            return solve(row, col+1, progressive)

        if board.validPlacement(row, col, value):
            board.grid[row][col] = value
            # if progressive:
            #     time.sleep(0.1)
            #     os.system("clear")
            #     board.showGrid()
    

            if solve(row, col+1, progressive):
                return True

        board.grid[row][col] = 0

    return False