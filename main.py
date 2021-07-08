#!/usr/bin/env python3
from Board import *
from BackTrack import *
import os 

def server_solve():
	if solve(0, 0, False):
		return board.showGrid()

def terminalSolve():
    if solve(0, 0, False): #Enable this for progressive solution
        os.system("clear")
        print(board.showGridTerminal())
        print("--- Winning ---")
    else:
        print("No solution was found")

if '__main__' == __name__:
	terminalSolve()
