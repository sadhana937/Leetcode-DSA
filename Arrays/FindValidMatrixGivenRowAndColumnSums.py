class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m = len(rowSum)
        n = len(colSum)
        arr = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                minval = min(rowSum[i], colSum[j])
                arr[i][j] = minval
                rowSum[i] -= minval
                colSum[j] -= minval
        return arr
