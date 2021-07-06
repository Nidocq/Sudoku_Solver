#!/usr/bin/env python3
from Board import *
board = Board()

def solve(row, col):
    print("board.grid[row] {}".format(board.grid[row]))
    for value in range(1, 9+1):
        print("Value is {} and is being set".format(value))
        board.grid[row][col] = value
        board.showGrid()
        if board.validPlacement(row, col):
            print("Recurse")
            if solve(row, col+1):
                return True
                print("Winning")
        else:
            continue