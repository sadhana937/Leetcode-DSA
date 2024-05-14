class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxval = 0
        rows = len(grid)
        cols = len(grid[0])

        def backtracking(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == 0:
                return 0

            val = grid[i][j]
            grid[i][j] = 0
            
            down = backtracking(i + 1, j)
            right = backtracking(i, j + 1)
            up = backtracking(i - 1, j)
            left = backtracking(i, j - 1)

            grid[i][j] = val

            return val + max(up, down, left, right)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 0:
                    maxval = max(maxval, backtracking(i, j))

        return maxval
