class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < sum(nums[:i]):
                return sum(nums[:i + 1])
        return -1
