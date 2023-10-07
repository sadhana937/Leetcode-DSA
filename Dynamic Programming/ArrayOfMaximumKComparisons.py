# Time complexity: O(n.m^2.k)
# Space complexity: O(n.m.k)

class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:  
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        MOD = 10 ** 9 + 7
        for i in range(m + 1):
            dp[n][i][0] = 1
        for i in range(n - 1, -1, -1):
            for max_so_far in range(m, -1, -1):
                for remain in range(k + 1):
                    ans = max_so_far * dp[i + 1][max_so_far][remain]
                    if remain > 0:
                        for num in range(max_so_far + 1, m + 1):
                            ans = ans + dp[i + 1][num][remain - 1]    
                    dp[i][max_so_far][remain] = ans % MOD
        return dp[0][0][k]
            
