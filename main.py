#!/usr/bin/env python3
from Board import *
from BackTrack import *

if solve(0, 0):
    print("--- Winning ---")
    board.showGrid()

else:
    print("No solution was found")
    board.showGrid()

    
