class Solution1:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0 or n % 2 != 0:
            return False
        return self.isPowerOfTwo(n/2)


class Solution2:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
