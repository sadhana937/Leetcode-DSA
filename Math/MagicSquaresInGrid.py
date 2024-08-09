class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0
        diagonal2_set = {(0,2), (1,1), (2,0)}
        not_eligible = {0, 10, 11, 12, 13, 14, 15}
        for i in range(m - 2):
            for j in range(n - 2):
                visited = set()
                rowsum = [0] * 3
                colsum = [0] * 3
                diagonal1 = 0
                diagonal2 = 0
                flag = True
                for p in range(3):
                    for q in range(3):
                        if grid[i + p][j + q] in visited or grid[i + p][j + q] in not_eligible:
                            flag = False
                        visited.add(grid[i + p][j + q])
                        rowsum[p] += grid[i + p][j + q]
                        colsum[q] += grid[i + p][j + q]
                        if p == q:
                            diagonal1 += grid[i + p][j + q]
                        if ((p,q)) in diagonal2_set:
                            diagonal2 += grid[i + p][j + q]
                    if not flag:
                        break
                if flag:
                    if colsum == [15,15,15] and rowsum == [15,15,15] and diagonal1 == 15 and diagonal2 == 15:
                        count += 1
        return count


                
