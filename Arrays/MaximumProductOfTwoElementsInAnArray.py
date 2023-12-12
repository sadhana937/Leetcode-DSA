class Solution1:
    def maxProduct(self, nums: List[int]) -> int:
        first = max(nums)
        nums.remove(first)
        second = max(nums)
        return (first - 1) * (second - 1)

class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        return (nums[n - 1] - 1) * (nums[n - 2] - 1)
