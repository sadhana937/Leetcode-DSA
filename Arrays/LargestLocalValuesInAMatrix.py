class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        output = [[0] * (cols - 2) for _ in range(rows - 2)]
        for i in range(rows - 2):
            for j in range(cols - 2):
                submatrix = [row[j : j + 3] for row in grid[i : i + 3]]
                output[i][j]  = max(max(row) for row in submatrix)
            
        return output
                
