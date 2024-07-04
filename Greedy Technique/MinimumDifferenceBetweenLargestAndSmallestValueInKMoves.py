class Solution:
    def minDifference(self, nums: List[int]) -> int:
        k = 3   # maximum of 3 moves considered for this question

        if len(nums) <= k + 1:
            return 0

        res, _ = math.inf, nums.sort()
        for (a, b) in [(k - i, -(1 + i)) for i in range(k + 1)]:
            res = min(res, nums[b] - nums[a])

        return res
