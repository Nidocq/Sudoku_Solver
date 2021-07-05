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

    def validPlacement(self, row, col):
        placement = self.grid[row][col]
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                print("y is : {}".format(y))
														      
                rowlist = []
                column = []
                square = []
                for lines in range(0, 9):    
                    print("Appending {}".format(self.grid[y][lines]))
                    if self.grid[y][lines] != 0:
                        rowlist.append(self.grid[y][lines])
                    
                    if self.grid[lines][x] != 0:
                        column.append(self.grid[lines][x])

                print(rowlist)
                if (len(rowlist) == len(set(rowlist))):
                    if len(column) == len(set(column)):
                        print("TURUURUEUUEU")
                        return True 
                    else:
                        print("NOT ELIGIBLEM")
                        return False
                else: 
                    print("NOT ELIGIBLE")
                    return False

                # for UDline in range(0, 9):
                #     print("UDline {}".format(self.grid[UDline][x]))
                #     if self.grid[UDline][x] != None:
                #         column.append(self.grid[UDline][x])
		


                # for poss_numb in range(1, 10):
                #     if poss_numb not in rowlist:
                #         if poss_numb not in column:
                #             if poss_numb not in square:
                #                 print(f"Number {self.grid[row][col]} is a valid number")
                #                 return True

										   