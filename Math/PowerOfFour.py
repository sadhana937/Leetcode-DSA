class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 0x555555555 (hexadecimal) is equivalent to binary '0101 ... 0101 0101'
        if n & (n - 1) == 0 and n & 0x5555555555:
            return True
        else:
            return False
