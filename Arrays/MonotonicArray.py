# An array is monotonic if it is either monotone increasing or monotone decreasing
# Time complexity: O(n)
# Space complexity: O(1)

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if nums[0] <= nums[n - 1]:
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    return False
        else:
            for i in range(n - 1):
                if nums[i] < nums[i + 1]:
                    return False
        return True
