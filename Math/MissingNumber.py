class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        set_num = set(nums)
        maximum = max(nums)
        for i in range(maximum + 1):
            if i not in set_num:
                return i
        return maximum + 1
