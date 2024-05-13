class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        # converting all the first element of rows to ONES
        for i in range(rows):
            if grid[i][0] == 0:
                for j in range(cols):
                    grid[i][j] = 1 - grid[i][j]

        # counting the number of ones in each column
        ones = [0] * cols
        for i in range(rows):
            for j in range(1, cols):
                ones[j] += grid[i][j]

        # complementing columns with less number of ones
        for i in range(rows):
            for j in range(1, cols):
                if ones[j] < (rows / 2):
                    grid[i][j] = 1 - grid[i][j]
        
        # finding the new sum
        summ = 0
        for i in grid:
            new = ''.join([str(j) for j in i])
            summ += int(new, 2)

        return summ               
