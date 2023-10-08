# Time complexity: O(m.n)
# Space complexity: O(m.n)

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        dp = [[float('-inf')] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                ans = nums1[i - 1] * nums2[j - 1] # computes the dot product of current elements
                dp[i][j] = max(ans,ans + dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) # assigns the max dot product obtained so far to d[i][j]
        return dp[m][n]
