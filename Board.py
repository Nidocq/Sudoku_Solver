#!/usr/bin/env python3

class Board():
    def __init__(self):
        self.grid = [[6, 0, 0, 1, 0, 0, 0, 4, 0],
        [0, 0, 1, 8, 6, 0, 2, 0, 0],
        [8, 9, 0, 2, 5, 4, 0, 0, 0],
        [2, 0, 0, 3, 8, 0, 1, 5, 0],
        [0, 7, 0, 0, 2, 6, 9, 8, 3],
        [3, 8, 9, 7, 1, 0, 0, 0, 0],
        [0, 2, 8, 9, 0, 1, 6, 3, 4],
        [7, 0, 4, 6, 0, 0, 8, 0, 5],
        [0, 0, 0, 5, 4, 0, 7, 1, 2]]
        
        self.size = 9

    def validPlacement(self, row, col, value):
        print("is this valid?")

        for lines in range(0, self.size):    
            if self.grid[row][lines] == value:
                return False
            
            if self.grid[lines][col] == value:
                return False
    
        startRow = row - row % 3
        startCol = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[i + startRow][j + startCol] == value:
                    return False

        return True 

    def showGrid(self):
        for i in self.grid:
            print(i)