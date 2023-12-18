class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        a = max(nums)
        nums.remove(a)
        b = max(nums)
        c = min(nums)
        nums.remove(c)
        d = min(nums)
        return (a * b) - (c * d)

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return (nums[n - 1] * nums[n - 2]) - (nums[1] * nums[0])
