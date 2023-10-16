# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        a = [1] * (rowIndex + 1)
        for i in range(1, rowIndex + 1):
            j = i - 1 
            while j > 0:
                a[j] = a[j] + a[j - 1]
                j -= 1
        return a
