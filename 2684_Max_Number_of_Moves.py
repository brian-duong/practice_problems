import numpy as np

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        for col in range(1, cols):
            unchanged = True
            for row in range(rows):
                val = grid[row][col]
                if val > grid[row][col - 1]:
                    unchanged = False
                    continue
                if row > 0:
                    if val > grid[row - 1][col - 1]:
                        unchanged = False
                        continue
                if row < rows - 1:
                    if val > grid[row + 1][col - 1]:
                        unchanged = False
                        continue
                grid[row][col] = 10 ** 6 + 1
            if unchanged:
                return col - 1
        return cols - 1
