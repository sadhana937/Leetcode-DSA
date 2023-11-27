class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        A, B, C, D = 4, 2, 2, 1
        mod = 10 ** 9 + 7

        for i in range(n - 1):
            A, B, C, D = (2 *(B + C)) % mod, A, (A + 2 * D) % mod, C

        return (A + B + C + D) % mod 
