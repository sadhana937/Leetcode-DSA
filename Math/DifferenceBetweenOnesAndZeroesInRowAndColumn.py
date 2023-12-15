class Solution1:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        diff = [[0] * n for _ in range(m)]
        col = list(zip(*grid))
        rowsum = [grid[i].count(1) - grid[i].count(0) for i in range(m)]
        colsum = [col[i].count(1) - col[i].count(0) for i in range(n)]
        for i in range(m):
            for j in range(n):
                diff[i][j] = rowsum[i] + colsum[j]

        return diff

class Solution2:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        diff = [[0] * n for _ in range(m)]
        one_rows = defaultdict(int)
        one_cols = defaultdict(int)
        zero_rows = defaultdict(int)
        zero_cols = defaultdict(int)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zero_rows[i] += 1
                    zero_cols[j] += 1
                else:
                    one_rows[i] += 1
                    one_cols[j] += 1

        for i in range(m):
            for j in range(n):
                diff[i][j] = one_rows[i] + one_cols[j] - zero_rows[i] - zero_cols[j]
        
        return diff
