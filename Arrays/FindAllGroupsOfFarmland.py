class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        output = []
        m = len(land)
        n = len(land[0])

        def dfs(r1, c1, r2, c2):
            # Mark all cells within the group as visited
            for i in range(r1, r2 + 1):
                for j in range(c1, c2 + 1):
                    land[i][j] = 0

            # Add the coordinates of the group to the output
            output.append([r1, c1, r2, c2])

        for i in range(m):
            for j in range(n):
                if land[i][j] == 1:
                    # Find the coordinates of the bottom right corner of the group
                    r2, c2 = i, j
                    while r2 < m and land[r2][j] == 1:
                        r2 += 1
                    while c2 < n and land[i][c2] == 1:
                        c2 += 1
                    r2 -= 1
                    c2 -= 1
                    # Perform DFS to mark and add the group
                    dfs(i, j, r2, c2)

        return output
