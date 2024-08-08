class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        output = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        num = 1
        while left <= right and top <= bottom:

            for i in range(left, right + 1):
                output[top][i] = num
                num += 1
            top += 1

            for i in range(top, bottom + 1):
                output[i][right] = num
                num += 1
            right -= 1

            for i in range(right, left - 1, -1):
                output[bottom][i] = num
                num += 1
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                output[i][left] = num
                num += 1
            left += 1
        
        return output
