#!/usr/bin/env python3
"""Sudoku Solver
"""

import numpy as np
import time

demo_grid = np.array(
    [[0, 0, 4, 0, 5, 0, 0, 0, 0],
     [9, 0, 0, 7, 3, 4, 6, 0, 0],
     [0, 0, 3, 0, 2, 1, 0, 4, 9],
     [0, 3, 5, 0, 9, 0, 4, 8, 0],
     [0, 9, 0, 0, 0, 0, 0, 3, 0],
     [0, 7, 6, 0, 1, 0, 9, 2, 0],
     [3, 1, 0, 9, 7, 0, 2, 0, 0],
     [0, 0, 9, 1, 8, 2, 0, 0, 3],
     [0, 0, 0, 0, 6, 0, 1, 0, 0]]
)

def searchgrid(row, col, nums, sudoku_grid):
    for r in row:
        for c in col:
            if sudoku_grid[r,c] in nums:
                nums.remove(sudoku_grid[r,c])
    return nums, sudoku_grid


def solve(sudoku_grid):
    i = 0
    while 0 in sudoku_grid:
        i += 1
        for row in range(9):
            for col in range(9):
                if sudoku_grid[row,col] == 0:
                    nums_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    nums_list, sudoku_grid = searchgrid(range(row, row+1), range(9), nums_list, sudoku_grid)
                    nums_list, sudoku_grid = searchgrid(range(9), range(col, col+1), nums_list, sudoku_grid)
                    grid_row = (row // 3) * 3
                    grid_col = (col // 3) * 3
                    nums_list, sudoku_grid = searchgrid(range(grid_row, grid_row+3), range(grid_col, grid_col+3), nums_list, sudoku_grid)
                    if len(nums_list) == 1:
                        sudoku_grid[row,col] = int(nums_list[0])
    print(f'Solved in {i} iterations!')
    print(sudoku_grid)

if __name__ == '__main__':
    solve(demo_grid)
