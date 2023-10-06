# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def integerBreak(self, n: int) -> int:
        result = 1
        if n < 3:
            return 1
        elif n == 3:
            return 2
        elif n % 3 == 1:
            result *= 4
            n -= 4
        elif n % 3 == 2:
            result *= 2
            n -= 2
        result *= ( 3 ** (n // 3))
        return result
