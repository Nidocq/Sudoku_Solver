#!/usr/bin/env python3
from Board import *
from BackTrack import *
import os 

if solve(0, 0, True): #Enable this for progressive solution
    os.system("clear")
    board.showGrid()
    print("--- Winning ---")
else:
    print("No solution was found")

    
