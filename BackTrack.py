#!/usr/bin/env python3
from Board import *
board = Board()

row = 0
col = 0

def solve(row, col):
    print("board.grid[row] {}".format(board.grid[row]))
    for value in range(1, 9+1):
        print("board.grid[row][col] {}".format(board.grid[row][col]))
        if board.grid[row][col] == 0:
            print("Value is {} and is being set".format(value))
            board.grid[row][col] = value
            if board.validPlacement(row, col):
                print("Recurse")
                if solve(row, col+1):
                    return True
        else:
            continue

#commenting