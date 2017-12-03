# -*- coding: utf-8 -*-
"""
Port of Bob Carpenter's Sudoku solver. Original
available at https://bob-carpenter.github.io/games/sudoku/java_sudoku.html
All credit goes to him, I just hacked a python version of it.
Created on Sun Dec  3 18:47:26 2017

@author: Stephen
"""

import numpy as np
from tco import with_continuations





def legal(i, j, v, cells):
    """
    Check the legality of a proposed move
    """
    # First check the row
    for k in range(9):
        if cells[i][k] == v:
            return False
    
    # Now check the column
    for k in range(9):
        if cells[k][j] == v:
            return False
        
    # Now check the box
    boxRowOffset = (i // 3) * 3
    boxColOffset = (j // 3) * 3
    for k in range(3):
        for m in range(3):
            if cells[boxRowOffset + k][boxColOffset + m] == v:
                return False
    
    # If we survived all of this, good
    return True

def parseProblem(initstate):
    """
    Initialise the board
    """
    cells = np.zeros((9,9),dtype=int)
    
    # For each input value we get, add it to the board
    for arg in initstate:
        i = int(arg[0])
        j = int(arg[1])
        v = int(arg[2])
        cells[i][j] = v
        
    return(cells)
        
def displayBoard(cells):
    """
    Pretty print of the board state
    """
    for i in range(9):
        if i % 3 == 0:
            print(' -----------------------')
        for j in range(9):
            if j % 3 == 0:
                print('| ', end='')
            val = ' ' if cells[i][j] == 0 else cells[i][j]
            print(val, end='')
            print(' ', end='')
        print('| ')
    print(' -----------------------')
            
    
@with_continuations()
def solve(i, j, cells, self = None):
    """
    Workhorse function, this makes a move and calls the 
    legality-checker. If it turns out to not be legal, blank the cell and
    return to the previous state
    """
    if i == 9:
        i = 0
        if j + 1 == 9:
            return True
    
    if cells[i][j] != 0:
        return self(i+1, j, cells)
    
    for val in range(1, 10):
        if legal(i, j, val, cells):
            cells[i][j] = val
            if self(i+1, j, cells):
                return True
    
    cells[i][j] = 0
    return False
    
if __name__ == '__main__':
    state = ['014', '023', '037', '069', '088', '125', 
             '143', '211', '263', '306', '342', '357', 
             '404', '427', '461', '483', '535', '544', 
             '589', '622', '673', '745', '764', '805', 
             '824', '851', '862', '876']
    board = parseProblem(state)
    solve(0, 0, board)
    displayBoard(board)